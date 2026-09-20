# Zirong Chen

# Idea: Benchmarking Work, Not Tasks — A Survey of Work Agent Evaluation

## 1. 我们认为这篇综述的核心创新点

现有 Work Agent / Office Agent / Professional Agent benchmark 已经覆盖了 Excel、PPT、Document、Web、Finance、Law、Research 等大量任务，但目前的总结方式大多仍停留在 **按 domain、artifact 或 benchmark 类型整理现有工作**。

我们希望进一步回答一个更本质的问题：

> **一个 benchmark 的成功，到底提供了多少证据，能够说明 Agent 真正具备现实工作能力？**

围绕这个问题，我们希望提出以下四个核心视角。

### 1.1 From Task Taxonomy to Work Evidence

我们不只整理“有哪些 benchmark”，而是关注：

> **Benchmark score 到 Real-World Work Capability 之间到底还隔着什么？**

同样是一个成功完成的任务，可能只证明 Agent 会修改一个 Excel 公式，也可能证明 Agent 能够自主完成一个包含检索、分析、跨工具操作和结果验证的完整 workflow。

因此：

> **Task Success ≠ Work Competence**

我们希望分析每个 benchmark 最终能够支持多大的 “work capability claim”。

---

### 1.2 Atomic Capability Decomposition

现有分类经常使用：

- Tool Use
- Reasoning
- Memory
- Planning

但这些能力本身仍然比较粗。

我们希望进一步将真实工作拆解成一组 **跨 domain、跨 artifact 的原子能力（atomic capabilities）**，例如：

1. **Perceive / Parse**  
   正确理解文件、表格、网页和界面。

2. **Retrieve & Ground**  
   找到正确的信息，并将其对应到正确实体、文件、页面或单元格。

3. **Maintain State**  
   维护约束、中间结果和当前 workflow 状态。

4. **Decompose & Plan**  
   将目标拆解成正确的子任务，并理解任务依赖关系。

5. **Reason / Compute**  
   完成逻辑、数值、规则和专业推理。

6. **Act & Compose Tools**  
   正确调用工具、组合工具并修改真实 artifact。

7. **Verify**  
   判断自己的结果是否正确。

8. **Recover & Adapt**  
   在出现错误、环境变化或反馈后进行修正。

一个真实工作任务往往不是考察某一个能力，而是：

\[
C_{\text{retrieve}}
\rightarrow
C_{\text{plan}}
\rightarrow
C_{\text{reason}}
\rightarrow
C_{\text{act}}
\rightarrow
C_{\text{verify}}
\]

因此我们希望从 **task-level evaluation** 进一步走向 **capability-level diagnosis**：

> **模型为什么失败？究竟是哪一种基础能力失败？**

---

### 1.3 Delegation Boundary

我们认为 benchmark 难度不仅取决于“任务本身有多难”，还高度取决于：

> **Benchmark designer 已经替 Agent 完成了多少工作？**

例如，同样是“完成财务分析”：

一种 benchmark 可能已经给定：

- 正确文件；
- 正确 sheet；
- 相关数据位置；
- 可使用工具；
- 输出模板；
- workflow。

Agent 实际只需要填写几个公式。

另一种 benchmark 可能只给出：

> “分析公司第三季度利润下降的原因并形成汇报。”

Agent 需要自己：

> 找材料 → 判断版本 → 提取证据 → 分析 → 计算 → 使用工具 → 生成报告 → 验证。

因此我们提出 **Delegation Boundary**：

> **哪些信息、工具、workflow 和中间结构由 benchmark 预先提供，哪些真正需要 Agent 自主完成？**

这有助于解释：

> 为什么某些 benchmark 看起来任务复杂，但实际上真正委托给 Agent 的能力很少。

---

### 1.4 Capability–Evaluation Gap

一个任务 **需要某项能力**，并不意味着 benchmark **真正评价了这项能力**。

例如一个 PPT 任务可能实际需要：

- factual correctness；
- information synthesis；
- planning；
- layout；
- visual design；
- consistency。

