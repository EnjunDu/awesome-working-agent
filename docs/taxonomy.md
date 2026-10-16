# Working Agents 分类与术语 v0.1

这是一版供团队共同修订的分类。先区分“论文是什么类型、研究哪类工作、需要哪些能力、怎样优化系统”，再映射到 survey 章节。每篇论文仅分配一个主分类；能力、优化机制和章节可以多选。细分类描述具体研究问题，优先复用已有术语。

分类边界与章节映射是维护者判断，不代表原论文作者采用同一套概念。`data/taxonomy.json` 保存受控词表；Excel 的 `Taxonomy` 页提供同一版术语说明。

## 主分类：用于浏览与写作分工

| 代码 | 中文术语 | 纳入边界 | 典型工作 |
| --- | --- | --- | --- |
| `artifact` | 工作产物生成与编辑 | 生成或编辑表格、文档、幻灯片等可交付产物；纯阅读理解归 related | SheetCopilot, SpreadsheetBench, PPTAgent, DeepPresenter |
| `workspace` | 工作空间与跨文件工作 | 发现材料、处理文件关系与跨应用依赖、完成职业工作包 | Workspace-Bench, OfficeBench, GDPval, APEX-Agents |
| `computer-use` | 计算机与应用操作 | GUI grounding、网页导航、桌面与移动端操作 | OSWorld, WebArena, SeeClick, AndroidWorld |
| `tool-enterprise` | 工具调用与企业流程 | 工具选择调用、状态化业务流程、用户与工具交互 | Toolformer, ReAct, AppWorld, ToolSandbox, τ-bench, CRMArena |
| `persistent` | 持续责任与长期工作 | 长期记忆、异步事件、主动性、个性化和长期工作评测 | MemGPT, LongMemEval, Proactive Agent, TimeArena |
| `harness` | 运行框架、训练与优化 | 跨领域运行基础设施、模型训练、运行框架与联合优化 | OpenHands, AutoGen, AFlow, GEPA, HiPER, SkillRL |
| `verification` | 验证、评判与恢复 | 自纠错、评判器、状态有效性、恢复与事务保证 | Self-Refine, CRITIC, Reflexion, Agent-as-a-Judge, SagaLLM |
| `safety` | 安全、注入与授权 | 提示注入、有害工具使用、委托授权和副作用约束 | AgentDojo, InjecAgent, ToolEmu, AgentHarm |
| `related` | 相关基础与工作影响 | 文档/答案型问答、规划基础、协调与数据库理论、劳动与生产率研究 | DocVQA, FinQA, TAT-QA, PlanBench, Future of Work with AI Agents |
| `swe-science` | 软件、数据科学与科研工作 | 软件工程、可执行数据分析、ML 实验与科研复现 | SWE-bench, SWE-agent, DSBench, ScienceAgentBench, PaperBench |

分类优先顺序：先判断最有区分度的工作对象或研究问题，再记录实现接口与优化机制。SWE-agent 归软件工作，同时标记接口优化；Spreadsheet-RL 归工作产物，同时标记强化学习。不能因为使用 GUI 就把所有办公 benchmark 都归 computer-use，也不能把所有训练论文都放进 harness。

原 README 的接口、工作属性和领域标签并未全部等同于新词表。此次把它们拆成明确的独立维度，并保留具体细分类与核验备注。例如文档 QA 的答案评测不会改写成产物生成评测。

## 条目类型：论文的贡献形式

| 值 | 含义 |
| --- | --- |
| `Method` | 智能体方法、算法、训练或优化方法 |
| `Benchmark` | 任务集、数据集、评估协议或评测环境 |
| `Framework` | 有对应论文的运行框架、平台或可复用研究基础设施 |
| `Survey` | 综述或研究路线图 |
| `Background` | 基础理论或实证背景研究 |
| `Product/Resource` | 无已确认论文的产品、文档、独立项目或资源，单列 Resources，不计论文数 |

方法和 benchmark 可以共存，写为 `Method;Benchmark`。`Product/Resource` 不能与学术条目类型混用。一个 dataset 的镜像、论文的预印本和会议版、项目改名，都不能重复计数。

## 能力标签：对齐第 4 章

