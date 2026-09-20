# Work-Agent Benchmark Survey

## 1. 这篇文章讲什么

过去两年，数字工作的评测对象一路扩张：从抽一个数字、改一张幻灯片，到搭一个财务模型、在含噪工作区里找齐材料出一份汇报，再到连续几周维护一个项目。任务越做越像真实工作。

但评分方式没有跟着一起走。GDPval 给 220 道真实职业交付物写了 10,453 条 rubric，最后用两两对比的 win-rate 定胜负；AA-Briefcase 设计了跨周依赖，第三周的任务要用第一周的产物，评分却是 all-pass 加 Elo。任务要求 agent 记住上周的口径，评分器只看这周交了什么。于是「它做到了吗」这个问题，在很多 benchmark 上没有答案——不是 agent 没做到，是没人在测。

所以这篇 survey 问的不是「benchmark 覆盖了哪些能力」，而是：**它们判定得了自己声称在测的东西吗。**

全文的量是一个差集。一项任务要求 Agent 具备某些能力，每项能力都有一个「不看到这一层证据就判不了」的门槛；评分器实际执行的检查够不到门槛的那些能力，就是这个 benchmark 欠下的账：

$$\text{Unverified}(b)=\{\,c \in \text{Req}(b)\;:\;E(b) < \text{MinEv}(c)\,\},
\qquad
\text{Debt}(b)=\frac{|\text{Unverified}(b)|}{|\text{Req}(b)|}$$

`Req(b)` 是任务要求的能力集合，`E(b)` 是评分器实际达到的证据层级，`MinEv(c)` 是判定能力 `c` 所需的最低证据层级。三者分别由 §4、§5、§2.4 给出。

欠账按能力算，不是把两个层级编号相减。一道只需判最终数值对错的多步计算题，要求的是分析推理，而分析推理在文本层就能判，它不欠账；一道只改一个幻灯片元素的小任务，要求的是交付物构建，必须打开产物才能判，这时候打开产物也不算证据过剩。

这个量可以标注、可以统计、可以排名，也可以被推翻。

全文回答六个问题，每个问题对应一章：

> **❶ Scope** — 什么算 work-agent benchmark？它和 long-horizon agent、评测指标这些概念是什么关系？（§2）
>
> **❷ Depth** — benchmark 要求 Agent 把一项工作推进到什么程度？（§3）
>
> **❸ Capability** — 这些任务要求 Agent 具备哪些能力？（§4）
>
> **❹ Evidence** — 评分器实际看得到什么？（§5）
>
> **❺ Debt** — 要求和证据之间差多少？（§6）
>
> **❻ Agenda** — 接下来优先做什么？（§7、§8）

问题 ❷❸❹ 不是三个并排的视角，而是一条因果链：**任务要求走多深，决定了它必然引出哪些能力；引出了哪些能力，决定了需要什么证据才能判定它们。** 因此 ❺ 是一次减法，不是又一个视角。这是这篇 survey 和按多个维度分别铺开的 survey 之间最主要的结构差别。

---

## 2. 三把尺子

### 2.1 纵轴 W1–W4：Demanded Work Depth

纵轴衡量的是：**一个 benchmark 要求 Agent 把一项工作推进到什么程度。**

有些任务只要求完成一个明确的小操作；有些任务要求把多个步骤串起来；再复杂一些，Agent 需要自己在工作环境中找信息、调用工具并根据反馈继续行动；最高一层则要求 Agent 跨越多轮甚至多个时间阶段，持续维护同一项工作。

因此，我们把任务分成四层：

$$
\boxed{
W1~\text{Bounded}
\rightarrow
W2~\text{Chained}
\rightarrow
W3~\text{Situated}
\rightarrow
W4~\text{Standing}
}
$$

---

#### W1 Bounded — 完成一个明确、封闭的工作单元

任务所需的信息、操作对象和目标都已经给定。Agent 只需要在这个范围内完成一次分析、生成、判断或编辑，不需要主动寻找额外材料，也不需要记住之前发生过什么。

例如：

