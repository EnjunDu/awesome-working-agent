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
FIELDS = [
    ('id','ID'),('title','论文名称'),('short_name','简称'),('year','年份'),
    ('url','论文链接'),('institutions','单位'),('kind','条目类型'),
    ('primary_category','主分类'),('subcategory','细分类'),('capabilities','能力标签'),
    ('optimization_types','优化类型'),('survey_sections','Survey章节'),
    ('contribution','核心贡献'),('code_url','代码链接'),('data_url','数据链接'),
    ('verification_status','核验状态'),('institution_source','单位来源'),
    ('metadata_source','元数据来源'),('draft_refs','草稿引用编号'),('origin','收录来源'),
    ('checked_on','复核日期'),('reading_status','阅读状态'),('owner','负责人'),
    ('writing_section','写作章节'),('writing_notes','写作备注'),('notes','核验备注')
]
LIST_FIELDS = {'capabilities','optimization_types','survey_sections','draft_refs','origin'}

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
    seen_ids=set(); seen_links=set()
    for p in records:
        tag=p.get('id','<missing>')
        if tag in seen_ids: errors.append(f'Duplicate ID: {tag}')
        seen_ids.add(tag)
        for f in ['id','title','short_name','kind','primary_category','verification_status']:
            if not p.get(f): errors.append(f'{tag}: missing {f}')
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
        for field in ['url','institution_source','metadata_source','code_url','data_url']:
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
      f'**{len(papers)} linked research papers and surveys** · **{len(resources)} separate resources** · Updated **{taxonomy["date"]}** · Taxonomy **v{taxonomy["version"]}**','',
      '[Download the detailed Excel paper list](paper_list.xlsx) · [Classification guide](docs/taxonomy.md) · [How to contribute](CONTRIBUTING.md) · [Machine-readable catalog](data/papers.json)','',
      'The public list is organized by the work or system being studied. The Excel adds paper-time institutions, detailed types, capability tags, optimization mechanisms, survey-section mappings, source checks, and editable reading/writing fields. Each paper has one stable ID and appears once below.','',
      '**Scope.** We cover digital knowledge work: producing artifacts, changing application or business state, connecting workspace objects, and maintaining delegated responsibilities. Document QA, general planning, theory, and work-impact studies are retained as supporting context in their own section. Products and documentation are counted separately.','',
      '**Start here.** [SheetCopilot](https://arxiv.org/abs/2305.19308) and [PPTAgent](https://arxiv.org/abs/2501.03936) for artifacts; [Workspace-Bench](https://arxiv.org/abs/2605.03596) and [OfficeBench](https://arxiv.org/abs/2407.19056) for workspaces; [OSWorld](https://arxiv.org/abs/2404.07972) for computer use; [AppWorld](https://arxiv.org/abs/2407.18901) and [τ-bench](https://arxiv.org/abs/2406.12045) for stateful tool use; [MemGPT](https://arxiv.org/abs/2310.08560) for memory; [SWE-agent](https://arxiv.org/abs/2405.15793), [AFlow](https://arxiv.org/abs/2410.10762), and [GEPA](https://arxiv.org/abs/2507.19457) for system design and optimization.','',
      '## Contents',''
    ]
    for c in taxonomy['categories']:
        lines.append(f'- [{c["name"]}](#{c["id"]})')
    lines+=['- [Surveys and roadmaps](#surveys)','- [Resources](#resources)','- [Curation and maintenance](#curation)','']
    def table(ps):
        if not ps:return []
        out=['| Paper | First year | Resources |','| --- | --- | --- |']
        for p in sorted(ps,key=lambda x:(-(x.get('year') or 0),x['short_name'].casefold())):
            name=esc(p['short_name']); title=esc(p['title'])
            label=f'**{name}**{title[len(name):]}' if title.casefold().startswith(name.casefold()) else f'**{name}**: {title}'
            links=[f'[Paper]({p["url"]})']
            for k,label2 in [('code_url','Code'),('data_url','Data')]:
                if p.get(k):links.append(f'[{label2}]({p[k]})')
            out.append(f'| {label} | {p.get("year") or "—"} | {" · ".join(links)} |')
        return out+['']
    for c in taxonomy['categories']:
        ps=[p for p in papers if p['primary_category']==c['id'] and 'Survey' not in p['kind']]
        lines += [f'<a id="{c["id"]}"></a>',f'## {c["name"]}','',c['scope'],'']
        if c['id']=='harness':
            platform=[p for p in ps if not p.get('optimization_types')]
            if platform:lines+=['### Platforms and execution systems','']+table(platform)
            remaining=list(ps)
            for p in platform:remaining.remove(p)
            for opt in taxonomy['optimization_types']:
                group=[p for p in remaining if opt['id'] in p.get('optimization_types',[])]
                if group:
                    lines += [f'### {opt["id"].replace("-"," ").capitalize()}','']+table(group)
                    for p in group:remaining.remove(p)
            lines+=table(remaining)
        else:lines+=table(ps)
    surveys=[p for p in papers if 'Survey' in p['kind']]
    lines+=['<a id="surveys"></a>','## Surveys and roadmaps','']+table(surveys)
    lines+=['<a id="resources"></a>','## Resources','','Non-paper documentation and project resources. These do not contribute to the research-paper count.','', '| Resource | Link |','| --- | --- |']
    for p in resources:lines.append(f'| {esc(p["title"])} | [Source]({p["url"]}) |')
    lines+=['','<a id="curation"></a>','## Curation and maintenance','',
      'This is a structured, evolving reading list. Coverage starts from the companion survey bibliography and the previous repository list, then reconciles identifiers against primary paper or project pages. It is not an exhaustive systematic census.','',
      '- **Identity checks:** paper titles and links are checked against primary sources. Excel distinguishes `verified` (identity plus affiliation evidence), `metadata-only` (identity checked; affiliation incomplete), and `pending` (identity still requires confirmation). A checked entry is not a claim that a team member has read the full paper.',
      '- **Years:** the first public preprint year is used when available, independently of later conference publication.',
      '- **Institutions:** the detailed list records paper-time participating institutions and their evidence. A shortened list of main institutions is labeled in the record.',
      '- **Classification:** the taxonomy is a provisional editorial scheme. Work form, persistence, and openness are different dimensions. Benchmark capability tags describe task demands; they do not establish a model’s competence.',
      (f'- **Open items:** {len(pending)} entries await identity confirmation in the Excel and catalog; they are excluded from the linked-paper count and tables.' if pending else f'- **Open items:** paper identities have source evidence; {sum(p["verification_status"]=="metadata-only" for p in papers)} affiliation records remain incomplete in the Excel.'),
      '- **Contributions:** add missing work, improve category boundaries, correct metadata, or help read and summarize a paper. See [CONTRIBUTING.md](CONTRIBUTING.md).','',
      'The Excel is the team editing surface. After editing it, run `python3 scripts/catalog.py --import-xlsx paper_list.xlsx` to update the catalog and this README. The command validates before writing and matches records by stable ID. Workbook values are authoritative; blank cells clear the corresponding fields. Run `python3 scripts/catalog.py --check` for a local consistency check.',''
    ]
    return '\n'.join(lines)

