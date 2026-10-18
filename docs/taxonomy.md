# Manuscript classification v0.4

The public awesome list uses three broad paper groups. The companion Excel carries the detailed authoring classification, following the revised manuscript outline and the 2026-10-16 literature supplement. Classification is an editorial judgment about how a source supports the survey, not an author's claim about the paper.

## Manuscript hierarchy

| Manuscript location | Role in the survey |
| --- | --- |
| 2.1 Definition and System View | Work scope, system responsibilities, the six process elements, and formalization |
| 2.2 Working Conditions | Work persistence and work-world openness |
| 2.3 Core Capabilities | Five capabilities needed to complete reliable digital work |
| 2.4 Related Agent Paradigms | Long-horizon, computer-use, and office agents |
| 3 Work Forms | Response, atomic action, multi-step, workflow, and workspace work |
| 5 Optimization | Environments, data, rewards, model learning, harness design, and joint optimization |
| 6 Evaluation and Resources | Tasks, observable evidence, judging, outcome metrics, and execution infrastructure |
| 7 Frontiers | Realistic environments, persistent responsibility, verification, and work-centric systems |

The workbook dictionary contains 65 explicit nodes from the available outline. It does not invent new numbered subsections. The former chapter 4 capability material now maps to chapter 2.3. Its original references are retained in a legacy field; no active record uses a chapter 4 code. Chapters 3, 5, 6, and 7 retain the supplied outline's numbering.

| Current capability section | Capability | Former location |
| --- | --- | --- |
| 2.3.1 | Perception and Understanding | 4.1 |
| 2.3.2 | Reasoning and Decision Making | 4.2 |
| 2.3.3 | Planning and Coordination | 4.3 |
| 2.3.4 | Execution and State Management | 4.4 |
| 2.3.5 | Verification, Recovery, and Replanning | 4.5 |

## Independent classification fields

Each academic record has one **primary manuscript section**, plus any useful **secondary sections**. The primary section gives the main authoring destination, allowing chapter counts without double counting. Secondary mappings retain other uses of the same paper.

The Excel displays chapter, section, subsection, research subtype, core capabilities, and optimization mechanisms in separate columns. Its 45 reusable research subtypes cover issues such as native object semantics, cross-object relations, evidence retrieval, professional judgment, dependency planning, state validity, object integrity, failure diagnosis, recovery, rewards, and judging procedures. These terms refine the manuscript hierarchy without creating invented subsection numbers.

Five capability tags summarize the research focus or task requirements. They do not establish that an evaluated model possesses the capability, and a benchmark's aggregate success rate is not an isolated capability measurement.

The original ten work-domain categories remain as legacy metadata for continuity. They no longer determine the public README sections or the main Excel classification.

## Section 3 evidence and publication metadata

The Section 3 research pack links 76 papers to 18 writing claims. These claim codes are displayed in the workbook's `Taxonomy` sheet; they are evidence labels, not additional manuscript subsections. The pack's primary work form is added as a secondary writing use when a paper already has a primary authoring destination.

Columns AN to AX record publication status, venue, publication year, publication URL, claim codes, evidence locations, evidence URLs, the applicable task or subset, BibTeX keys, citation audits, and source writing priorities. `published`, `accepted`, and `preprint` are distinct from affiliation verification. The existing year column retains the first confirmed public year; the publication-year column records formal publication only. Empty publication metadata means it was not covered by this source update.

Source priorities A, B, and F mean main-text choice, supporting or boundary evidence, and historical foundation. They do not grade research quality. The original source's reading-depth statements remain separate from team reading assignments.

Work forms depend on the delegated task and the evaluated setting. Grounding coordinates and function-call syntax do not establish a successful state change. Workflow generation or prediction does not establish business workflow execution. Given-context and full-workspace settings from the same paper can support different forms. The five forms are not assumed to be mutually exclusive or a strict capability ranking.

## Optimization mechanisms

The Section 5 source adds 127 chapter-specific uses. Its primary destination is retained separately in Excel column AY, so an existing paper's use in another chapter remains visible. Three existing Chapter 5 destinations are refined: EnterpriseLab to trajectory curation (5.1.2), CogEvol to supervised training (5.2.1), and UI-Mate to agentic reinforcement learning (5.2.2). Their earlier destinations remain secondary uses. The source's legacy capability chapter 4 is mapped to the active 2.3.1–2.3.5 sections.

Columns AZ to BJ preserve source reading suggestions, concrete methods and optimization mechanisms, executor-weight updates, harness targets, environments, identifiers, dates, publication snapshots, evidence limits, and version notes. These source details complement the controlled research-type vocabulary; they do not introduce a new category for every paper. Training a prompt or harness designer is distinct from updating the downstream executor, and optimizing multiple harness components does not by itself establish joint model-weight training.

| Mechanism | Section |
| --- | --- |
| Task and environment synthesis | 5.1.1 |
| Trajectory collection and curation | 5.1.2 |
| Reward and verification signals | 5.1.3 |
| Mid-training and supervised fine-tuning | 5.2.1 |
| Agentic reinforcement learning | 5.2.2 |
| On-policy distillation | 5.2.3 |
| Self-improving model training | 5.2.4 |
| Tool and interface optimization | 5.3.1 |
| Prompt and workflow optimization | 5.3.2 |
| Memory and skill optimization | 5.3.3 |
| Model-harness coupling and joint optimization | 5.4 |

Mechanism tags can overlap. Being cited in an optimization section is not sufficient evidence that a paper proposes that mechanism. Inference-time search is distinct from learning a better harness across tasks; verbal reflection does not itself imply gradient-based reinforcement learning.

## Evidence boundaries

- **Persistence:** distinguish elapsed execution, information retention, and a delegated responsibility that remains open. AA-Briefcase v1.1 uses independent task runs; a multi-week project background does not establish cross-task state continuity.
- **Perception and professional judgment:** specialist notation and document parsing concern object understanding. They do not automatically establish professional decisions or end-to-end work execution.
- **Editing and completion:** preserving a document under controlled edits is useful evidence about integrity. It does not by itself establish business task success, user satisfaction, or realized economic value.
- **Recovery and transactions:** selected environment rollback with retained reflection is distinct from idempotency, commit protocols, and transaction guarantees.
- **Variants:** PPTAgent's PPTEval and Microsoft's PPT-Eval are different resources. AgentWorld and Agent World Model are different papers. A renamed arXiv revision such as C-World/ToolGym is one paper.
- **Reading depth:** source-list statements about abstract screening, project inspection, or relevant full-text sections are provenance. They remain separate from the team's reading status.

The controlled nodes and terms are stored in `data/taxonomy.json` and displayed with Chinese labels in Excel. See [Contributing](../CONTRIBUTING.md) for editing, synchronization, and evidence requirements.
