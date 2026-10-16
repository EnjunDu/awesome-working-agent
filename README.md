# Awesome Working Agents

![Working Agents research map](assets/working-agents.svg)

> From answering questions to completing digital work: papers on artifacts, workspaces, tools, computer use, persistent responsibilities, and the systems that make them reliable.

**290 linked research papers and surveys** · **14 separate resources** · Updated **2026-10-16** · Taxonomy **v0.1**

[Download the detailed Excel paper list](paper_list.xlsx) · [Classification guide](docs/taxonomy.md) · [How to contribute](CONTRIBUTING.md) · [Machine-readable catalog](data/papers.json)

The public list is organized by the work or system being studied. The Excel adds paper-time institutions, detailed types, capability tags, optimization mechanisms, survey-section mappings, source checks, and editable reading/writing fields. Each paper has one stable ID and appears once below.

**Scope.** We cover digital knowledge work: producing artifacts, changing application or business state, connecting workspace objects, and maintaining delegated responsibilities. Document QA, general planning, theory, and work-impact studies are retained as supporting context in their own section. Products and documentation are counted separately.

**Start here.** [SheetCopilot](https://arxiv.org/abs/2305.19308) and [PPTAgent](https://arxiv.org/abs/2501.03936) for artifacts; [Workspace-Bench](https://arxiv.org/abs/2605.03596) and [OfficeBench](https://arxiv.org/abs/2407.19056) for workspaces; [OSWorld](https://arxiv.org/abs/2404.07972) for computer use; [AppWorld](https://arxiv.org/abs/2407.18901) and [τ-bench](https://arxiv.org/abs/2406.12045) for stateful tool use; [MemGPT](https://arxiv.org/abs/2310.08560) for memory; [SWE-agent](https://arxiv.org/abs/2405.15793), [AFlow](https://arxiv.org/abs/2410.10762), and [GEPA](https://arxiv.org/abs/2507.19457) for system design and optimization.

## Contents

- [Artifact-Centric Agents](#artifact)
- [Workspace & Cross-Artifact Agents](#workspace)
- [Computer-Use & Application Agents](#computer-use)
- [Tool, API & Enterprise Workflow Agents](#tool-enterprise)
- [Persistent & Long-Horizon Work Agents](#persistent)
- [Harnesses, Training & Optimization](#harness)
- [Verification, Judging & Recovery](#verification)
- [Safety, Injection & Authorization](#safety)
- [Related Foundations & Work Impact](#related)
- [Software, Data Science & Research Agents](#swe-science)
- [Surveys and roadmaps](#surveys)
- [Resources](#resources)
- [Curation and maintenance](#curation)

<a id="artifact"></a>
## Artifact-Centric Agents

Create or edit a spreadsheet, slide deck, or document. Use workspace when discovering dependencies across deliverables is central. Read-only understanding belongs in related foundations.

| Paper | First year | Resources |
| --- | --- | --- |
| **AeSlides**: Incentivizing Aesthetic Layout in LLM-Based Slide Generation via Verifiable Rewards | 2026 | [Paper](https://arxiv.org/abs/2604.22840) · [Code](https://github.com/ympan0508/aeslides) |
| **AutoDesign**: Meta-Harness Optimization for Long-Horizon Agentic Design | 2026 | [Paper](https://arxiv.org/abs/2608.13560) · [Code](https://github.com/Yaxin9Luo/AutoDesign) |
| **BlueFin**: Benchmarking LLM Agents on Financial Spreadsheets | 2026 | [Paper](https://arxiv.org/abs/2605.30907) |
| **CogEvol**: Towards Efficient and Reliable Learning Environment Generation | 2026 | [Paper](https://arxiv.org/abs/2608.30968) · [Code](https://github.com/CogEvol/CogEvol-4B) |
| **DeepPresenter**: Environment-Grounded Reflection for Agentic Presentation Generation | 2026 | [Paper](https://arxiv.org/abs/2602.22839) · [Code](https://github.com/icip-cas/PPTAgent) |
| **MiLDEdit / MiLDEAgent**: MiLDEdit: Reasoning-Based Multi-Layer Design Document Editing | 2026 | [Paper](https://arxiv.org/abs/2601.04589) |
| **PresentBench**: A Fine-Grained Rubric-Based Benchmark for Slide Generation | 2026 | [Paper](https://arxiv.org/abs/2603.07244) · [Code](https://github.com/PresentBench/PresentBench) · [Data](https://huggingface.co/datasets/PresentBench/PresentBench) |
| **SlideRL / Learning to Present**: Learning to Present: Inverse Specification Rewards for Agentic Slide Generation | 2026 | [Paper](https://arxiv.org/abs/2603.16839) · [Code](https://github.com/pushing-the-frontier/slide-forge-llm) · [Data](https://huggingface.co/datasets/KarthikRagunathAnandaKumar/sliderl-multi-turn-rollouts) |
| **Spreadsheet-RL**: Advancing Large Language Model Agents on Realistic Spreadsheet Tasks via Reinforcement Learning | 2026 | [Paper](https://arxiv.org/abs/2605.22642) · [Code](https://github.com/Spreadsheet-RL/Spreadsheet-RL) · [Data](https://huggingface.co/datasets/Spreadsheet-RL/Spreadsheet-RL) |
| **SpreadsheetBench 2**: Evaluating Agents on End-to-End Business Spreadsheet Workflows | 2026 | [Paper](https://arxiv.org/abs/2606.29955) · [Code](https://github.com/RUCKBReasoning/SpreadsheetBench-2) · [Data](https://huggingface.co/datasets/KAKA22/SpreadsheetBench-v2) |
| **AutoPresent / SlidesBench**: AutoPresent: Designing Structured Visuals from Scratch | 2025 | [Paper](https://arxiv.org/abs/2501.00912) · [Code](https://github.com/para-lost/AutoPresent) |
| **PPTAgent**: Generating and Evaluating Presentations Beyond Text-to-Slides | 2025 | [Paper](https://arxiv.org/abs/2501.03936) · [Code](https://github.com/icip-cas/PPTAgent) |
| **SheetAgent**: Towards A Generalist Agent for Spreadsheet Reasoning and Manipulation via Large Language Models | 2024 | [Paper](https://arxiv.org/abs/2403.03636) |
| **SpreadsheetBench**: Towards Challenging Real World Spreadsheet Manipulation | 2024 | [Paper](https://arxiv.org/abs/2406.14991) · [Code](https://github.com/RUCKBReasoning/SpreadsheetBench) · [Data](https://huggingface.co/datasets/KAKA22/SpreadsheetBench) |
| **CoEdIT**: Text Editing by Task-Specific Instruction Tuning | 2023 | [Paper](https://arxiv.org/abs/2305.09857) |
| **InstructExcel**: A Benchmark for Natural Language Instruction in Excel | 2023 | [Paper](https://aclanthology.org/2023.findings-emnlp.265/) · [Code](https://github.com/microsoft/InstructExcel) |
| **PPTC** Benchmark: Evaluating Large Language Models for PowerPoint Task Completion | 2023 | [Paper](https://arxiv.org/abs/2311.01767) · [Code](https://github.com/gydpku/PPTC) |
| **SheetCopilot**: Bringing Software Productivity to the Next Level through Large Language Models | 2023 | [Paper](https://arxiv.org/abs/2305.19308) · [Code](https://github.com/BraveGroup/SheetCopilot) |
| **PEER**: A Collaborative Language Model | 2022 | [Paper](https://arxiv.org/abs/2208.11663) |

<a id="workspace"></a>
## Workspace & Cross-Artifact Agents

Discover and connect files, applications, and deliverables in a workspace; occupational work packages.

| Paper | First year | Resources |
| --- | --- | --- |
| **AgentIF-OneDay**: A Task-level Instruction-Following Benchmark for General AI Agents in Daily Scenarios | 2026 | [Paper](https://arxiv.org/abs/2601.20613) |
| **Agents’ Last Exam**: Agents' Last Exam | 2026 | [Paper](https://arxiv.org/abs/2606.05405) |
| **APEX-Agents** | 2026 | [Paper](https://arxiv.org/abs/2601.14242) · [Data](https://huggingface.co/datasets/mercor/apex-agents) |
| **BankerToolBench**: Evaluating AI Agents in End-to-End Investment Banking Workflows | 2026 | [Paper](https://arxiv.org/abs/2604.11304) · [Code](https://github.com/Handshake-AI-Research/bankertoolbench) |
| **CentaurBench**: Benchmarking LLM Capabilities on Augmenting vs. Automating Real-World Work Tasks | 2026 | [Paper](https://arxiv.org/abs/2608.18554) · [Code](https://github.com/kennywong524/best-player-not-best-coach) |
| **EnvCraft**: Synthesizing Executable Environments in Agentic RL for Claw-like Agent | 2026 | [Paper](https://arxiv.org/abs/2609.05576) · [Code](https://github.com/zeng-yirong/EnvCraft) · [Data](https://huggingface.co/datasets/EnvCraft/EnvCraft-Data) |
| **GraphForge**: Training Working Agents with Graph-Anchored Workspace Synthesis | 2026 | [Paper](https://arxiv.org/abs/2609.38923) · [Data](https://huggingface.co/datasets/groundhogLLM/GraphForge-SFT-2169-clean) |
| **JobBench**: Aligning Agent Work With Human Will | 2026 | [Paper](https://arxiv.org/abs/2605.26329) · [Code](https://github.com/Job-Bench/job-bench-eval) · [Data](https://huggingface.co/datasets/JobBench/job-bench) |
| **NexForge**: Scaling Agent Capabilities through Requirement-Driven Task Synthesis for LLMs | 2026 | [Paper](https://arxiv.org/abs/2607.14186) |
| **OmegaUse-OfficeVal**: Benchmarking LLM Agents on Long-Horizon Office-Suite Tasks with Economic Grounding | 2026 | [Paper](https://arxiv.org/abs/2607.27155) · [Code](https://github.com/baidu-frontier-research/OmegaUse-OfficeVal) · [Data](https://huggingface.co/datasets/baidu-frontier-research/OmegaUse-OfficeVal) |
| **Skill2Env**: Capability-Oriented Environment Synthesis from Skills for General Agents | 2026 | [Paper](https://arxiv.org/abs/2609.33772) · [Code](https://github.com/AllSpark-Research/AgentEnv) |
| **StagedWorkspace**: A Versioned Workspace for Knowledge-Work Agents | 2026 | [Paper](https://arxiv.org/abs/2608.18050) |
| **StartupBench**: Benchmarking General-Purpose Agents on Market-Validated End-to-End Workflows | 2026 | [Paper](https://arxiv.org/abs/2608.17800) |
| **WorkBuddy Bench**: Tencent WorkBuddy Bench: A Multi-Domain Coding-Agent Benchmark with Contamination-Resistant Task Construction | 2026 | [Paper](https://arxiv.org/abs/2607.20911) |
| **WorkGenesis**: Building the Worlds That Teach Agents to Work | 2026 | [Paper](https://arxiv.org/abs/2609.39325) |
| **Workspace-Bench** 1.0: Benchmarking AI Agents on Workspace Tasks with Large-Scale File Dependencies | 2026 | [Paper](https://arxiv.org/abs/2605.03596) · [Code](https://github.com/OpenDataBox/Workspace-Bench) |
| **FINCH / FinWorkBench**: Finch: Benchmarking Finance & Accounting across Spreadsheet-Centric Enterprise Workflows | 2025 | [Paper](https://arxiv.org/abs/2512.13168) · [Code](https://github.com/FinWorkBench/Finch) · [Data](https://huggingface.co/datasets/FinWorkBench/Finch) |
| **GDPval**: Evaluating AI Model Performance on Real-World Economically Valuable Tasks | 2025 | [Paper](https://arxiv.org/abs/2510.04374) |
| **OdysseyBench**: Evaluating LLM Agents on Long-Horizon Complex Office Application Workflows | 2025 | [Paper](https://arxiv.org/abs/2508.09124) |
| **Remote Labor Index**: Measuring AI Automation of Remote Work | 2025 | [Paper](https://arxiv.org/abs/2510.26787) |
| **Collaborative Gym**: A Framework for Enabling and Evaluating Human-Agent Collaboration | 2024 | [Paper](https://arxiv.org/abs/2412.15701) · [Code](https://github.com/SALT-NLP/collaborative-gym) |
| **OfficeBench**: Benchmarking Language Agents across Multiple Applications for Office Automation | 2024 | [Paper](https://arxiv.org/abs/2407.19056) · [Code](https://github.com/zlwang-cs/OfficeBench) |
| **GAIA**: a benchmark for General AI Assistants | 2023 | [Paper](https://arxiv.org/abs/2311.12983) |

<a id="computer-use"></a>
## Computer-Use & Application Agents

GUI grounding, web navigation, desktop and mobile control. A GUI interface alone does not override a more distinctive work objective.

| Paper | First year | Resources |
| --- | --- | --- |
| **ADMIRE**: Adaptive Milestone Reward for GUI Agents | 2026 | [Paper](https://arxiv.org/abs/2602.11524) |
| **Component Routing**: Not All Experience Belongs in the Weights: Component Routing for Self-Improving GUI Agents | 2026 | [Paper](https://arxiv.org/abs/2610.01787) |
| **GHD / The Next Screenshot Knows**: The Next Screenshot Knows: Gated Hindsight Distillation for Mobile GUI Agents | 2026 | [Paper](https://arxiv.org/abs/2608.06065) |
| **LiteGUI**: Lightweight GUI Agents via Multi-Solution Guided Distillation and Dual-Level Reinforcement Learning | 2026 | [Paper](https://arxiv.org/abs/2605.07505) |
| **SEE**: Structure-aware Exploring & Exploiting for Long-horizon GUI Agent Trajectory Synthesis | 2026 | [Paper](https://arxiv.org/abs/2607.18046) · [Code](https://github.com/Zhh-Fan/SEE-Structure-aware-Exploring-Exploiting-for-Long-horizon-GUI-Agent-Trajectory-Synthesis) |
| **Terminal-Bench**: Benchmarking Agents on Hard, Realistic Tasks in Command Line Interfaces | 2026 | [Paper](https://arxiv.org/abs/2601.11868) · [Code](https://github.com/harbor-framework/terminal-bench) |
| **UI-Copilot**: Advancing Long-Horizon GUI Automation via Tool-Integrated Policy Optimization | 2026 | [Paper](https://arxiv.org/abs/2604.13822) |
| **UI-Mate**: Advancing Open-Weight Foundation GUI Agents with In-Context Demonstrations | 2026 | [Paper](https://arxiv.org/abs/2608.15930) |
| **UI-Mem**: Self-Evolving Experience Memory for Online Reinforcement Learning in Mobile GUI Agents | 2026 | [Paper](https://arxiv.org/abs/2602.05832) |
| **WildClawBench**: A Benchmark for Real-World, Long-Horizon Agent Evaluation | 2026 | [Paper](https://arxiv.org/abs/2605.10912) |
| **Agent S2**: A Compositional Generalist-Specialist Framework for Computer Use Agents | 2025 | [Paper](https://arxiv.org/abs/2504.00906) · [Code](https://github.com/simular-ai/Agent-S) |
| **ComputerRL**: Scaling End-to-End Online Reinforcement Learning for Computer Use Agents | 2025 | [Paper](https://arxiv.org/abs/2508.14040) |
| **FieldWorkArena**: Agentic AI Benchmark for Real Field Work Tasks | 2025 | [Paper](https://arxiv.org/abs/2505.19662) |
| **GUI-Actor**: Coordinate-Free Visual Grounding for GUI Agents | 2025 | [Paper](https://arxiv.org/abs/2506.03143) · [Code](https://github.com/microsoft/GUI-Actor) |
| **ScreenSpot-Pro**: GUI Grounding for Professional High-Resolution Computer Use | 2025 | [Paper](https://arxiv.org/abs/2504.07981) · [Code](https://github.com/likaixin2000/ScreenSpot-Pro-GUI-Grounding) · [Data](https://huggingface.co/datasets/likaixin/ScreenSpot-Pro) |
| **UFO2**: The Desktop AgentOS | 2025 | [Paper](https://arxiv.org/abs/2504.14603) · [Code](https://github.com/microsoft/UFO/) |
| **UI-TARS**: Pioneering Automated GUI Interaction with Native Agents | 2025 | [Paper](https://arxiv.org/abs/2501.12326) |
| **Agent Q**: Advanced Reasoning and Learning for Autonomous AI Agents | 2024 | [Paper](https://arxiv.org/abs/2408.07199) |
| **AgentTrek**: Agent Trajectory Synthesis via Guiding Replay with Web Tutorials | 2024 | [Paper](https://arxiv.org/abs/2412.09605) |
| **AndroidWorld**: A Dynamic Benchmarking Environment for Autonomous Agents | 2024 | [Paper](https://arxiv.org/abs/2405.14573) · [Code](https://github.com/google-research/android_world) |
| **DigiRL**: Training In-The-Wild Device-Control Agents with Autonomous Reinforcement Learning | 2024 | [Paper](https://arxiv.org/abs/2406.11896) |
| **OmniParser** for Pure Vision Based GUI Agent | 2024 | [Paper](https://arxiv.org/abs/2408.00203) |
| **OS-Copilot**: Towards Generalist Computer Agents with Self-Improvement | 2024 | [Paper](https://arxiv.org/abs/2402.07456) |
| **OSWorld**: Benchmarking Multimodal Agents for Open-Ended Tasks in Real Computer Environments | 2024 | [Paper](https://arxiv.org/abs/2404.07972) · [Code](https://github.com/xlang-ai/OSWorld) · [Data](https://github.com/xlang-ai/OSWorld/tree/main/evaluation_examples) |
| **SeeClick**: Harnessing GUI Grounding for Advanced Visual GUI Agents | 2024 | [Paper](https://aclanthology.org/2024.acl-long.505/) · [Code](https://github.com/njucckevin/SeeClick) |
| **VideoWebArena**: Evaluating Long Context Multimodal Agents with Video Understanding Web Tasks | 2024 | [Paper](https://arxiv.org/abs/2410.19100) |
| **VisualWebArena**: Evaluating Multimodal Agents on Realistic Visual Web Tasks | 2024 | [Paper](https://arxiv.org/abs/2401.13649) |
| **WebLINX**: Real-World Website Navigation with Multi-Turn Dialogue | 2024 | [Paper](https://arxiv.org/abs/2402.05930) |
| **WebRL**: Training LLM Web Agents via Self-Evolving Online Curriculum Reinforcement Learning | 2024 | [Paper](https://arxiv.org/abs/2411.02337) |
| **WebVoyager**: Building an End-to-End Web Agent with Large Multimodal Models | 2024 | [Paper](https://arxiv.org/abs/2401.13919) |
| **Windows Agent Arena**: Evaluating Multi-Modal OS Agents at Scale | 2024 | [Paper](https://arxiv.org/abs/2409.08264) · [Code](https://github.com/microsoft/WindowsAgentArena) |
| **WorkArena**: How Capable Are Web Agents at Solving Common Knowledge Work Tasks? | 2024 | [Paper](https://arxiv.org/abs/2403.07718) |
| **WorkArena++**: Towards Compositional Planning and Reasoning-based Common Knowledge Work Tasks | 2024 | [Paper](https://arxiv.org/abs/2407.05291) · [Code](https://github.com/ServiceNow/WorkArena) |
| **Mind2Web**: Towards a Generalist Agent for the Web | 2023 | [Paper](https://arxiv.org/abs/2306.06070) |
| **WebArena**: A Realistic Web Environment for Building Autonomous Agents | 2023 | [Paper](https://arxiv.org/abs/2307.13854) |
| **WebShop**: Towards Scalable Real-World Web Interaction with Grounded Language Agents | 2022 | [Paper](https://arxiv.org/abs/2207.01206) |

<a id="tool-enterprise"></a>
## Tool, API & Enterprise Workflow Agents

Function calling, tool-mediated work, stateful business processes, and user-tool interaction.

| Paper | First year | Resources |
| --- | --- | --- |
| **Agent World Model**: Infinity Synthetic Environments for Agentic Reinforcement Learning | 2026 | [Paper](https://arxiv.org/abs/2602.10090) · [Code](https://github.com/Snowflake-Labs/agent-world-model) |
| **AgentMercury**: Your Agent Can Synthesize Verifiable Environments for Business Scenarios at scale | 2026 | [Paper](https://arxiv.org/abs/2608.20634) · [Data](https://huggingface.co/datasets/Minbyul/AgentMercury-corpus-sample) |
| **AutomationBench (Zapier)**: AutomationBench | 2026 | [Paper](https://arxiv.org/abs/2604.18934) · [Code](https://github.com/zapier/AutomationBench) |
| **DMRL**: Document-Mediated Reinforcement Learning for Skill Optimization in Advertising Recommendation | 2026 | [Paper](https://arxiv.org/abs/2609.02170) |
| **E-Bench**: Benchmarking Multi-Step Tool-Use Agents in Real-World Product Scenarios | 2026 | [Paper](https://arxiv.org/abs/2607.23722) |
| **E-Commerce Bench**: Evaluating LLM Agents on Long-Horizon Autonomous Business Operation | 2026 | [Paper](https://arxiv.org/abs/2608.30730) |
| **EnterpriseClawBench**: Benchmarking Agents from Real Workplace Sessions | 2026 | [Paper](https://arxiv.org/abs/2606.23654) |
| **EnterpriseLab**: A Full-Stack Platform for developing and deploying agents in Enterprises | 2026 | [Paper](https://arxiv.org/abs/2603.21630) |
| **EnterpriseOps-Gym**: Environments and Evaluations for Stateful Agentic Planning and Tool Use in Enterprise Settings | 2026 | [Paper](https://arxiv.org/abs/2603.13594) |
| **EnvScaler**: Scaling Tool-Interactive Environments for LLM Agent via Programmatic Synthesis | 2026 | [Paper](https://arxiv.org/abs/2601.05808) · [Code](https://github.com/RUC-NLPIR/EnvScaler) |
| **HealthAgentBench**: A Unified Benchmark Suite of Realistic Agentic Healthcare Environments for Challenging Frontier AI Agents | 2026 | [Paper](https://arxiv.org/abs/2606.31179) · [Code](https://github.com/microsoft/HealthAgentBench) |
| **MCP-Atlas**: A Large-Scale Benchmark for Tool-Use Competency with Real MCP Servers | 2026 | [Paper](https://arxiv.org/abs/2602.00933) |
| **OmniaBench**: Benchmarking General AI Agents Across Diverse Scenarios | 2026 | [Paper](https://arxiv.org/abs/2607.14989) |
| **TDScaling**: Beyond Quantity: Trajectory Diversity Scaling for Code Agents | 2026 | [Paper](https://arxiv.org/abs/2602.03219) |
| **BFCL**: The Berkeley Function Calling Leaderboard (BFCL): From Tool Use to Agentic Evaluation of Large Language Models | 2025 | [Paper](https://proceedings.mlr.press/v267/patil25a.html) · [Code](https://github.com/ShishirPatil/gorilla/tree/main/berkeley-function-call-leaderboard) |
| **CRMArena-Pro**: Holistic Assessment of LLM Agents Across Diverse Business Scenarios and Interactions | 2025 | [Paper](https://arxiv.org/abs/2505.18878) · [Code](https://github.com/SalesforceAIResearch/CRMArena) · [Data](https://huggingface.co/datasets/Salesforce/CRMArenaPro) |
| **EnterpriseBench**: Can LLMs Help You at Work? A Sandbox for Evaluating LLM Agents in Enterprise Environments | 2025 | [Paper](https://aclanthology.org/2025.emnlp-main.466/) |
| **Flex-TravelPlanner**: A Benchmark for Flexible Planning with Language Agents | 2025 | [Paper](https://arxiv.org/abs/2506.04649) |
| **MCP-Bench**: Benchmarking Tool-Using LLM Agents with Complex Real-World Tasks via MCP Servers | 2025 | [Paper](https://arxiv.org/abs/2508.20453) · [Code](https://github.com/Accenture/mcp-bench) |
| **MedAgentBench**: A Realistic Virtual EHR Environment to Benchmark Medical LLM Agents | 2025 | [Paper](https://arxiv.org/abs/2501.14654) · [Code](https://github.com/stanfordmlgroup/MedAgentBench) |
| **ReTool**: Reinforcement Learning for Strategic Tool Use in LLMs | 2025 | [Paper](https://arxiv.org/abs/2504.11536) |
| **Routine**: A Structural Planning Framework for LLM Agent System in Enterprise | 2025 | [Paper](https://arxiv.org/abs/2507.14447) |
| **Toolathlon**: The Tool Decathlon: Benchmarking Language Agents for Diverse, Realistic, and Long-Horizon Task Execution | 2025 | [Paper](https://arxiv.org/abs/2510.25726) · [Code](https://github.com/hkust-nlp/Toolathlon) |
| **τ²-Bench**: Evaluating Conversational Agents in a Dual-Control Environment | 2025 | [Paper](https://arxiv.org/abs/2506.07982) · [Code](https://github.com/sierra-research/tau2-bench) |
| **AppWorld**: A Controllable World of Apps and People for Benchmarking Interactive Coding Agents | 2024 | [Paper](https://arxiv.org/abs/2407.18901) · [Code](https://github.com/stonybrooknlp/appworld) |
| **CodeAct**: Executable Code Actions Elicit Better LLM Agents | 2024 | [Paper](https://arxiv.org/abs/2402.01030) · [Code](https://github.com/xingyaoww/code-act) |
| **CRMArena**: Understanding the Capacity of LLM Agents to Perform Professional CRM Tasks in Realistic Environments | 2024 | [Paper](https://arxiv.org/abs/2411.02305) · [Code](https://github.com/SalesforceAIResearch/CRMArena) |
| **Graph-enhanced Asynchronous Planning**: Graph-enhanced Large Language Models in Asynchronous Plan Reasoning | 2024 | [Paper](https://arxiv.org/abs/2402.02805) |
| **Spider 2.0**: Evaluating Language Models on Real-World Enterprise Text-to-SQL Workflows | 2024 | [Paper](https://arxiv.org/abs/2411.07763) · [Code](https://github.com/xlang-ai/Spider2) |
| **TheAgentCompany**: Benchmarking LLM Agents on Consequential Real World Tasks | 2024 | [Paper](https://arxiv.org/abs/2412.14161) · [Code](https://github.com/TheAgentCompany/TheAgentCompany) |
| **ToolSandbox**: A Stateful, Conversational, Interactive Evaluation Benchmark for LLM Tool Use Capabilities | 2024 | [Paper](https://arxiv.org/abs/2408.04682) · [Code](https://github.com/apple/ToolSandbox) |
| **TravelPlanner**: A Benchmark for Real-World Planning with Language Agents | 2024 | [Paper](https://arxiv.org/abs/2402.01622) · [Code](https://github.com/OSU-NLP-Group/TravelPlanner) · [Data](https://huggingface.co/datasets/osunlp/TravelPlanner) |
| **WorkBench**: a Benchmark Dataset for Agents in a Realistic Workplace Setting | 2024 | [Paper](https://arxiv.org/abs/2405.00823) · [Code](https://github.com/olly-styles/WorkBench) |
| **τ-bench**: A Benchmark for Tool-Agent-User Interaction in Real-World Domains | 2024 | [Paper](https://arxiv.org/abs/2406.12045) · [Code](https://github.com/sierra-research/tau-bench) |
| **API-Bank**: A Comprehensive Benchmark for Tool-Augmented LLMs | 2023 | [Paper](https://arxiv.org/abs/2304.08244) · [Code](https://github.com/AlibabaResearch/DAMO-ConvAI/tree/main/api-bank) |
| **FireAct**: Toward Language Agent Fine-tuning | 2023 | [Paper](https://arxiv.org/abs/2310.05915) |
| **LLM+P**: Empowering Large Language Models with Optimal Planning Proficiency | 2023 | [Paper](https://arxiv.org/abs/2304.11477) |
| **MINT**: Evaluating LLMs in Multi-turn Interaction with Tools and Language Feedback | 2023 | [Paper](https://arxiv.org/abs/2309.10691) · [Code](https://github.com/xingyaoww/mint-bench) · [Data](https://github.com/xingyaoww/mint-bench/blob/main/docs/DATA.md) |
| **Toolformer**: Language Models Can Teach Themselves to Use Tools | 2023 | [Paper](https://arxiv.org/abs/2302.04761) |
| **ToolLLM / ToolBench**: ToolLLM: Facilitating Large Language Models to Master 16000+ Real-world APIs | 2023 | [Paper](https://arxiv.org/abs/2307.16789) · [Code](https://github.com/OpenBMB/ToolBench) |
| **ReAct**: Synergizing Reasoning and Acting in Language Models | 2022 | [Paper](https://arxiv.org/abs/2210.03629) · [Code](https://github.com/ysymyth/ReAct) |

<a id="persistent"></a>
## Persistent & Long-Horizon Work Agents

Memory, asynchronous work, proactive assistance, personalization, and long-horizon evaluation. Execution length does not itself prove persistent responsibility.

| Paper | First year | Resources |
| --- | --- | --- |
| **ChronoMem**: Version Control and Semantic Rollback for Large Language Model Agent Memory | 2026 | [Paper](https://arxiv.org/abs/2607.27773) |
| **InfiAgent**: An Infinite-Horizon Framework for General-Purpose Autonomous Agents | 2026 | [Paper](https://arxiv.org/abs/2601.03204) · [Code](https://github.com/ChenglinPoly/infiAgent) |
| **On-Policy Distillation**: Rethinking On-Policy Distillation of Large Language Models: Phenomenology, Mechanism, and Recipe | 2026 | [Paper](https://arxiv.org/abs/2604.13016) · [Code](https://github.com/thunlp/OPD) |
| **PAST-Bench / Hermes+**: PAST-Bench: Benchmarking the Foundations of Recursive Self-Improvement in Personal Agents | 2026 | [Paper](https://arxiv.org/abs/2608.04003) · [Code](https://github.com/Gen-Verse/PAST-Bench) |
| **StateGuard**: Analytical-State Management with Validity-Aware Intervention for Long-Horizon Data Agents | 2026 | [Paper](https://arxiv.org/abs/2609.34134) |
| **StreamMemBench**: Streaming Evaluation of Agent Memory for Future-Oriented Assistance | 2026 | [Paper](https://arxiv.org/abs/2606.14571) · [Code](https://github.com/landian60/StreamMemBench) |
| **VibeLifeBench**: Can Your Life Agent Be Proactive and Persistent in a Living World? | 2026 | [Paper](https://arxiv.org/abs/2608.10875) |
| **Mem0**: Building Production-Ready AI Agents with Scalable Long-Term Memory | 2025 | [Paper](https://arxiv.org/abs/2504.19413) · [Code](https://github.com/mem0ai/mem0) |
| **METR time horizon**: Measuring AI Ability to Complete Long Software Tasks | 2025 | [Paper](https://arxiv.org/abs/2503.14499) |
| **SagaLLM**: Context Management, Validation, and Transaction Guarantees for Multi-Agent LLM Planning | 2025 | [Paper](https://arxiv.org/abs/2503.11951) |
| **Zep**: A Temporal Knowledge Graph Architecture for Agent Memory | 2025 | [Paper](https://arxiv.org/abs/2501.13956) · [Code](https://github.com/getzep/graphiti) |
| **LoCoMo**: Evaluating Very Long-Term Conversational Memory of LLM Agents | 2024 | [Paper](https://arxiv.org/abs/2402.17753) · [Code](https://github.com/snap-research/LoCoMo) · [Data](https://github.com/snap-research/locomo/tree/main/data) |
| **LongMemEval**: Benchmarking Chat Assistants on Long-Term Interactive Memory | 2024 | [Paper](https://arxiv.org/abs/2410.10813) · [Code](https://github.com/xiaowu0162/LongMemEval) |
| **Proactive Agent**: Shifting LLM Agents from Reactive Responses to Active Assistance | 2024 | [Paper](https://arxiv.org/abs/2410.12361) · [Code](https://github.com/thunlp/ProactiveAgent) |
| **TimeArena**: Shaping Efficient Multitasking Language Agents in a Time-Aware Simulation | 2024 | [Paper](https://arxiv.org/abs/2402.05733) |
| **ExpeL**: LLM Agents Are Experiential Learners | 2023 | [Paper](https://arxiv.org/abs/2308.10144) |
| **Generative Agents**: Interactive Simulacra of Human Behavior | 2023 | [Paper](https://arxiv.org/abs/2304.03442) |
| **MemGPT**: Towards LLMs as Operating Systems | 2023 | [Paper](https://arxiv.org/abs/2310.08560) · [Code](https://github.com/letta-ai/letta) |
| **Voyager**: An Open-Ended Embodied Agent with Large Language Models | 2023 | [Paper](https://arxiv.org/abs/2305.16291) |

<a id="harness"></a>
## Harnesses, Training & Optimization

Execution platforms and cross-domain environment, data, model, harness, and joint optimization. Domain-specific methods stay in their work category; optimization mechanism is recorded independently.

### Platforms and execution systems

| Paper | First year | Resources |
| --- | --- | --- |
| **DSec**: DeepSeek Elastic Compute (DSec): A Sandbox Infrastructure for Effective Agentic Training at Scale | 2026 | [Paper](https://arxiv.org/abs/2609.22978) |
| **MultiAgentBench**: Evaluating the Collaboration and Competition of LLM agents | 2025 | [Paper](https://arxiv.org/abs/2503.01935) · [Code](https://github.com/MultiagentBench/MARBLE) |
| **WorkTeam**: Constructing Workflows from Natural Language with Multi-Agents | 2025 | [Paper](https://arxiv.org/abs/2503.22473) |
| **ADAS**: Automated Design of Agentic Systems | 2024 | [Paper](https://arxiv.org/abs/2408.08435) |
| **AgentBoard**: An Analytical Evaluation Board of Multi-turn LLM Agents | 2024 | [Paper](https://arxiv.org/abs/2401.13178) |
| **AgentSquare**: Automatic LLM Agent Search in Modular Design Space | 2024 | [Paper](https://arxiv.org/abs/2410.06153) |
| **AsyncLM**: Asynchronous LLM Function Calling | 2024 | [Paper](https://arxiv.org/abs/2412.07017) |
| **BrowserGym**: The BrowserGym Ecosystem for Web Agent Research | 2024 | [Paper](https://arxiv.org/abs/2412.05467) · [Code](https://github.com/ServiceNow/BrowserGym) |
| **Magentic-One**: A Generalist Multi-Agent System for Solving Complex Tasks | 2024 | [Paper](https://arxiv.org/abs/2411.04468) · [Code](https://github.com/microsoft/autogen) |
| **OpenHands**: An Open Platform for AI Software Developers as Generalist Agents | 2024 | [Paper](https://arxiv.org/abs/2407.16741) · [Code](https://github.com/OpenHands/OpenHands) |
| **AutoGen**: Enabling Next-Gen LLM Applications via Multi-Agent Conversation | 2023 | [Paper](https://arxiv.org/abs/2308.08155) · [Code](https://github.com/microsoft/autogen) |
| **CAMEL**: Communicative Agents for "Mind" Exploration of Large Language Model Society | 2023 | [Paper](https://arxiv.org/abs/2303.17760) |

### Trajectory curation

| Paper | First year | Resources |
| --- | --- | --- |
| **CurateEvo**: Data-Curation Evolving for Agentic Post-Training | 2026 | [Paper](https://arxiv.org/abs/2607.06140) |
| **OpenThoughts-Agent**: Data Recipes for Agentic Models | 2026 | [Paper](https://arxiv.org/abs/2606.24855) · [Code](https://github.com/open-thoughts/OpenThoughts-Agent) |

### Mid training sft

| Paper | First year | Resources |
| --- | --- | --- |
| **TrajLong**: Co-Designing Agentic and Long-Context Supervision for Mid-Training | 2026 | [Paper](https://arxiv.org/abs/2610.04973) |

### Agentic rl

| Paper | First year | Resources |
| --- | --- | --- |
| **HiPER**: Hierarchical Reinforcement Learning with Explicit Credit Assignment for Large Language Model Agents | 2026 | [Paper](https://arxiv.org/abs/2602.16165) · [Code](https://github.com/JonP07/HiPER-agent) |

### On policy distillation

| Paper | First year | Resources |
| --- | --- | --- |
| **Guided-OPD**: On-Policy Distillation with Curriculum Turn-level Guidance for Multi-turn Agents | 2026 | [Paper](https://arxiv.org/abs/2606.15912) |
| **Revisiting DAgger** in the Era of LLM-Agents | 2026 | [Paper](https://arxiv.org/abs/2605.12913) |
| **Skill-SD**: Skill-Conditioned Self-Distillation for Multi-turn LLM Agents | 2026 | [Paper](https://arxiv.org/abs/2604.10674) |
| **SOD**: Step-wise On-policy Distillation for Small Language Model Agents | 2026 | [Paper](https://arxiv.org/abs/2605.07725) · [Code](https://github.com/YoungZ365/SOD) |
| **TCOD**: Exploring Temporal Curriculum in On-Policy Distillation for Multi-turn Autonomous Agents | 2026 | [Paper](https://arxiv.org/abs/2604.24005) · [Code](https://github.com/kokolerk/TCOD) |

### Self improving training

| Paper | First year | Resources |
| --- | --- | --- |
| **RePro**: Retrospective Progress-Aware Self-Refinement for LLM Agent Training | 2026 | [Paper](https://arxiv.org/abs/2606.14302) |
| **SDPO**: Reinforcement Learning via Self-Distillation | 2026 | [Paper](https://arxiv.org/abs/2601.20802) · [Code](https://github.com/lasgroup/SDPO) |
| **SRD**: Self-Retrospection Distillation: Turning Post-hoc Experiences into Prior Foresight | 2026 | [Paper](https://arxiv.org/abs/2610.08077) · [Code](https://github.com/SalesforceAIResearch/SRD) |

### Tool interface

| Paper | First year | Resources |
| --- | --- | --- |
| **JTPRO**: A Joint Tool-Prompt Reflective Optimization Framework for Language Agents | 2026 | [Paper](https://arxiv.org/abs/2604.19821) |
| **PRISM / Beyond Prompts**: Beyond Prompts: Measuring and Optimizing LLM Tool-Agent Harnesses | 2026 | [Paper](https://arxiv.org/abs/2609.05736) · [Code](https://github.com/airbnb/agent-harness-optimizer) |
| **TACO**: A Self-Evolving Framework for Efficient Terminal Agents via Observational Context Compression | 2026 | [Paper](https://arxiv.org/abs/2604.19572) · [Code](https://github.com/multimodal-art-projection/TACO) |
| **Tool Description Rewriter**: Learning to Rewrite Tool Descriptions for Reliable LLM-Agent Tool Use | 2026 | [Paper](https://arxiv.org/abs/2602.20426) |

### Prompt workflow

| Paper | First year | Resources |
| --- | --- | --- |
| **ActiveSaddler**: Automated Curriculum Learning for Agent Harness Optimization | 2026 | [Paper](https://arxiv.org/abs/2610.00906) |
| **Adaptive Auto-Harness**: Sustained Self-Improvement for Agentic System Deployment on Open-Ended Task Streams | 2026 | [Paper](https://arxiv.org/abs/2606.01770) · [Code](https://github.com/A-EVO-Lab/a-evolve/tree/release/adaptive-auto-harness) |
| **MESH-Harness**: Self-Improving Agent Harnesses via Bandit-Guided Compositional Evolution | 2026 | [Paper](https://arxiv.org/abs/2610.05300) |
| **Meta-Harness**: End-to-End Optimization of Model Harnesses | 2026 | [Paper](https://arxiv.org/abs/2603.28052) · [Code](https://github.com/stanford-iris-lab/meta-harness-tbench2-artifact) |
| **RHO**: Evolving Agents in the Dark: Retrospective Harness Optimization via Self-Preference | 2026 | [Paper](https://arxiv.org/abs/2606.05922) · [Code](https://github.com/wbopan/retro-harness) |
| **VERSE**: Verified Self-Evolving Optimizer for Agent Harnesses | 2026 | [Paper](https://arxiv.org/abs/2610.02616) · [Code](https://github.com/wzekai/VERSE) |
| **GEPA**: Reflective Prompt Evolution Can Outperform Reinforcement Learning | 2025 | [Paper](https://arxiv.org/abs/2507.19457) · [Code](https://github.com/gepa-ai/gepa) |
| **AFlow**: Automating Agentic Workflow Generation | 2024 | [Paper](https://arxiv.org/abs/2410.10762) · [Code](https://github.com/FoundationAgents/AFlow) |

### Memory skill

| Paper | First year | Resources |
| --- | --- | --- |
| **SkillOpt**: Executive Strategy for Self-Evolving Agent Skills | 2026 | [Paper](https://arxiv.org/abs/2605.23904) |
| **SkillSmith**: Co-Evolving Skills and Tools for Self-Improving Agent Systems | 2026 | [Paper](https://arxiv.org/abs/2606.01314) |
| **ACE**: Agentic Context Engineering: Evolving Contexts for Self-Improving Language Models | 2025 | [Paper](https://arxiv.org/abs/2510.04618) · [Code](https://github.com/ace-agent/ace) |
| **ReasoningBank**: Scaling Agent Self-Evolving with Reasoning Memory | 2025 | [Paper](https://arxiv.org/abs/2509.25140) · [Code](https://github.com/google-research/reasoning-bank) |
| **AWM**: Agent Workflow Memory | 2024 | [Paper](https://arxiv.org/abs/2409.07429) · [Code](https://github.com/zorazrw/agent-workflow-memory) |

### Model harness coupling

| Paper | First year | Resources |
| --- | --- | --- |
| **FST**: Learning, Fast and Slow: Towards LLMs That Adapt Continually | 2026 | [Paper](https://arxiv.org/abs/2605.12484) |
| **JIT-Agent**: Scaling Harness Intelligence via Just-in-Time Harness Evolution | 2026 | [Paper](https://arxiv.org/abs/2608.25593) · [Code](https://github.com/bingreeky/JIT) |
| **SIA**: Self Improving AI with Harness & Weight Updates | 2026 | [Paper](https://arxiv.org/abs/2605.27276) |
| **Skill-Alpha**: Progressive Agent Skill Generation via Reinforcement Learning | 2026 | [Paper](https://arxiv.org/abs/2608.01678) · [Code](https://github.com/ejhshen/skill-alpha) |
| **SkillRL**: Evolving Agents via Recursive Skill-Augmented Reinforcement Learning | 2026 | [Paper](https://arxiv.org/abs/2602.08234) · [Code](https://github.com/aiming-lab/SkillRL) |
| **SMITH**: Joint Optimization of Tool Creation and Use for Large Language Model Agents | 2026 | [Paper](https://arxiv.org/abs/2608.24571) · [Code](https://github.com/appier-research/smith) |
| **Optimas**: Optimizing Compound AI Systems with Globally Aligned Local Rewards | 2025 | [Paper](https://arxiv.org/abs/2507.03041) |

<a id="verification"></a>
## Verification, Judging & Recovery

Feedback, self-correction, evaluators, state validity, recovery, and transaction guarantees.

| Paper | First year | Resources |
| --- | --- | --- |
| **Anchor**: Mitigating Artifact Drift in Agent Benchmark Generation | 2026 | [Paper](https://arxiv.org/abs/2605.26321) |
| **Sim2Real User Simulation**: Mind the Sim2Real Gap in User Simulation for Agentic Tasks | 2026 | [Paper](https://arxiv.org/abs/2603.11245) |
| **VERA**: Scaling Verifiable Environments for Agentic co-Evolution | 2026 | [Paper](https://arxiv.org/abs/2610.05923) · [Code](https://github.com/AutoMedBench/VERA) |
| **Verified Tool Calls** Improve LLM Agent Reliability Under Non-Atomic Failures | 2026 | [Paper](https://arxiv.org/abs/2608.02645) |
| **Who Verifies the Verifier?** Co-Evolving Inspectable Graders with Self-Improving Agents | 2026 | [Paper](https://arxiv.org/abs/2610.11464) |
| **AgentRewardBench**: Evaluating Automatic Evaluations of Web Agent Trajectories | 2025 | [Paper](https://arxiv.org/abs/2504.08942) |
| **Great Models Think Alike** and this Undermines AI Oversight | 2025 | [Paper](https://arxiv.org/abs/2502.04313) · [Code](https://github.com/model-similarity/lm-similarity) |
| **Process Reward Models That Think** | 2025 | [Paper](https://arxiv.org/abs/2504.16828) |
| **Agent-as-a-Judge**: Evaluate Agents with Agents | 2024 | [Paper](https://arxiv.org/abs/2410.10934) |
| **Self-Preference in LLM Evaluators**: LLM Evaluators Recognize and Favor Their Own Generations | 2024 | [Paper](https://arxiv.org/abs/2404.13076) |
| **CRITIC**: Large Language Models Can Self-Correct with Tool-Interactive Critiquing | 2023 | [Paper](https://arxiv.org/abs/2305.11738) · [Code](https://github.com/microsoft/ProphetNet/tree/master/CRITIC) |
| **LATS**: Language Agent Tree Search Unifies Reasoning Acting and Planning in Language Models | 2023 | [Paper](https://arxiv.org/abs/2310.04406) · [Code](https://github.com/andyz245/LanguageAgentTreeSearch) |
| **MT-Bench / Chatbot Arena**: Judging LLM-as-a-Judge with MT-Bench and Chatbot Arena | 2023 | [Paper](https://arxiv.org/abs/2306.05685) · [Code](https://github.com/lm-sys/FastChat/tree/main/llm-judge) |
| **Reflexion**: Language Agents with Verbal Reinforcement Learning | 2023 | [Paper](https://arxiv.org/abs/2303.11366) · [Code](https://github.com/noahshinn/reflexion) |
| **Self-Refine**: Iterative Refinement with Self-Feedback | 2023 | [Paper](https://arxiv.org/abs/2303.17651) · [Code](https://github.com/madaan/self-refine) |
| **Reward Model Overoptimization**: Scaling Laws for Reward Model Overoptimization | 2022 | [Paper](https://arxiv.org/abs/2210.10760) |

<a id="safety"></a>
## Safety, Injection & Authorization

Prompt injection, harmful tool use, permission boundaries, delegation, and side-effect control.

| Paper | First year | Resources |
| --- | --- | --- |
| **Auditing Financial Agent Self-Evolution**: Auditing Self-Evolution in Financial Agents: Capability Gains, Security Drift, and Execution-Interface Mismatch | 2026 | [Paper](https://arxiv.org/abs/2608.17684) |
| **CI-Work**: Benchmarking Contextual Integrity in Enterprise LLM Agents | 2026 | [Paper](https://aclanthology.org/2026.acl-industry.103/) · [Code](https://aka.ms/ci-work) |
| **Facts Without Rules**: Boundary Metadata Collapse in Multi-Agent LLM Handoffs | 2026 | [Paper](https://arxiv.org/abs/2608.29028) · [Code](https://github.com/CrowdDynamicsLab/facts_without_rules_emnlp_2026) |
| **Authenticated Delegation** and Authorized AI Agents | 2025 | [Paper](https://arxiv.org/abs/2501.09674) |
| **AgentDojo**: A Dynamic Environment to Evaluate Prompt Injection Attacks and Defenses for LLM Agents | 2024 | [Paper](https://arxiv.org/abs/2406.13352) · [Code](https://github.com/ethz-spylab/agentdojo) |
| **AgentHarm**: A Benchmark for Measuring Harmfulness of LLM Agents | 2024 | [Paper](https://arxiv.org/abs/2410.09024) |
| **InjecAgent**: Benchmarking Indirect Prompt Injections in Tool-Integrated Large Language Model Agents | 2024 | [Paper](https://arxiv.org/abs/2403.02691) |
| **ToolEmu**: Identifying the Risks of LM Agents with an LM-Emulated Sandbox | 2023 | [Paper](https://arxiv.org/abs/2309.15817) |

<a id="related"></a>
## Related Foundations & Work Impact

Document/answer-only tasks, planning foundations, coordination and database theory, productivity and occupational studies. Retain as context and distinguish from end-to-end working-agent evidence.

| Paper | First year | Resources |
| --- | --- | --- |
| **GDP.pdf**: Benchmarking Grounded Multimodal Reasoning over Professional PDF Documents | 2026 | [Paper](https://arxiv.org/abs/2607.11192) · [Data](https://huggingface.co/datasets/surgeai/GDP.pdf) |
| **Legal Research Bench**: Measuring End-to-End Reliability in Long-Horizon Legal Research Agents | 2026 | [Paper](https://arxiv.org/abs/2610.00609) · [Code](https://github.com/vals-ai/legal-research-bench) |
| **OfficeQA Pro**: An Enterprise Benchmark for End-to-End Grounded Reasoning | 2026 | [Paper](https://arxiv.org/abs/2603.08655) · [Code](https://github.com/databricks/officeqa) · [Data](https://huggingface.co/datasets/databricks/officeqa) |
| **PSEBench**: A Controllable and Verifiable Benchmark for Evaluating LLMs in Patient Safety Event Triage | 2026 | [Paper](https://arxiv.org/abs/2606.05463) |
| **SpreadsheetAgent**: Towards Robust Real-World Spreadsheet Understanding with Multi-Agent Multi-Format Reasoning | 2026 | [Paper](https://arxiv.org/abs/2604.12282) · [Code](https://github.com/renhouxing/SpreadsheetAgent) |
| **BrowseComp**: A Simple Yet Challenging Benchmark for Browsing Agents | 2025 | [Paper](https://arxiv.org/abs/2504.12516) |
| **Finance Agent Benchmark**: Benchmarking LLMs on Real-world Financial Research Tasks | 2025 | [Paper](https://arxiv.org/abs/2508.00828) |
| **Future of Work with AI Agents**: Auditing Automation and Augmentation Potential across the U.S. Workforce | 2025 | [Paper](https://arxiv.org/abs/2506.06576) |
| **PRBench**: Large-Scale Expert Rubrics for Evaluating High-Stakes Professional Reasoning | 2025 | [Paper](https://arxiv.org/abs/2511.11562) |
| **ResearchRubrics**: A Benchmark of Prompts and Rubrics For Evaluating Deep Research Agents | 2025 | [Paper](https://arxiv.org/abs/2511.07685) |
| **AssistantBench**: Can Web Agents Solve Realistic and Time-Consuming Tasks? | 2024 | [Paper](https://arxiv.org/abs/2407.15711) |
| **MMLongBench-Doc**: Benchmarking Long-context Document Understanding with Visualizations | 2024 | [Paper](https://arxiv.org/abs/2407.01523) · [Code](https://github.com/mayubo2333/MMLongBench-Doc) · [Data](https://huggingface.co/datasets/yubo2333/MMLongBench-Doc) |
| **OmniDocBench**: Benchmarking Diverse PDF Document Parsing with Comprehensive Annotations | 2024 | [Paper](https://arxiv.org/abs/2412.07626) · [Code](https://github.com/opendatalab/OmniDocBench) |
| **SpreadsheetLLM**: Encoding Spreadsheets for Large Language Models | 2024 | [Paper](https://arxiv.org/abs/2407.09025) |
| **FinanceBench**: A New Benchmark for Financial Question Answering | 2023 | [Paper](https://arxiv.org/abs/2311.11944) · [Code](https://github.com/patronus-ai/financebench) |
| **LawBench**: Benchmarking Legal Knowledge of Large Language Models | 2023 | [Paper](https://arxiv.org/abs/2309.16289) · [Code](https://github.com/open-compass/LawBench) |
| **LegalBench**: A Collaboratively Built Benchmark for Measuring Legal Reasoning in Large Language Models | 2023 | [Paper](https://arxiv.org/abs/2308.11462) |
| **Productivity Effects of Generative AI**: Experimental evidence on the productivity effects of generative artificial intelligence | 2023 | [Paper](https://doi.org/10.1126/science.adh2586) |
| **ChartQA**: A Benchmark for Question Answering about Charts with Visual and Logical Reasoning | 2022 | [Paper](https://arxiv.org/abs/2203.10244) · [Code](https://github.com/vis-nlp/ChartQA) |
| **ConvFinQA**: Exploring the Chain of Numerical Reasoning in Conversational Finance Question Answering | 2022 | [Paper](https://arxiv.org/abs/2210.03849) · [Code](https://github.com/czyssrs/ConvFinQA) |
| **PlanBench**: An Extensible Benchmark for Evaluating Large Language Models on Planning and Reasoning about Change | 2022 | [Paper](https://arxiv.org/abs/2206.10498) · [Code](https://github.com/karthikv792/LLMs-Planning) |
| **ScienceQA**: Learn to Explain: Multimodal Reasoning via Thought Chains for Science Question Answering | 2022 | [Paper](https://arxiv.org/abs/2209.09513) · [Code](https://github.com/lupantech/ScienceQA) · [Data](https://huggingface.co/datasets/derek-thomas/ScienceQA) |
| **FinQA**: A Dataset of Numerical Reasoning over Financial Data | 2021 | [Paper](https://arxiv.org/abs/2109.00122) · [Code](https://github.com/czyssrs/FinQA) |
| **TAT-QA**: A Question Answering Benchmark on a Hybrid of Tabular and Textual Content in Finance | 2021 | [Paper](https://arxiv.org/abs/2105.07624) · [Code](https://github.com/NExTplusplus/tat-qa) |
| **DocVQA**: A Dataset for VQA on Document Images | 2020 | [Paper](https://arxiv.org/abs/2007.00398) |
| **PubMedQA**: A Dataset for Biomedical Research Question Answering | 2019 | [Paper](https://arxiv.org/abs/1909.06146) · [Code](https://github.com/pubmedqa/pubmedqa) |
| **HotpotQA**: A Dataset for Diverse, Explainable Multi-hop Question Answering | 2018 | [Paper](https://arxiv.org/abs/1809.09600) · [Code](https://github.com/hotpotqa/hotpot) |
| **Productivity J-Curve**: The Productivity J-Curve: How Intangibles Complement General Purpose Technologies | 2018 | [Paper](https://doi.org/10.1257/mac.20180386) |
| **Gradient Episodic Memory** for Continual Learning | 2017 | [Paper](https://arxiv.org/abs/1706.08840) |
| **SQuAD**: 100,000+ Questions for Machine Comprehension of Text | 2016 | [Paper](https://arxiv.org/abs/1606.05250) |
| **Life Beyond Distributed Transactions** | 2007 | [Paper](https://doi.org/10.1145/3012426.3025012) |
| **Case Handling**: a new paradigm for business process support | 2005 | [Paper](https://doi.org/10.1016/j.datak.2004.07.003) |
| **Ten Challenges for Automation Team Players**: Ten Challenges for Making Automation a “Team Player” in Joint Human-Agent Activity | 2004 | [Paper](https://doi.org/10.1109/MIS.2004.74) |
| **Sagas** | 1987 | [Paper](https://doi.org/10.1145/38713.38742) |

<a id="swe-science"></a>
## Software, Data Science & Research Agents

Software development, executable data analysis, ML experiments, and research replication. Record an interface or optimization tag separately.

| Paper | First year | Resources |
| --- | --- | --- |
| **CODESKILL**: Learning Self-Evolving Skills for Coding Agents | 2026 | [Paper](https://arxiv.org/abs/2605.25430) |
| **daVinci-Dev**: Agent-native Mid-training for Software Engineering | 2026 | [Paper](https://arxiv.org/abs/2601.18418) · [Code](https://github.com/GAIR-NLP/daVinci-Dev) |
| **daVinci-Env / OpenSWE**: daVinci-Env: Open SWE Environment Synthesis at Scale | 2026 | [Paper](https://arxiv.org/abs/2603.13023) · [Code](https://github.com/GAIR-NLP/OpenSWE) |
| **DrugDiscoveryBench**: Can Coding Agents Assist Early-Stage Drug Discovery? | 2026 | [Paper](https://labs.scale.com/leaderboard/drugdiscoverybench) · [Code](https://github.com/scaleapi/DrugDiscoveryBench) · [Data](https://huggingface.co/datasets/ScaleAI/DrugDiscoveryBench-Preview) |
| **Function-Aware FIM**: Function-Aware Fill-in-the-Middle as Mid-Training for Coding Agent Foundation Models | 2026 | [Paper](https://arxiv.org/abs/2607.12463) · [Code](https://github.com/TIGER-AI-Lab/FIM-Midtraining) |
| **HiL-Bench** (Human-in-Loop Benchmark): Do Agents Know When to Ask for Help? | 2026 | [Paper](https://arxiv.org/abs/2604.09408) · [Code](https://github.com/hilbenchauthors/hil-bench) · [Data](https://huggingface.co/datasets/ScaleAI/hil-bench) |
| **Socratic-SWE**: Self-Evolving Coding Agents via Trace-Derived Agent Skills | 2026 | [Paper](https://arxiv.org/abs/2606.07412) |
| **SWE Atlas**: Benchmarking Coding Agents Beyond Issue Resolution | 2026 | [Paper](https://arxiv.org/abs/2605.08366) · [Code](https://github.com/scaleapi/SWE-Atlas) |
| **SWE-INTERACT**: Reimagining SWE Benchmarks as User-Driven Long-Horizon Coding Sessions | 2026 | [Paper](https://arxiv.org/abs/2606.30573) · [Code](https://github.com/scaleapi/SWE-Interact) |
| **DABstep**: Data Agent Benchmark for Multi-step Reasoning | 2025 | [Paper](https://arxiv.org/abs/2506.23719) |
| **DataSciBench**: An LLM Agent Benchmark for Data Science | 2025 | [Paper](https://arxiv.org/abs/2502.13897) · [Code](https://github.com/THUDM/DataSciBench) |
| **METR Developer Productivity RCT**: Measuring the Impact of Early-2025 AI on Experienced Open-Source Developer Productivity | 2025 | [Paper](https://arxiv.org/abs/2507.09089) |
| **MLGym**: A New Framework and Benchmark for Advancing AI Research Agents | 2025 | [Paper](https://arxiv.org/abs/2502.14499) · [Code](https://github.com/facebookresearch/MLGym) |
| **PaperBench**: Evaluating AI's Ability to Replicate AI Research | 2025 | [Paper](https://arxiv.org/abs/2504.01848) · [Code](https://github.com/openai/preparedness) |
| **R2E-Gym**: Procedural Environments and Hybrid Verifiers for Scaling Open-Weights SWE Agents | 2025 | [Paper](https://arxiv.org/abs/2504.07164) |
| **SWE-Lancer**: Can Frontier LLMs Earn $1 Million from Real-World Freelance Software Engineering? | 2025 | [Paper](https://arxiv.org/abs/2502.12115) |
| **Agentless**: Demystifying LLM-based Software Engineering Agents | 2024 | [Paper](https://arxiv.org/abs/2407.01489) · [Code](https://github.com/OpenAutoCoder/Agentless) |
| **AutoCodeRover**: Autonomous Program Improvement | 2024 | [Paper](https://arxiv.org/abs/2404.05427) |
| **Data Interpreter**: An LLM Agent For Data Science | 2024 | [Paper](https://arxiv.org/abs/2402.18679) · [Code](https://github.com/geekan/MetaGPT) |
| **DiscoveryBench**: Towards Data-Driven Discovery with Large Language Models | 2024 | [Paper](https://arxiv.org/abs/2407.01725) · [Code](https://github.com/allenai/discoverybench) · [Data](https://huggingface.co/datasets/allenai/discoverybench) |
| **DSBench**: How Far Are Data Science Agents from Becoming Data Science Experts? | 2024 | [Paper](https://arxiv.org/abs/2409.07703) · [Code](https://github.com/LiqiangJing/DSBench) |
| **MLE-bench**: Evaluating Machine Learning Agents on Machine Learning Engineering | 2024 | [Paper](https://arxiv.org/abs/2410.07095) |
| **RE-Bench**: Evaluating frontier AI R&D capabilities of language model agents against human experts | 2024 | [Paper](https://arxiv.org/abs/2411.15114) · [Code](https://github.com/METR/ai-rd-tasks) |
| **ScienceAgentBench**: Toward Rigorous Assessment of Language Agents for Data-Driven Scientific Discovery | 2024 | [Paper](https://arxiv.org/abs/2410.05080) · [Code](https://github.com/OSU-NLP-Group/ScienceAgentBench) · [Data](https://huggingface.co/datasets/osunlp/ScienceAgentBench) |
| **SWE-agent**: Agent-Computer Interfaces Enable Automated Software Engineering | 2024 | [Paper](https://arxiv.org/abs/2405.15793) |
| **SWE-Gym**: Training Software Engineering Agents and Verifiers with SWE-Gym | 2024 | [Paper](https://arxiv.org/abs/2412.21139) · [Code](https://github.com/SWE-Gym/SWE-Gym) |
| **SWT-Bench**: Testing and Validating Real-World Bug-Fixes with Code Agents | 2024 | [Paper](https://arxiv.org/abs/2406.12952) |
| **ChatDev**: Communicative Agents for Software Development | 2023 | [Paper](https://arxiv.org/abs/2307.07924) |
| **MetaGPT**: Meta Programming for A Multi-Agent Collaborative Framework | 2023 | [Paper](https://arxiv.org/abs/2308.00352) · [Code](https://github.com/geekan/MetaGPT) |
| **RepoBench**: Benchmarking Repository-Level Code Auto-Completion Systems | 2023 | [Paper](https://arxiv.org/abs/2306.03091) · [Code](https://github.com/Leolty/repobench) |
| **SWE-bench**: Can Language Models Resolve Real-World GitHub Issues? | 2023 | [Paper](https://arxiv.org/abs/2310.06770) |
| **DS-1000**: A Natural and Reliable Benchmark for Data Science Code Generation | 2022 | [Paper](https://arxiv.org/abs/2211.11501) |

<a id="surveys"></a>
## Surveys and roadmaps

| Paper | First year | Resources |
| --- | --- | --- |
| **Co-Evolution in Agentic Systems**: Toward Self-Directed Evolution Beyond Human Design | 2026 | [Paper](https://arxiv.org/abs/2608.10299) |
| **Code as Agent Harness** | 2026 | [Paper](https://arxiv.org/abs/2605.18747) |
| **Externalization in LLM Agents**: A Unified Review of Memory, Skills, Protocols and Harness Engineering | 2026 | [Paper](https://arxiv.org/abs/2604.08224) |
| **Proactivity-Gym**: Foundations of Proactive Agents: Principles, Technical Layers, and Proactivity-Gym | 2026 | [Paper](https://arxiv.org/abs/2609.37267) |
| **Reliable Self-Evolving Agents**: Diving into Reliable Self-Evolving Agents: A Survey | 2026 | [Paper](https://wkqdzkd.github.io/Awesome-Reliable-Self-Evolving-Agents/Diving_into_Reliable_Self-Evolving_Agents_A_Survey.pdf) · [Code](https://github.com/wkqdzkd/Awesome-Reliable-Self-Evolving-Agents) |
| **Self-Improvements in Modern Agentic Systems**: A Survey | 2026 | [Paper](https://arxiv.org/abs/2607.13104) |
| **The Evolution of AI Office**: From Passive Assistants to Goal-Driven Agents | 2026 | [Paper](https://www.alphaxiv.org/abs/2609.evolution-ai-office-agents) |
| **Towards Long-Horizon Agents**: A Survey | 2026 | [Paper](https://openreview.net/forum?id=HyhfhlbWGh) · [Code](https://github.com/RUC-NLPIR/Awesome-Long-Horizon-Agents) |
| **A Survey of Self-Evolving Agents**: What, When, How, and Where to Evolve on the Path to Artificial Super Intelligence | 2025 | [Paper](https://arxiv.org/abs/2507.21046) |
| **A Survey on Latent Reasoning** | 2025 | [Paper](https://arxiv.org/abs/2507.06203) |
| **Lifelong Learning of LLM Agents**: Lifelong Learning of Large Language Model based Agents: A Roadmap | 2025 | [Paper](https://arxiv.org/abs/2501.07278) |
| **Memory in the Age of AI Agents** | 2025 | [Paper](https://arxiv.org/abs/2512.13564) |
| **Provenance in Databases**: Why, How, and Where | 2009 | [Paper](https://doi.org/10.1561/1900000006) |
| **Interdisciplinary Study of Coordination**: The interdisciplinary study of coordination | 1993 | [Paper](https://doi.org/10.1145/174666.174668) |

<a id="resources"></a>
## Resources

Non-paper documentation and project resources. These do not contribute to the research-paper count.

| Resource | Link |
| --- | --- |
| Codex Manual | [Source](https://developers.openai.com/codex/codex-manual.md) |
| Claude Code Overview | [Source](https://code.claude.com/docs/en/overview) |
| Microsoft Copilot architecture and how it works | [Source](https://learn.microsoft.com/en-us/microsoft-365/copilot/microsoft-365-copilot-architecture) |
| The O*NET Content Model | [Source](https://www.onetcenter.org/content.html) |
| AA-AnalystAgent | [Source](https://artificialanalysis.ai/evaluations/aa-analyst-agent) |
| AA-Briefcase: Agentic Knowledge Work Benchmark | [Source](https://artificialanalysis.ai/evaluations/aa-briefcase) |
| BigLaw Bench | [Source](https://github.com/harveyai/biglaw-bench) |
| Excel Modeling Benchmark | [Source](https://www.vals.ai/benchmarks/emb) |
| Harvey Legal Agent Benchmark | [Source](https://www.harvey.ai/blog/introducing-harveys-legal-agent-benchmark) |
| MedCode | [Source](https://www.vals.ai/benchmarks/medcode) |
| MedScribe | [Source](https://www.vals.ai/benchmarks/medscribe) |
| Medical Long Context Reasoning (MLCR-AA) | [Source](https://artificialanalysis.ai/evaluations/mlcr-aa) |
| PinchBench | [Source](https://github.com/pinchbench/skill) |
| Tax Agent Bench | [Source](https://www.vals.ai/benchmarks/tax_agent_bench) |

<a id="curation"></a>
## Curation and maintenance

This is a structured, evolving reading list. Coverage starts from the companion survey bibliography and the previous repository list, then reconciles identifiers against primary paper or project pages. It is not an exhaustive systematic census.

- **Identity checks:** paper titles and links are checked against primary sources. Excel distinguishes `verified` (identity plus affiliation evidence), `metadata-only` (identity checked; affiliation incomplete), and `pending` (identity still requires confirmation). A checked entry is not a claim that a team member has read the full paper.
- **Years:** the first public preprint year is used when available, independently of later conference publication.
- **Institutions:** the detailed list records paper-time participating institutions and their evidence. A shortened list of main institutions is labeled in the record.
- **Classification:** the taxonomy is a provisional editorial scheme. Work form, persistence, and openness are different dimensions. Benchmark capability tags describe task demands; they do not establish a model’s competence.
- **Open items:** paper identities have source evidence; 2 affiliation records remain incomplete in the Excel.
- **Contributions:** add missing work, improve category boundaries, correct metadata, or help read and summarize a paper. See [CONTRIBUTING.md](CONTRIBUTING.md).

The Excel is the team editing surface. After editing it, run `python3 scripts/catalog.py --import-xlsx paper_list.xlsx` to update the catalog and this README. The command validates before writing and matches records by stable ID. Workbook values are authoritative; blank cells clear the corresponding fields. Run `python3 scripts/catalog.py --check` for a local consistency check.
