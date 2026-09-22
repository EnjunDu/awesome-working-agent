# Awesome Working Agents

> A curated list of papers on AI agents that perform real-world **digital work** — over artifacts, workspaces, applications, tools, and persistent environments.

**Scope.** We include work where *an agent must perform or maintain digital work over artifacts, workspaces, applications, tools, or persistent environments.* Pure question answering and document understanding — however professional the domain — are collected separately under [Related](#-related-work-oriented-reasoning--document-understanding), so that this list does not gradually expand into "Awesome Document QA + Tool Agent + GUI Agent + Long Context".

Sections are organized by **what the agent works on**, not by Method/Benchmark split, so that methods and benchmarks on the same research line sit together. Domain (finance, legal, …) and research focus (planning, memory, …) are **tags**, never sections — a single paper like APEX-Agents spans investment banking, consulting and corporate law, and would otherwise be duplicated three times. Three later sections are an exception: harnesses, verification and safety cut across every artifact type, and splitting them by artifact would scatter one research line across five tables.

**How we read this literature.** The companion survey separates three questions that a single "difficulty" ordering tends to merge:

- **Work composition** — what structure of work is delegated, and what structure must hold for it to be *accepted*: an informational response, a bounded effect, a coherent goal, a dependency-structured process, or a coupled set of deliverables. Crossing applications, running long, or touching many files does not by itself move a task up this scale.
- **Work persistence** — how long the state, commitments, dependencies and invariants bearing on acceptance must survive. Time horizon and responsibility horizon are different quantities: an eight-hour task scored the moment it ends leaves nothing outstanding.
- **Work-world openness** — how much of the relevant world can be enumerated before execution: object discovery, representational heterogeneity, dynamics, external actors, authority, and whether more than one action sequence is acceptable.

These are orthogonal, which is why the list is not sorted by any of them.

---

## Contents

- [📄 Artifact-Centric Agents](#-artifact-centric-agents)
- [🗂️ Workspace & Cross-Artifact Agents](#️-workspace--cross-artifact-agents)
- [🖥️ Computer-Use & Application Agents](#️-computer-use--application-agents)
- [🔧 Tool, API & Enterprise Workflow Agents](#-tool-api--enterprise-workflow-agents)
- [🕒 Persistent & Long-Horizon Work Agents](#-persistent--long-horizon-work-agents)
- [🧩 Harnesses, Platforms & Workflow Construction](#-harnesses-platforms--workflow-construction)
- [✅ Verification, Judging & Feedback](#-verification-judging--feedback)
- [🛡️ Safety, Injection & Side-Effect Control](#️-safety-injection--side-effect-control)
- [📚 Related: Work-Oriented Reasoning & Document Understanding](#-related-work-oriented-reasoning--document-understanding)
- [🔗 Adjacent: SWE, ML & Research Agents](#-adjacent-swe-ml--research-agents)
- [Tag Vocabulary](#tag-vocabulary)
- [Contributing](#contributing)

---

## Tag Vocabulary

Tags are a **closed vocabulary**. Do not invent new ones without a PR discussion.

**① Artifact / Interface** — pick 1–2

`spreadsheet` `document` `slides` `pdf` `code` `multi-file` `gui` `browser` `terminal` `api` `database`

**② Work Property** — pick 1–2

`generation` `editing` `cross-file` `state-change` `long-horizon` `interactive`

**③ Domain** — pick 1 (2 only if genuinely cross-domain)

`general` `office` `finance` `legal` `healthcare` `science` `enterprise` `ecommerce`

**④ Evaluation** *(benchmarks only)* — pick 1–2

| tag | what the grader looks at |
|---|---|
| `answer-eval` | a returned value, label, or text |
| `artifact-eval` | the produced file, parsed and inspected |
| `state-eval` | the resulting workspace / database / system state |
| `trajectory-eval` | execution logs or cross-session evidence |

**⑤ Research Focus** *(methods only)* — pick 1–2

`planning` `tool-use` `memory` `verification` `self-correction` `collaboration` `learning`

Benchmarks carry tags from ①②③④; methods carry ①⑤③. A benchmark does not "focus on planning" — it *probes* planning, which is why ⑤ is reserved for methods.

**Availability** is written inline in the Links column rather than as a tag: absence of a `[Data]` link means the data is not publicly downloadable, annotated as *gated*, *leaderboard only*, *not released*, or *private*.

---

## 📄 Artifact-Centric Agents

The unit of work is **one well-defined deliverable**: a workbook, a deck, a document, a report. The target file is given; the agent produces or edits it.

### Benchmarks

| Paper | Venue | Links | Tags |
|---|---|---|---|
| **SpreadsheetBench 2** | arXiv 2026 | [Paper](https://arxiv.org/abs/2606.29955) · [Data](https://huggingface.co/datasets/KAKA22/SpreadsheetBench-v2) | `spreadsheet` `editing` `finance` `artifact-eval` |
| **BlueFin** | arXiv 2026 | [Paper](https://arxiv.org/abs/2605.30907) | `spreadsheet` `generation` `finance` `artifact-eval` |
| **Finch / FinWorkBench** | ACL 2026 | *not released* | `spreadsheet` `cross-file` `finance` `artifact-eval` |
| **Excel Modeling Bench** | vals.ai | *leaderboard only* | `spreadsheet` `generation` `finance` `artifact-eval` |
| **PresentBench** | 2025 | [Data](https://huggingface.co/datasets/lynnzuo/PresentBench) | `slides` `generation` `general` `artifact-eval` |
| **PPTC** | arXiv 2023 | [Paper](https://arxiv.org/abs/2311.01767) · [Code](https://github.com/gydpku/PPTC) | `slides` `editing` `office` `artifact-eval` |
| **PPTEval / PPTAgent** | EMNLP 2025 | [Code](https://github.com/icip-cas/PPTAgent) | `slides` `generation` `office` `artifact-eval` |
| **OmegaUse-OfficeVal** | Baidu, 2025 | [Data](https://huggingface.co/datasets/baidu-frontier-research/OmegaUse-OfficeVal) | `document` `editing` `office` `artifact-eval` |
| **MedScribe** | vals.ai | *leaderboard only* | `document` `generation` `healthcare` `artifact-eval` |
| **SpreadsheetBench** | NeurIPS 2024 | [Paper](https://arxiv.org/abs/2406.14991) | `spreadsheet` `editing` `office` `artifact-eval` |
| **InstructExcel** | EMNLP 2023 | — | `spreadsheet` `editing` `office` `artifact-eval` |
| **DocVQA** | WACV 2021 | [Paper](https://arxiv.org/abs/2007.00398) | `pdf` `generation` `general` `answer-eval` |

### Methods

| Paper | Venue | Links | Tags |
|---|---|---|---|
| **SheetCopilot** | NeurIPS 2023 | [Paper](https://arxiv.org/abs/2305.19308) | `spreadsheet` `tool-use` `office` |
| **SpreadsheetLLM** | arXiv 2024 | [Paper](https://arxiv.org/abs/2407.09025) | `spreadsheet` `tool-use` `office` |
| **Spreadsheet-RL** | arXiv 2026 | [Paper](https://arxiv.org/abs/2605.22642) | `spreadsheet` `learning` `office` |
| **PPTAgent** | EMNLP 2025 | [Paper](https://arxiv.org/abs/2501.03936) · [Code](https://github.com/icip-cas/PPTAgent) | `slides` `planning` `office` |
| **AutoPresent** | CVPR 2025 | — | `slides` `learning` `general` |
| **AeSlides** | arXiv 2026 | [Paper](https://arxiv.org/abs/2604.22840) | `slides` `learning` `general` |
| **Learning to Present (SlideRL)** | arXiv 2026 | [Paper](https://arxiv.org/abs/2603.16839) | `slides` `learning` `general` |
| **CoEdIT** | EMNLP 2023 | — | `document` `learning` `general` |
| **PEER** | arXiv 2022 | [Paper](https://arxiv.org/abs/2208.11663) | `document` `collaboration` `general` |

---

## 🗂️ Workspace & Cross-Artifact Agents

Not "here is the file, edit it" but **"enter a workspace, find the material yourself, work out how the pieces relate, then deliver"**. File discovery, version and lineage reasoning, dependency tracking, and multi-artifact deliverable packages live here.

### Benchmarks

| Paper | Venue | Links | Tags |
|---|---|---|---|
| **Workspace-Bench** | ByteDance, arXiv 2026 | [Paper](https://arxiv.org/abs/2605.03596) · [Data](https://huggingface.co/datasets/Workspace-Bench/Workspace-Bench) | `multi-file` `cross-file` `general` `state-eval` |
| **BankerToolBench** | arXiv 2026 | [Paper](https://arxiv.org/abs/2604.11304) · [Data](https://huggingface.co/datasets/handshake-ai-research/bankertoolbench) | `multi-file` `generation` `finance` `artifact-eval` |
| **GDPval** | OpenAI, 2025 | [Data](https://huggingface.co/datasets/openai/gdpval) | `multi-file` `generation` `general` `artifact-eval` |
| **JOBBench** | 2025 | [Data](https://huggingface.co/datasets/JobBench/job-bench) | `multi-file` `generation` `general` `artifact-eval` |
| **APEX-Agents** | Mercor, 2025 | [Data](https://huggingface.co/datasets/mercor/apex-agents) *(gated)* · [Recipe](https://github.com/Mercor-Intelligence/ApexAgents-SkyRL-Recipe) | `multi-file` `long-horizon` `finance` `artifact-eval` |
| **PinchBench** | 2025 | [Code](https://github.com/pinchbench/skill) | `multi-file` `cross-file` `office` `artifact-eval` |
| **WorkBuddy-Bench** | Tencent, arXiv 2026 | [Paper](https://arxiv.org/abs/2607.20911) · [Data](https://huggingface.co/datasets/tencent/workbuddy-bench) | `multi-file` `editing` `general` `artifact-eval` |
| **Harvey LAB / BigLaw Bench** | Harvey, 2024 | [LAB](https://github.com/harveyai/harvey-labs) · [BigLaw](https://github.com/harveyai/biglaw-bench) | `document` `cross-file` `legal` `artifact-eval` |
| **PRBench** | ACL 2026 | [Paper](https://arxiv.org/abs/2511.11562) | `document` `generation` `finance` `artifact-eval` |
| **Remote Labor Index** | arXiv 2025 | [Paper](https://arxiv.org/abs/2510.26787) | `multi-file` `generation` `general` `artifact-eval` |
| **CentaurBench** | arXiv 2026 | [Paper](https://arxiv.org/abs/2608.18554) | `multi-file` `interactive` `general` `artifact-eval` |
| **AA-AnalystAgent** | Artificial Analysis | *private* | `spreadsheet` `generation` `finance` `answer-eval` |
| **OfficeBench** | arXiv 2024 | [Paper](https://arxiv.org/abs/2407.19056) · [Code](https://github.com/zlwang-cs/OfficeBench) | `multi-file` `cross-file` `office` `state-eval` |
| **GAIA** | ICLR 2024 | [Paper](https://arxiv.org/abs/2311.12983) | `multi-file` `cross-file` `general` `answer-eval` |
| **AssistantBench** | EMNLP 2024 | [Paper](https://arxiv.org/abs/2407.15711) | `browser` `cross-file` `general` `answer-eval` |
| **BrowseComp** | arXiv 2025 | [Paper](https://arxiv.org/abs/2504.12516) | `browser` `cross-file` `general` `answer-eval` |

### Methods

| Paper | Venue | Links | Tags |
|---|---|---|---|
| *contributions welcome* | | | |

---

## 🖥️ Computer-Use & Application Agents

The agent drives a **computer**: GUI, desktop applications, browser, OS, or a real terminal harness. The interface itself is the object of study.

### Benchmarks

| Paper | Venue | Links | Tags |
|---|---|---|---|
| **OSWorld** | NeurIPS 2024 | [Code](https://github.com/xlang-ai/OSWorld) | `gui` `state-change` `general` `state-eval` |
| **WorkArena** | ServiceNow, ICML 2024 | [Data](https://huggingface.co/datasets/ServiceNow/WorkArena-Instances) | `browser` `state-change` `enterprise` `state-eval` |
| **WorkArena++** | arXiv 2024 | [Paper](https://arxiv.org/abs/2407.05291) | `browser` `long-horizon` `enterprise` `state-eval` |
| **Windows Agent Arena** | Microsoft, 2024 | — | `gui` `state-change` `office` `state-eval` |
| **FieldWorkArena** | arXiv 2025 | [Paper](https://arxiv.org/abs/2505.19662) | `gui` `state-change` `enterprise` `state-eval` |
| **WildClawBench** | arXiv 2026 | [Paper](https://arxiv.org/abs/2605.10912) | `terminal` `long-horizon` `general` `trajectory-eval` |
| **WebArena** | ICLR 2024 | [Paper](https://arxiv.org/abs/2307.13854) | `browser` `state-change` `general` `state-eval` |
| **VisualWebArena** | ACL 2024 | [Paper](https://arxiv.org/abs/2401.13649) | `browser` `state-change` `general` `state-eval` |
| **VideoWebArena** | arXiv 2024 | [Paper](https://arxiv.org/abs/2410.19100) | `browser` `long-horizon` `general` `state-eval` |
| **WebShop** | NeurIPS 2022 | [Paper](https://arxiv.org/abs/2207.01206) | `browser` `state-change` `ecommerce` `state-eval` |
| **Mind2Web** | NeurIPS 2023 | [Paper](https://arxiv.org/abs/2306.06070) | `browser` `state-change` `general` `trajectory-eval` |
| **WebLINX** | ICML 2024 | [Paper](https://arxiv.org/abs/2402.05930) | `browser` `interactive` `general` `trajectory-eval` |
| **AndroidWorld** | ICLR 2025 | [Paper](https://arxiv.org/abs/2405.14573) | `gui` `state-change` `general` `state-eval` |
| **ScreenSpot-Pro** | arXiv 2025 | [Paper](https://arxiv.org/abs/2504.07981) | `gui` `state-change` `office` `answer-eval` |

### Methods

| Paper | Venue | Links | Tags |
|---|---|---|---|
| **SWE-agent** | NeurIPS 2024 | [Paper](https://arxiv.org/abs/2405.15793) | `code` `tool-use` `general` |
| **WebRL** | ICLR 2025 | [Paper](https://arxiv.org/abs/2411.02337) | `browser` `learning` `general` |
| **DigiRL** | NeurIPS 2024 | [Paper](https://arxiv.org/abs/2406.11896) | `gui` `learning` `general` |
| **ComputerRL** | arXiv 2025 | [Paper](https://arxiv.org/abs/2508.14040) | `gui` `learning` `general` |
| **Agent Q** | arXiv 2024 | [Paper](https://arxiv.org/abs/2408.07199) | `browser` `planning` `general` |

---

## 🔧 Tool, API & Enterprise Workflow Agents

Work is done through **tools, function calls, APIs, MCP servers, databases and SaaS systems** rather than through a cursor. The goal is usually to execute a real business workflow and **change system state**.

### Benchmarks

| Paper | Venue | Links | Tags |
|---|---|---|---|
| **AutomationBench** | Upstage, 2025 | [Data](https://huggingface.co/datasets/UpstageShareSpace/automationBench) | `api` `state-change` `enterprise` `state-eval` |
| **τ²-bench** | Sierra, 2025 | [Code](https://github.com/sierra-research/tau2-bench) · [Data](https://huggingface.co/datasets/HuggingFaceH4/tau2-bench-data) | `database` `state-change` `enterprise` `state-eval` |
| **EnterpriseOps-Gym** | ServiceNow, 2025 | [Data](https://huggingface.co/datasets/ServiceNow-AI/EnterpriseOps-Gym) | `api` `state-change` `enterprise` `state-eval` |
| **E-Bench** | Tencent, arXiv 2026 | [Paper](https://arxiv.org/abs/2607.23722) | `api` `state-change` `general` `state-eval` |
| **EcomAgentBench / E-Commerce Bench** | arXiv 2026 | [Paper](https://arxiv.org/abs/2608.30730) · [Code](https://github.com/Morizeyao/EComAgentBench_) · [Data](https://huggingface.co/datasets/ecomagentbench/EcomAgentBenchProductDB) | `database` `state-change` `ecommerce` `state-eval` |
| **Toolathlon** | HKUST, 2025 | [Data](https://huggingface.co/datasets/hkust-nlp/Toolathlon) *(gated)* · [Gym](https://github.com/eigent-ai/toolathlon_gym) | `api` `state-change` `general` `state-eval` |
| **AppWorld** | ACL 2024 *(Best Resource)* | — | `api` `state-change` `general` `state-eval` |
| **MCP-Atlas** | arXiv 2026 | [Paper](https://arxiv.org/abs/2602.00933) | `api` `state-change` `general` `state-eval` |
| **OmniaBench** | Huawei, 2025 | [Code](https://github.com/scuuy/OmniaBench) | `api` `state-change` `general` `state-eval` |
| **TheAgentCompany** | 2024 | [Code](https://github.com/TheAgentCompany/TheAgentCompany) | `multi-file` `long-horizon` `enterprise` `state-eval` |
| **CRMArena** | NAACL 2025 | [Paper](https://arxiv.org/abs/2411.02305) | `database` `state-change` `enterprise` `state-eval` |
| **CRMArena-Pro** | arXiv 2025 | [Paper](https://arxiv.org/abs/2505.18878) | `database` `state-change` `enterprise` `state-eval` |
| **EnterpriseBench** | EMNLP 2025 | — | `multi-file` `long-horizon` `enterprise` `state-eval` |
| **EnterpriseClawBench** | arXiv 2026 | [Paper](https://arxiv.org/abs/2606.23654) *(protocol only, data private)* | `api` `state-change` `enterprise` `state-eval` |
| **CI-Work** | ACL 2026 | — | `api` `state-change` `enterprise` `trajectory-eval` |
| **PSEBench** | arXiv 2026 | [Paper](https://arxiv.org/abs/2606.05463) | `document` `interactive` `healthcare` `answer-eval` |
| **API-Bank** | EMNLP 2023 | [Paper](https://arxiv.org/abs/2304.08244) | `api` `state-change` `general` `answer-eval` |
| **ToolLLM / ToolBench** | ICLR 2024 | [Paper](https://arxiv.org/abs/2307.16789) | `api` `state-change` `general` `answer-eval` |
| **ToolSandbox** | arXiv 2024 | [Paper](https://arxiv.org/abs/2408.04682) | `api` `state-change` `general` `state-eval` |
| **τ-bench** | arXiv 2024 | [Paper](https://arxiv.org/abs/2406.12045) | `database` `interactive` `enterprise` `state-eval` |
| **MINT** | ICLR 2024 | [Paper](https://arxiv.org/abs/2309.10691) | `api` `interactive` `general` `trajectory-eval` |
| **WorkBench** | arXiv 2024 | [Paper](https://arxiv.org/abs/2405.00823) | `database` `state-change` `enterprise` `state-eval` |
| **TravelPlanner** | ICML 2024 | [Paper](https://arxiv.org/abs/2402.01622) | `api` `state-change` `general` `answer-eval` |
| **Flex-TravelPlanner** | arXiv 2025 | [Paper](https://arxiv.org/abs/2506.04649) | `api` `interactive` `general` `answer-eval` |
| **PlanBench** | NeurIPS 2023 | [Paper](https://arxiv.org/abs/2206.10498) | `api` `state-change` `general` `answer-eval` |

### Methods

| Paper | Venue | Links | Tags |
|---|---|---|---|
| **ReAct** | ICLR 2023 | [Paper](https://arxiv.org/abs/2210.03629) | `api` `planning` `general` |
| **Toolformer** | NeurIPS 2023 | [Paper](https://arxiv.org/abs/2302.04761) | `api` `tool-use` `general` |
| **CodeAct** | ICML 2024 | [Paper](https://arxiv.org/abs/2402.01030) | `code` `tool-use` `general` |
| **ReTool** | arXiv 2025 | [Paper](https://arxiv.org/abs/2504.11536) | `code` `learning` `general` |
| **LLM+P** | arXiv 2023 | [Paper](https://arxiv.org/abs/2304.11477) | `api` `planning` `general` |
| **AutoGen** | arXiv 2023 | [Paper](https://arxiv.org/abs/2308.08155) | `api` `collaboration` `general` |
| **CAMEL** | NeurIPS 2023 | [Paper](https://arxiv.org/abs/2303.17760) | `api` `collaboration` `general` |
| **MetaGPT** | ICLR 2024 | [Paper](https://arxiv.org/abs/2308.00352) | `code` `collaboration` `general` |
| **ChatDev** | ACL 2024 | [Paper](https://arxiv.org/abs/2307.07924) | `code` `collaboration` `general` |

---

## 🕒 Persistent & Long-Horizon Work Agents

Work that **survives the session**: multi-day or multi-week projects, long-term state, evolving environments, constraints established earlier that must still hold later. This is the newest and thinnest section — which is itself informative.

### Benchmarks

| Paper | Venue | Links | Tags |
|---|---|---|---|
| **AA-Briefcase** | Artificial Analysis, 2025 | [Lite](https://huggingface.co/datasets/ArtificialAnalysis/AA-Briefcase-Lite) · [Harness](https://github.com/ArtificialAnalysis/Stirrup) *(full set private)* | `multi-file` `long-horizon` `general` `artifact-eval` |
| **VibeLifeBench** | Xiaohongshu, 2025 | [Data](https://huggingface.co/datasets/EvolventAI/Vibelifebench) | `database` `long-horizon` `general` `trajectory-eval` |
| **OdysseyBench** | Microsoft Research, 2025 | *not released* | `multi-file` `long-horizon` `office` `state-eval` |
| **Agents' Last Exam (ALE-CLI)** | arXiv 2026 | [Paper](https://arxiv.org/abs/2606.05405) | `terminal` `long-horizon` `science` `artifact-eval` |
| **AgentIF-OneDay** | arXiv 2026 | [Paper](https://arxiv.org/abs/2601.20613) | `multi-file` `interactive` `general` `artifact-eval` |
| **ResearchRubrics** | arXiv 2025 | [Paper](https://arxiv.org/abs/2511.07685) | `document` `long-horizon` `science` `artifact-eval` |
| **LongMemEval** | ICLR 2025 | [Paper](https://arxiv.org/abs/2410.10813) | `database` `long-horizon` `general` `answer-eval` |
| **LoCoMo** | ACL 2024 | [Paper](https://arxiv.org/abs/2402.17753) | `database` `long-horizon` `general` `answer-eval` |
| **METR time horizon** | arXiv 2025 | [Paper](https://arxiv.org/abs/2503.14499) | `code` `long-horizon` `general` `trajectory-eval` |
| **AgentBoard** | NeurIPS 2024 | [Paper](https://arxiv.org/abs/2401.13178) | `api` `long-horizon` `general` `trajectory-eval` |

### Methods

| Paper | Venue | Links | Tags |
|---|---|---|---|
| **MemGPT** | arXiv 2023 | [Paper](https://arxiv.org/abs/2310.08560) | `api` `memory` `general` |
| **Mem0** | arXiv 2025 | [Paper](https://arxiv.org/abs/2504.19413) | `database` `memory` `general` |
| **Generative Agents** | UIST 2023 | [Paper](https://arxiv.org/abs/2304.03442) | `api` `memory` `general` |
| **Voyager** | TMLR 2024 | [Paper](https://arxiv.org/abs/2305.16291) | `code` `learning` `general` |
| **ExpeL** | AAAI 2024 | [Paper](https://arxiv.org/abs/2308.10144) | `api` `learning` `general` |
| **On-Policy Distillation** | arXiv 2026 | [Paper](https://arxiv.org/abs/2604.13016) | `api` `learning` `general` |

---

## 🧩 Harnesses, Platforms & Workflow Construction

The object of study is the **system around the model**: the action and observation interface, the execution platform, and the procedure itself. These entries change what an agent can do without changing its weights, which is why the survey treats a reported score as belonging to a configuration rather than to a model.

| Paper | Venue | Links | Tags |
|---|---|---|---|
| **OpenHands** | ICLR 2025 | [Paper](https://arxiv.org/abs/2407.16741) · [Code](https://github.com/All-Hands-AI/OpenHands) | `code` `tool-use` `general` |
| **BrowserGym** | arXiv 2024 | [Paper](https://arxiv.org/abs/2412.05467) · [Code](https://github.com/ServiceNow/BrowserGym) | `browser` `tool-use` `general` |
| **AFlow** | ICLR 2025 | [Paper](https://arxiv.org/abs/2410.10762) | `api` `planning` `general` |
| **ADAS** | ICLR 2025 | [Paper](https://arxiv.org/abs/2408.08435) | `api` `planning` `general` |
| **AgentSquare** | ICLR 2025 | [Paper](https://arxiv.org/abs/2410.06153) | `api` `planning` `general` |
| **Agent Workflow Memory** | arXiv 2024 | [Paper](https://arxiv.org/abs/2409.07429) | `browser` `memory` `general` |
| **Code as Agent Harness** | arXiv 2026 | [Paper](https://arxiv.org/abs/2605.18747) | `code` `tool-use` `general` |

---

## ✅ Verification, Judging & Feedback

How anyone establishes that the work is actually correct, and what happens when it is not. Runtime checking, external judging, reward modelling and self-correction sit together because they differ in *purpose* rather than in mechanism: the same checker can drive a repair, score a run, or supply a training signal.

| Paper | Venue | Links | Tags |
|---|---|---|---|
| **Agent-as-a-Judge** | arXiv 2024 | [Paper](https://arxiv.org/abs/2410.10934) | `multi-file` `verification` `general` |
| **AgentRewardBench** | arXiv 2025 | [Paper](https://arxiv.org/abs/2504.08942) | `browser` `verification` `general` |
| **Process Reward Models That Think** | arXiv 2025 | [Paper](https://arxiv.org/abs/2504.16828) | `code` `verification` `general` |
| **CRITIC** | ICLR 2024 | [Paper](https://arxiv.org/abs/2305.11738) | `api` `self-correction` `general` |
| **Self-Refine** | NeurIPS 2023 | [Paper](https://arxiv.org/abs/2303.17651) | `document` `self-correction` `general` |
| **Reflexion** | NeurIPS 2023 | [Paper](https://arxiv.org/abs/2303.11366) | `api` `self-correction` `general` |
| **LATS** | ICML 2024 | [Paper](https://arxiv.org/abs/2310.04406) | `api` `planning` `general` |
| **SWT-Bench** | NeurIPS 2024 | [Paper](https://arxiv.org/abs/2406.12952) | `code` `verification` `general` |
| **MT-Bench / LLM-as-a-Judge** | NeurIPS 2023 | [Paper](https://arxiv.org/abs/2306.05685) | `document` `verification` `general` |

---

## 🛡️ Safety, Injection & Side-Effect Control

Completing the task and causing no disallowed effect are two conditions, not one. These resources measure the second: whether an agent preserves the boundary between evidence it reads and instructions it obeys, and whether it respects authority while acting.

| Paper | Venue | Links | Tags |
|---|---|---|---|
| **AgentDojo** | NeurIPS 2024 | [Paper](https://arxiv.org/abs/2406.13352) | `api` `state-change` `general` `trajectory-eval` |
| **InjecAgent** | ACL 2024 | [Paper](https://arxiv.org/abs/2403.02691) | `api` `state-change` `general` `trajectory-eval` |
| **ToolEmu** | ICLR 2024 | [Paper](https://arxiv.org/abs/2309.15817) | `api` `state-change` `general` `trajectory-eval` |
| **AgentHarm** | ICLR 2025 | [Paper](https://arxiv.org/abs/2410.09024) | `api` `state-change` `general` `trajectory-eval` |

---

## 📚 Related: Work-Oriented Reasoning & Document Understanding

Professional tasks that are **read-only**: the agent answers, classifies or cites, but never produces or modifies a work artifact. Kept separate so the main list stays about *doing* work.

| Paper | Venue | Links | Tags |
|---|---|---|---|
| **LegalBench** | NeurIPS 2023 | [Data](https://huggingface.co/datasets/nguha/legalbench) | `document` `legal` `answer-eval` |
| **Legal Research Bench** | vals.ai | [Code](https://github.com/vals-ai/legal-research-bench) *(samples only)* | `document` `legal` `answer-eval` |
| **Tax Agent Bench** | vals.ai | *leaderboard only* | `document` `finance` `answer-eval` |
| **Finance Agent v2** | arXiv 2025 | [Paper](https://arxiv.org/abs/2508.00828) · [Data](https://huggingface.co/datasets/vals-ai/finance_agent_benchmark) *(50/927 public)* | `pdf` `finance` `answer-eval` |
| **OfficeQA** | Databricks, 2025 | [Data](https://huggingface.co/datasets/databricks/officeqa) *(gated)* · [Mirror](https://huggingface.co/datasets/NEAR-AI/officeqa) | `pdf` `office` `answer-eval` |
| **MMLongBench-Doc** | NeurIPS 2024 | [Code](https://github.com/mayubo2333/MMLongBench-Doc) | `pdf` `general` `answer-eval` |
| **MedCode** | vals.ai | *leaderboard only* | `document` `healthcare` `answer-eval` |
| **MLCR-AA** | Wisedocs / AA | *private* | `document` `healthcare` `answer-eval` |
| **GDP.pdf** | Surge AI / AA | — | `pdf` `general` `answer-eval` |
| **FinQA** | EMNLP 2021 | [Paper](https://arxiv.org/abs/2109.00122) | `pdf` `finance` `answer-eval` |
| **TAT-QA** | ACL 2021 | [Paper](https://arxiv.org/abs/2105.07624) | `pdf` `finance` `answer-eval` |
| **ConvFinQA** | EMNLP 2022 | [Paper](https://arxiv.org/abs/2210.03849) | `pdf` `finance` `answer-eval` |
| **LawBench** | arXiv 2023 | [Paper](https://arxiv.org/abs/2309.16289) | `document` `legal` `answer-eval` |
| **ChartQA** | ACL 2022 | [Paper](https://arxiv.org/abs/2203.10244) | `pdf` `general` `answer-eval` |
| **OmniDocBench** | CVPR 2025 | [Paper](https://arxiv.org/abs/2412.07626) | `pdf` `general` `answer-eval` |

---

## 🔗 Adjacent: SWE, ML & Research Agents

Long-horizon agent benchmarks whose domain is software, ML engineering or scientific research rather than knowledge work. Registered for reference; not the focus of this list.

| Paper | Venue | Links | Tags |
|---|---|---|---|
| **SWE-bench** | ICLR 2024 | [Paper](https://arxiv.org/abs/2310.06770) | `code` `editing` `general` `state-eval` |
| **SWE-Lancer** | ICML 2025 | [Paper](https://arxiv.org/abs/2502.12115) | `code` `editing` `general` `state-eval` |
| **RepoBench** | ICLR 2024 | [Paper](https://arxiv.org/abs/2306.03091) | `code` `cross-file` `general` `answer-eval` |
| **DS-1000** | ICML 2023 | [Paper](https://arxiv.org/abs/2211.11501) | `code` `generation` `science` `state-eval` |
| **DSBench** | ICLR 2025 | [Paper](https://arxiv.org/abs/2409.07703) | `multi-file` `generation` `science` `artifact-eval` |
| **DataSciBench** | arXiv 2025 | [Paper](https://arxiv.org/abs/2502.13897) | `code` `generation` `science` `state-eval` |
| **DABstep** | arXiv 2025 | [Paper](https://arxiv.org/abs/2506.23719) | `multi-file` `cross-file` `science` `answer-eval` |
| **ScienceAgentBench** | ICLR 2025 | [Paper](https://arxiv.org/abs/2410.05080) | `code` `generation` `science` `artifact-eval` |
| **DiscoveryBench** | arXiv 2024 | [Paper](https://arxiv.org/abs/2407.01725) | `multi-file` `generation` `science` `answer-eval` |
| **PaperBench** | arXiv 2025 | [Paper](https://arxiv.org/abs/2504.01848) | `multi-file` `long-horizon` `science` `artifact-eval` |
| **MLE-bench** | ICLR 2025 | [Paper](https://arxiv.org/abs/2410.07095) | `code` `long-horizon` `science` `state-eval` |
| **RE-Bench** | arXiv 2024 | [Paper](https://arxiv.org/abs/2411.15114) | `code` `long-horizon` `science` `state-eval` |
| **FireAct** | arXiv 2023 | [Paper](https://arxiv.org/abs/2310.05915) | `api` `learning` `general` |

Also registered without individual rows: SWE-Atlas, SWE-INTERACT, Terminal-Bench, MLGym, DrugDiscoveryBench, HiL-Bench.

---

## Surveys

| Title | Links |
|---|---|
| The Evolution of AI Office: From Passive Assistants to Goal-Driven Agents | [Paper](https://www.alphaxiv.org/pdf/2609.evolution-ai-office-agents) |
| Towards Long-Horizon Agents: A Survey | [Paper](https://openreview.net/pdf?id=HyhfhlbWGh) |
| Memory in the Age of AI Agents: Forms, Functions and Dynamics | [Paper](https://arxiv.org/abs/2512.13564) |
| Diving into Reliable Self-Evolving Agents: A Survey | [Paper](https://wkqdzkd.github.io/Awesome-Reliable-Self-Evolving-Agents/Diving_into_Reliable_Self-Evolving_Agents_A_Survey.pdf) |
| Code as Agent Harness: Toward Executable, Verifiable, and Stateful Agent Systems | [Paper](https://arxiv.org/abs/2605.18747) |
| Self-Improvements in Modern Agentic Systems: A Survey | [Paper](https://arxiv.org/abs/2607.13104) |
| Co-Evolution in Agentic Systems | [Paper](https://arxiv.org/abs/2608.10299) |
| Lifelong Learning of LLM-based Agents: A Roadmap | [Paper](https://arxiv.org/abs/2501.07278) |

---

## Contributing

A paper belongs here if the agent **performs or maintains digital work** over artifacts, workspaces, applications, tools, or persistent environments.

**One paper, one section.** Many benchmarks span several settings; place each in the section matching its *most distinctive* requirement and cover the rest with tags. Precedents:

| Benchmark | Section | Why |
|---|---|---|
| OfficeBench | Workspace | cross-application Office workflow, not a single deliverable |
| AA-Briefcase | Persistent | cross-week dependency dominates the multi-file aspect |
| TheAgentCompany | Tool & Enterprise | the simulated company's systems, not the files, are the object |
| WildClawBench | Computer-Use | runs in a real CLI harness with real tools |
| GDPval | Workspace | occupational deliverable packages, though 95/220 tasks ship no input files |
| WorkBuddy-Bench | Workspace | spans code/web/office/security; the multi-file setting is what unifies them |

Keep the tables narrow: no task counts, dataset sizes, or leaderboard scores in the main tables.