NS={'m':'http://schemas.openxmlformats.org/spreadsheetml/2006/main'}

def read_workbook(path):
    """Read literal Excel cells, retaining raw URLs and rejecting formulas in the catalog."""
    with zipfile.ZipFile(path) as z:
        strings=[]
        if 'xl/sharedStrings.xml' in z.namelist():
            for si in ET.fromstring(z.read('xl/sharedStrings.xml')):
                strings.append(''.join(t.text or '' for t in si.iter(f'{{{NS["m"]}}}t')))
        wb=ET.fromstring(z.read('xl/workbook.xml'))
        rels=ET.fromstring(z.read('xl/_rels/workbook.xml.rels'))
        targets={r.attrib['Id']:r.attrib['Target'] for r in rels}
        result=[]
        for sheet in wb.find('m:sheets',NS):
            if sheet.attrib['name'] not in ['Paper List','Resources']:continue
            rid=sheet.attrib['{http://schemas.openxmlformats.org/officeDocument/2006/relationships}id']
            target=targets[rid]
            target=target.lstrip('/') if target.startswith('/') else 'xl/'+target
            rows=[]
            for row in ET.fromstring(z.read(target)).findall('.//m:sheetData/m:row',NS):
                cells={}
                for cell in row:
                    formula=cell.findtext('m:f',None,NS)
                    hyperlink=None
                    if formula is not None:
                        match=re.fullmatch(r'(?:_xlfn\.)?HYPERLINK\("((?:""|[^"])*)","((?:""|[^"])*)"\)',formula)
                        col=re.match(r'[A-Z]+',cell.attrib['r']).group()
                        if not match or col not in ['E','N','O','Q','R'] or match[1]!=match[2]:raise ValueError(f'Catalog cells must be literal values or identical literal URL hyperlinks: {sheet.attrib["name"]}!{cell.attrib["r"]}')
                        hyperlink=match[1].replace('""','"')
                    value=cell.findtext('m:v','',NS)
                    if cell.attrib.get('t')=='s':value=strings[int(value)]
                    elif cell.attrib.get('t')=='inlineStr':value=''.join(t.text or '' for t in cell.findall('.//m:t',NS))
                    if hyperlink is not None:value=hyperlink
                    col=re.match(r'[A-Z]+',cell.attrib['r']).group()
                    cells[col]=value
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
                value=row.get(columns[field],'').strip()
                if field in LIST_FIELDS:
                    value=[v.strip() for v in value.split(';') if v.strip()]
                    if field=='draft_refs':value=[int(x) for x in value]
                elif field=='year':value=int(float(value)) if value else None
                elif field=='checked_on' and value:
                    if re.fullmatch(r'\d+(?:\.\d+)?',value):
                        value=(datetime.datetime(1899,12,30)+datetime.timedelta(days=float(value))).date().isoformat()
                    else:value=datetime.datetime.fromisoformat(value.replace('Z','+00:00')).date().isoformat()
                p[field]=value
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
    if args.import_xlsx:
        (ROOT/'data/papers.json').write_text(json.dumps(records,ensure_ascii=False,indent=2)+'\n')
    if args.import_xlsx or args.build_readme:
        (ROOT/'README.md').write_text(render_readme(records,taxonomy))
    print(json.dumps(stats,ensure_ascii=False))
    if args.check and (ROOT/'README.md').read_text()!=render_readme(records,taxonomy):raise ValueError('README differs from catalog; run --build-readme')

if __name__=='__main__':main()
