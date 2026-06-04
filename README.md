# Coding Agent Prompt Best Practice

## 仓库定位

这个仓库是一套 **AI 编码 Agent 的工程化驾驶方法**，不是一个 Prompt 集合。核心产品是 `cybernetic-systems-engineering-v2`（CSE v2）— 一个基于控制论 + 系统工程 + 总体设计（GDA）的三层路由式 skill，用 2408 行结构化协议覆盖工程语义闭环、性能并发控制、遗留代码安全变更、工程远见、主动交互与审查门禁。

仓库同时提供：

- CSE v2 的全套可执行协议（15 个 reference 文件 + router + 薄入口）
- Codex CLI 的 CSV 驱动循环 prompt
- Harness Engineering 执行框架
- 跨语言重构、门禁设计、审查模板等可复用知识库
- Claude Code / Gemini CLI 的执行与审查型 prompt 模板

---

## 核心产品：CSE v2

**`cybernetic-systems-engineering-v2/`** 是本仓库的核心。它把软件开发建模为闭环控制系统，用三层渐进路由加载替代了 v1 的 792 行单块文件：

```
[L0] SKILL.md (139行) + router.md (59行)     ← 永远同时加载：行为协议 + Control Contract + GDA + 路由表
  │
  ├─ [L1] router 按任务信号匹配 1 个自包含协议 (~120行/个)
  │     ├── §A 工程语义闭环：事务/幂等/状态机/异常/日志
  │     ├── §B 性能与并发控制：观测基线/影响矩阵/并发归属
  │     └── §C 遗留代码安全变更：边界冻结/特征测试/扩展点
  │
  └─ [L2] 按需深读
        ├── engineering-forethought    — 工程远见：漂移识别/升级触发/预见性自检/预训练知识调用
        ├── agent-interaction-protocols — 主动交互：会话审视/预实现校准/漂移中断/残余风险追踪
        ├── review-protocol            — 审查协议：回归优先/输出分级/Harness Backlog/演进叙事审计
        ├── project-control-topology   — 控制面/数据面/状态面/复杂性转移账本/owner matrix
        ├── decision-principles        — 机制优于策略/MTTR-first/抽象审查/演进式架构
        ├── sensor-engineering         — 基线建立/去噪/schema-sensitive/无观测不优化
        ├── dynamic-control-diseases   — 采样新鲜度/去抖滞回/anti-chatter/windup
        ├── playbooks                  — 11 类实战剧本
        ├── quality-gates              — 6 反模式 + 交付格式 + 证据信赖度
        └── gda-framework              — 五维方法论 + 理论底座 + 现代映射附录
```

**v1（`cybernetic-systems-engineering/`）仍然保留，适用于：** 想一次通读完整理论体系的场景、不需要路由匹配的简单任务。v2 是推荐的默认入口。

---

## 目录总览

