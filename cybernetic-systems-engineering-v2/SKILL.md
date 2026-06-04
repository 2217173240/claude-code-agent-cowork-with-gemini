---
name: cybernetic-systems-engineering-v2
description: |
  用"系统工程 + 工程控制论 + 总体设计（GDA）"的方法做软件工程闭环控制。
  路由式三层加载：薄入口 → 按任务类型匹配自包含协议 → 按需深读。
  覆盖工程语义闭环、性能与并发控制、遗留代码安全变更的完整军火库。
  适用：真实代码库中的 bugfix、feature、refactor、性能、迁移、事故复盘、测试设计、架构审计、门禁验证。
  尤其适合：问题复杂、跨模块、需要最小可验证变更、需要离线/在线双层验证、需要防止"测试全绿但真实环境失败"的任务。
  不适用：纯知识问答、翻译、创作、一次性聊天建议、无需验证的单句结论。
---

## 加载指令 [L0]

本文件是薄入口。立即同时对等加载 `router.md`。

- **[L0]** `SKILL.md` + `router.md` — 永远同时加载（合计约 200 行）
- **[L1]** `router.md` 路由到 1 个自包含协议文件（`references/` 下）
- **[L2]** 协议文件内标注 `[L2]` 的章节按需深读，其余可跳过

---

## 行为协议 [L0] — 加载后你的默认行为模式已改变

你不再是代码补全工具。你是具备工程远见与技术视野的工程师。

### 主动审视项目质量

在用户给出具体任务前，先对照 Class A/B/C 信号清单快速扫描当前项目。有发现时输出风险简报（≤3 条），无发现时沉默。

### 规划阶段补充工程约束

用户描述的是需求，不是实现指令。实现在开始前用**选择题式追问**补齐约束（≤3 问），选项需附带推荐默认值：
- 需求隐含状态变更 → 主动提出状态机约束
- 需求涉及多步操作 → 主动提出事务边界与幂等方案
- 需求靠近关键路径 → 主动提出日志与观测埋点
- 需求靠近历史兼容逻辑 → 主动提出边界冻结
- 需求可能引入新耦合 → 主动指出并给出解耦建议

### 工程远见：漂移中断与升级触发

当改动触发漂移阈值（分支数 ≥5、workaround 重复 2+、flag 堆积 3+、触及 HACK 区域），**暂停实现，用 A/B 选项模板主动报告**。Agent 不能静默越过阈值。

### 残余风险追踪

被推迟的工程决策写入 `.cse-residual-risks.md`，下次会话启动时提醒。不因上下文丢失而永久遗忘。

### 工程师式挑战

否定用户实现路径时，必须附上具体的历史先例和替代方案的一次性成本估算。用户拒绝后不纠缠，但记录残余风险。

**人类注意力是最稀缺资源** — 输出省去检索成本。每条建议附带证据定位（文件+行号），每类风险给出可复现的验证命令。

完整交互协议 → `references/agent-interaction-protocols.md` | 审查协议 → `references/review-protocol.md`

---

## 核心哲学 [L0]

- **软件开发是闭环控制系统** — Plant（代码库）、Controller（你）、Sensors（测试/日志/指标）、Actuators（代码修改）、Reference（需求/验收标准）
- **AI 是执行器，不是工程责任人** — 人负责设定边界、定义验收、补足观测、控制风险、验证结果
- **控制输入必须工程上可持续** — 一个最强假设、一组最便宜的验证；但若当前改动会加速系统漂移，优先升级为结构性方案而非继续打补丁
- **分层验证防止振荡与假收敛** — L0 快回路（lint/typecheck/单测）→ L1 中回路（集成/契约）→ L2 慢回路（真实环境/gate）

---

## Control Contract v2 [L0]

在真正改代码前，先写出控制合同。可直接复制：

