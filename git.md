````markdown
# Git 最小指令清单（可直接复制）
> 约定：PowerShell 逐行执行；远端 `origin` 走 SSH（`git@github.com:...`）；占位符用 `<...>`。

---

## 0. 首次克隆（一次性）
```powershell
git clone <ssh_repo_url>
cd <repo_dir>
````

---

## 1. 从远端拉取（同步到最新）

```powershell
git switch main
git pull --rebase
```

> 如果你维护的是 fork，需要对齐上游 `upstream`：

```powershell
git fetch upstream --prune
git switch main
git rebase upstream/main
```

---

## 2. 本地上传（提交并推送）

### 新增或修改文件

```powershell
git add -A
git commit -m "<提交说明>"
git push
```

### 仅修改已跟踪文件（少一步）

```powershell
git commit -am "<提交说明>"
git push
```

---

## 3. 分支开发（推荐）

```powershell
git switch main
git pull --rebase
git switch -c feature/<任务>      # 首次创建；之后用：git switch feature/<任务>
git add -A
git commit -m "<提交说明>"
git push -u origin HEAD           # 首次推送建立跟踪
```

### 分支期间保持与主干同步

```powershell
git fetch origin --prune
git rebase origin/main
git push --force-with-lease
```

---

## 4. 常见阻塞的最短解

### 提示 non-fast-forward（远端比你新）

```powershell
git fetch origin --prune
git rebase origin/main
git push --force-with-lease
```

### 变基或合并出现冲突

```powershell
# 按提示编辑冲突文件，保留你要的版本
git add -A
git rebase --continue      # 如果是合并流程：git merge --continue
```

---

## 5. 远端检查与切换为 SSH（必要时）

```powershell
git remote -v
git remote set-url origin git@github.com:<owner>/<repo>.git
```

> fork 场景（可选）：

```powershell
git remote add upstream git@github.com:<upstream_owner>/<repo>.git
```

```
```