- 从一份 PDF 中找出某个数字；
- 判断一条法律条款属于哪一类；
- 总结一份给定文档；
- 修改 PPT 中指定位置的文字。

这类任务可以是真实工作，但它们本质上仍是一个**封闭的小任务**。

代表 Benchmark：LegalBench、OfficeQA、MMLongBench-Doc。

---

#### W2 Chained — 把多个步骤串成一个完整结果

任务不能靠一个局部操作完成，而是需要连续完成多个相互依赖的步骤。

例如：

> 找到数据 → 做计算 → 比较结果 → 写出分析结论。

或者：

> 阅读多份材料 → 提取关键信息 → 做专业判断 → 生成完整报告。

这里的关键变化是：**前一步做错，会影响后面的结果。**

因此，Agent 不仅要会完成单个步骤，还要能够：

- 拆解任务；
- 安排执行顺序；
- 保存中间结果；
- 保证不同步骤之间前后一致。

这一层开始出现明显的 **error propagation**。

代表 Benchmark：SpreadsheetBench 2、Finance Agent v2、BankerToolBench。

---

#### W3 Situated — 在真实工作环境中边做边决定

这一层中，任务不再把所有信息和执行路径提前告诉 Agent。

Agent 需要自己进入一个工作空间，判断：

- 应该看哪些文件；
- 哪个版本才是最新的；
- 接下来应该调用什么工具；
- 当前操作是否成功；
- 环境发生变化后下一步应该怎么做。

执行过程变成一个持续循环：

$$
\text{Observe}
\rightarrow
\text{Decide}
\rightarrow
\text{Act}
\rightarrow
\text{Observe}
$$

例如：

> 在一个包含大量文件的目录中找到正确材料，识别草稿和最终版，修改 Excel，再根据结果更新 Word 或 PPT。

这一层真正开始考察 Agent 是否能够**在环境中工作**，而不只是对给定输入进行处理。

新增的要求包括：

- Workspace exploration；
- Tool / GUI / API interaction；
- Environment feedback；
- State tracking；
- Error recovery。

代表 Benchmark：Workspace-Bench、OSWorld、OfficeBench、tau²-bench、EnterpriseOps-Gym。

---

#### W4 Standing — 跨时间持续维护同一项工作

最高一层不再是"完成一次任务"，而是**持续负责一项工作**。

过去的结果会影响现在，新信息到来以后，Agent 需要知道哪些已有内容需要更新；任务中断之后，还要能够从之前的状态继续。

例如：

> 第一周完成市场分析，第二周收到新数据后更新模型，第三周根据管理层反馈修改报告和 PPT，同时保持前几周已经确定的数据口径和结论逻辑一致。

这类任务要求 Agent 维护：

- 长期任务状态；
- 文件和结果版本；
- 过去已经确认的约束；
- 不同阶段之间的依赖；
- 新信息对旧结果的影响。

因此，W4 关注的是：

> **Agent 能不能持续维护一项工作，而不是每次都从头开始。**

代表 Benchmark：AA-Briefcase、VibeLifeBench。

---

### 2.2 横轴 C1–C7：Capability Coverage

横轴是多标签的能力清单，按在工作中承担的功能分成三组。它服务于标注和交叉分析，正文按组展开。

**理解与决策**

- **C1 Task and Workspace Understanding**——哪些信息与任务有关。指令与约束解析、文件发现、文档与表格解析、多模态理解、来源定位、版本识别、跨文件关系识别。
- **C2 Analysis and Professional Reasoning**——这些信息意味着什么。数值计算、数据分析、多来源综合、比较与因果推断、领域规则应用。
- **C3 Planning and Coordination**——接下来该做什么、怎么组织。任务分解、顺序与依赖安排、工具与资源调度、需求澄清、角色分工、审批与交接。

**执行与交付**

- **C4 Tool and Environment Interaction**——决策能否正确落到环境上。工具选择与参数构造，代码、命令行、API、浏览器、GUI 和企业系统的操作，读取反馈并改变状态。
- **C5 Deliverable Construction and Editing**——产出能否真正拿来用。内容组织与生成，结构、公式、布局与呈现，编辑与格式转换，保留既有内容，多产物之间保持一致。