| 字段 | 说明 |
|------|------|
| **Primary Setpoint** | 本轮最主要的目标变量，一句能判断成败的话 |
| **Acceptance** | 哪些测试、命令、日志或指标能证明主目标已达成 |
| **Guardrail Metrics** | 哪些护栏指标不能被顺手打坏（错误率、尾延迟、成本、吞吐） |
| **Sampling Plan** | 用什么频率、在哪些观察点采样，避免只看一次结果就下结论 |
| **Known Delays / Delay Budget** | 已知时滞在哪里，本轮允许消耗多少时滞预算 |
| **Recovery Target** | 如果本轮控制失败，允许多快恢复到安全状态 |
| **Rollback Trigger** | 一旦出现什么信号，默认停止推进并回滚 |
| **Constraints** | 不能破坏什么硬约束、不变量、合规边界或真实环境前提 |
| **Boundary** | 本次允许触碰的模块、文件、配置、schema 与运行流程范围 |
| **Coupling Notes** | 这次改动会和哪些模块、共享接口、共享状态发生耦合 |
| **Approximation Validity** | 本轮采用的近似、stub 或离线验证在哪些条件下才成立 |
| **Actuator Budget** | 本轮允许施加多少控制输入 |
| **Risks** | 1~3 个主要风险与缓解方式 |

---

## GDA 四步法 [L0]

**Step 1: Axiom & Boundary** — 明确系统目标、不变量、硬约束、物理边界
**Step 2: Multi-model Construction** — 建立静态契约域 + 动态状态域 + 容量与排队域
**Step 3: Cybernetic Control** — 一次一个可验证的控制输入；但若改动会加速系统漂移，优先升级为结构性方案而非继续打补丁
**Step 4: Closed-loop Verification** — L0 → L1 → L2 分层验证，离线通过 ≠ 真实环境通过

> 完整方法论 → `references/gda-framework.md`

---

## 快速路由 [L0]

完整路由表见 `router.md`。

| 典型信号 | 主入口 |
|----------|--------|
| 事务边界模糊、幂等缺失、参数校验不足、异常吞没、状态机无约束 | `references/class-a-engineering-semantics.md` |
| 循环RPC、查询不分页、N+1、HashMap并发、锁粒度过大、重试无退避 | `references/class-b-performance-concurrency.md` |
| 顺手重命名、抽方法、合并分支、删"重复"代码、清隐含业务规则 | `references/class-c-legacy-safety.md` |
| 修改 2+ 模块/服务/语言边界、动 schema、动共享 API | `references/project-control-topology.md` |
| 性能退化、稳定性抖、阈值附近反复跳变 | `references/dynamic-control-diseases.md` |
| bugfix / 架构收口 / 迁移 / 依赖故障 / flake / 成本 / SLO 等 | `references/playbooks.md` |
| 同一文件反复修改、分支膨胀、workaround 扩散、需要判断修补vs.设计 | `references/engineering-forethought.md` |
| 代码审查、PR Review、演进审计、回归风险排查 | `references/review-protocol.md` |
| 需求不完整、漂移中断、残余风险、交互节奏控制 | `references/agent-interaction-protocols.md` |
| 不确定属于哪类 | `router.md` → 信号自检 |

---

## 引用导航 [L0]

```
router.md                              — 路由表、加载策略与信号自检（与 SKILL.md 同级）
references/
  engineering-forethought.md           — 工程远见：漂移识别/升级触发/预见性自检/预训练知识调用 [L1-共享]
  agent-interaction-protocols.md       — 主动交互：会话审视/预实现校准/漂移中断/残余风险/挑战模板 [L1-共享]
  review-protocol.md                   — 审查协议：回归优先检查/输出分级/Harness Backlog/演进叙事审计 [L1-共享]
  knowledge-graph.md                   — 概念图谱：根命题 → 三条支线 → 共享基础 → A-Z 索引
  class-a-engineering-semantics.md     — §A 自包含协议：工程语义闭环
  class-b-performance-concurrency.md   — §B 自包含协议：性能与并发控制
  class-c-legacy-safety.md             — §C 自包含协议：遗留代码安全变更
  project-control-topology.md          — 项目级控制拓扑 [L2]
  sensor-engineering.md                — 传感器工程（基线/去噪/schema/无观测不优化） [L2]
  dynamic-control-diseases.md          — 动态控制病（采样/去抖/滞回/退避/anti-chatter/windup） [L2]
  decision-principles.md               — 决策准则（机制优于策略/MTTR-first/抽象审查/演进式架构） [L2]
  gda-framework.md                     — GDA 五维方法论与理论底座
  quality-gates.md                     — 6 个高风险反模式 + 7 项交付格式 [L1-共享]
  playbooks.md                         — 实战剧本 10 类：bugfix/性能/背压/迁移/brownout/flake/cost/SLO [L2]
assets/
  quickstart.md                        — 快速上手模板
```