```
.
├── README.md
├── LICENSE
│
├── cybernetic-systems-engineering-v2/   ← 核心：CSE v2 三层路由式 skill
│   ├── SKILL.md                          L0 薄入口（行为协议 + 核心哲学 + Control Contract + GDA）
│   ├── router.md                         L0 路由引擎（13 任务类型匹配 + 信号自检 4 问）
│   ├── agents/openai.yaml                skill 元数据
│   ├── assets/quickstart.md             快速上手（路由式一句话入口）
│   └── references/                      15 个协议/参考文件
│
├── cybernetic-systems-engineering/       CSE v1（单块 skill，保留作为理论参考）
│   ├── SKILL.md                          792 行完整理论论述
│   ├── agents/openai.yaml
│   ├── assets/quickstart.md
│   ├── scripts/issues.csv               v1 迭代记录（CSE-001 ~ CSE-019）
│   └── references/
│       ├── gda-framework.md              GDA 五维方法论
│       └── README.md
│
├── harness-engineering/                  Harness-first 执行 skill
│   ├── SKILL.md                          先定义成功边界 → 逐层放权 → 自主探索
│   ├── agents/openai.yaml
│   └── references/harness-engineering-digest.md
│
├── codex-auto-prompt/                    Codex CLI CSV 驱动开发
│   ├── prompt/
│   │   ├── prompt.md                    读取 issues.csv → 开发-测试-提交循环
│   │   └── doc.md                       CSV 结构说明 + 避坑点
│   └── seed-Agentsmd/
│       └── AGENTS.md                    通用 AGENTS.md 种子模板
│
└── documents/                            知识库与 Prompt 模板
    ├── claude-cn.md / claude-en.md       执行型 Prompt（身份/准则/工具/SOP/规范）
    ├── gemini-cn.md / gemini-en.md       顾问型 Prompt（审查/反馈/禁止直接写代码）
    ├── 从 SWE-CI 到 Harness Engineering.md  SWE-CI 论文解读 + 共性技巧 + 审查 Prompt 模板
    ├── cross_language_refactor_reusable_kb.md  跨语言重构知识库（流程/验收/CI/人机协作）
    └── cc的最佳用法.md                   Claude Code 三条实战心法
```

---

## 文件导航

### `cybernetic-systems-engineering-v2/` — 核心 skill

| 文件 | 内容 | 何时用 |
|------|------|--------|
| `SKILL.md` | L0 薄入口：行为协议（主动审视/预实现校准/漂移中断/残余风险）、核心哲学、Control Contract v2 模板、GDA 四步摘要、快速路由 | 每次加载 skill 时自动读取 |
| `router.md` | L0 路由引擎：13 种任务类型匹配表、漂移/交互子路由、信号自检 4 问 | 与 SKILL.md 同时加载 |
| `agents/openai.yaml` | skill 元数据：display_name "Cybernetic Systems Engineering v2" | Codex/其他平台注册 skill 时 |
| `assets/quickstart.md` | 一句话入口 + 最小控制模板 + 典型示例 | 首次使用，快速定位对应协议 |
| `references/class-a-engineering-semantics.md` | §A 工程语义闭环：幂等/事务/状态机/异常/日志 — 从需求升级为工程约束 | 事务模糊、幂等缺失、异常吞没、状态机无约束 |
| `references/class-b-performance-concurrency.md` | §B 性能与并发控制：观测基线 6 选 2 + 7 knob 影响矩阵 + 并发归属 7 问 | N+1、循环 RPC、锁滥用、重试无退避、无观测即优化 |
| `references/class-c-legacy-safety.md` | §C 遗留代码安全变更：边界冻结 10 项 + 5 扩展模式 + 特征测试 4 步法 | 顺手重构、删"重复"代码、改历史兼容逻辑 |
| `references/engineering-forethought.md` | 工程远见：漂移信号清单/升级触发框架/预见性自检 5 问/预训练知识调用 | 分支膨胀、workaround 扩散、需要判断修补 vs. 设计 |
| `references/agent-interaction-protocols.md` | 主动交互：会话审视/预实现校准/漂移中断 A-B 模板/残余风险跨会话追踪/工程师式挑战模板 | 需求不完整、实现中触发漂移阈值、工程决策被推迟 |
| `references/review-protocol.md` | 审查协议：回归优先检查清单（5 项）/ 输出分级（Must-fix/Should-fix/Follow-ups/Tests/Risk Register）/ Harness Backlog 生成 / 演进叙事审计 | 代码审查、PR Review、commit range 交叉审计、全库审计 |
| `references/quality-gates.md` | 6 个高风险反模式 + 7 项交付格式（含证据信赖度） | 交付前自查、跨任务通用质量门 |
| `references/project-control-topology.md` | 控制面/数据面/状态面三分法、复杂性转移账本、owner matrix、升级路径、冻结条件 | 跨模块变更、涉及共享接口/状态 |
| `references/dynamic-control-diseases.md` | 采样新鲜度、去抖/滞回/退避/冷却、anti-chatter/windup、控制器冲突 | 性能抖动、阈值反复跳变、重试风暴 |
| `references/decision-principles.md` | 机制优于策略、MTTR-first、抽象审查（WET）、演进式架构（two-way door） | 需要架构决策、评估多个修复方案 |
| `references/sensor-engineering.md` | 基线建立、传感器去噪、schema-sensitive 路径、无观测不优化 | 观测不稳定、涉及真实数据库/网络/扩展加载 |
| `references/playbooks.md` | 11 类实战剧本：bugfix/背压/迁移/brownout/flake/成本/SLO/演进叙事审计 | 明确的任务类型，需要步骤骨架 |
| `references/gda-framework.md` | GDA 五维方法论、四步法完整论述、三类支线对位表、现代映射附录 | 需要理论深度、需要解释"为什么这样设计" |
| `references/knowledge-graph.md` | 概念树 + A-Z 索引（60+ 条目） | 需要理解概念间关联、快速定位某个概念 |