**持续性与可靠性**

- **C6 Memory and State Management**——已有工作能否继续支撑后续执行。进度与中间结果维护、历史信息保存与恢复、版本与依赖跟踪、约束延续、经验复用。
- **C7 Verification and Adaptive Revision**——能否发现问题并正确修订。结果核验、错误定位与修复、反馈适应、重规划、更新向下游传播。

### 2.3 证据轴 E1–E4：Evidenced Depth

**这是这篇 survey 的核心贡献。** 前两把尺子量的是任务，这把尺子量的是评分器；欠账就出在两者之间。

E 轴问的是：**评分器实际看到了什么。** 不是评分方法叫什么名字，不是它判得严不严，而是它拿到手的信息本身能支持什么结论。

#### E1 Answer-level

评分器拿到的是一段文本、一个值或一个标签，判定方式是与 gold 比对、标签准确率或引用有效性检查。不需要打开任何产物，不需要访问环境。

即使 agent 交的是 .docx，只要评分器只抽出其中文字做比对，仍然是 E1。

代表：OfficeQA、LegalBench、Finance Agent v2、MMLongBench-Doc、Tax Agent。

#### E2 Artifact-level

评分器打开产物本体，解析它的内部结构。读取单元格与公式、执行公式重算、检查 OOXML 结构、渲染后查版式、按 rubric 逐条核对产物内容，都在这一层。

**判定准则：只要判定动作需要拿到产物本体并解析其结构，就算 E2。** 检查文件名和 basename 也算，因为它需要产物存在。

E2 的上界是：它只看 agent 交出来的东西，不看 agent 没交的东西。

代表：SpreadsheetBench 2、PPTC、PresentBench、BankerToolBench、OmegaUse、JOBBench、BigLaw Bench。

#### E3 State-level

评分器看整个工作空间或系统的最终状态：环境状态断言、数据库 diff、execution-based evaluator，以及检查不该动的对象有没有被动。

**E2 与 E3 的分界线：E2 问「交出来的东西对不对」，E3 问「整个工作空间还对不对」。** 能判定「未被要求修改的部分保持原样」的，是 E3。

代表：OSWorld、WorkArena、AutomationBench、EnterpriseOps-Gym、tau²-bench、E-Bench、OfficeBench、OmniaBench、TheAgentCompany。

#### E4 Process & Continuity-level

评分器拿到跨时间点的证据：执行 log、中间状态快照、前序阶段的产物、时间推进之后的环境。判定的是早期约束在后期是否仍然成立、中断之后能否接上、注入的变化有没有被传播、该发现的问题有没有被发现。

**E3 与 E4 的分界线：E3 看终态的一张快照，E4 至少需要两个时间点或一条执行记录。** 任务分了多轮不构成 E4，必须是判定动作本身跨越时间点。

代表：VibeLifeBench。

### 2.4 三轴相乘

每项能力都有它的最低可判定证据层级。低于这个层级，能力标签就是空的。

| 能力                | 最低可判定证据                  | 原因                                               |
| ------------------- | ------------------------------- | -------------------------------------------------- |
| C1 理解与 grounding | E2；涉及 file discovery 时为 E3 | 用没用对源，要看产物内容；找没找对文件，要看工作区 |
| C2 分析与专业推理   | E1                              | 结论对错在文本层可判                               |
| C3 规划与协调       | E3                              | 规划只能从实际动了什么反推                         |
| C4 工具与环境交互   | E3                              | 操作正确与否体现在环境状态上                       |
| C5 交付物构建与编辑 | E2                              | 需要解析产物结构                                   |
| C6 记忆与状态管理   | E4                              | 「有没有保持」只能跨时间点判                       |
| C7 验证与适应性修订 | E4，或注入已知故障后的 E3       | 要判「该发现而没发现」，先得有一个已知故障         |

