## 概念树

```
根命题: AI是执行器，人定义边界、验收、观测、验证
  │
  ├── 支线A: 工程语义闭环
  │   │  入口: class-a-engineering-semantics.md
  │   │
  │   ├── Control Contract v2 ──────────────→ ../SKILL.md L0 模板 + class-a §契约实操
  │   ├── 验证分层 L0 / L1 / L2 ──────────→ class-a §验证分层
  │   ├── 工程语义 Review 清单 ──────────→ class-a §Review清单（7项检查点）
  │   ├── schema-sensitive 路径 ──────────→ sensor-engineering.md §schema规则
  │   ├── 假收敛反模式 ────────────────→ quality-gates.md §反模式 1
  │   ├── 弱断言反模式 ────────────────→ quality-gates.md §反模式 4
  │   └── 与支线B/C交汇 ────────────────→ project-control-topology.md §复杂性转移账本
  │
  ├── 支线B: 性能与并发控制
  │   │  入口: class-b-performance-concurrency.md
  │   │
  │   ├── 观测基线协议 ────────────────→ class-b §观测基线
  │   ├── 控制输入→输出影响矩阵 ────────→ class-b §影响矩阵
  │   ├── 并发归属检查 ────────────────→ class-b §并发归属
  │   ├── 动态控制病 ────────────────→ dynamic-control-diseases.md
  │   │   ├── 采样与观测新鲜度
  │   │   ├── 去抖 / 滞回 / 退避 / 冷却
  │   │   └── anti-chatter / anti-windup / 控制器冲突
  │   ├── 机制优于策略 ────────────────→ decision-principles.md §机制优于策略
  │   ├── 无观测不优化 ────────────────→ sensor-engineering.md §无观测不优化
  │   ├── profiling / trace / golden signals ─→ sensor-engineering.md §基线建立
  │   └── 与支线A/C交汇 ────────────────→ project-control-topology.md §复杂性转移账本
  │
  └── 支线C: 遗留代码安全变更
      │  入口: class-c-legacy-safety.md
      │
      ├── 边界冻结协议（只扩展不改写）──→ class-c §边界冻结
      ├── 特征测试协议 ────────────────→ class-c §特征测试
      ├── 抽象审查（WET > 错误抽象）───→ class-c §抽象审查 + decision-principles.md §抽象审查
      ├── 扩展点策略目录 ────────────────→ class-c §扩展点策略
      ├── 演进式架构 / 可逆决策 ──────────→ decision-principles.md §演进式架构
      ├── two-way door / one-way door ────→ decision-principles.md §演进式架构
      ├── 迁移桥接期 / shadow / canary ──→ decision-principles.md §演进式架构
      └── 与支线A/B交汇 ────────────────→ project-control-topology.md

共享基础概念
  ├── 行为协议 ────────────────────────→ ../SKILL.md §行为协议 + engineering-forethought.md
  │   ├── 主动审视项目质量（会话启动扫描）
  │   ├── 规划阶段补充工程约束（预实现校准对话）
  │   ├── 补丁漂移识别与升级触发
  │   ├── 预见性自检 5 问
  │   ├── 预训练知识调用框架
  │   ├── 工程师式自信的操作化
  │   └── Agent 主动交互协议 ──────────→ agent-interaction-protocols.md
  │       ├── 会话启动审视协议
  │       ├── 预实现校准对话（选择题式追问）
  │       ├── 漂移中断协议（A/B 模板 + 阈值表）
  │       ├── 残余风险追踪协议（跨会话记忆）
  │       ├── 工程师式挑战模板
  │       └── 交互节奏控制（频率上限 + 沉默规则）
  ├── GDA 四步法 ──────────────────────→ ../SKILL.md L0 + gda-framework.md
  ├── 项目级控制拓扑 ──────────────────→ project-control-topology.md
  │   ├── 控制面 / 数据面 / 状态面 三分法
  │   ├── 复杂性转移账本
  │   ├── owner matrix（最小权责矩阵）
  │   ├── 默认升级路径（4级）
  │   ├── 接口冻结条件
  │   └── 跨模块裁决规则
  ├── 传感器工程 ──────────────────────→ sensor-engineering.md
  │   ├── 基线建立 (git status → diff → 最便宜验证)
  │   ├── 传感器去噪（3~5次重跑 / 固定种子 / 隔离依赖）
  │   └── schema-sensitive 路径
  ├── 决策准则 ────────────────────────→ decision-principles.md
  │   ├── 机制优于策略 (禁止硬编码 timeout/retry/阈值)
  │   ├── MTTR-first & crash-only
  │   ├── 抽象审查协议 (WET / 物理解耦 / 共变关系)
  │   └── 演进式架构 & two-way door
  ├── 质量关卡 ────────────────────────→ quality-gates.md
  │   ├── 6 个高风险反模式
  │   └── 交付格式（7 项结构 + 证据来源/置信度）
  ├── 审查协议 ────────────────────────→ review-protocol.md
  │   ├── 回归优先检查清单（5 项）
  │   ├── 审查输出分级（Must-fix/Should-fix/Follow-ups/Tests/Risk Register）
  │   ├── Harness Backlog 生成（审查 → guardrail 转化）
  │   └── 演进叙事审计（COMMIT_RANGE_CROSS_REVIEW）
  └── 实战剧本 ────────────────────────→ playbooks.md
      ├── bugfix / 测试补强 / 架构收口
      ├── 性能退化 / 异步背压
      ├── 迁移 cutover / 依赖 brownout
      ├── 配置回滚 / flake triage
      └── 成本失控 / SLO 漂移
```