### `cybernetic-systems-engineering/` — CSE v1（保留参考）

| 文件 | 内容 | 何时用 |
|------|------|--------|
| `SKILL.md` | 792 行完整理论论述（控制拓扑/传感器工程/动态控制病/决策准则/实战剧本） | 想一次通读全部理论，或不需要路由匹配的简单场景 |
| `references/gda-framework.md` | 五维方法论 + GDA 四步法 + 架构启示 | 理论深度需求 |
| `scripts/issues.csv` | v1 从 CSE-001 到 CSE-019 的完整迭代记录 | 了解 skill 的演进历史 |

### `harness-engineering/` — 执行框架 skill

| 文件 | 内容 | 何时用 |
|------|------|--------|
| `SKILL.md` | Harness-first 执行协议：成功边界 → 逐层放权 → 自主探索预算 → 求助阈值 → 可追溯交付 | 复杂排障、CI 修复、需要可观测可协作的执行框架 |
| `references/harness-engineering-digest.md` | OpenAI《Harnesses are underrated》中文蒸馏 | 理解 harness 设计原则与案例 |

### `codex-auto-prompt/` — Codex CLI 驱动

| 文件 | 内容 | 何时用 |
|------|------|--------|
| `prompt/prompt.md` | 以 `issues.csv` 驱动的读取-开发-测试-提交循环 prompt | 用 Codex CLI 做持续集成式开发 |
| `prompt/doc.md` | CSV 结构说明、长期运行原理、使用步骤与避坑 | 理解和配置 CSV 驱动开发 |
| `seed-Agentsmd/AGENTS.md` | 去项目绑定信息的通用 AGENTS.md 种子模板 | 为新项目快速建立 AGENTS.md 基线 |

### `documents/` — 知识库与 Prompt 模板

| 文件 | 内容 | 何时用 |
|------|------|--------|
| `claude-cn.md` | Claude Code 执行型中文 Prompt（身份、准则、SOP、规范、思维模型） | 需要一个"直接写代码"的 agent prompt |
| `claude-en.md` | 英文版 | 同上 |
| `gemini-cn.md` | Gemini CLI 顾问型中文 Prompt（审查/规则保真/禁止直接写代码） | 需要一个"只审不写"的顾问 agent |
| `gemini-en.md` | 英文版 | 同上 |
| `从 SWE-CI 到 Harness Engineering.md` | SWE-CI 论文关键结论、Harness Engineering 行业共识、GPT‑5.4/Opus 4.6 共性技巧、审查 Prompt 模板（ROLE → MODES → PHASE 0-4 → OUTPUT） | 理解"为什么回归是 AI 编程的第一敌人"、落地审查自动化、为 Codex `/review` 配置自定义指令 |
| `cross_language_refactor_reusable_kb.md` | 大型跨语言重构流程：Harness × CSV Loop 融合、阶段验收模板、最小证据集、CI 门禁、人机协作 | 做跨语言迁移或大规模重构时的方法论参照 |
| `cc的最佳用法.md` | Claude Code 三条实战心法：非 Plan Mode 不纠正、不要 `/compact`、三轮未完成就重开 | Claude Code 重度用户的避坑技巧 |

