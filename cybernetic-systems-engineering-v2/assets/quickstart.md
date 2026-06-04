# Quickstart

> 路由入口 → `../router.md` | 薄入口 → `../SKILL.md`

## 一句话入口

遇到以下情况，直接跳到对应协议：

- 事务缺/幂等缺/异常吞/状态机无约束 → `../references/class-a-engineering-semantics.md`
- 循环RPC/N+1/无分页/锁滥用 → `../references/class-b-performance-concurrency.md`
- 顺手改名/抽方法/删分支/改历史逻辑 → `../references/class-c-legacy-safety.md`
- 跨模块/动schema/动共享接口 → `../references/project-control-topology.md`
- 性能退化/振荡/抖 → `../references/dynamic-control-diseases.md`
- 同一文件反复改/分支膨胀/workaround扩散 → `../references/engineering-forethought.md`
- 代码审查/PR Review/演进审计 → `../references/review-protocol.md`
- bugfix / 架构收口 / 迁移 / flake 等 → `../references/playbooks.md`
- 不确定属于哪类 → `../router.md` 信号自检

---

## 什么时候用

适合：

- bugfix
- feature
- refactor
- 性能优化
- 测试补强
- 事故复盘
- 架构审计
- gate / handoff

尤其适合：

- “问题复杂、不能只看单个文件”
- “离线通过但真实环境失败”
- “需要最小可验证变更”
- “需要系统级收口，不只是修一行代码”

## 最短使用姿势

在提示词里显式写：

- `$cybernetic-systems-engineering-v2`

如果任务会持续多轮、需要检查点和恢复，可以同时加载 harness-engineering skill 搭配使用。

## 最小可用控制模板 v2

### Control Contract v2

- Primary Setpoint:
- Acceptance:
- Guardrail Metrics:
- Sampling Plan:
- Known Delays / Delay Budget:
- Recovery Target:
- Rollback Trigger:
- Constraints:
- Boundary:
- Coupling Notes:
- Approximation Validity:
- Actuator Budget:
- Risks:

### State Estimate

- Entry:
- Key state:
- Key invariants:
- Current error:

### Plan

1. 先测量（建立观测基线）
2. 判断误差是局部的还是结构性的
3. 局部 → 最小修复；结构性 → 升级为结构性方案（不累积漂移）
4. 分层验证（L0 → L1 → L2）
5. 记录 residual risk（写入 `.cse-residual-risks.md`）

## 一个典型例子

### 用户问题

“本地 `cargo test` 全绿，但真实 Windows + VPN 环境下 `PG_CH` 回测炸了。请定位原因并补离线测试。”

### 这个 skill 会做什么

1. 先建立控制合同
2. 区分：
   - 语义层测试
   - schema 契约层测试
   - 真实环境 gate
3. 把问题从“单个 bugfix”升级成：
   - 根因定位
   - 测试缺口审计
   - 最小修复
   - 离线回归矩阵
   - gate handoff

## 记住

这个 skill 的核心不是：

- 用更多术语
- 画更复杂的图

而是：

- 更快得到可信误差信号
- 工程上可持续地改动（不累积漂移）
- 更清楚地区分”已验证”与”尚未验证”
