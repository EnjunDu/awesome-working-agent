# Contributing

Add missing papers, improve category boundaries, correct links or affiliations, and share reading notes. Classification v0.1 is provisional. A terminology change should include examples of what moves and why.

## Team workflow

1. Download or open `paper_list.xlsx`. Filter `Paper List` by primary category, detailed subtype, optimization type, or survey section. The yellow columns are reading status, owner, writing section, and writing notes. Initial entries are **unassigned**, even when their bibliographic metadata has been checked.
2. Edit the workbook. Add new records at the bottom of the table. Use a new, unused stable ID in the form `WA-xxxx`; never reuse or renumber existing IDs. Keep each paper on one row. Use semicolons in the multi-value fields listed below.
3. Save the workbook, then run from the repository root:

   ```bash
   python3 scripts/catalog.py --import-xlsx paper_list.xlsx
   python3 scripts/catalog.py --check
   ```

   The script reads the Excel, validates IDs and vocabulary, and updates `data/papers.json` and `README.md`. It does not modify the workbook. Workbook values are authoritative: a blank cell clears the corresponding field. Review and commit all three files together. No Python packages are needed.
4. Use a pull request to coordinate simultaneous edits. Excel files do not merge reliably. If two people edit at once, reconcile by stable ID before importing; never replace a colleague's newer workbook with an older copy.

中文：先在 Excel 认领和补充，再运行导入命令同步 JSON 与 README。保留原 ID，新增论文只分配新 ID。多人同时修改时按 ID 合并；优先通过 PR 协调，避免直接覆盖二进制 Excel。

## Required evidence

- Give the full title, a primary paper link, first public preprint year when known, entry kind, one primary category, and a specific subtype.
- Check title and link identity. Prefer arXiv, ACL Anthology, a publisher, or an official project page. Use the paper's publication-time affiliations, with a front-matter or official-project source. Name a shortened institution list explicitly in the verification notes.
- Use `verified` only when both identity and affiliation have evidence. Use `metadata-only` for a checked paper whose affiliation is incomplete. Use `pending` when paper identity or the proposed link is unresolved. Pending entries are retained in the Excel and JSON but omitted from the README paper tables.
- Record a code or dataset link only when the paper or official project identifies it. A project page is not automatically a code repository or dataset. Leave unknown links empty.
- Keep methods, benchmarks, frameworks, surveys, background research, and products distinct. A product or documentation entry uses `Product/Resource` and belongs in the `Resources` sheet, outside the research-paper count. A dataset with an identified research paper is represented by that paper; a standalone data/project resource is not counted as another paper.
- Deduplicate conference/preprint versions, renamed projects, and aliases. A newer version of the same work keeps its ID. Explain a title change in the verification notes.

## Fields and vocabulary

See [the classification guide](docs/taxonomy.md) and `Taxonomy` in Excel. The machine-readable vocabulary is `data/taxonomy.json`.

- Multi-value fields: `能力标签`, `优化类型`, `Survey章节`, `草稿引用编号`, `收录来源` use `;` separators. `条目类型` may also contain multiple allowed kinds, e.g. `Method;Benchmark`.
- `主分类` is a single browsing category. `细分类` is a concise specific description; reuse an existing term where applicable. Capability and optimization labels must come from the controlled vocabulary.
- `Survey章节` is a proposed cross-reference to the supplied survey outline, not evidence that the paper has been written up or read. `写作章节` and `写作备注` are team decisions.
- `草稿引用编号` preserves the bibliography number in the supplied 2026-10-16 draft. These numbers are provenance, not stable identifiers and not a promise that later drafts keep the numbering.
- Keep URLs as HTTPS strings and years as numbers. Literal URL cells and `HYPERLINK("url","url")` formulas are accepted by the importer. Other catalog formulas and renamed headers are not supported. `Overview` formulas count up to 1,999 papers and 199 resources; extend those ranges when the catalog grows beyond them.

The importer refuses duplicate IDs/URLs, unknown controlled vocabulary, missing required fields, unsupported catalog formulas, resources on the wrong sheet, and imports that silently remove existing IDs. It validates before writing. For a deliberate deletion, review and remove the record from the JSON and Excel together, then run `--build-readme` and `--check`.

## Scope and counts

Broad coverage should follow the conceptual gaps in the survey. Do not add unrelated papers to reach a round number. Retain foundational QA and planning work in the related section, and distinguish a benchmark's task requirements from the properties its grader actually inspects. A long run or many files does not by itself establish persistent responsibility or greater autonomy.

The README is generated. To change the presentation or curation text, edit `scripts/catalog.py`, run `python3 scripts/catalog.py --build-readme`, and check the diff. For metadata changes, edit the Excel first so that the workbook, JSON, and README stay synchronized.
