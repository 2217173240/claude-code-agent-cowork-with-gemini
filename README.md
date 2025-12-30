# Claude-Code Agent 与 Gemini 协同工作流

## 简介

本工作流是以最简单的提示词模板为载体的、适用于基于需求的结果导向的软件开发全流程和人在回路的代码审查。

## 仓库内容（可直接复制使用）

*   Claude-Code 执行型 Agent 模板：[`documents/claude-cn.md`](documents/claude-cn.md)（中文）、[`documents/claude-en.md`](documents/claude-en.md)（英文）
*   Gemini-CLI 审查/顾问型模板：[`documents/gemini-cn.md`](documents/gemini-cn.md)（中文）、[`documents/gemini-en.md`](documents/gemini-en.md)（英文）
*   CC 使用心法（三条）：[`documents/cc的最佳用法.md`](documents/cc的最佳用法.md)
*   Codex CLI 自动闭环 Prompt：[`codex-auto-prompt/prompt/prompt.md`](codex-auto-prompt/prompt/prompt.md)
*   Codex CLI Prompt 说明文档：[`codex-auto-prompt/prompt/doc.md`](codex-auto-prompt/prompt/doc.md)

## 环境与软件要求

### 环境
*   macOS & Linux 终端 (包括 WSL)

### 软件
*   `claude-code`
*   `gemini-cli`

## 使用方法

1.  **在 `claude-code` 中设置 Agent**:
    *   在 `claude-code` 中，使用 `/sub-agent` 命令导入本仓库 `documents` 文件夹中的模板：[`documents/claude-cn.md`](documents/claude-cn.md) / [`documents/claude-en.md`](documents/claude-en.md)。
    *   或者，将上述模板内容设置为您 `CLAUDE.MD` 的基础内容。

2.  **在 `gemini-cli` 中设置 Agent**:
    *   在初始化并登录 `gemini-cli` 后，导入本仓库 `documents` 文件夹中的模板：[`documents/gemini-cn.md`](documents/gemini-cn.md) / [`documents/gemini-en.md`](documents/gemini-en.md)。
    *   这些模板会将 Gemini 约束为“审查/架构顾问”角色：核心职责是提出审查意见与行动规划，而不是直接写代码。

3.  **协作流程**:
    *   在协作过程中，使用统一的 `@+文件名` 语法来对齐两个 CLI 中 agent 的上下文颗粒度，确保没有任何过时信息。
    *   在修改期间，要保持任务规划文档的实时更新。

4.  **模型角色**:
    *   由于 Gemini 2.5 Pro 并未针对 agent 能力进行特别训练，我们利用其 1M token 的长上下文能力来承担代码审查和提出解决方案的环节，只让具有 200K 上下文的 Claude 模型专注于任务的执行。

## Codex CLI 自动闭环（可选）

如果你希望把“任务状态 + 验收标准”外置成文件，使用 `issues.csv` 驱动长时间的自动闭环开发，可以直接使用本仓库的 Codex CLI Prompt：

*   驱动 Prompt：[`codex-auto-prompt/prompt/prompt.md`](codex-auto-prompt/prompt/prompt.md)
*   配套说明：[`codex-auto-prompt/prompt/doc.md`](codex-auto-prompt/prompt/doc.md)

## 工作流程

在按上述步骤初始化 agent 后，用户必须扮演**人在回路的审查角色**。您需要负责手动审查、复制和粘贴 Claude 与 Gemini 之间的通信（例如，从 Claude 到 Gemini 的汇报，或从 Gemini 到 Claude 的建议）。这确保了两个模型之间的通信符合您的期望，并避免了因让大语言模型自主决策而可能导致的短视效应。

## 思维精华（CC 使用心法）

我只总结最重要的三点，只记住这三个最简单的点让你 CC 智力直线上升：

1、除非在 planmode，永远不要纠正 CC。如果 CC 做错了，直接 clear → git reset ->修改原始 prompt 叫他不要犯这个错。不然你就会收到典中典的“您说的对”。

2、永远不要使用 /compact。你就当没有这个命令，如果一个需求执行到 context 满了还没完成，把这个需求拆成两个。 clear → git reset → 只做第一个需求。

3、如果一个需求三轮对话还没完成，重新来，context 用到 60% 就差不多了。想清楚你要干什么，clear → git reset → 重新编辑 prompt 。

一句话总结：CC 开发团队说过的，错了不要改，直接重新来。没错，绝对是正解。

## 核心思想

1.  **规避 LLM 的局限性**:
    由于 LLM 底层数学规律的缺陷可能导致错误复合效应和上下文窗口限制，本工作流避免使用单一模型来完成完整的“代码审查-代码修改”循环。反之，它引入了 Gemini 的长上下文能力，以尽量减少因上下文窗口限制导致的信息丢失，并降低因平方成本诅咒（quadratic cost curse）而产生的高昂 API 使用费用。

2.  **发挥各自优势**:
    `claude-code` 环境及其完整的工具生态系统，是与 **Claude 4** 模型系列的训练紧密结合的。这使得 **Claude 4** 系列成为目前在“vibe coding”领域最强大的 agent。结合我个人使用 Cursor、Augment 等软件的实际体验，可以说，目前提出的这套方案是实践中门槛最低，并且能够切实完成代码重构等复杂任务的最优解。

## 联系与反馈

如果您有任何建议或疑问，欢迎在本仓库中提出 issue，或联系 `2217173240@qq.com`（请勿发送 QQ 好友请求）。


