import copy
import importlib.util
import json
import unittest
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

if __name__=='__main__':unittest.main()
