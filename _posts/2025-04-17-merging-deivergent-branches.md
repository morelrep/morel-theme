### ✅ PRE-MERGE SAFETY (BACKUP & PREP)
- **Check status of local `main`** before doing anything:
```bash
  git status
```
- **Create a backup branch of `main`** before doing anything:
  ```bash
  git checkout main
  git pull origin main # Only if main is not up to date with origin
  git checkout -b backup-main-before-merge
  ```
- **Create a backup of the feature branch too**, just in case:
  ```bash
  git checkout your-feature-branch
  git checkout -b feature-backup
  ```

### 📥 BRING FEATURE BRANCH UP TO DATE
- **Merge `main` into your branch first** to resolve conflicts there:
  ```bash
  git checkout your-feature-branch
  git pull origin main
  ```
- Resolve conflicts if any → test locally → commit merge.

### 🔀 MERGE INTO MAIN (CLEANLY)
- **Switch to `main` and merge** the updated feature branch:
  ```bash
  git checkout main
  git merge your-feature-branch
  ```

### 🔍 FILE CHECK / CLEANUP
- **Check for untracked or orphan files/folders**:
  ```bash
  git status
  git clean -fdn  # Dry run — shows what would be deleted
  git clean -fd   # Actual cleanup (use with caution)
  ```

### 💥 IF THINGS GO WRONG
- **Reset `main` to the backup if needed**:
  ```bash
  git checkout main
  git reset --hard backup-main-before-merge
  git push origin main --force  # only if already pushed
  ```

### 🧼 OPTIONAL: DELETE BACKUP BRANCHES AFTER SUCCESS
- Once confident:
  ```bash
  git branch -d backup-main-before-merge
  git branch -d feature-backup
  ```