这张表是全文的枢纽。W 不直接参与计算——它决定任务会引出哪些能力（W3 必然引出 C1 和 C4，W4 必然引出 C6），欠账则沿着能力算：

$$\text{Debt}(b)=\frac{\bigl|\{\,c \in \text{Req}(b): E(b) < \text{MinEv}(c)\,\}\bigr|}{|\text{Req}(b)|}$$

得到的是一个 0 到 1 的比例，可以按 benchmark 排名，也可以按能力或按 W 层聚合，看欠账集中在哪里。

**标注时 `E(b)` 按评分器实际执行的检查动作定级，不按它能访问什么定级。** 手里握着完整执行 log、最后却只抽一句答案做比对的评分器，是 E1 不是 E4。

---

## 3. 文章包含哪些 Section

三把尺子决定骨架。W、C、E 各用一章系统交代现状，第六章做交叉分析，第七章把发现变成研究问题：

$$
\boxed{
\underbrace{\text{要求多深}}_{\S3~W}
\;\rightarrow\;
\underbrace{\text{要求哪些能力}}_{\S4~C}
\;\rightarrow\;
\underbrace{\text{判定得了什么}}_{\S5~E}
\;\rightarrow\;
\underbrace{\text{差多少}}_{\S6}
\;\rightarrow\;
\underbrace{\text{怎么补}}_{\S7}
}
$$

箭头是因果，不是并列。W 决定任务会引出哪些能力，能力决定判定它需要什么证据，证据够不够就是欠账。

**每个分类章的最后一节固定是「本章结论的边界」**，说明这一章的内容支持什么结论、支持不了什么结论，而支持不了的那部分正是下一章要处理的。这个写法借自 `Diving into Reliable Self-Evolving Agents`——它的每个 L 章都以 `Reliability and the Fixed-X Limit` 收尾，再由 §8 汇总成跨层综合。这样 verification debt 全程在场，但不占据正文分类内容的位置：

> §3 末 · 深度说明任务有多大，不说明它在考什么 → §4
> §4 末 · 能力标签只记录任务要求，不代表评测判定过 → §5
> §5 末 · 每一级证据各自支持什么结论，够不到的地方留给 → §6

主体三章的职责是把这个领域已经形成的任务设置、能力要求和评测设计系统整理出来，§6 才做交叉分析。分类内容是主体，欠账是贯穿视角。

全文用同一个场景贯穿——经营分析。从表里取一个数（W1），到出一份完整分析报告（W2），到在含噪工作区里找齐材料并更新汇报（W3），到连续几个周期维护同一套口径（W4）。引言、框架图、评测章和研究议程都用它，读者不用在章节之间重新建立语境。

---

### Section 1 · Introduction

**本章回答：为什么要问「判定得了什么」。**

四段推进。第一段讲评测对象的扩张，从单点操作走到持续项目。第二段落到具体错配：GDPval 写了一万条 rubric 却用 win-rate 定胜负，AA-Briefcase 设计了跨周依赖却只看这周交了什么。第三段提出 verification debt，说明它是一个可以标注、可以统计的量。第四段给贡献。

引言提出的是一个待回答的问题，不是一个已经成立的结论：**现有 work-agent benchmark 要求哪些工作能力，它们的评测证据又能支持哪些能力结论。** 答案由标注决定，标题也由标注决定。

三项贡献：

1. **一个把任务设置、能力要求和判定证据接在一起的框架**，以及由它导出的一个可计算指标——某个 benchmark 要求的能力里，有多大比例得不到足够证据支持。
2. **一次覆盖全部数字工作形态的实测标注。** 任务级的 W 与 C，评分器级的 E，以及两万余条 rubric criteria 的逐条证据分级。
3. **由测量结果推出的研究议程。** 不是「需要更好的记忆」，而是「哪一层证据缺失、缺失导致什么结论不成立、补上它需要什么」。

**交棒：** 引言最后给出那六个问题和它们各自的章节，读者带着一张地图进入正文。

---

### Section 2 · Formulation and Scope
**什么算 work-agent benchmark？它和相邻概念是什么关系？**