---

## 怎么选用

### 按"我当前的任务"选

| 我想... | 先看... |
|---------|---------|
| 做 bugfix/feature/refactor，需要系统工程方法 | `cybernetic-systems-engineering-v2/assets/quickstart.md`（一句话入口）→ `router.md`（按信号匹配协议） |
| 做代码审查/PR Review/全库审计 | `cybernetic-systems-engineering-v2/references/review-protocol.md` |
| 做性能优化/稳定性排查 | `cybernetic-systems-engineering-v2/references/class-b-performance-concurrency.md` |
| 改遗留代码，不想顺手破坏 | `cybernetic-systems-engineering-v2/references/class-c-legacy-safety.md` |
| 把 agent 放进复杂排障/CI 修复 | `harness-engineering/SKILL.md` |
| 用 Codex CLI 做 CSV 驱动持续开发 | `codex-auto-prompt/prompt/prompt.md` + `prompt/doc.md` |
| 理解为什么"回归"是 AI 编程的现实瓶颈 | `documents/从 SWE-CI 到 Harness Engineering.md` |
| 拿到一个可直接用的审查 prompt 模板 | 同上文件的 §即插即用的代码库审查 Prompt Template |
| 做跨语言迁移或大规模重构 | `documents/cross_language_refactor_reusable_kb.md` |
| 给新项目配一个 AGENTS.md 基线 | `codex-auto-prompt/seed-Agentsmd/AGENTS.md` |

### 按"我想深入学习系统论"选

1. `cybernetic-systems-engineering-v2/SKILL.md` — 核心哲学与行为协议
2. `cybernetic-systems-engineering-v2/references/gda-framework.md` — 五维方法论与四步法
3. `cybernetic-systems-engineering/SKILL.md` — v1 的完整理论论述（可选，用于完整学术理解）
4. `cybernetic-systems-engineering/scripts/issues.csv` — 理解整个体系的迭代演化过程

---

## v1 → v2 演化路径

| 维度 | v1 | v2 |
|------|----|----|
| 入口 | 792 行单块文件一次性加载 | L0 薄入口（~200 行）+ 按任务匹配 |
| 内容组织 | 按理论框架（拓扑→传感器→决策→剧本） | 按任务类型（工程语义/性能并发/遗留安全 + 远见/交互/审查） |
| 加载策略 | 全量加载 | L0 → L1 → L2 渐进路由 |
| 上下文消耗 | ~800 行每次 | ~300 行起（L0 + L1），按需扩展到 L2 |
| Agent 主动性 | 无 | 行为协议 + 交互协议（会话审视/预实现校准/漂移中断/残余风险） |
| 审查能力 | 无 | 回归优先审查协议 + Harness Backlog 生成 |
| 概念导航 | 线性阅读 | router + knowledge-graph 双向索引 |

v1 适合需要完整理论理解的场景。v2 适合实际工程使用——它把理论收束为可执行协议，并根据任务信号自动匹配。

---

## 仓库最适合的场景

- 将 Codex/Claude 等编码 Agent 放入复杂工程任务，用 CSE v2 做系统性控制
- 构建 Agent 的主动交互能力（不等用户报错，自己发现并报告漂移、约束缺口、残余风险）
- 自动化代码审查（回归优先、证据驱动、Harness Backlog 产出）
- Codex CLI 的 CSV 驱动长时间自动开发与自审
- Claude Code 与 Gemini CLI 的分工协作（执行 vs. 审查）
- 需要 harness-first 执行框架的复杂排障或 CI 修复
- 跨语言重构方法论的落地参照