但最终 evaluator 可能主要依赖截图 + VLM judge 来评估视觉质量。

因此：

\[
\text{Required Capability}
\neq
\text{Evaluated Capability}
\]

我们希望系统分析这种：

> **Capability–Evaluation Gap**

即：

> benchmark 声称或实际需要考察哪些能力，以及它的 verifier 到底真正覆盖了哪些能力。

---

## 2. 我们对 Work Agent Benchmark 的整体理解

我们认为，Work Agent 的目标正在从：

> **完成一个 isolated task**

逐渐走向：

> **承担一段真实工作流程甚至持续工作责任。**

Coding Agent 是一个非常成功的特殊案例：

\[
\text{Understand Repo}
\rightarrow
\text{Plan}
\rightarrow
\text{Edit}
\rightarrow
\text{Test}
\rightarrow
\text{Deliver}
\]

其重要优势在于代码环境具有较强的：

- structure；
- executability；
- statefulness；
- verifiability。

相比之下，真实知识工作通常发生在更加异构的 workspace 中：

> PDF + Excel + PPT + Word + Web + Email + SaaS + Code

同时包含：

- 不完整信息；
- 多文件关系；
- 多步 workflow；
- 跨工具操作；
- 专业约束；
- 模糊目标；
- 弱 verifier；
- 动态反馈。

因此我们认为：

> **Work Agent Benchmark 的核心问题不是“任务够不够复杂”，而是“它到底把多少真实工作委托给了 Agent，又对这些工作能力提供了多强的评价证据”。**

我们希望使用如下统一视角描述一个 benchmark：

\[
\boxed{
\text{Work Context}
\rightarrow
\text{Delegation Boundary}
\rightarrow
\text{Atomic Capability Composition}
\rightarrow
\text{Execution}
\rightarrow
\text{Verification}
\rightarrow
\text{Supported Work Claim}
}
\]

其中：

### Work Context
回答：

> Agent 在做什么工作？

包括：

- Domain / Role；
- Artifact；
- Workspace；
- Task setting。

### Delegation Boundary
回答：

> 哪些东西已经给 Agent，哪些需要 Agent 自己解决？

例如：

- relevant files 是否给定；
- toolset 是否给定；
- workflow 是否给定；
- output schema 是否给定；
- feedback 是否提供。

### Atomic Capability Composition
回答：

> 这个工作真正需要哪些底层能力？

### Verification
回答：

> Benchmark 到底如何判断这些能力是否做对？

例如：

- Exact Match；
- Rule-based；
- Execution-based；
- Rubric；
- LLM Judge；
- VLM Judge；
- Expert / Human Evaluation。

最终，我们希望回答：

> **这个 benchmark 的结果究竟能够支持多大的真实工作能力结论？**

---

## 3. Work Delegation Level：从完成任务到承担工作

除了上述 taxonomy，我们希望提出一个 **L1–L5 Work Delegation Level**。

它不是简单的“难度等级”，也不是“文件数量等级”，而是表示：

> **随着 level 增加，有多少真实工作责任被逐渐交给 Agent。**

### L1 — Atomic Skill

Agent 完成一个局部、明确的能力单元。

例如：

> 修复一个 Excel 公式。

核心是单一或少量 atomic capabilities。

---

### L2 — Composite Task

多个能力被组合起来完成一个完整任务，但 workflow 较为明确。

例如：

> 根据若干材料完成一张分析表。

---

### L3 — Workflow Ownership

Agent 不仅执行步骤，还需要自己组织 workflow。

例如：

> 阅读 PDF → 搜索 Web → 更新 Excel → 生成 PPT。

此时开始真正要求：

- planning；
- dependency reasoning；
- tool composition；
- intermediate-state management。

---

### L4 — Situated Professional Work

任务开始接近真实职业环境：

- 需求不完全明确；
- 存在专业规范；
- 信息存在冲突；
- 需要反复修改；
- 需要 recovery；
- workspace 会动态变化。