**2.1 数字工作与 work-agent benchmark。** 给出操作性定义：评测 agent 能否在文件、工具、软件或数字环境上完成目标导向的工作，产出可用的交付物或可验证的状态变化。同时定义 work goal、workspace、artifact、environment state、acceptance criteria 这几个全文通用的对象。

**2.2 三把尺子。** W、C、E 的精炼定义，以及 Table 3 那张「能力 → 最低可判定证据」对应表——它是把三把尺子接起来的枢纽，后面 §6 的计算全靠它。详细展开留给后三章。

**2.3 概念边界。** 在讲任何内容之前，先把两个新概念和它们最容易被误读成的东西分开。

- **Demanded Depth 不是 long-horizon。** long-horizon 量的是执行跨了多少个 context window，我们量的是依赖跨了哪一类边界。一个几十分钟的 GUI 任务可能是 W3，一道两小时的纯写作题只是 W1。
- **我们说的 verification 是 benchmark 的评分器，不是 agent 自带的 verifier。** `Towards Long-Horizon Agents` 的 §4.6 已经把 verification level 用在 harness 内部的 process-versus-outcome 验证上。那是 agent 的一项能力，在我们这里是 C7；E1–E4 讲的是外部评分器拿什么判 agent，两者是被测者和判分人的关系。
- **Evidenced Depth 不是评分方法的分类。** E1–E4 不是 exact match、rubric、LLM judge、agentic judge 换个名字。决定层级的是评分器实际执行了什么检查：同一个 agentic judge 可以停在 E2，也可以像 VibeLifeBench 那样读执行 log 做到 E4。
- **Verification debt 不是 benchmark saturation。** 饱和是分数刷满了，欠账是分数根本没在测那件事。一个通过率 20% 的 benchmark 照样可以欠一身账。

**产出：** Figure 1（全文结构图）、Figure 2（三轴 taxonomy）、Table 1（benchmark landscape）、Table 2（标注准则）、Table 3（能力 → 最低可判定证据）。

**交棒：** 尺子和口径都定好了，接下来三章分别用它们量一遍。

---

### Section 3 · Work Settings — How Far Do Benchmarks Ask the Agent to Go?
**现有 benchmark 把哪些工作变成了怎样的任务？**

3.1 到 3.4 对应 W1 到 W4，每节用同一套比较顺序：

> 任务目标与输入 → 工作区与依赖设置 → 任务是怎么造出来的 → 同层 benchmark 之间的设计差异 → 这一层还没覆盖到的工作形态

读者看完不只是知道「某个 benchmark 属于 W3」，还知道它**怎样构成一个 W3 任务**，以及同层的几个 benchmark 差在哪里。

**3.5 任务来源与构造方式。** 横向看题是怎么来的：职业专家撰写（GDPval、JOBBench）、真实工作包整理（BankerToolBench、AA-Briefcase）、从 commit 与 PR 反构（WorkBuddy）、程序化与模型辅助合成、知识引导合成。构造方式和深度层级相关——合成任务集中在 W1 和 W2，真实工作包和模拟环境才撑得起 W3 和 W4。

**3.6 分布综合。** W 级 × domain、W 级 × workspace 类型、W 级 × 产物形态，以及按年份看深度是怎么涨上去的。

这一章会给出一个反直觉的结果：**被当作真实职业工作代表的 benchmark，深度往往低于它的叙述。** GDPval 的 220 道题里有 95 道没有任何参考文件，按 W 轴只能算 W1 或 W2——它测的是专业知识和写作，不是工作执行。

**产出：** Figure 3（深度分布）、Table 4（任务来源 × W 级对照）、Table 5（同一场景在 W1–W4 的四个任务实例）。

**3.7 本章结论的边界。** 深度说明任务有多大、依赖有多长，不说明它在考什么。同为 W3，一个可能重在工作区探索，另一个重在跨应用操作。能力要单独看一遍。

---

### Section 4 · Capability Requirements — What Do They Ask the Agent to Do?
**这些任务要求哪些能力，能力要求怎样随深度变化？**

