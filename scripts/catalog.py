#!/usr/bin/env python3
"""Validate the shared catalog, generate README, or import the maintained Excel.

Uses Python's standard library only. The Excel is edited with Excel/LibreOffice;
this script reads its cells and never writes or reformats the workbook.
"""
import argparse
import copy
import datetime
import json
import re
import xml.etree.ElementTree as ET
import zipfile
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SCHEMA=json.loads((ROOT/'data/workbook_schema.json').read_text())['fields']
FIELDS=[(f['key'],f['label']) for f in SCHEMA]
FIELD_SPEC={f['key']:f for f in SCHEMA}
LIST_FIELDS={f['key'] for f in SCHEMA if f.get('format') in ['list','int_list','vocab_list','node_list']}
DERIVED_FIELDS={f['key'] for f in SCHEMA if f.get('format')=='derived'}

def item_code(item):
    return item.get('code',item.get('id'))

def vocabulary(taxonomy,name):
    return {item_code(x):x for x in taxonomy[name]}

def load():
    return (json.loads((ROOT/'data/papers.json').read_text()),
            json.loads((ROOT/'data/taxonomy.json').read_text()))

def canonical_url(url):
    url=url.strip().replace('http://','https://').rstrip('/')
    match=re.search(r'^https://(?:www\.)?arxiv.org/(?:abs|pdf|html)/(\d{4}\.\d{4,5})(?:v\d+)?(?:\.pdf)?(?:[?#].*)?$',url)
    return 'arxiv:'+match.group(1) if match else url

def validate(records,taxonomy):
    errors=[]
    allowed={key:{x['id'] for x in taxonomy[key]} for key in ['categories','kinds','capabilities','optimization_types']}
    node_codes=set(vocabulary(taxonomy,'survey_nodes'))
    detail_codes=set(vocabulary(taxonomy,'detailed_type_vocab'))
    core_codes=set(vocabulary(taxonomy,'core_capabilities'))
    seen_ids=set(); seen_links=set()
    for p in records:
        tag=p.get('id','<missing>')
        if tag in seen_ids: errors.append(f'Duplicate ID: {tag}')
        seen_ids.add(tag)
        for f in ['id','title','short_name','kind','primary_category','verification_status']:
            if not p.get(f): errors.append(f'{tag}: missing {f}')
        if not re.fullmatch(r'WA-\d{4,}',tag):errors.append(f'{tag}: invalid stable ID')
        if p.get('primary_survey_node') not in node_codes:errors.append(f'{tag}: invalid primary manuscript section')
        for field,codes in [('secondary_survey_nodes',node_codes),('detailed_types',detail_codes),('core_capabilities',core_codes)]:
            if not isinstance(p.get(field),list):errors.append(f'{tag}: {field} must be a list');continue
            for value in p[field]:
                if value not in codes:errors.append(f'{tag}: invalid {field}: {value}')
        if not p.get('detailed_types'):errors.append(f'{tag}: missing detailed research type')
        expected=list(dict.fromkeys([p.get('primary_survey_node')]+p.get('secondary_survey_nodes',[])))
        if p.get('survey_sections')!=expected:errors.append(f'{tag}: manuscript section fields disagree')
        if any(s.startswith('4') for s in p.get('survey_sections',[])):errors.append(f'{tag}: retired chapter 4 belongs only in legacy_survey_sections')
        if p.get('reading_priority','') not in ['', '核心','补充','候选']:errors.append(f'{tag}: invalid source reading priority')
        if p.get('publication_status','') not in ['', 'published','accepted','preprint','unconfirmed']:errors.append(f'{tag}: invalid publication status')
        py=p.get('publication_year')
        if py is not None and (not isinstance(py,int) or not 1900<=py<=int(taxonomy['date'][:4])):errors.append(f'{tag}: invalid publication year')
        if p.get('publication_status')=='published' and py is None:errors.append(f'{tag}: published record needs publication year')
        claims=p.get('section3_claim_ids',[])
        if not isinstance(claims,list) or any(x not in vocabulary(taxonomy,'section3_claims') for x in claims):errors.append(f'{tag}: unknown Section 3 claim')
        if claims and not p.get('section3_evidence_url'):errors.append(f'{tag}: Section 3 claims need an evidence URL')
        if p.get('section3_priority','') not in ['', 'A','B','F']:errors.append(f'{tag}: invalid Section 3 writing priority')
        if p.get('primary_category') not in allowed['categories']: errors.append(f'{tag}: unknown category')
        for k in p.get('kind','').split(';'):
            if k.strip() not in allowed['kinds']: errors.append(f'{tag}: unknown kind {k}')
        if 'Product/Resource' in p.get('kind','') and p['kind']!='Product/Resource':errors.append(f'{tag}: Product/Resource cannot be mixed with paper kinds')
        for f in ['capabilities','optimization_types']:
            if not isinstance(p.get(f,[]),list): errors.append(f'{tag}: {f} must be a list'); continue
            for value in p.get(f,[]):
                if value not in allowed[f]: errors.append(f'{tag}: unknown {f}: {value}')
        if p.get('verification_status') not in taxonomy['verification_statuses']: errors.append(f'{tag}: unknown verification status')
        if p.get('reading_status') not in taxonomy['reading_statuses']: errors.append(f'{tag}: unknown reading status')
        if p.get('year') is not None and (not isinstance(p['year'],int) or not 1900<=p['year']<=int(taxonomy['date'][:4])): errors.append(f'{tag}: invalid year')
        for field in ['url','institution_source','metadata_source','code_url','data_url','publication_url','section3_evidence_url']:
            u=p.get(field,'')
            if u and (not re.match(r'^https?://\S+$',u) or any(x in u for x in ['<','>','"'])): errors.append(f'{tag}: invalid {field}')
        if p.get('verification_status')!='pending' and not p.get('url'): errors.append(f'{tag}: confirmed record lacks URL')
        if p.get('verification_status')=='verified' and (not p.get('institution_source') or not p.get('institutions')): errors.append(f'{tag}: verified needs affiliation and source')
        url=canonical_url(p.get('url',''))
        if url and url in seen_links: errors.append(f'Duplicate canonical URL: {url}')
        if url: seen_links.add(url)
    if errors: raise ValueError('\n'.join(errors))
    return {'records':len(records),'papers':sum(p['kind']!='Product/Resource' for p in records),'statuses':dict(Counter(p['verification_status'] for p in records))}

