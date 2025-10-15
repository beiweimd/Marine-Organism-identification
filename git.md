12345678
# Git 人话速查表

> 心智模型：**拍快照（commit）+ 移动指针（分支/远端）**。工作区 → 暂存区（index） → 仓库。

## 查看现状

* 当前改了什么：`git status`
* 查看差异（未暂存）：`git diff`
* 查看差异（已暂存）：`git diff --staged`
* 简洁历史图：`git log --oneline --graph --decorate -n 30`
* 谁改了这行：`git blame <文件>`
* 在历史中搜文本：`git grep -n "关键词"`

## 纳入与提交

* 选择性加入：`git add -p`（按块挑）
* 全量加入：`git add -A`
* 提交：`git commit -m "说明"`
* 修补上一次提交：`git commit --amend`（可配合 `--no-edit`）
* 修复型提交（配合 autosquash）：`git commit --fixup <提交哈希>` → `git rebase -i --autosquash`

## 撤销与恢复（按破坏性从低到高）

* 丢弃未暂存改动：`git restore <文件>`
* 从暂存区撤回：`git restore --staged <文件>`
* 回到某快照但保留改动：`git reset --soft <提交>`
* 回到某快照并重置暂存区：`git reset <提交>`（或 `--mixed`，默认）
* 回到某快照并清理工作区：`git reset --hard <提交>`（危险）
* 公开历史回滚：`git revert <提交>`（生成反向提交）
* 清理未跟踪文件：`git clean -fd`（谨慎）

## 暂存抽屉（stash）

* 收起当前改动（含未跟踪）：`git stash push -u -m "说明"`
* 列表：`git stash list`
* 查看差异：`git stash show -p stash@{0}`
* 取回并删除：`git stash pop`（或保留：`git stash apply`）
* 删除某条：`git stash drop stash@{0}`

## 分支

* 新建并切换：`git switch -c feature/x`
* 切换：`git switch main`
* 重命名：`git branch -m old new`
* 删除：`git branch -d feature/x`（强制 `-D`）
* 查看跟踪关系：`git branch -vv`

## 合并与变基

* 只允许快进合并（无合并提交）：`git merge --ff-only other`
* 常规合并：`git merge other` → 解决冲突 → `git add` → `git commit`
* 变基让历史变直：`git rebase other` → 冲突后 `git rebase --continue/--abort/--skip`
* 交互式整理历史：`git rebase -i <基底>`（重排/合并/改消息）

## 精准搬运

* 拣选某提交：`git cherry-pick <提交>`（失败用 `--continue/--abort`）
* 保留来源信息：`git cherry-pick -x <提交>`

$1**从仓库拉取（常用）**

* 初次克隆：`git clone <url>`（建议用 SSH）

* 指定目录名：`git clone <url> <目录>`

* 日常更新：`git fetch origin --prune` → `git pull --rebase`（避免合并提交）

* 仅快进对齐主分支：`git merge --ff-only origin/main`

* 切到主分支再更新：`git switch main` → `git pull --rebase`

* 查看远端：`git remote -v`

* 增加远端：`git remote add origin <url>`

* 改远端 URL（切 SSH）：`git remote set-url origin git@github.com:org/repo.git`

* 拉远端引用：`git fetch origin --prune`

* 只快进对齐主分支：`git merge --ff-only origin/main`

* 首次推送并建立跟踪：`git push -u origin HEAD`

* 拉取并重放本地提交：`git pull --rebase`

* 安全强推（有他人更新就拒绝）：`git push --force-with-lease`

## 标签（版本标记）

* 轻量标签：`git tag v1.2.3`
* 带注解：`git tag -a v1.2.3 -m "说明"`
* 推送单个标签：`git push origin v1.2.3`
* 推送全部标签：`git push --tags`
* 删除本地/远端：`git tag -d v1.2.3` / `git push origin :refs/tags/v1.2.3`

## 定位与排错

* 找回“丢失”的提交：`git reflog` → `git reset --hard <哈希>`
* 二分定位坏提交：`git bisect start` → `git bisect bad` → `git bisect good <哈希>` → 反复到结论 → `git bisect reset`
* 仓库体检：`git fsck`
* 网络抓包日志：`GIT_CURL_VERBOSE=1 git fetch origin`

## 性能与体积

* 打包与清理：`git gc`
* 浅克隆：`git clone --depth 1 <url>`
* 局部检出：`git sparse-checkout set <路径>`（需 `git sparse-checkout init`）
* 只拉元数据：`git clone --filter=blob:none <url>`

## 子模块 / 子树（外部仓库集成）

* 子模块克隆：`git clone --recursive <url>` 或 `git submodule update --init --recursive`
* 添加子模块：`git submodule add <url> <路径>`
* 子树拉取：`git subtree add --prefix=<路径> <url> <分支> --squash`

## 常用别名（建议）

将以下写入 `~/.gitconfig`：

```ini
[alias]
  lg = log --oneline --graph --decorate --all
  st = status -sb
  co = switch
  cob = switch -c
  rb = rebase
  cp = cherry-pick
```

## Windows/PowerShell 贴士

* 旧版 PowerShell 不支持 `||`。改用：`git merge --abort; if ($LASTEXITCODE -ne 0) { git reset --merge }`
* HTTPS 断流：`git config --global http.version HTTP/1.1` 或换 SSH。
* 代理：`git config --global http.proxy http://127.0.0.1:7890`；取消：`git config --global --unset http.proxy`

## 团队硬规（推荐）

* 主干受保护且只快进：合入用 `--ff-only` 或 squash 合并。
* 个人分支本地保持 `rebase` 线性，PR 后合并。
* 线上回滚优先 `revert`，避免公共分支 `reset --hard`。
* 合并前保持工作区干净：用 `stash` 或临时提交。