4.1 到 4.3 按三组展开：理解与决策（C1–C3）、执行与交付（C4–C5）、持续性与可靠性（C6–C7）。每组回答四件事：能力的定义、什么样的任务条件会引出它、现有 benchmark 用什么设置去制造这些条件、它和其他能力怎么组合。

任务设置是重点。用版本冲突引出来源识别，用含噪目录引出工作区探索，用注入的文件错误引出修复，用跨阶段依赖引出状态延续——这些设置本身就是这个领域积累下来的设计经验，值得单独整理。

**4.4 能力如何随 W 变化。** 同一项能力在不同深度上要求完全不同：C6 在 W1 只是保持当前信息，在 W2 是保存相互依赖的中间结果，在 W3 变成跟踪已执行动作与待办，到 W4 才是跨阶段恢复进度、更新历史约束。这是把两条轴放在一起看才能得到的东西。

**4.5 能力组合。** 共现分析、能力组合随 W 变化、哪些组合还没有 benchmark 覆盖。

**产出：** Figure 4（Benchmark × Capability 覆盖热力图）、能力随 W 变化的对照表。

**4.6 本章结论的边界。** 这一章标注的是 **required capability**——任务要求 Agent 具备什么。它不等于 **verified capability**。一个 benchmark 可以大量引出 C6，却从不检查 C6。两者的匹配情况留到 §6，因为那需要先知道评测是怎么设计的。

---

### Section 5 · Evaluation Design — Targets, Evidence, and Scoring
**「工作完成了」是怎么被判定的？**

这一章系统整理评测设计。一次判定拆成五个层面，它们经常被混在一起讲，分开之后 benchmark 之间的差异才看得清楚：

> **评价对象**（判的是什么东西）→ **验收性质**（要它满足什么）→ **证据**（凭什么判）→ **检查动作**（怎么验）→ **评分方式**（怎么变成分数）

以 SpreadsheetBench 2 的一道建模题为例：评价对象是产出的 workbook，验收性质是计算路径用活公式而非硬编码，证据是原生 xlsx 文件，检查动作是解析公式并重算，评分方式是单元格级加权通过率。这五样换任何一个，结论的效力都不同。

**5.1 评价对象。** answer、artifact、environment state、process 四类，以及它们在现有 benchmark 里的分布。

**5.2 验收性质。** 正确性、完整性、结构有效性、可用与可编辑、来源可追溯、跨文件一致、专业合规。`The Evolution of AI Office` 归纳过六个交付物质量维度，我们沿用它的成果，但把「要它满足什么」和「凭什么能判」分开——这两件事它是并在一起讲的，而分开之后才能问出「某个质量维度有没有对应的证据」。

**5.3 证据层级 E1–E4。** 本章核心。四级定义、判定准则和边界案例，特别是 E2/E3 与 E3/E4 两条界线。

**5.4 检查动作与评分机制。** 规则断言、执行式检查、rubric 逐条核对、LLM judge、agentic judge、人工专家，以及它们各自能触到哪一级证据。这里要打掉一个常见误解：**评分方法的名字不决定它的证据层级。** rule-based 可以停在 E1 也可以做到 E3，取决于它断言的是答案还是环境状态；agentic judge 可以是 E2，也可以像 VibeLifeBench 那样读执行 log 做到 E4。决定层级的是它实际执行了什么检查，不是它叫什么。

**5.5 rubric criteria 的证据层级分布。** 本章的实证部分。本地已下载两万余条真实 criteria：GDPval 10,453 条、PresentBench 约 1.3 万条 checklist、Workspace-Bench 1,143 条能力标注、BigLaw 151 条、OmegaUse 100 个 rubric json、JOBBench 128 题加权 rubric、AA-Briefcase 63 条 checks。逐条判定「这条 criterion 需要看到哪一级证据才能验」，给出按 benchmark 分组的分布。这是目前没有人做过的一次测量，结果决定后两章怎么写。

