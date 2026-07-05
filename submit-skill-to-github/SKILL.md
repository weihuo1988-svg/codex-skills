---
name: submit-skill-to-github
description: 将 Codex skill 提交到用户的 GitHub skills 集合仓库。用于用户要求上传、发布、同步、归档或更新某个 skill 到 GitHub，尤其是仓库 weihuo1988-svg/codex-skills；按“一 skill 一个独立文件夹”的结构整理文件、维护根目录 README、验证 skill、提交并推送到远端。
---

# Submit Skill To GitHub

## Core Outcome

把一个 Codex skill 安全提交到 `https://github.com/weihuo1988-svg/codex-skills`，并保持仓库结构清晰：

- 根目录用于 `README.md` 和仓库级文件。
- 每个 skill 使用一个顶层目录，目录名必须等于 skill 名。
- skill 目录内保留标准结构：`SKILL.md`、`agents/openai.yaml`，以及实际用到的 `references/`、`scripts/`、`assets/`。

## Workflow

### 1. Identify the skill

- 从用户请求、当前上下文或明确路径中确定要提交的 skill。
- 优先使用已安装 skill 路径：`/Users/alinyao/.codex/skills/<skill-name>`。
- 读取 `SKILL.md` frontmatter，确认 `name` 与目标目录名一致。
- 如果 skill 名、路径或版本不明确，先问一个简短问题。

### 2. Prepare the repository

- 使用仓库：`https://github.com/weihuo1988-svg/codex-skills.git`。
- 如果已有本地工作区，先检查 `git status --short --branch`。
- 如果需要从远端同步，使用 `git fetch` 和安全的 fast-forward 更新；不要覆盖未提交改动。
- 根目录必须有 `README.md`，说明这是用户开发的 Codex skills 集合仓库。
- 不要把单个 skill 的 `SKILL.md`、`agents/`、`references/` 直接放在仓库根目录。

### 3. Copy the skill into its folder

- 在仓库根目录创建或更新 `<skill-name>/`。
- 复制完整 skill 内容，包括：
  - `SKILL.md`
  - `agents/openai.yaml`
  - 实际存在且非空的 `references/`、`scripts/`、`assets/`
- 不复制 `.git`、临时文件、压缩包、测试输出、系统缓存或空的资源目录。
- 如果是在更新现有 skill，只替换该 skill 目录内相关内容，不改动其他 skill。

### 4. Validate before commit

- 对仓库中的 `<skill-name>/` 运行 `quick_validate.py`。
- 检查仓库顶层布局，确认每个 skill 都是独立目录，根目录没有散落的 skill 本体文件。
- 若验证失败，修复后再提交。

### 5. Commit and push

- 提交信息使用清晰动词，例如：
  - `Add <skill-name> skill`
  - `Update <skill-name> skill`
  - `Organize skills repository layout`
- 推送到 `origin main`。
- 推送后用 `git ls-remote origin main` 或等价方式确认远端提交哈希与本地一致。

## Safety Rules

- 不要 force push，除非用户明确要求并说明原因。
- 不要删除或移动其他 skill，除非用户明确要求。
- 如果远端已有新提交且无法 fast-forward，先停止并说明冲突。
- 如果没有 GitHub 凭据或网络权限，先完成本地仓库和压缩包，再说明还差什么。
- 默认不要创建公开仓库；如果需要新建仓库，优先私有，并确认用户意图。

## Final Report

最终回复保持简洁，说明：

- 更新或新增了哪个 skill。
- 仓库结构是否已符合“一 skill 一个文件夹”。
- 验证命令是否通过。
- 本地提交和远端 `main` 的提交哈希。
- 如果没能推送，说明缺少的凭据、网络权限或远端信息。
