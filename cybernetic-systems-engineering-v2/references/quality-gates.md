## 质量关卡（Quality Gates） [L1-共享]

> 路由入口 → `../router.md` | 概念图谱 → `knowledge-graph.md`

---

### 高风险反模式（必须主动检查）

1. **假收敛**
   - 单测通过，但真实环境条件未覆盖

2. **双真相**
   - 文档一套、主链一套、备用路径一套

3. **影子实现**
   - callback_dispatcher 更完整，但主链不用
   - helper 存在，但主链不可达

4. **弱断言**
   - 只有 `is_ok()`，没有行为语义断言

5. **测试驱动代码偏离职责**
   - 为了测试方便扩大 `pub` 面
   - 暴露本不该公开的内部实现

6. **把离线测试当 gate**
   - 真实 schema / 真实扩展 / 真实网络问题无法由 stub 替代

---

### 交付格式

最终交付优先按下面结构组织：

1. **Summary**
2. **State Estimate / Root Cause**
3. **Changes**
4. **Verification**
5. **Recovery Evidence**
6. **Observability Evidence**
7. **Residual Risks / Gate Boundary**

其中：

- **Recovery Evidence**
  - 说明怎么恢复、多久恢复、触发了什么回滚或重启语义、恢复预算是否满足
- **Observability Evidence**
  - 说明依据什么判断问题存在、优化有效或风险仍在
  - 至少给出本轮关键日志、指标、trace、profiling 或 gate 证据中的一类
- **每条发现的标注要求**
  - 每条发现必须标注：证据来源（命令输出/测试报告/文件路径/行号）+ 置信度（High/Medium/Low）
  - 不允许 Low 置信度的结论直接作为 Must-fix 依据

如果是长任务，还应同步：

- 审计文档
- 回归矩阵
- handoff 文档