---

## 概念 A-Z 索引

| 概念 | 位置 |
|------|------|
| anti-chatter | `dynamic-control-diseases.md` §anti-chatter |
| anti-windup | `dynamic-control-diseases.md` §anti-windup |
| backoff（退避） | `dynamic-control-diseases.md` §退避策略 |
| agent interaction protocols（Agent 主动交互协议） | `agent-interaction-protocols.md` |
| behavioral protocol（行为协议） | `../SKILL.md` §行为协议 + `engineering-forethought.md` |
| brownout（依赖部分故障） | `playbooks.md` §依赖brownout |
| canary | `decision-principles.md` §演进式架构 |
| characterization test（特征测试） | `class-c-legacy-safety.md` §特征测试 |
| confidence level（置信度标注） | `review-protocol.md` §审查输出分级 + `quality-gates.md` §交付格式 |
| Control Contract v2 | `../SKILL.md` L0 模板 |
| controller conflict（控制器冲突） | `dynamic-control-diseases.md` §控制器冲突 |
| control plane / data plane / state plane | `project-control-topology.md` §三分法 |
| cooling window（冷却窗口） | `dynamic-control-diseases.md` §冷却时间 |
| cost runaway（成本失控） | `playbooks.md` §成本失控 |
| crash-only | `decision-principles.md` §MTTR-first |
| debounce（去抖） | `dynamic-control-diseases.md` §去抖 |
| decision principles（决策准则） | `decision-principles.md` |
| drift detection（漂移识别） | `engineering-forethought.md` §补丁漂移识别 |
| dynamic control diseases（动态控制病） | `dynamic-control-diseases.md` |
| drift interrupt（漂移中断） | `agent-interaction-protocols.md` §漂移中断协议 |
| engineering forethought（工程远见） | `engineering-forethought.md` + `../SKILL.md` §行为协议 |
| escalation trigger（升级触发） | `engineering-forethought.md` §升级触发与决策框架 |
| evidence-driven（证据驱动） | `review-protocol.md` §审查哲学 + `quality-gates.md` §交付格式 |
| evolution narrative audit（演进叙事审计） | `review-protocol.md` §演进叙事审计 + `playbooks.md` §演进叙事 |
| evolutionary architecture（演进式架构） | `decision-principles.md` §演进式架构 |
| extend-only（只扩展不改写） | `class-c-legacy-safety.md` §边界冻结 |
| flake triage | `playbooks.md` §flake triage |
| foresight checklist（预见性自检） | `engineering-forethought.md` §预见性自检框架 |
| frozen boundary（冻结边界） | `project-control-topology.md` §接口冻结条件 |
| GDA 四步法 | `gda-framework.md` |
| guardrail metrics（护栏指标） | `../SKILL.md` L0 Control Contract |
| harvest backlog（Harness Backlog） | `review-protocol.md` §Harness Backlog 生成 |
| hysteresis（滞回） | `dynamic-control-diseases.md` §滞回区间 |
| knowledge graph（概念图谱） | `references/knowledge-graph.md`（本文件） |
| mechanism over policy（机制优于策略） | `decision-principles.md` §机制优于策略 |
| MTTR-first | `decision-principles.md` §MTTR-first |
| Must-fix / Should-fix / Follow-ups（审查输出分级） | `review-protocol.md` §审查输出分级 |
| no observation no optimization（无观测不优化） | `sensor-engineering.md` §无观测不优化 |
| observability evidence（观测证据） | `quality-gates.md` §交付格式 |
| one-way door | `decision-principles.md` §演进式架构 |
| owner matrix（权责矩阵） | `project-control-topology.md` §owner matrix |
| patching vs. designing（修补 vs. 设计） | `engineering-forethought.md` §升级触发与决策框架 |
| playbooks（实战剧本） | `playbooks.md` |
| pre-implementation calibration（预实现校准） | `agent-interaction-protocols.md` §预实现校准对话 |
| pre-training knowledge（预训练知识） | `engineering-forethought.md` §预训练知识调用框架 |
| project control topology（项目级控制拓扑） | `project-control-topology.md` |
| recovery evidence（恢复证据） | `quality-gates.md` §交付格式 |
| regression-first review（回归优先审查） | `review-protocol.md` §回归优先检查清单 |
| residual risk tracking（残余风险追踪） | `agent-interaction-protocols.md` §残余风险追踪协议 |
| review protocol（审查协议） | `review-protocol.md` |
| router（路由索引） | `router.md`（根目录） |
| sampling aliasing（采样别名） | `dynamic-control-diseases.md` §采样与观测 |
| sensor engineering（传感器工程） | `sensor-engineering.md` |
| shadow implementation（影子实现） | `quality-gates.md` §反模式 3 |
| SLO drift | `playbooks.md` §SLO漂移 |
| stale metrics（陈旧指标） | `dynamic-control-diseases.md` §陈旧指标 |
| two-way door | `decision-principles.md` §演进式架构 |
| WET over wrong abstraction | `decision-principles.md` §抽象审查 |
| zero-regression rate（零回归率） | `review-protocol.md` §审查哲学 |