| 标签 | 中文术语 | 章节 |
| --- | --- | --- |
| `perception` | 感知与理解 | 4.1 |
| `reasoning` | 推理与决策 | 4.2 |
| `planning` | 规划 | 4.3 |
| `coordination` | 协作与协调 | 4.3 |
| `execution` | 执行 | 4.4 |
| `state-management` | 状态管理 | 4.4 |
| `memory` | 记忆 | 4.4、5.3.3、7.2 |
| `verification` | 验证 | 4.5、6.2 |
| `recovery` | 恢复与重规划 | 4.5 |
| `learning` | 学习与优化，辅助研究标签 | 5 |

`learning` 是研究侧重标签，不额外声称它是第 4 章的核心能力。Benchmark 上的标签表示任务考察需求；Method 上的标签表示方法侧重。两者都不直接证明某个模型掌握了该能力。

## 优化机制：对齐第 5 章

| 代码 | 统一术语 | 章节 | 典型工作 |
| --- | --- | --- | --- |
| `environment-synthesis` | 任务与环境合成 | 5.1.1 | NexForge, GraphForge, WorkGenesis, EnvScaler |
| `trajectory-curation` | 轨迹收集与筛选 | 5.1.2 | SEE, OpenThoughts-Agent, CurateEvo |
| `reward-verification` | 奖励与验证信号 | 5.1.3 | Spreadsheet-RL, AeSlides, Learning to Present |
| `mid-training-sft` | 中期训练与监督微调 | 5.2.1 | daVinci-Dev, TrajLong, Function-Aware FIM |
| `agentic-rl` | 智能体强化学习 | 5.2.2 | HiPER, Adaptive Milestone Reward, ReTool |
| `on-policy-distillation` | 同策略蒸馏 | 5.2.3 | TCOD, SOD, Skill-SD |
| `self-improving-training` | 自改进模型训练 | 5.2.4 | Socratic-SWE, Self-Retrospection Distillation |
| `tool-interface` | 接口与工具优化 | 5.3.1 | SWE-agent, JTPRO, Beyond Prompts |
| `prompt-workflow` | 提示与工作流优化 | 5.3.2 | AFlow, GEPA, Meta-Harness |
| `memory-skill` | 记忆与技能优化 | 5.3.3 | Agent Workflow Memory, ReasoningBank, SkillOpt |
| `model-harness-coupling` | 模型与运行框架耦合优化 | 5.4 | UI-Copilot, SkillRL, Optimas |

这些机制允许交叉。章节引用与机制标签分别维护：在某小节被引用，不自动等于提出该机制。CogEvol 题名中的 learning environment 指教学内容及交互页面，不能据此标为训练智能体的环境合成。Reflexion 的 verbal reinforcement learning 也不等于梯度强化学习。

## 工作条件与工作形式

草稿第 2.2 节给出两条独立工作条件轴：

- **Work persistence / 工作持续性**：委托责任何时关闭，是否在等待、事件或会话后继续保留。
- **Work-world openness / 工作世界开放性**：相关材料、对象关系、接口、动态、权限与其他参与者能否在执行前枚举。

第 3 章另外区分 response-level、atomic-action-level、multi-step-level、workflow-level、workspace-level 五类工作形式。不要直接把工作形式当作自主性、智能或难度等级。长时间运行、多文件、跨应用也不能直接证明持续责任。

当前 Excel 不替每篇论文强行打这两条轴的分数。要做进一步比较，应先记录任务要求和验收证据，再讨论其工作形式与条件。

## 证据与协作状态

- `verified`：题名、链接和记录的单位有一手或作者管理的来源依据。
- `metadata-only`：题名和链接已核验，单位仍不完整或未披露。
- `pending`：论文身份或链接还需确认，不进入 README 论文表和已链接论文计数。

这些状态不表示“已读”、同行评审或全面系统综述。阅读状态独立维护；初始为“未分配”。单位按记录所指版本的论文首页或官方项目核验，主要单位节选与不同版本的差异在核验备注注明。年份优先采用可确认的最早公开预印本年。

修改分类时，建议在 PR 中给出边界定义、至少两个代表例子、一个容易混淆的反例，以及需要移动的论文 ID。同步修改词表、Excel 和本文，避免写作中出现多个同义名称。
