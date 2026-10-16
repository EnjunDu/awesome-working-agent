# Contributing

Contributions can add missing papers, correct metadata, improve classification boundaries, or share reading notes. Public-facing text is in English. The internal Excel uses Chinese labels and notes for the writing team.

## Edit the Excel, then synchronize

1. Open `paper_list.xlsx`. `Paper List` contains academic work; `Resources` contains products, official articles, documentation, and projects without an identified paper. Keep one record per paper and retain its stable `WA-xxxx` ID.
2. Choose a manuscript section code in column H. Columns F, G, and I automatically show its chapter, section, and subsection through lookups into `Taxonomy`. These three columns are derived labels. Add research subtypes, core capabilities, other relevant sections, and optimization mechanisms in their separate columns.
3. Use the yellow columns for the team's reading status, owner, writing section, and writing notes. The source list's reading-depth claim is a separate provenance field. It does not mean a team member has read the paper.
4. Save the workbook, then run from the repository root:

   ```bash
   python3 scripts/catalog.py --import-xlsx paper_list.xlsx
   python3 scripts/catalog.py --check
   python3 -m unittest discover -s tests
   ```

   Python's standard library is sufficient. The importer validates before updating the JSON catalog and README. It reads but does not reformat the workbook. Workbook values are authoritative: a blank cell clears the corresponding field.
5. Review and commit the Excel, `data/papers.json`, and generated `README.md` together. Coordinate simultaneous workbook edits through pull requests and reconcile conflicts by stable ID. Excel files do not merge reliably.

## Add a paper

- Append a row to the correct Excel table. Choose a new unused stable ID; never renumber existing IDs. Copy the derived formulas in F, G, and I from the previous row and select a valid section code in H.
- Use the full English title, a primary paper URL, and the first confirmed public release year when available. A conference version, renamed project, and preprint of the same work share one record.
- Record publication-time affiliations from the paper's front matter or an official project source. Explain a shortened institution list or version-specific affiliation in the verification notes. Do not infer historical affiliations from current employment.
- Keep methods, benchmarks, frameworks, surveys, background studies, and non-paper resources distinct. A multi-role paper may use `Method;Benchmark`. `Product/Resource` must stand alone and belongs in `Resources`.
- Add code and data URLs only when identified by the paper or official project. Distinguish a sample from the full dataset, and a resource collection from a direct dataset download.
- Record the contribution, its use in the survey, and the limits of the evidence separately. Do not promote an abstract-level candidate to a detailed experimental or causal claim without checking the relevant methods and results.

## Classification and vocabulary

The public README has only three broad paper lists: **Agents, Methods & Systems**, **Benchmarks & Evaluation**, and **Surveys & Foundations**. Fine classification belongs in the Excel, following [the manuscript guide](docs/taxonomy.md).

- The primary section is an authoring destination. Additional uses belong in the secondary-section field. The retired chapter 4 capability material moves to 2.3.1-2.3.5; original section mappings remain in a separate legacy field.
- Research subtypes, the five core capabilities, optimization mechanisms, and legacy work domains are different dimensions. Do not merge them into a single type hierarchy.
- Multi-value fields use English semicolons. Controlled fields accept either vocabulary codes or their Chinese labels from `Taxonomy`. Secondary sections accept codes with or without their displayed names.
- Keep titles and short names in English. The README generator rejects Chinese public titles. Chinese contributions, evidence limits, classifications, and team notes are supported in the Excel and catalog.
- Edit `data/taxonomy.json` and the Excel glossary together when changing vocabulary. Extend the lookup and validation ranges when adding section nodes. Use examples and counterexamples to explain a proposed boundary change. `data/workbook_schema.json` defines the workbook's columns and import rules.

## Verification and source provenance

`verified` means the paper identity and the recorded affiliation have source evidence. `metadata-only` means the identity is checked but the affiliation is incomplete. `pending` means the identity remains unresolved; these records stay in the workbook and JSON but are omitted from public paper tables.

These statuses do not imply full-paper reading, peer review, or exhaustive coverage. The 2026-10-16 supplement's original reading-depth and citation-status statements are preserved as source claims. Its appendix explicitly says the entries were not rechecked; previous independent bibliographic verification is kept separate. `data/source_ledger.json` reconciles every supplement item to a stable catalog ID.

The Section 3 evidence pack is reconciled in `data/literature_sources/section3_2026.json`, with a companion BibTeX collection. Excel columns AN to AX retain publication metadata and task-specific evidence for its 76 records. Add new claim codes to `section3_claims` in the taxonomy and to the workbook glossary together. Keep publication status separate from `verification_status`: acceptance is not formal publication, and neither proves that a team member has read the paper. `publication_year` is numeric and remains blank for preprints and accepted papers awaiting publication. Source priorities A/B/F describe writing use and do not replace the team's assignments.

The importer rejects unknown controlled terms, unsupported formulas, duplicate IDs or canonical paper URLs, resources on the wrong sheet, and any import that silently removes an existing ID. Literal URL cells and `HYPERLINK("url","url")` are supported; other formulas are allowed only in the three derived classification-label columns. Both Excel date systems are supported.

The summary formulas cover up to 1,999 academic records and 199 non-paper resources. Extend their ranges when the collection grows beyond those bounds. For a deliberate deletion, review and remove the same ID from the JSON and Excel together, then run `--build-readme` and `--check`.

The README is generated. Edit its layout or English curation text in `scripts/catalog.py`, then run `python3 scripts/catalog.py --build-readme`. Add work to close conceptual gaps, rather than to reach a round paper count.