def esc(value):
    return str(value).replace('|','\\|').replace('\n',' ')

def render_readme(records,taxonomy):
    confirmed=[p for p in records if p['verification_status']!='pending']
    papers=[p for p in confirmed if p['kind']!='Product/Resource']
    pending=[p for p in records if p['verification_status']=='pending']
    resources=[p for p in confirmed if p['kind']=='Product/Resource']
    lines=[
      '# Awesome Working Agents','','![Working Agents research map](assets/working-agents.svg)','',
      '> From answering questions to completing digital work: papers on artifacts, workspaces, tools, computer use, persistent responsibilities, and the systems that make them reliable.','',
      f'**{len(papers)} papers, surveys, and foundational studies** · **{len(resources)} non-paper resources** · Updated **{taxonomy["date"]}**','',
      '[Excel paper list](paper_list.xlsx) · [Classification guide](docs/taxonomy.md) · [Contributing](CONTRIBUTING.md) · [Catalog data](data/papers.json)','',
      'A broad reading list for agents that create artifacts, operate applications and tools, connect workspace objects, and maintain delegated work. Supporting research covers document understanding, planning, state management, verification, safety, and the value of work.','',
      'Browse the three paper lists below. The companion Excel provides the detailed manuscript classification, institutions, contributions, evidence limits, and team reading notes. Each paper appears once.','',
      '**Start here:** [ReAct](https://arxiv.org/abs/2210.03629), [SheetCopilot](https://arxiv.org/abs/2305.19308), [PPTAgent](https://arxiv.org/abs/2501.03936), [AppWorld](https://arxiv.org/abs/2407.18901), [OSWorld](https://arxiv.org/abs/2404.07972), [Workspace-Bench](https://arxiv.org/abs/2605.03596), [DELEGATE-52](https://arxiv.org/abs/2604.15597), [LongDS-Bench](https://arxiv.org/abs/2605.30434), and [GDPval](https://arxiv.org/abs/2510.04374).','',
      '[Agents, Methods & Systems](#methods) · [Benchmarks & Evaluation](#benchmarks) · [Surveys & Foundations](#surveys) · [Resources](#resources)',''
    ]
    def table(ps):
        if not ps:return []
        out=['| Paper | First year | Resources |','| --- | --- | --- |']
        for p in sorted(ps,key=lambda x:(-(x.get('year') or 0),x['short_name'].casefold())):
            name=esc(p['short_name']); title=esc(p['title'])
            label=f'**{name}**{title[len(name):]}' if title.casefold().startswith(name.casefold()) else f'**{name}**: {title}'
            links=[f'[Paper]({p["url"]})']
            for k,label2 in [('code_url','Code'),('data_url','Data')]:
                if p.get(k):links.append(f'[{label2}]({p[k]})')
            if p.get('publication_url') and p['publication_url']!=p['url'] and p.get('publication_status') in ['published','accepted']:
                label2='Accepted' if p['publication_status']=='accepted' else 'Publication'
                links.append(f'[{label2}]({p["publication_url"]})')
            out.append(f'| {label} | {p.get("year") or "—"} | {" · ".join(links)} |')
        return out+['']
    groups={'methods':[],'benchmarks':[],'surveys':[]}
    for p in papers:
        kinds={x.strip() for x in p['kind'].split(';')}
        group='surveys' if 'Survey' in kinds else ('methods' if kinds & {'Method','Framework'} else ('benchmarks' if 'Benchmark' in kinds else 'surveys'))
        groups[group].append(p)
    for group,name in [('methods','Agents, Methods & Systems'),('benchmarks','Benchmarks & Evaluation'),('surveys','Surveys & Foundations')]:
        lines += [f'<a id="{group}"></a>','',f'## {name}','']+table(groups[group])
    lines+=['<a id="resources"></a>','','## Resources','','Products, documentation, and standalone projects without an identified paper. These are excluded from the paper count.','', '| Resource | Link |','| --- | --- |']
    for p in resources:lines.append(f'| {esc(p["title"])} | [Source]({p["url"]}) |')
    lines+=['',
      '**Curation.** Entries are reconciled against primary paper or official project sources and deduplicated across versions and aliases. Years use the first confirmed public release when available. Bibliographic verification is separate from full-paper reading; detailed evidence and limitations are recorded in the Excel. This is an evolving narrative-review collection.','',
      '**Literature sources.** The [AI Office bibliography crosswalk](data/literature_sources/ai_office_2026.json) accounts for all 292 references in [The Evolution of AI Office](https://www.alphaxiv.org/abs/2609.evolution-ai-office-agents), including non-paper references outside this collection. The [work-form research crosswalk](data/literature_sources/work_forms_2026.json) records 11 additional candidates, primary-source matches, and classification corrections.','',
      'The [Section 3 evidence pack](data/literature_sources/section3_2026.json) maps 76 papers to 18 writing claims and preserves 40 citation audits. The Excel separates publication status, evidence locations, and task-specific scope. A [BibTeX collection](data/literature_sources/section3_2026.bib) is also available.','',
      f'**Open metadata:** {len(pending)} identities await confirmation and are omitted from the lists; {sum(p["verification_status"]=="metadata-only" for p in papers)} paper affiliations remain incomplete. See [Contributing](CONTRIBUTING.md) for the maintenance workflow.',''
    ]
    output='\n'.join(lines)
    if re.search(r'[\u3400-\u9fff]',output):raise ValueError('Public README must be entirely English; check titles and resource names')
    return output

