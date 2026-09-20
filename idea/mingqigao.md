# From Task Completion to Work Responsibility
## A Survey of Working Agent Evaluation and Benchmarks

**从任务完成到工作承担：Working Agent 的评测与基准综述**

## 1. 这篇文章讲什么

Working agent 的评测对象正在从信息答复和局部操作，扩展到专业成果、企业流程、持续项目和角色职责。这些工作在文件、工具、软件和数字环境中完成，最终留下的可以是一组正确数值、一份可用模型、相互对应的业务记录，也可以是一段时间内的服务与经营结果。

随着工作承担范围扩大，正确性的对象也在变化。局部操作需要完成目标修改；完整交付需要同时满足内容、结构和专业约束；关联流程需要维持前置条件、交接与一致性；持续工作需要在变化中保留承诺、传播更新并安排后续行动。

**本文的中心论点是：工作责任的扩展，表现为 agent 需要维护的约束从局部结果延伸到完整成果、工作依赖和时间。理解 working agent 的能力进展，需要同时考察这些要求如何进入任务、哪些环节交由 agent 完成，以及评价如何判断它们。**

全文据此回答五个问题：

| 研究问题 | 具体内容 | 对应章节 |
|---|---|---|
| RQ1 · Work | 现有 benchmark 要求 agent 承担什么范围的工作？ | §2–6 |
| RQ2 · Delegation | 在同一工作层级，材料、流程、工具和历史状态的提供方式如何改变能力要求？ | §2–6、§8.2 |
| RQ3 · Evaluation | 工作完成由哪些性质定义，评分器通过什么证据和检查作出判定？ | §7、§8.3 |
| RQ4 · Progress | 已报告的成功与失败揭示了哪些局部、组合和持续工作能力？ | §8.4–8.6 |
| RQ5 · Agenda | 下一代任务、评价与 agent 设计应优先解决哪些问题？ | §9 |

论文形成三项贡献。

**第一，工作承担层级与委托条件的联合框架。**以 L0–L5 组织分散的信息任务、文件操作、专业交付、企业流程和持续工作，将横向能力放到具体任务条件中解释。框架既用于文献归位，也用于分析层级转换。

**第二，覆盖任务构造、执行协议与评价设计的系统图谱。**建立 benchmark、任务、具体要求和评分检查之间的对应，比较领域、工作产物、依赖结构、材料供给、状态继承和验收方式，形成可检索、可追溯的资料集。

**第三，跨 benchmark 的验收覆盖分析与评分器审计。**通过要求标注和成对提交测试，分析哪些工作性质得到直接检查，哪些检查只覆盖部分条件，以及评分器对明确违规与合法变化是否敏感；结合文献中的 agent 表现，提出工作依赖、持续状态与协作评价的研究议程。

全文结构沿着以下关系推进：

> **工作承担范围（§3–6）→ 任务条件与能力组合（贯穿 §3–6）→ 评价设计（§7）→ 跨层发现（§8）→ 研究议程（§9）。**

## 2. 统一分析框架

### 2.1 Working agent 与 benchmark 的分析对象

本文将 working agent 定义为：在目标与职责约束下，使用信息、工具和数字环境完成工作，并留下可验收成果、状态变化或持续服务结果的 agent 系统。

主体覆盖办公生产力、企业业务操作、专业知识工作与持续服务。信息问答和局部操作构成基础工作单元；软件工程及模拟经营中的代表任务用于分析可执行验证、依赖管理和持续职责。纯知识考试与一般推理题仅在明确连接这些工作单元时进入比较。

全文使用六个基础对象：

| 对象 | 定义 | 在文献整理中的作用 |
|---|---|---|
| Work goal | 工作要达到的结果及使用目的 | 判断任务终点与业务语境 |
| Workspace | 可访问的文件、记录、工具与软件环境 | 描述材料和行动空间 |
| Work product | 可交付、交接或继续使用的成果 | 比较内容、结构和功能要求 |
| Work state | 文件、业务系统、承诺与执行进度的当前状态 | 描述操作结果及后续依赖 |
| Work requirement | 任务明确要求成立的性质或条件 | 连接能力需求与验收检查 |
| Evaluation protocol | 执行、反馈、提交、判分和汇总规则 | 确定成绩对应的运行条件 |

以任务为单位确定工作层级；以具体要求为单位分析验收覆盖；以模型及运行配置为单位整理表现。同一 benchmark 的不同任务可以进入不同层级。

### 2.2 纵向主线：L0–L5 工作承担层级

| 层级 | 定义与判定依据 | 新增的工作责任 | 真实任务锚点 |
|---|---|---|---|
| **L0 Information Results** 信息结果 | 完成一个明确的信息子问题，工作终点是抽取、计算或判断结果 | 建立材料、口径与结论的正确对应 | OfficeQA Pro：财政资料回归系数 |
| **L1 Local Operations** 局部操作 | 在既有成果或环境中完成明确范围的修改 | 正确实施改变，满足功能及保留要求 | SpreadsheetBench：写入指定区域的查找公式 |
| **L2 Complete Deliverables** 完整交付 | 围绕一个工作目标形成可独立验收、使用或交接的专业成果 | 组织内容与结构，满足整体质量和使用条件 | GDPval dashboard；TAC 员工手册；AA-Briefcase 市场模型 |
| **L3 Integrated Workflows** 关联工作流 | 完成具有各自业务目的、又通过前置条件或交接相连的环节、成果或状态变更 | 维护跨环节依赖、实体对应和整体完成条件 | WorkArena++ 入职；TAC 确认反馈后更新工单 |
| **L4 Continuing Projects** 持续项目 | 运行中出现新信息、反馈或环境变化后，继续维护同一项目及其历史状态 | 保留约束与承诺，传播更新，调整既有计划和成果 | VibeLife 装修项目与动态差旅 |
| **L5 Persistent Responsibilities** 持续职责 | 在规定角色和权限内处理持续出现的工作需要与事件 | 发现待办、安排优先级、协调资源并持续达成角色目标 | Vending-Bench 2 年度经营 |