例如：

> 完成一次较完整的金融、法律或研究分析任务。

---

### L5 — Persistent Work Responsibility

Agent 不再只是完成一个 task，而是承担持续工作责任：

- cross-session memory；
- changing goals；
- new documents / emails；
- human feedback；
- dynamic re-planning；
- proactive actions；
- sustained verification。

即从：

> **Task Agent**

逐步走向：

> **Autonomous Knowledge Worker**

---

## 4. 我们希望通过这篇综述得到的 Insights

我们不希望这些结论预先写死，而希望通过系统整理现有 benchmark 后进行验证。

目前值得重点分析的 hypothesis 包括：

### Insight 1: Domain Diversity ≠ Capability Diversity

现有 benchmark 看起来覆盖：

- Finance；
- Law；
- Research；
- Healthcare；
- Office。

但拆解到底层能力后，可能仍集中在少数能力：

> Retrieval + Reasoning + Artifact Editing。

因此：

\[
\text{Domain Diversity}
\not\Rightarrow
\text{Capability Diversity}
\]

---

### Insight 2: Benchmark Difficulty Is Strongly Shaped by Hidden Scaffolding

很多 benchmark 的难度可能来自表面任务，而真正关键的 retrieval、tool selection、workflow construction 等步骤已经被 benchmark designer 提前完成。

因此需要分析：

> **任务本身的复杂性**  
> vs.  
> **真正 delegated 给 Agent 的复杂性**。

---

### Insight 3: Primitive Competence ≠ Workflow Reliability

Agent 可能单项能力都不错，但在 long-horizon workflow 中仍然失败。

例如单步成功率均为 90%，连续 10 个关键步骤的整体成功率理论上只有：

\[
0.9^{10}\approx 35\%
\]

因此现实工作失败可能来自：

> **能力组合和误差累积，而不是某一个 primitive 完全不会。**

---

### Insight 4: Verifier Strength May Shape Agent Progress

Coding Agent 的快速发展可能与强 verifier 密切相关：

- compiler；
- unit tests；
- execution feedback。

Spreadsheet 也具有一定程度的 executable verification。

相比之下：

- PPT aesthetics；
- legal judgment；
- professional reports；
- research synthesis

往往依赖更加主观的 verifier。

因此值得分析：

\[
\text{Verifier Strength}
\leftrightarrow
\text{Observed Agent Progress}
\]

---

### Insight 5: Artifact Competence ≠ Occupational Competence

会操作 Excel，并不等于会做金融工作。

会生成 PPT，也不等于会做咨询工作。

会检索法律文本，也不等于具备律师工作能力。

真实职业工作往往要求：

\[
\text{Artifact Skill}
+
\text{Domain Judgment}
+
\text{Workflow Planning}
+
\text{Verification}
+
\text{Uncertainty Handling}
\]

因此：

> **Artifact competence should not be conflated with professional work competence.**

---

### Insight 6: Required Capability ≠ Evaluated Capability

我们希望系统统计：

- 一个 benchmark 的任务实际上需要什么；
- 它最终 evaluator 真正检查了什么。

从而发现当前 benchmark 是否存在系统性的：

> **Capability–Evaluation Gap**

---

## 5. 建议论文目录

# 1. Introduction: From Tasks to Work

## 1.1 The Rise of Work Agents
## 1.2 Why Task Success Is Not Enough
## 1.3 Benchmarking Work, Not Tasks
## 1.4 Contributions

---

# 2. What Is a Work Agent?

## 2.1 Definition

\[
Goal + Workspace + Tools
\rightarrow
Trajectory
\rightarrow
Deliverable
\]

## 2.2 Relations to Neighboring Agents

- Coding Agents
- Web Agents
- Computer-Use Agents
- Office Agents
- Domain-Specific Agents

## 2.3 What Counts as Real-World Work?

---

# 3. A Unified Framework for Work-Agent Evaluation

## 3.1 Work Context

- Domain
- Role
- Artifact
- Workspace