NS={'m':'http://schemas.openxmlformats.org/spreadsheetml/2006/main'}

def read_workbook(path):
    """Read literal Excel cells, retaining raw URLs and rejecting formulas in the catalog."""
    with zipfile.ZipFile(path) as z:
        strings=[]
        if 'xl/sharedStrings.xml' in z.namelist():
            for si in ET.fromstring(z.read('xl/sharedStrings.xml')):
                strings.append(''.join(t.text or '' for t in si.iter(f'{{{NS["m"]}}}t')))
        wb=ET.fromstring(z.read('xl/workbook.xml'))
        props=wb.find('m:workbookPr',NS)
        epoch=datetime.datetime(1904,1,1) if props is not None and props.get('date1904','0').lower() in ['1','true'] else datetime.datetime(1899,12,30)
        rels=ET.fromstring(z.read('xl/_rels/workbook.xml.rels'))
        targets={r.attrib['Id']:r.attrib['Target'] for r in rels}
        result=[]
        for sheet in wb.find('m:sheets',NS):
            if sheet.attrib['name'] not in ['Paper List','Resources']:continue
            rid=sheet.attrib['{http://schemas.openxmlformats.org/officeDocument/2006/relationships}id']
            target=targets[rid]
            target=target.lstrip('/') if target.startswith('/') else 'xl/'+target
            rows=[]; header=None
            for row in ET.fromstring(z.read(target)).findall('.//m:sheetData/m:row',NS):
                cells={}
                for cell in row:
                    col=re.match(r'[A-Z]+',cell.attrib['r']).group()
                    key=next((f['key'] for f in SCHEMA if header and header.get(col)==f['label']),None)
                    formula=cell.findtext('m:f',None,NS)
                    hyperlink=None
                    if formula is not None:
                        if key in DERIVED_FIELDS:
                            cells[col]='';continue
                        match=re.fullmatch(r'(?:_xlfn\.)?HYPERLINK\("((?:""|[^"])*)","((?:""|[^"])*)"\)',formula)
                        if not match or FIELD_SPEC.get(key,{}).get('format')!='url' or match[1]!=match[2]:raise ValueError(f'Unsupported formula in {sheet.attrib["name"]}!{cell.attrib["r"]}; only derived classification labels and literal URL hyperlinks are supported')
                        hyperlink=match[1].replace('""','"')
                    value=cell.findtext('m:v','',NS)
                    if cell.attrib.get('t')=='s':value=strings[int(value)]
                    elif cell.attrib.get('t')=='inlineStr':value=''.join(t.text or '' for t in cell.findall('.//m:t',NS))
                    if hyperlink is not None:value=hyperlink
                    if FIELD_SPEC.get(key,{}).get('format')=='date' and re.fullmatch(r'\d+(?:\.\d+)?',value):
                        value=(epoch+datetime.timedelta(days=float(value))).date().isoformat()
                    cells[col]=value
                if header is None:header=cells
                rows.append(cells)
            result.append((sheet.attrib['name'],rows))
        return result