L0→L1 将信息结果落实为改变；L1→L2 将局部操作组织为整体成果；L2→L3 将完整环节连接为工作流程；L3→L4 引入对已有工作的持续维护；L4→L5 扩展到需要持续选择和安排工作的角色职责。

层级按实际委托单元与运行协议定位。复杂回归计算可以属于 L0；以文本提交的完整法律意见可以属于 L2。工作簿内部公式作为成果内部约束分析；员工创建与资产分配属于相连的业务环节。场景年份、运行步数、文件数量与上下文长度分别记录。

持续性需要从协议确认：后续阶段是否承接已经形成的成果、状态或承诺，外部变化何时发生，agent 是否继续维护这些对象。AA-Briefcase 当前各任务独立运行、不继承自己的前序提交，因而其多周背景与实际状态延续应分列记录。[官方协议说明](https://artificialanalysis.ai/articles/aa-briefcase)

### 2.3 横向解释：C1–C7 能力及其工作作用

| 能力 | 具体内容 | 随工作层级扩展的作用 |
|---|---|---|
| **C1 Understanding and Grounding** | 目标理解、文档解析、材料定位、来源与版本识别 | 从定位事实到理解工作区、依赖来源及变更影响 |
| **C2 Analysis and Professional Reasoning** | 计算、信息综合、专业规则、权衡与判断 | 从得出局部结论到组织专业成果、支撑项目决策 |
| **C3 Planning and Coordination** | 分解、步骤安排、协议执行、澄清、审批与交接 | 从安排操作到管理前置条件、重规划与优先级 |
| **C4 Tool and Environment Interaction** | 工具选择与参数、代码、API、GUI、反馈读取 | 从局部编辑到跨系统改变和业务执行 |
| **C5 Deliverable Construction** | 内容组织、结构、公式、版式、可编辑性与可用性 | 从形成成果到满足交接和下游使用要求 |
| **C6 Memory and State Management** | 中间结果、历史记录、版本、依赖与承诺维护 | 从任务内状态到项目延续与跨任务资源协调 |
| **C7 Verification and Adaptive Revision** | 核验、定位错误、修复、反馈适应和更新传播 | 从自检局部结果到恢复工作流和持续监测 |

能力采用多标签。标注依据是任务中的可观察要求，例如版本冲突需要来源判断，资产归属需要实体对应，变更后维护排期需要依赖更新。Agent 的自检归 C7；外部评分器属于评价协议。

正文每一层讨论能力怎样组合，第 8 章再比较这些作用如何改变。文件类型用于解释结构和操作差异：表格提供公式与引用关系，演示稿涉及视觉和叙事，文档涉及层次、溯源与修订，企业记录涉及对象间约束。

### 2.4 同层差异：Delegation Boundary

委托边界描述工作开始时已经提供什么，以及执行中仍需 agent 作出什么判断。采用四组字段：

| 条件 | 记录内容 | 可形成的对照 |
|---|---|---|
| **Information** 材料 | 全工作区、筛选材料、相关页、解析文本、抽取事实 | 自行找材料与直接使用相关材料 |
| **Procedure** 流程 | 目标、模板、操作清单、可检索协议、审批条件 | 显式步骤与协议检索 |
| **Execution** 执行 | 工具接口、自动化脚本、既有技能、环境恢复支持 | 不同操作封装下仍需作出的决定 |
| **Continuity** 延续 | 历史记录、前序产物、状态继承、事件与反馈 | 重新开始、接收历史包与延续已有工作 |

工具可用性作为实验条件记录；实际代为完成的检索、组织或操作环节另作标注。OfficeQA 的全文库与 oracle 页、WorkArena++ 的步骤呈现与协议检索是同任务对照的起点。

### 2.5 连接任务与评分：具体要求链

本文用一条逐项可追溯的链连接任务与评价：

> **任务明确要求 → 可观察的成功条件 → Rubric 声明 → 评分器使用的证据与检查 → 运行中的判定。**

例如，任务要求工作簿可随数据更新，成功条件是输入变化后相关结果与图表正确响应；验收可以使用原生文件、公式检查和重算。任务要求确认负责人反馈后再修改工单，成功条件包含正确联系人、完成确认、目标工单和动作关系。

证据范围包括答案、原生文件、环境状态与过程记录。每项检查可组合多个范围。覆盖描述评分器针对哪些性质作出判断；可靠性描述这些判断是否准确、稳定。

## 3. 论文完整目录

### 1. Introduction
1.1 Working Agents and the Expansion of Work  
1.2 From Local Correctness to Work Responsibility  
1.3 Research Questions and Contributions

### 2. Scope and Analytical Framework
2.1 Working Agents, Work Products, and Work States  
2.2 L0–L5: Levels of Work Responsibility  
2.3 Capabilities and Their Roles Across Levels  
2.4 Delegation Boundaries and Provided Support  
2.5 Work Requirements and Evaluation Records  
2.6 Literature Collection and Annotation

### 3. L0–L1: Information Results and Local Operations
3.1 Grounded Retrieval, Understanding, and Analysis  
3.2 Local Artifact Editing and State Changes  
3.3 Task Sources, Construction, and Input Conditions  
3.4 Capability Composition and Local Failure Modes  
3.5 Correctness, Functionality, and Preservation

### 4. L2: Complete and Usable Work Deliverables
4.1 Documents and Professional Reports  
4.2 Spreadsheets, Models, and Analytical Products  
4.3 Presentations and Visual Communication  
4.4 Materials, Templates, and Workspace Exploration  
4.5 Integrating Content, Structure, and Professional Constraints  
4.6 Deliverable Quality and Downstream Use

### 5. L3: Integrated Workflows and Dependency Management
5.1 Dependencies Across Artifacts and Work Stages  
5.2 Cross-Application and Enterprise Workflows  
5.3 Procedures, Coordination, and Human Handoffs  
5.4 Environment Construction and Delegation Conditions  
5.5 Error Propagation and Workflow Completion

### 6. L4–L5: Continuing Projects and Persistent Responsibilities
6.1 L4: Revising Projects Under Changing Conditions  
6.2 State Continuity, Commitments, and Recovery  
6.3 L5: Task Streams, Priorities, and Role Objectives  
6.4 Event Generation, Time, and Interaction Protocols  
6.5 Sustained Performance and Work Outcomes

### 7. Evaluation Design: Requirements, Evidence, and Decisions
7.1 Evaluation Targets and Acceptance Properties  
7.2 Evidence Sources and Implemented Checks  
7.3 Rule-Based, Executable, Model-Based, and Human Evaluation  
7.4 Execution Protocols, Budgets, and Feedback  
7.5 Score Aggregation and Reported Metrics  
7.6 Validity, Reliability, and Reproducibility

### 8. Cross-Benchmark Synthesis: Delegation, Coverage, and Reliability
8.1 The Landscape of Work Levels and Capability Combinations  
8.2 Delegation Conditions Within and Across Levels  
8.3 Work Requirements and Evaluation Coverage  
8.4 Paired Submission Audits  
8.5 Reported Agent Performance and Failure Patterns  
8.6 Implications for Agent Design

### 9. Research Agenda: Advancing Work Through Better Evaluation
9.1 Constructing Tasks from Work Dependencies  
9.2 Evaluating Change, Continuity, and Persistent Roles  
9.3 Calibrating Evaluators with Valid and Invalid Outcomes  
9.4 Generalization Across Domains, Artifacts, and Interfaces  
9.5 Human Collaboration, Work Value, and Resource Use  
9.6 Shared Evaluation Infrastructure

### 10. Conclusion

### Appendices
A. Search Strategy and Benchmark Inventory  
B. Task-Level Mapping and Annotation Guide  
C. Ten Source-Grounded Task Cards  
D. Requirement–Check Correspondence  
E. Audit Materials and Detailed Results  
F. Data, Environments, Evaluators, and Access Conditions

## 4. 每一章具体写什么

### Section 1 · Introduction

**本章论证：工作责任扩展改变了能力要求和完成标准，需要一个连接任务、委托与评价的综述框架。**

**1.1 Working Agents and the Expansion of Work。**从信息助手、文件操作到专业交付和持续工作展开。以三个已发布案例建立直观跨度：SpreadsheetBench 的局部公式操作、WorkArena++ 的入职流程、VibeLife 的变化项目。说明工作完成可能留下文件、业务状态和持续结果。

**1.2 From Local Correctness to Work Responsibility。**沿着成果、依赖和时间解释新增约束。同样是“完成财务分析”，输入材料是否已经筛选、流程是否已经安排、成果是否需要继续更新，会形成不同能力要求。用局部值检查、员工—资产关系检查和变更后项目维护说明验收对象的扩展。

**1.3 Research Questions and Contributions。**给出五个研究问题和三项贡献。Figure 1 展示分层 benchmark 主体、评价综述、跨层分析和研究议程之间的关系。引言中使用已经核实的设计事实；分布、覆盖比例和审计结果由 §8 提供后写入。

**本章产出：**Figure 1；研究问题与章节对应；三项贡献的成稿段落。

### Section 2 · Scope and Analytical Framework

**本章论证：统一工作单元、委托条件和具体要求，才能让异构 benchmarks 进入同一套比较。**

**2.1 Working Agents, Work Products, and Work States。**给出六个基础对象，区分完整交付、业务状态和持续结果。列明主体范围及相邻研究的纳入方式。Benchmark 主表在这里首次出现，帮助读者看到论文覆盖哪些工作形态。

**2.2 L0–L5: Levels of Work Responsibility。**完整定义层级及判定条件。按“工作终点—新增责任—运行条件—典型例子”呈现。使用复杂分析仍属信息结果、完整工作簿内部依赖、入职跨实体关系、真实状态延续四组实例解释关键分界。

**2.3 Capabilities and Their Roles Across Levels。**介绍 C1–C7，并展示能力作用的变化。规划从操作安排扩展到工作依赖与优先级；状态管理从中间结果扩展到承诺、版本与角色任务。能力标签进入主表，详细组合随 §3–6 展开。

**2.4 Delegation Boundaries and Provided Support。**定义材料、流程、执行与延续四组条件。给出 OfficeQA 和 WorkArena++ 的两个原生对照，说明它们分别改变哪些工作环节。正文保持对提供条件的描述；受控表现比较进入 §8.2。

**2.5 Work Requirements and Evaluation Records。**建立任务要求、成功条件、验收声明、实现检查和运行观察的记录关系。示例行分别使用公式功能、公司政策忠实性和确认后改状态。记录评分器检查了什么以及资料来源。

**2.6 Literature Collection and Annotation。**以现有 HTML 文献清单和参考综述为种子，补充论文、官方仓库、数据卡及运行说明，进行前后向检索。记录版本、访问日期、公开任务与评价资料；去重时保留 benchmark 版本关系。两名作者对十项任务独立试标，讨论分歧后固定手册，再按层级、领域和任务形态扩展语料。模板与生成实例分别编号。

**本章产出：**Figure 2（L0–L5 与委托/能力/验收的关系）；Table 1（benchmark 总表）；Table 2（定义与标注实例）。

**与后文的连接：**§3–6 使用同一字段比较文献；§7 完整展开评价；§8 将字段连接为分析结果。

### Section 3 · L0–L1: Information Results and Local Operations

**本章论证：基础工作单元包含不同的信息与修改要求，它们构成更大工作单元的可复用基础。**

**3.1 Grounded Retrieval, Understanding, and Analysis。**覆盖文档检索、跨页理解、表格信息提取、数值分析与职业相关判断。比较给定片段、相关文件与完整资料库；单来源与多来源；答案格式、单位和来源要求。OfficeQA Pro 的回归任务作为锚点，解释检索与计算的组合。

**3.2 Local Artifact Editing and State Changes。**覆盖表格单元格修改、幻灯片局部编辑、文档格式调整、指定业务字段更新。比较目标范围是否明确、操作是否改变既有内容、是否要求公式或其他可执行结构，以及未修改内容的保留条件。SpreadsheetBench 59196 用于连接当前值与公式功能。

**3.3 Task Sources, Construction, and Input Conditions。**比较来自用户需求、现成文档、编辑前后状态和模板生成的任务。说明输入扰动、多测试工作簿、干扰材料与解析预处理怎样形成不同难点。把材料获取与目标操作所占的工作分别记录。

**3.4 Capability Composition and Local Failure Modes。**按检索定位、口径理解、计算、操作与自检组织文献报告的失败。讨论错误如何影响后续成果，例如错误抽取污染模型、局部编辑破坏引用。原始成绩按各自任务、模型和配置呈现。

**3.5 Correctness, Functionality, and Preservation。**归纳本层的验收性质：答案正确、目标区域正确、功能成立、保留条件满足。这里只说明各类任务如何定义完成；评分执行机制在 §7 统一比较。

**核心材料：**T01 OfficeQA Pro；T02 SpreadsheetBench。扩展相关任务来自 LegalBench、MMLongBench-Doc、Finance Agent、PPTC、OSWorld 与 Windows Agent Arena，按原题归位。

**本章产出：**Table 3：输入条件、操作范围、能力组合及验收性质对照。

**进入下一章：**完整成果需要同时组织多个局部结果，并满足整体使用条件。

### Section 4 · L2: Complete and Usable Work Deliverables

**本章论证：完整交付把内容、结构、专业要求与后续使用结合起来，局部正确需要汇合为整体质量。**

**4.1 Documents and Professional Reports。**覆盖报告、手册、备忘录、专业意见与研究综合。比较材料整合、论证组织、来源忠实性、规范适用、受众和内容完整性。TAC 员工手册作为具体例子，区分栏目名称、实质内容和公司材料之间的关系。

**4.2 Spreadsheets, Models, and Analytical Products。**覆盖建模、分析表、dashboard 和模板型工作工具。比较数据组织、公式、引用、约束、筛选与图表；将输入变化后的响应作为可用性的重要观察。GDPval 产量 dashboard 与 AA-Briefcase 市场模型分别展示操作管理和专业建模的交付要求。

**4.3 Presentations and Visual Communication。**覆盖材料到演示稿、报告到 slides、模板内生成和完整演示稿修订。比较内容选择、叙事顺序、数据忠实性、版式、视觉一致性和可编辑结构；记录输入与输出之间的对应。

**4.4 Materials, Templates, and Workspace Exploration。**横向比较本层中给定材料、含噪工作区、现成模板、参考成品与自由组织的差异。材料供给决定 agent 需要完成哪些检索和取舍；输出模板决定哪些结构已被设计。复杂资料池中的一次专业成果仍以实际交付目标归类。

**4.5 Integrating Content, Structure, and Professional Constraints。**分析 C1、C2、C5 与 C7 怎样共同形成整体质量。重点写约束之间的联系：数据改变如何影响图表和论证，内容压缩怎样影响忠实性，专业判断如何进入产品结构。综合文献中的失败，而非按文件类型各重复一次能力列表。

**4.6 Deliverable Quality and Downstream Use。**整理正确性、完整性、结构有效性、可读性、可编辑性、专业适用性和后续使用。沿用并引用 AI Office 的交付物质量研究，再把性质对应到具体任务。[AI Office 全文](https://github.com/Qwen-Applications/AI-Office-Survey/blob/main/main.pdf)

**核心材料：**T03 GDPval dashboard；T04 TAC 手册；T05 AA-Briefcase-Lite 市场模型。扩展 PresentBench、PPTEval、SpreadsheetBench 2、BankerToolBench、JOBBench、OmegaUse-OfficeVal、Harvey LAB/BigLaw 的相关成果任务。

**本章产出：**Figure 3（成果内部约束与后续使用）；Table 4（交付类型、材料条件、质量要求和验收对象）。

**进入下一章：**当成果进入后续业务环节，正确性还需要覆盖成果和动作之间的关系。

### Section 5 · L3: Integrated Workflows and Dependency Management

**本章论证：工作流的完成依赖于局部结果之间的前置条件、实体对应和交接，评价需要能表达这些关系。**

**5.1 Dependencies Across Artifacts and Work Stages。**按四类关系展开：数据与来源依赖、结论与表示一致性、审批与行动前提、产物与下游使用。用小型依赖图表示源数据、模型、报告和演示材料之间的关系；区分并行独立交付与需要共同成立的关系。

**5.2 Cross-Application and Enterprise Workflows。**覆盖跨文件工作区、桌面/浏览器跨应用、企业系统和业务对象链。比较实体标识、跨系统信息传递、状态变更与执行顺序。WorkArena++ 的员工—订单—资产链展示跨对象关系，TAC 的沟通—工单更新展示条件依赖。

**5.3 Procedures, Coordination, and Human Handoffs。**整理显式步骤、可检索协议、需要自行组织的任务；加入需求澄清、审批、协作者反馈和交接。说明人类承担的判断及 agent 的权限、行动范围，比较如何模拟协作者及其回应。

**5.4 Environment Construction and Delegation Conditions。**比较固定快照、可执行企业环境、浏览器与桌面应用、模拟用户和工具 API。讨论重置、共享状态、环境噪声、初始数据及任务生成方式。WorkArena++ 原生的两种步骤提供条件用于展示同一工作目标下的条件变化。

**5.5 Error Propagation and Workflow Completion。**归纳前置条件遗漏、对象错配、失效信息传递、操作顺序错误和局部成功后的整体失败。记录 workflow success、子任务结果与关系条件如何结合。展示直接检查资产归属的设计，并与仅检查多个局部状态的设计比较。

**核心材料：**T06 WorkArena++ 入职；T07 TAC 状态确认与更新。扩展 OfficeBench、AppWorld、AutomationBench、CRMArena/Pro、tau²-bench、Toolathlon 与 Workspace-Bench 中具有工作关系的任务。

**本章产出：**Figure 4（同一流程的委托条件与依赖）；Table 5（依赖类型、环境、协作方式与流程完成条件）。

**进入下一章：**工作流在新信息到来后继续运行，需要维护已经建立的关系和承诺。

### Section 6 · L4–L5: Continuing Projects and Persistent Responsibilities

**本章论证：持续工作需要在环境变化和新事件中延续已有约束；角色职责进一步要求主动组织不断出现的工作。**

**6.1 L4: Revising Projects Under Changing Conditions。**覆盖新材料、需求修订、预算变化、资源失效和协作者更新。比较变化如何注入、agent 何时可见、哪些旧成果需要更新。VibeLife 装修案例用于展示预算、审批和工程变化之间的影响链；差旅案例展示航班、会议和费用约束的共同维护。

**6.2 State Continuity, Commitments, and Recovery。**记录上下文、文件、业务记录、计划和承诺如何延续；比较任务重启、暂停恢复、阶段切换及历史压缩。讨论旧约束保持、版本识别、过期状态更新和错误恢复。区分 agent 处理造成的改变与环境自行演进，在相应任务中选择可观察证据。

**6.3 L5: Task Streams, Priorities, and Role Objectives。**覆盖有持续角色目标的经营与服务任务。比较周期任务、突发事件、优先级、资源竞争和职责完成。Vending-Bench 2 展示一个固定评估时段内的持续经营目标；将经营结果与行为诊断分别呈现。

**6.4 Event Generation, Time, and Interaction Protocols。**系统比较场景时间、模拟时间、实际运行时间、事件安排、用户回应、心跳触发与停止条件。画出状态继承和事件可见性的时间线，明确完整历史一次性提供、独立子任务执行、连续项目推进和角色任务流各自的协议。

**6.5 Sustained Performance and Work Outcomes。**整理阶段完成、历史约束保持、变化响应、恢复、及时性及终局结果。介绍相应指标怎样对齐任务目标；跨阶段诊断与最终业务结果可以共同解释持续工作。

**核心材料：**T08 VibeLife 装修；T09 VibeLife 工作坊差旅；T10 Vending-Bench 2。其他持续任务按事件与运行协议扩展归位。AA-Briefcase 在此作为执行协议对照，其已核实的一次交付任务仍放 §4。

**本章产出：**Figure 5（持续工作协议时间线）；Table 6（状态继承、事件、职责、停止条件与评价对象）。

**进入下一章：**各层已经明确工作要求，§7 统一比较这些要求如何转化为判定。

### Section 7 · Evaluation Design: Requirements, Evidence, and Decisions

**本章论证：评价设计由验收性质、证据、检查动作、执行协议与分数汇总共同构成，各部分需要分别比较。**

**7.1 Evaluation Targets and Acceptance Properties。**先整理判定对象：答案、成果、环境状态、工作过程和持续结果；再整理性质：正确、完整、功能、呈现、来源、关系、约束保持、及时性及业务目标。建立性质与对象的多对多映射，保留领域中的专业验收条件。

**7.2 Evidence Sources and Implemented Checks。**按答案文本、原生文件、环境状态和过程记录整理证据。对应检查动作包括值匹配、公式读取与重算、文件结构和渲染、数据库引用核对、语义评判、事件窗口查询与轨迹条件判断。比较原生证据能提供什么，以及具体实现实际判断了什么。

**7.3 Rule-Based, Executable, Model-Based, and Human Evaluation。**分别综述确定性规则、执行式检查、模型判断、具备工具取证能力的评分 agent 和人工专家；说明 rubric 如何由不同执行者使用。比较可处理的性质、所需参考、判定稳定性、校准及组合方式。讨论 agent 自检与外部评分共享工具或信息时的独立性。

**7.4 Execution Protocols, Budgets, and Feedback。**记录输入解析、工具、记忆重置、状态继承、尝试次数、失败重试、运行预算、评分预算、反馈是否可见及终止条件。对任务实例、完整 agent 系统和评分器分别记录配置。比较单次表现、重复运行可靠性、阶段执行和完整项目执行的实验单位。

**7.5 Score Aggregation and Reported Metrics。**整理精确匹配、单元格/条目通过率、任务全通过、加权 rubric、成对偏好、胜率/Elo、轨迹与终局效用等指标。重点解释汇总怎样处理部分完成、关键约束、负面副作用、成本和时间。通过已有任务说明局部均值、全条件通过和整体偏好回答的不同问题。

**7.6 Validity, Reliability, and Reproducibility。**从任务、参考标准和评分器三个层面整理评价效度。任务层面比较职业代表性、材料来源、模板/实例重叠、训练测试划分与污染控制；参考标准层面比较来源质量、专家一致性和有效解的多样性；评分器层面比较与人工判断的一致性、合法变化鲁棒性、错误敏感性及重复运行波动。同时记录执行与取证成本、环境复现条件。资源表包含数据、输入文件、运行环境、评分代码、提示词、版本与访问条件。

**核心材料：**十项任务中的验收设计，加上完整文献池的评分章节和公开实现。GDPval 与 AA-Briefcase 用于整体质量和 rubric；SpreadsheetBench、WorkArena++ 与 TAC 用于具体检查；VibeLife 与 Vending-Bench 用于时间和结果协议。

**本章产出：**Table 7（性质—证据—动作—执行者—汇总）；Table 8（协议、可靠性证据与复现条件）。

**与 §8 的分工：**本章整理已有评价设计；§8 使用统一记录计算分布、覆盖和审计结果。

### Section 8 · Cross-Benchmark Synthesis: Delegation, Coverage, and Reliability

**本章论证：将工作层级、委托条件和验收检查放在一起，才能说明当前进展集中在哪里，以及不同结果如何被解释。**

**8.1 The Landscape of Work Levels and Capability Combinations。**给出层级 × 领域/职业、层级 × 产物/环境、层级 × 能力的分布；展示同一能力在不同工作单元中的具体作用。Benchmark 数、任务数和要求数分别统计。数据来源与构造方式进入分组，同时记录公开的采样、去重、参考标准和数据划分信息，分析哪些工作组合已有较多材料、哪些仍待覆盖，以及样本如何代表相应工作。

**8.2 Delegation Conditions Within and Across Levels。**统计材料、步骤、执行支持和历史状态的提供方式。先整理跨库设计分布，再分析 OfficeQA 的全文库/oracle 条件及 WorkArena++ 的步骤呈现/协议检索。受控运行固定任务配置、模型、工具和预算，分别报告变化的条件与结果。模型自身判断、环境预处理和系统支持通过已知配置解释。

**8.3 Work Requirements and Evaluation Coverage。**将每项明确要求连接到 rubric、实现检查和可观察证据。统计直接覆盖、部分覆盖、未覆盖与资料不足；比较公式功能、内容忠实、前置条件、实体关系、历史约束和变化传播等性质。展示四个对照：值与公式功能；栏目与实质内容；局部状态与条件依赖；阶段记录与实际恢复。

**8.4 Paired Submission Audits。**选择有明确要求、评分入口与有效基准的任务，构造单项违规及合法变体。首轮覆盖局部公式、完整手册、员工资产关系和确认后改状态；动态项目在完成运行环境复现后加入。分别报告违规检出、合法变体误拒和重复评分波动，连续评分报告配对变化。

**8.5 Reported Agent Performance and Failure Patterns。**系统归纳文献中的表现，按原始任务与配置保留成绩；将有证据支持的错误映射到局部能力、成果整合、依赖协调、项目延续和持续职责。对可多因解释的失败保留组合标签。结合审计结果，讨论评分能揭示的失败与尚需追加诊断的问题。

**8.6 Implications for Agent Design。**用短节连接 benchmark 与方法：材料定位对应检索和工作区探索；业务依赖对应计划、协议与工具编排；持续状态对应记忆、版本和任务状态；完整质量对应自检、渲染和修复；角色任务流对应调度与协作。方法表记录针对的工作要求、改变的执行条件、已报告增益与支持证据。选择 PPTAgent、StagedWorkspace 及文献池中的代表系统展开，控制篇幅。

**本章产出：**Figure 6（跨层覆盖图谱）；Figure 7（要求与实际检查）；Figure 8（成对审计结果）；Table 9（性能、失败与方法回应）。

**进入下一章：**把识别出的任务设置、验收缺口和能力瓶颈转化为下一代设计问题。

### Section 9 · Research Agenda: Advancing Work Through Better Evaluation

**本章论证：下一代评测应围绕具体工作依赖、持续条件和验收需求进行构造，并连接到可实施的 agent 改进。**

**9.1 Constructing Tasks from Work Dependencies。**从工作目标分解环节、对象和条件，构造数据来源、实体引用、审批和交接关系；通过材料缺口、冲突版本、依赖深度与预给步骤形成受控变化。将现有知识图谱出题思路落到“目标要求—任务结构—验收检查”的共同生成。

**9.2 Evaluating Change, Continuity, and Persistent Roles。**设计需要承接自身成果的项目，注入有时机和影响对象的事件，检查旧约束保持、更新传播和恢复。进一步构造角色任务流，明确职责、权限、资源竞争、优先级和终止条件。将事件来源、环境自然演化和 agent 行动记录为可区分因素。

**9.3 Calibrating Evaluators with Valid and Invalid Outcomes。**为任务发布合法变体、单项违规和独立检查，将评分器的敏感性与误判作为配套结果。对开放式专业成果结合专家标准、原生文件行为与语义判断，研究取证范围与评分成本的配置。

**9.4 Generalization Across Domains, Artifacts, and Interfaces。**分层研究同任务的新数据/模板、同能力的新产物、同流程的新领域、同目标的新软件接口，以及变化条件下的持续执行。控制目标要求和评分性质，让迁移结果有共同的比较基础。

**9.5 Human Collaboration, Work Value, and Resource Use。**把澄清、审批、交接和复核作为任务过程的一部分，记录人工时间与质量收益。联合呈现成功、使用价值、及时性、执行成本、评分成本与人工投入；以具体职业目标解释指标选择。

**9.6 Shared Evaluation Infrastructure。**建立任务包、状态快照、环境适配、检查组件、评分日志和版本记录的共享格式。同步维护论文表格与 awesome 列表，发布任务卡和审计材料；让新任务能够复用已有环境与评价组件。

**本章产出：**Table 10（前文发现—设计变量—验收条件—研究问题），附录 F 资源清单与配套仓库结构。

### Section 10 · Conclusion

总结工作责任如何从局部结果扩展到成果、依赖和时间，以及这一扩展怎样改变任务构造、能力组合与评价。以 §8 的具体结果概括当前覆盖和研究重点，收束到可持续、可验收的工作能力。

## 5. 横向分析与实证的执行规范

### 5.1 四种材料分别保存

| 层面 | 记录什么 | 可支持的判断 |
|---|---|---|
| 任务要求 | Prompt、任务政策、明确输出要求及成功条件 | 工作要求是什么 |
| 验收声明 | Rubric、checklist、专家标准 | 评价设计声称检查什么 |
| 实现检查 | 评分代码、评分提示词、输入和判断路径 | 实现直接或部分覆盖什么 |
| 运行观察 | 有效提交、评分日志、具体判定 | 在样例上实际判断了什么 |

十项任务已经完成原题和公开评价材料的初步核验；成对审计尚未执行。正式分析逐项保存版本、来源定位和核验状态。以当前公开材料可判断的范围填写记录。

### 5.2 要求的划分与覆盖标注

一项要求应对应一个能够独立判断的成功条件。并列要求拆分，语义相同的重复条目合并，并保存与原始 rubric 的映射。任务明确要求进入主要分析；为扩展研究新增的要求单独保存。

- **直接覆盖：**实现包含针对该成功条件的直接判断。
- **部分覆盖：**实现只判断部分子条件或间接特征，例如用栏目名称代表内容完整性。
- **未覆盖：**已审阅完整相关评分路径，未找到对应检查。
- **资料不足：**无法取得实现，或无法确认有关评分路径。

针对某项性质实施了语义判断可以构成设计覆盖，其判定准确性由评分器校准与审计进一步研究。部分覆盖保留类别，不赋固定折扣分。

### 5.3 统计单位与四项指标

主表保存 benchmark、版本、任务模板、任务实例和要求 ID。十项锚点用于编码校准；扩展样本按层级、领域和任务类型分层，公布抽样清单及各组数量。重复 seed 作为同一设计的运行重复记录。

| 指标 | 分子 | 分母 | 汇总方式 |
|---|---|---|---|
| 要求直接覆盖率 | 有直接实现检查的要求数 | 实现情况可判断的原题要求数 | 先算任务比例，再在 benchmark 内宏平均 |
| 资料不足率 | 实现情况不可判断的要求数 | 全部原题要求数 | 与覆盖率并列报告 |
| 违规检出率 | 各违规变体的检出比例之和 | 完成有效评分的违规变体数 | 按要求类型与评分器报告 |
| 合法变体误拒率 | 各合法变体的误拒比例之和 | 完成有效评分的合法变体数 | 与违规检出率并列报告 |

部分覆盖与未覆盖给出分布。没有可判断要求的任务不计算覆盖率，并保留在资料可得性统计中。跨 benchmark 的整体汇总使用 benchmark 宏平均，同时呈现分组和样本数。不同 benchmark 的原始成功率在其原始协议下呈现；同任务受控对照用于研究条件变化。

### 5.4 成对审计协议

每组审计材料包含：一个经独立核验满足任务全部相关要求的基准提交，一个仅破坏目标要求的违规变体，一个保持这些要求成立的合法变体，以及独立核对其标签的方法。预先记录目标验收项、评分入口、判定阈值、随机性和重复次数。每个变体先计算多次有效评分中的判定比例，再对变体求均值；重复运行不增加独立变体数。环境故障单列；连续评分呈现同一基准下的配对变化。

| 首轮任务 | 目标性质 | 违规变体 | 合法变体 | 核对方式 |
|---|---|---|---|---|
| SpreadsheetBench 59196 | 原题要求的公式功能 | 公式替换为当前同值常量 | 使用等价公式 | 读取公式并改变输入重算 |
| TAC 员工手册 | 某节实质内容或源材料一致性 | 保留栏目与可读性，删除关键内容或改错明确政策 | 同义改写并保持实质内容 | 源材料与文档内容逐项复核 |
| WorkArena++ 入职 | 新员工与资产归属关系 | 把资产归给另一用户 | 使用等价合法执行路径 | 数据库对象和引用字段核对 |
| TAC 状态确认 | 确认完成后再更新 | 缺少完成确认，保持完成终态 | 等价的明确完成回复 | 核对对话、对象与动作关系 |

前两项以成果为主要实验对象；后两项需要可复现环境状态或轨迹。动态项目审计在确认兼容环境与回放入口后实施，延续相同的单项要求控制。

## 6. 十项任务怎样进入全文

| ID | 任务 | 主归属 | 再次使用的位置 |
|---|---|---|---|
| T01 | OfficeQA Pro UID0013 | §3.1 | §2.4 委托条件；§8.2 同任务对照 |
| T02 | SpreadsheetBench 59196 | §3.2 | §7.2 检查动作；§8.3–8.4 公式验收 |
| T03 | GDPval 产量 dashboard | §4.2 | §4.6 下游使用；§7 专业成果评价 |
| T04 | TAC 员工手册 | §4.1 | §8.3–8.4 完整性和来源一致性 |
| T05 | AA-Briefcase-Lite w1_t2 | §4.2、§4.4 | §6.4 场景跨度与执行协议对照 |
| T06 | WorkArena++ OnBoardUserTask | §5.2–5.4 | §8.2 委托条件；§8.4 关系验收 |
| T07 | TAC 确认反馈并更新问题 | §5.2–5.3 | §8.3–8.4 条件依赖 |
| T08 | VibeLife office_fitout_15d | §6.1–6.2 | §7.2、§7.4 时间与状态检查 |
| T09 | VibeLife galapagos_no_us_transit | §6.1–6.2 | §7.2 不同要求的检查实现 |
| T10 | Vending-Bench 2 年度经营 | §6.3、§6.5 | §7.5 业务指标；§9.5 工作价值 |

详细原题、任务 ID、评分代码和来源链接收录于配套 [10 项任务试标卡](/Users/echominkki/.codex/.chatgpt-projects/g-p-6aafe26acd04819186aab66d5019db57/output/Working-Agent-Survey-10-Task-Cards.md)。十项锚点校准论证语言，完整文献语料支撑全景分布与综合分析。

## 7. 图表清单

| 编号 | 图表内容 | 位置 | 需要的材料 |
|---|---|---|---|
| Figure 1 | 全文结构：责任扩展、评价设计、综合分析与研究议程 | §1 | 中心论点与章节关系 |
| Figure 2 | L0–L5 × 委托条件/能力/验收对象 | §2 | 层级定义和真实锚点 |
| Figure 3 | 成果内部约束与下游使用 | §4 | Dashboard、市场模型和报告实例 |
| Figure 4 | 工作流依赖及同目标下的委托条件 | §5 | 入职流程与跨系统任务 |
| Figure 5 | 场景时间、状态继承、事件和验收时间线 | §6 | AA-Briefcase、VibeLife、Vending 协议 |
| Figure 6 | 层级、领域、产物与能力组合的覆盖分布 | §8.1 | 完整标注主表 |
| Figure 7 | 具体要求、验收声明与实际检查的对应 | §8.3 | 要求—检查标注 |
| Figure 8 | 违规检出与合法变体误拒 | §8.4 | 实际完成的成对审计 |
| Table 1 | Benchmark 总表 | §2 | 名称、版本、领域、任务、环境、数据与评价 |
| Table 2 | 框架定义与标注实例 | §2 | 层级、条件、要求、覆盖规则 |
| Table 3 | 信息任务与局部操作对照 | §3 | 输入、目标范围、能力、验收性质 |
| Table 4 | 完整交付对照 | §4 | 产物、专业要求、材料与可用性 |
| Table 5 | 关联工作流对照 | §5 | 依赖、实体、交接、协作与完成条件 |
| Table 6 | 持续工作协议对照 | §6 | 状态、事件、时间、职责及结果 |
| Table 7 | 性质—证据—动作—执行者—汇总 | §7 | 评分设计与实现 |
| Table 8 | 协议、评分可靠性和复现条件 | §7 | 配置、校准、成本与资源 |
| Table 9 | 已报告表现、失败及方法回应 | §8 | 文献结果与配置 |
| Table 10 | 发现—设计变量—验收条件—研究问题 | §9 | 综合章结果与设计方案 |

Figure 1 负责讲清论文的展开方式；Figure 2 负责框架；Figure 6–8 承载数据分析结果。完整条目和细粒度结果放入附录，正文图表保留最能回答研究问题的比较。

## 8. 资料组织与写作分工

### 8.1 配套资料结构

- **Benchmark inventory：**论文与版本、官方仓库、数据地址、职业/领域、环境、公开程度。
- **Task records：**任务 ID、模板与实例关系、目标、输入、层级、委托条件、能力及运行协议。
- **Requirement records：**任务要求、成功条件、rubric 映射、证据、检查、覆盖状态与来源定位。
- **Result records：**模型、运行配置、原始指标、失败标签及出处。
- **Audit records：**基准、违规与合法变体、独立检查、评分结果、运行状态与日志。

各章节共用这五组资料，通过 ID 关联。Awesome 列表和论文主表从同一文献记录维护；Overleaf 负责正文和排版。

### 8.2 分工单元与明确交付

| 工作包 | 负责范围 | 交付内容 |
|---|---|---|
| A · 基础与专业交付 | §3–4 | 相关任务归位、同层比较表、能力与质量分析、已报告结果 |
| B · 企业流程 | §5 | 依赖类型、环境/协作者、委托条件、完成条件与失败模式 |
| C · 持续工作 | §6 | 事件协议、状态继承、项目/职责分界、持续评价与资源条件 |
| D · 评价与审计 | §7、§8.3–8.4 | 评分设计总表、要求标注、成对提交与实际结果 |
| E · 统稿与综合 | §1–2、§8.1–8.2/8.5–8.6、§9–10 | 统一定义、跨层分析、方法回应、图表及叙事一致性 |

每个主体工作包提交本章正文、文献比较表、任务记录与具体来源，并与评价负责人复核本章引用的评分描述。统稿以共同字段合并材料，再据分析结果回写引言、贡献和研究议程。

## 9. 参考综述的写法如何落实在本稿

| 写法来源 | 本稿采用的组织方式 | 具体落点 |
|---|---|---|
| [Co-Evolution](https://arxiv.org/pdf/2608.10299v1) | 层级变化对应新进入的问题与条件 | §3–6 从成果到依赖、时间与职责 |
| [Memory](https://arxiv.org/html/2512.13564v2) | 不同维度分别回答不同问题 | L 层级、C 能力、委托条件与评价记录 |
| [Reliable Self-Evolving Agents](https://www.preprints.org/manuscript/202609.0913) | 分层主体之后设置跨层综合 | §3–6 与 §8 的分工 |
| [Code as Agent Harness](https://arxiv.org/html/2605.18747v1)、[Externalization](https://arxiv.org/html/2604.08224v1) | 从类别进一步分析系统关系 | 工作依赖、状态传播与方法回应 |
| [Long-Horizon Agents](https://www.preprints.org/manuscript/202607.1328)、[Lifelong Learning Roadmap](https://arxiv.org/pdf/2501.07278v2) | 研究问题贯穿章节，运行条件连接未来设计 | §6、§7.4 与 §9 |
| [AI Office](https://github.com/Qwen-Applications/AI-Office-Survey/blob/main/main.pdf) | 围绕可用工作产物组织质量分析 | §4、§7.1 与专业成果比较 |
| [Designing Benchmarks for Knowledge Work](https://arxiv.org/html/2605.23262v2) | 连接工作活动、测试条件、工作产品与评价结果 | 在共同表示基础上扩展跨层语料与检查审计 |

本稿的写作重心是：**用工作承担层级形成全景，用任务条件解释差异，用具体要求与验收检查形成发现。**