**5.6 可靠性、成本与可复现性。** 评分器的多次运行稳定性、环境复现难度、评分开销。这一节解释了证据层级的成因：E3 和 E4 贵，所以多数 benchmark 停在 E2——欠账往往是成本约束的结果，不是疏忽。

**产出：** Figure 5（criteria 证据层级分布）、Table 6（验收性质 × 证据 × 检查动作对照）。

**5.7 本章结论的边界。** 到这里我们分别知道了任务要求什么、评测能判什么。两者匹配得怎么样，需要把 §4 的 required 和本章的 evidence 放在一起才能回答。

---

### Section 6 · Cross-Benchmark Synthesis — Coverage, Results, and Verification Gaps
**把三章放在一起看，这个领域呈现什么形状？**

综合分析章，对应 `Diving into Reliable Self-Evolving Agents` 的 §8 位置。三层递进，前两层是铺垫，第三层是本文的原创发现。

**6.1 覆盖。** 哪些工作设置、能力组合、评价对象已经被充分覆盖，哪些还是空白。领域和产物形态的分布也在这里给出——全景统计显示金融和通用商业占了过半题量，而人力资源、政务这些域几乎没有专门的 benchmark。

**6.2 已报告的结果与失败。** 文献自己报告的失败按 C1–C7 归纳：找错材料、算错、规划错、工具操作错、交付物结构错、状态丢失、该发现的错没发现。这里只整理 benchmark 的产出，不展开改进方法——那属于 harness 和训练的范围，`Towards Long-Horizon Agents` 已经用两章篇幅覆盖。

**6.3 要求与证据的错配。** 本章重点。把 §4 的 required capability 和 §5 的 evidence level 对起来，算出每个 benchmark 有多大比例的能力要求得不到足够证据支持，并看欠账集中在哪几项能力上。

C6 和 C7 是重点观察对象，它们只能靠 E4 判定。最典型的一组是 W4 任务与 E4 判定之间的落差：AA-Briefcase 的任务按 `w1_t1` 编号，后周用前周的产物，评分却是 all-pass 加 Elo；榜首只有 3% 的任务全 criteria 通过，这个数字现在无法归因到是能力不足还是判定过严。VibeLifeBench 是目前唯一接近 E4 的。

**6.4 counterfeit submission 测试。** 挑 6–8 个有可执行 verifier 的 benchmark，按明确设计的违规类型构造表面通过、实质失败的提交：数值正确但用硬编码替换公式；交付物正确但破坏了无关文件；后一阶段丢掉前一阶段确立的口径；先注入一个已知故障，看 Agent 该发现而没发现时评分器是否照样给过。得到的漏判率是**在这组违规类型下**对评分器盲区的测量——换一组反例会暴露另一些盲区，所以它是 6.3 的定点验证，不是欠账总量。

**6.5 现有结论的适用范围。** 把前四节接起来：一个 benchmark 上的提升，只能支持关于被判定的那部分能力的结论。这也给跨 benchmark 迁移难以观察提供了一个解释——如果优化发生在没被判定的维度上，迁移不会出现在分数里。

**产出：** Figure 6（required vs verified 散点，对角线为全部被判定）、Table 7（欠账排名）、Table 8（漏判率）。

---

### Section 7 · Open Challenges and Research Agenda
**基于前面量到的结果，下一步优先做什么？**

按四个维度组织，不按话题堆。这个维度化写法取自 `Towards Long-Horizon Agents` §7 和 `Diving into Reliable Self-Evolving Agents` §9——两篇独立选了几乎相同的维度切分，说明它是成熟模式。每个维度固定两段：先说前文量到了什么，再说因此该做什么。

**7.1 Construction — 怎么造出更有诊断力的任务。** 增加文件数、步骤数、职业数不自动让 benchmark 变好，能被控制的是信息缺口、依赖关系、版本冲突、隐藏约束和反馈时机。全景里那条出题飞轮挂在这里，但入口要反过来：不是先选领域和操作再配 rubric，而是先定目标能力与目标证据层级，再反推需要什么任务结构和什么 verifier。现成的正面案例是 **SpreadsheetBench 从 v1 到 v2**——v1 只比对输出单元格，一份把计算写死成常数的工作簿照样通过；v2 把「本该是公式的硬编码」写进 Debugging 那 100 题的任务要求，并要求未改动的单元格保持原样。证据深度是设计选择，不是模型能力的函数。