def import_xlsx(path,existing,taxonomy):
    old={p['id']:p for p in existing}; records=[]
    for sheet,rows in read_workbook(path):
        if not rows:continue
        header=rows[0]
        columns={field:next((col for col,val in header.items() if val==label),None) for field,label in FIELDS}
        missing=[label for field,label in FIELDS if not columns[field]]
        if missing:raise ValueError(f'{sheet}: missing headers {missing}')
        for row in rows[1:]:
            if not any(row.get(c,'').strip() for c in columns.values()):continue
            ident=row.get(columns['id'],'').strip()
            p=copy.deepcopy(old.get(ident,{}))
            for field,_ in FIELDS:
                if field in DERIVED_FIELDS:continue
                value=row.get(columns[field],'').strip()
                if field in LIST_FIELDS:
                    value=[v.strip() for v in value.split(';') if v.strip()]
                    fmt=FIELD_SPEC[field].get('format')
                    if fmt=='int_list':value=[int(x) for x in value]
                    elif fmt=='node_list':value=[re.match(r'^\d+(?:\.\d+)*',x).group() if re.match(r'^\d+(?:\.\d+)*',x) else x for x in value]
                    elif fmt=='vocab_list':
                        vocab=vocabulary(taxonomy,FIELD_SPEC[field]['vocab'])
                        reverse={v.get('name',v.get('zh','')):k for k,v in vocab.items()}
                        value=[x if x in vocab else reverse.get(x,x) for x in value]
                elif FIELD_SPEC[field].get('format')=='year':value=int(float(value)) if value else None
                elif field=='kind':value=';'.join(x.strip() for x in value.split(';'))
                elif field=='checked_on' and value:
                    if re.fullmatch(r'\d+(?:\.\d+)?',value):
                        value=(datetime.datetime(1899,12,30)+datetime.timedelta(days=float(value))).date().isoformat()
                    else:value=datetime.datetime.fromisoformat(value.replace('Z','+00:00')).date().isoformat()
                p[field]=value
            p['survey_sections']=list(dict.fromkeys([p['primary_survey_node']]+p['secondary_survey_nodes']))
            if (sheet=='Resources') != (p['kind']=='Product/Resource'):
                raise ValueError(f'{p["id"]}: resource rows belong in Resources; academic papers belong in Paper List')
            records.append(p)
    removed=set(old)-{p.get('id') for p in records}
    if removed:raise ValueError(f'Import would remove existing IDs: {sorted(removed)}. Review deliberate deletions in the JSON and Excel together; ordinary imports cannot silently drop rows.')
    validate(records,taxonomy)
    return sorted(records,key=lambda x:x['id'])

def main():
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--check',action='store_true')
    ap.add_argument('--import-xlsx',type=Path)
    ap.add_argument('--build-readme',action='store_true')
    args=ap.parse_args(); records,taxonomy=load()
    if args.import_xlsx:records=import_xlsx(args.import_xlsx,records,taxonomy)
    stats=validate(records,taxonomy)
    readme=render_readme(records,taxonomy) if args.import_xlsx or args.build_readme else None
    if args.import_xlsx:
        (ROOT/'data/papers.json').write_text(json.dumps(records,ensure_ascii=False,indent=2)+'\n')
    if readme is not None:
        (ROOT/'README.md').write_text(readme)
    print(json.dumps(stats,ensure_ascii=False))
    if args.check and (ROOT/'README.md').read_text()!=render_readme(records,taxonomy):raise ValueError('README differs from catalog; run --build-readme')

if __name__=='__main__':main()
