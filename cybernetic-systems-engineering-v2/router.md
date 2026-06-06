## 加载策略

[L0] 本文件与 `SKILL.md` 永远同时加载，作为路由入口。
[L1] 按下方路由表匹配任务类型后，加载对应的 `references/` 文件。
[L2] reference 文件内标注 `[L2]` 的章节按需深读，其余可跳过。

---

## 路由表

| 任务类型 | 典型信号 | 主入口 | 深读 |
|----------|----------|--------|------|
| 工程语义缺失 | 事务边界模糊、幂等缺失、参数校验不足、异常吞没、关键日志缺失、状态转换无约束 | `references/class-a-engineering-semantics.md` | `references/gda-framework.md` |
| 性能并发风险 | 循环RPC、查询不分页、N+1 SQL、大对象一次性加载、HashMap用于并发、锁粒度过大、重试无退避、异步无限流 | `references/class-b-performance-concurrency.md` | `references/dynamic-control-diseases.md` |
| 遗留代码越界 | 顺手重命名变量、抽取公共方法、合并分支逻辑、删除"重复"代码、改动历史兼容逻辑、清理隐式业务规则 | `references/class-c-legacy-safety.md` | `references/decision-principles.md` |
| 跨模块变更 | 修改 2+ 模块/服务/语言边界、动 schema、动共享 API、动统一门禁 | `references/project-control-topology.md` | `references/gda-framework.md` |
| 性能退化 | 延迟上升、吞吐下降、CPU/内存/IO 打满 | `references/dynamic-control-diseases.md` | `references/playbooks.md` §性能退化 |
| 稳定性抖动 / flake | 间歇失败、阈值附近反复跳变、偶发不可稳定复现 | `references/dynamic-control-diseases.md` | `references/playbooks.md` §flake triage |
| 明确 bugfix | 明确报错、已知根因、单点故障 | `references/playbooks.md` §bugfix | `references/quality-gates.md` |
| 架构收口 / 审计清理 | 影子实现仍在、双真相并存、重复事实源未收敛 | `references/playbooks.md` §架构收口 | `references/decision-principles.md` |
| 成本 / SLO 漂移 | 成本失控、SLO 长期漂移 | `references/playbooks.md` §成本失控 / §SLO漂移 | `references/decision-principles.md` |
| 配置异常 | 变更后系统行为突变、灰度回放异常 | `references/playbooks.md` §配置回滚 | `references/sensor-engineering.md` |
| 依赖故障 | 下游慢/挂/brownout、部分降级 | `references/playbooks.md` §依赖brownout | `references/decision-principles.md` |
| 代码审查 / PR Review | diff、commit、commit range、全库审计 | `references/review-protocol.md` | `references/quality-gates.md` |

---

## 补丁漂移 / 需要结构性升级

| 任务类型 | 典型信号 | 主入口 | 深读 |
|----------|----------|--------|------|
| 漂移识别与升级触发 | 同一文件被反复修改、分支数膨胀、workaround 扩散、用户连续提相似需求 | `references/engineering-forethought.md` | `references/decision-principles.md` |

---

## 主动交互 / Agent 触发机制

| 任务类型 | 典型信号 | 主入口 | 深读 |
|----------|----------|--------|------|
| 需求不完整 / 约束缺位 | 用户给的描述不含幂等/事务/状态机/观测要求、实现中途触发漂移阈值、工程决策被推迟 | `references/agent-interaction-protocols.md` | `references/engineering-forethought.md` |

---

## 信号自检

如果从上方路由表匹配不到明确类型，按以下四问自检后重新匹配：

1. **为什么要改？** — 修复缺陷 / 提升性能 / 增强可观测性 / 清理技术债？
2. **改动范围是什么？** — 单文件 / 单模块 / 跨模块 / 动 schema 或共享契约？
3. **被改对象谁拥有？** — 你自己 / 同组 / 跨组 / 共享边界 owner / 总体设计部？
4. **怎么验证改对了？** — 单测 / 集成 / 真实环境 / 需要新观测点？

根据答案回到路由表。如果仍无法匹配，默认先读 `references/project-control-topology.md`。

---

## 激活清单

命中任一路由后，先加载并满足对应协议，再继续下一步。下面是每条路由的**必须深读**清单：

| 路由命中 | 必须深读 |
|----------|----------|
| `references/class-a-engineering-semantics.md` | `references/gda-framework.md`, `references/agent-interaction-protocols.md` |
| `references/class-b-performance-concurrency.md` | `references/dynamic-control-diseases.md`, `references/sensor-engineering.md` |
| `references/class-c-legacy-safety.md` | `references/decision-principles.md`, `references/engineering-forethought.md` |
| `references/project-control-topology.md` | `references/gda-framework.md`, `references/quality-gates.md` |
| `references/dynamic-control-diseases.md` | `references/sensor-engineering.md`, `references/playbooks.md` |
| `references/playbooks.md` | `references/quality-gates.md`, `references/decision-principles.md` |
| `references/engineering-forethought.md` | `references/agent-interaction-protocols.md`, `references/decision-principles.md` |
| `references/review-protocol.md` | `references/quality-gates.md`, `references/knowledge-graph.md` |
| `references/agent-interaction-protocols.md` | `references/engineering-forethought.md`, `references/quality-gates.md` |
| `references/quality-gates.md` | `references/review-protocol.md`, `references/gda-framework.md` |

---

## 概念图谱入口

需要理解概念之间的关联网络时 → `references/knowledge-graph.md`
