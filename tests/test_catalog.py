import copy
import importlib.util
import json
import datetime
import re
import tempfile
import unittest
import zipfile
from pathlib import Path
from unittest.mock import patch

ROOT=Path(__file__).resolve().parents[1]
spec=importlib.util.spec_from_file_location('catalog',ROOT/'scripts/catalog.py')
catalog=importlib.util.module_from_spec(spec);spec.loader.exec_module(catalog)

class CatalogTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.records,cls.tax=catalog.load()

    def test_preprint_pdf_versions_share_identity(self):
        urls=['https://arxiv.org/abs/2402.01030','https://arxiv.org/pdf/2402.01030v4.pdf','http://arxiv.org/html/2402.01030v2']
        self.assertEqual(len({catalog.canonical_url(u) for u in urls}),1)

    def test_duplicate_identity_is_rejected(self):
        a=copy.deepcopy(next(p for p in self.records if 'arxiv.org/abs/' in p['url']))
        b=copy.deepcopy(a);b['id']='WA-9999';b['url']=a['url'].replace('/abs/','/pdf/')+'v2.pdf'
        with self.assertRaisesRegex(ValueError,'Duplicate canonical URL'):catalog.validate([a,b],self.tax)

    def test_nonpaper_mixed_type_is_rejected(self):
        p=copy.deepcopy(self.records[0]);p['kind']='Product/Resource;Framework'
        with self.assertRaisesRegex(ValueError,'cannot be mixed'):catalog.validate([p],self.tax)

    def test_same_count_cannot_replace_existing_id(self):
        old=copy.deepcopy(self.records[:2]);new=copy.deepcopy(old);new[1]['id']='WA-9999'
        headers={str(i):label for i,(_,label) in enumerate(catalog.FIELDS)}
        rows=[headers]+[{str(i):';'.join(map(str,p.get(field,[]))) if field in catalog.LIST_FIELDS else str(p.get(field) or '') for i,(field,_) in enumerate(catalog.FIELDS)} for p in new]
        with patch.object(catalog,'read_workbook',return_value=[('Paper List',rows)]):
            with self.assertRaisesRegex(ValueError,'remove existing IDs'):catalog.import_xlsx(Path('unused.xlsx'),old,self.tax)

    def test_actual_workbook_roundtrip(self):
        result=catalog.import_xlsx(ROOT/'paper_list.xlsx',self.records,self.tax)
        self.assertEqual(result,sorted(self.records,key=lambda x:x['id']))

    def test_readme_matches_catalog(self):
        self.assertEqual((ROOT/'README.md').read_text(),catalog.render_readme(self.records,self.tax))

    def test_public_english_and_three_paper_groups(self):
        text=catalog.render_readme(self.records,self.tax)
        self.assertIsNone(re.search(r'[\u3400-\u9fff]',text))
        self.assertEqual(re.findall(r'^## (.+)$',text,re.M),['Agents, Methods & Systems','Benchmarks & Evaluation','Surveys & Foundations','Resources'])
        self.assertEqual(text.count('[Paper]('),sum(p['kind']!='Product/Resource' and p['verification_status']!='pending' for p in self.records))

    def test_old_chapter_is_legacy_only(self):
        self.assertTrue(all(not s.startswith('4') for p in self.records for s in p['survey_sections']))
        self.assertTrue(any(s.startswith('4') for p in self.records for s in p['legacy_survey_sections']))

    def test_all_supplement_entries_reconciled(self):
        ledger=json.loads((ROOT/'data/source_ledger.json').read_text())['items']
        self.assertEqual({p['list_id'] for p in ledger},{f'L{i:03d}' for i in range(1,150)})
        self.assertEqual(len(ledger),149)
        self.assertTrue({p['catalog_id'] for p in ledger}<={p['id'] for p in self.records})

    def test_excel_1904_dates(self):
        serial=(datetime.datetime(2026,10,16)-datetime.datetime(1904,1,1)).days
        ns='http://schemas.openxmlformats.org/spreadsheetml/2006/main'
        with tempfile.TemporaryDirectory() as d:
            file=Path(d)/'date.xlsx'
            with zipfile.ZipFile(file,'w') as z:
                z.writestr('xl/workbook.xml',f'<workbook xmlns="{ns}" xmlns:r="http://schemas.openxmlformats.org/officeDocument/2006/relationships"><workbookPr date1904="1"/><sheets><sheet name="Paper List" sheetId="1" r:id="rId1"/></sheets></workbook>')
                z.writestr('xl/_rels/workbook.xml.rels','<Relationships xmlns="http://schemas.openxmlformats.org/package/2006/relationships"><Relationship Id="rId1" Target="worksheets/sheet1.xml"/></Relationships>')
                z.writestr('xl/worksheets/sheet1.xml',f'<worksheet xmlns="{ns}"><sheetData><row r="1"><c r="A1" t="inlineStr"><is><t>复核日期</t></is></c></row><row r="2"><c r="A2"><v>{serial}</v></c></row></sheetData></worksheet>')
            self.assertEqual(catalog.read_workbook(file)[0][1][1]['A'],'2026-10-16')

    def test_kind_whitespace_does_not_change_group(self):
        p=copy.deepcopy(self.records[0]);p['kind']='Method; Survey'
        text=catalog.render_readme([p],self.tax)
        self.assertIn(p['short_name'],text.split('## Surveys & Foundations')[1])

if __name__=='__main__':unittest.main()