**7.2 Verification — 怎么判得更准。** 把缺失的证据层级补上：给 W3 的任务加环境侧断言，给 W4 的任务加跨阶段探针。把 counterfeit 样本变成 benchmark 的常规组件——每个任务配一组「看起来对但实质错」的负例，用来标定评分器本身，让评分器的盲区成为随 benchmark 一起发布的已知量。

**7.3 Generalization — 结论能迁移多远。** 把迁移拆成不同距离：同任务的新模板、同能力的新文件类型、同工作流的新领域、同目标的新软件接口。关键是在比较时控制被判定的维度，否则分不清是能力没迁移还是根本没测。

**7.4 Delegation — 真实工作价值。** OmegaUse 记录了 `human_labor_time` 和 `task_price_proxy`，BankerToolBench 记录了人均 5 小时、最长 21 小时。这些字段让质量、时间、成本和人工介入可以一起被评价，而不是只看 pass rate。

---

### Section 8 · Resources — Availability and Reproducibility

短章。八篇参考里三篇有对应位置（Memory §6、Self-Improvements §8、Long-Horizon §6.6），对 benchmark survey 更是必需。

给出完整清单：数据地址、环境是否可搭、评分器是否开源、许可与访问限制。全景 §G 已经整理好这部分，实测结论是 26 个 benchmark 里 20 个能完整下载，5 个只有榜单页示例。

这一章接回主线：欠账其实有两层，一层是评分器看不到，另一层是研究者拿不到数据和评分器，连复核别人的判定都做不了。

**产出：** Table 8（资源与可得性清单）。

---

### Section 9 · Conclusion

一句话收束：工作评测正在覆盖越来越完整的执行过程，下一步是让任务要求、能力标签和验收证据对应起来，这样 benchmark 上的进展才说明得了可迁移的工作能力。

---

### 图表一览

**Figure 1 是全文结构图，不是 taxonomy 矩阵。** 它的职责是让读者一眼看懂文章怎么展开：三个正文模块 Work Settings（§3）、Capability Requirements（§4）、Evaluation Design（§5）横向排开，W1–W4、C1–C7、E1–E4 分别嵌在对应模块内部，下方用一个综合区连到 Cross-Benchmark Synthesis（§6）和 Research Agenda（§7）。三轴矩阵另设一张 taxonomy 图。

| 编号 | 内容 | 所在章 |
|---|---|---|
| Figure 1 | 全文结构图：三个正文模块 + 综合区 | §1 / §2 |
| Figure 2 | 三轴 taxonomy：W1–W4 × C1–C7，E1–E4 标注在格子上 | §2 |
| Figure 3 | 工作深度分布，可按年份或 domain 分组 | §3 |
| Figure 4 | Benchmark × Capability 覆盖热力图 | §4 |
| Figure 5 | rubric criteria 的证据层级分布 | §5 |
| Figure 6 | required vs verified 散点，对角线为全部被判定 | §6 |
| Table 1 | Benchmark landscape：domain、题量、W 级、E 级、workspace、产物、评分方式 | §2 |
| Table 2 | W / C / E 的标注准则：定义、正例、反例、边界案例 | §2 |
| Table 3 | 能力与最低可判定证据的对应关系（全文枢纽） | §2 |
| Table 4 | 任务来源 × W 级对照 | §3 |
| Table 5 | 同一场景在 W1–W4 的四个任务实例 | §3 |
| Table 6 | 验收性质 × 证据 × 检查动作对照 | §5 |
| Table 7 | 各 benchmark 的欠账排名 | §6 |
| Table 8 | counterfeit 漏判率 | §6 |
| Table 9 | 资源与可得性清单 | §8 |

