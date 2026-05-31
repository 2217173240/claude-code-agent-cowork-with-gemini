# References

> 路由入口 → `../router.md` | 薄入口 → `../SKILL.md`

---

## 使用顺序

1. 先读 `../router.md`
   - 匹配任务类型，确定主入口文件
2. 加载路由指向的 `references/` 文件
   - Class A/B/C 协议为自包含，不需依赖其他文件即可执行
3. 需要理论深度时按需加载 L2 文件

---

## 文件索引

### L1 — 自包含协议（由路由表匹配后加载）

| 文件 | 覆盖场景 | 行数 |
|------|---------|------|
| `class-a-engineering-semantics.md` | 工程语义缺失：事务/幂等/状态机/异常/日志 | ~150 |
| `class-b-performance-concurrency.md` | 性能并发风险：观测基线/影响矩阵/并发归属/控制病 | ~150 |
| `class-c-legacy-safety.md` | 遗留代码安全：边界冻结/特征测试/抽象审查/扩展点 | ~150 |

### L1-共享 — 通用行为与质量关卡

| 文件 | 内容 |
|------|------|
| `engineering-forethought.md` | 工程远见：漂移识别、升级触发、预见性自检 5 问、预训练知识调用框架 |
| `agent-interaction-protocols.md` | 主动交互：会话审视、预实现校准、漂移中断、残余风险追踪、工程师式挑战模板 |
| `quality-gates.md` | 6 个高风险反模式 + 7 项交付格式模板 |

### L2 — 按需深读

| 文件 | 内容 | 原出处 |
|------|------|--------|
| `project-control-topology.md` | 项目级控制拓扑、控制面/数据面/状态面、复杂性转移账本、owner matrix、升级路径、接口冻结 | 原 SKILL.md 项目级控制拓扑 |
| `sensor-engineering.md` | 基线建立、传感器去噪、schema-sensitive 路径、无观测不优化 | 原 SKILL.md §4.1-4.3 |
| `dynamic-control-diseases.md` | 采样与观测新鲜度、去抖/滞回/退避/冷却、anti-chatter/anti-windup/控制器冲突 | 原 SKILL.md §4.4-4.6 |
| `decision-principles.md` | 机制优于策略、MTTR-first、抽象审查协议、演进式架构 | 原 SKILL.md §5.1-5.4 |
| `playbooks.md` | 实战剧本 10 类：bugfix/测试补强/架构收口/性能退化/异步背压/迁移/brownout/配置回滚/flake/成本/SLO | 原 SKILL.md §8 |
| `gda-framework.md` | GDA 五维方法论、四步法完整论述、现代映射附录 | 原 gda-framework.md |

### 导航

| 文件 | 内容 |
|------|------|
| `engineering-forethought.md` | 工程远见与技术视野：漂移识别、升级触发框架、预见性自检 5 问、预训练知识调用、工程师式自信的操作化 |
| `agent-interaction-protocols.md` | Agent 主动交互协议：会话审视、预实现校准、漂移中断、残余风险追踪、工程师式挑战模板、交互节奏控制 |
| `knowledge-graph.md` | 概念图谱：根命题 → 三条支线 → 共享基础 → 概念 A-Z 索引 |