## 3.2 Delegation Boundary

- Information
- Tools
- Workflow
- Output Schema
- Feedback

## 3.3 Atomic Capability Taxonomy

- Perceive / Parse
- Retrieve & Ground
- Maintain State
- Decompose & Plan
- Reason / Compute
- Act & Compose Tools
- Verify
- Recover & Adapt

## 3.4 Capability Composition

讨论原子能力如何组成完整 workflow。

## 3.5 Verification and Work Evidence

讨论：

\[
Required\ Capability
\rightarrow
Evaluated\ Capability
\rightarrow
Supported\ Work\ Claim
\]

---

# 4. Landscape of Work-Agent Benchmarks

## 4.1 General Knowledge Work
## 4.2 Finance
## 4.3 Law
## 4.4 Research
## 4.5 Office and Productivity
## 4.6 Other Professional Domains

该章节主要用于系统整理现有 benchmark，而不是作为全文核心 taxonomy。

---

# 5. Artifact and Workspace Perspectives

## 5.1 Spreadsheet
## 5.2 Document and PDF
## 5.3 Presentation
## 5.4 Web and SaaS
## 5.5 Multi-Artifact Workspace
## 5.6 Cross-Application Workspace

---

# 6. From Atomic Skills to Real Work: Work Delegation Levels

## 6.1 L1 — Atomic Skill
## 6.2 L2 — Composite Task
## 6.3 L3 — Workflow Ownership
## 6.4 L4 — Situated Professional Work
## 6.5 L5 — Persistent Work Responsibility

并将已有 benchmark 映射到 L1–L5。

---

# 7. What Do Current Benchmarks Actually Measure?

这是全文最重要的 empirical analysis / insight 章节。

## 7.1 Capability Coverage

现有 benchmark 主要在测什么能力？

## 7.2 Delegation Coverage

哪些工作实际上仍由 benchmark designer 提前完成？

## 7.3 Capability–Evaluation Gap

任务需要什么能力，evaluator 真正检查什么能力？

## 7.4 Composition and Long-Horizon Failure

primitive competence 与 workflow reliability 是否存在明显差异？

## 7.5 Verifier Strength

不同 verifier 强度是否对应不同的 Agent 发展速度和表现？

## 7.6 Domain Breadth vs Capability Breadth

表面上的 domain diversity 是否真的带来了 capability diversity？

---

# 8. Fundamental Findings and Tensions

## 8.1 Task Success vs Work Competence
## 8.2 Artifact Competence vs Occupational Competence
## 8.3 Realism vs Verifiability
## 8.4 Specialization vs Generality
## 8.5 Outcome vs Process
## 8.6 Static Benchmarks vs Dynamic Work
## 8.7 Primitive Strength vs Composition Reliability

---

# 9. Designing the Next Generation of Work-Agent Benchmarks

## 9.1 Make the Delegation Boundary Explicit
## 9.2 Diagnose Atomic Capabilities
## 9.3 Evaluate Both Process and Outcome
## 9.4 Strengthen Independent Verification
## 9.5 Introduce Dynamic and Recoverable Workflows
## 9.6 Move Toward Cross-Artifact and Cross-Session Work
## 9.7 Include Human–Agent Collaboration

---

# 10. Outlook: From Task Completion to Work Responsibility

最终讨论 Work Agent benchmark 如何从：

\[
\text{Task Completion}
\]

逐渐走向：

\[
\text{Work Responsibility}
\]

以及真正的 General Work Agent 应该如何被评价。

---

## 6. 一句话总结

> **我们希望这篇综述不只是回答“现在有哪些 Work Agent benchmarks”，而是回答“这些 benchmark 到底证明了 Agent 会什么、为什么模型仍然不会完成真实工作，以及下一代 benchmark 应该如何更准确地诊断和推动真实工作能力”。**

可以概括为：

> **Decompose Work → Diagnose Capabilities → Audit Evidence → Measure Delegation → Guide Future Benchmarks.**

# Notes
