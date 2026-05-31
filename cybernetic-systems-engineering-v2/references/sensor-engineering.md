## 传感器工程（Sensor Engineering） [L2]

> 路由入口 → `../router.md` | 概念图谱 → `knowledge-graph.md`
> 前序必读 → `project-control-topology.md`

---

### 基线建立

默认顺序：

1. `git status` / `git diff`
2. 读取 issue、相关代码、最近改动、已有 review
3. 跑最便宜的验证路径
4. 记录失败命令、失败用例、关键信号

### 传感器去噪

如果信号不稳定：

- 重跑 3~5 次
- 固定随机种子 / 时区 / 并发
- 隔离外部依赖
- 把偶现变成最小稳定复现

### 特别规则：schema-sensitive 路径

凡是涉及以下任一因素：

- 真实数据库列类型
- SQL cast
- 驱动参数序列化
- `PG_CH` / 真实 broker / 真实文件系统 / 真实扩展加载

都必须明确区分：

1. **语义测试**
   - fake fetcher / stub / resolver 白盒
2. **schema 契约测试**
   - 锁定关键 SQL / schema / 分支行为
3. **真实环境 gate**
   - Windows / VPN / 真实数据库 / 真实 broker

禁止把：

- "resolver 语义通过"
- "cargo test 全绿"

直接写成：

- "真实环境通过"

### 无观测，不优化

任何性能或稳定性优化，默认都要先拿到观测基线。

最小入场券：

- **trace**
  - 先看跨服务链路到底卡在哪一跳
- **flame graph**
  - 先看 CPU / wall time 真正烧在什么调用栈
- **profiling baseline**
  - 先记录修改前的基线，不要只拿修改后的单次结果自嗨
- **golden signals**
  - 至少关注延迟、流量、错误、饱和度这类核心信号
- **对照实验**
  - 能做 A/B、shadow、canary 或前后对照时，优先做对照，而不是纯猜测

默认规则：

1. 无观测，不优化
2. 观测不足时，默认先补观测点、profiling 或链路追踪，再决定是否改代码
3. 任何"感觉这里慢""猜这里有瓶颈"的说法，都不能直接升级成优化动作
4. 优化结果至少要和修改前的 profiling baseline 做一次对照
