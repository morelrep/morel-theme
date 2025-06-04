Got it! Let’s go step by step with explicit examples, making it crystal clear when we’re working in the **main repository** and when we’re dealing with the **submodule**.

---

## **Step 1: Create a Main Repository**
First, let’s set up a **main repository** where we will add a submodule.

```bash
mkdir main-repo
cd main-repo
git init
echo "This is the main repo" > README.md
git add README.md
git commit -m "Initial commit in main repository"
```
Now we have a **main Git repository** initialized.

---

## **Step 2: Create a Separate Repository for the Submodule**
A Git submodule is just another Git repository. Let’s create one that we’ll later add to the **main-repo**.

```bash
cd ..
mkdir submodule-repo
cd submodule-repo
git init
echo "This is the submodule" > submodule.txt
git add submodule.txt
git commit -m "Initial commit in submodule"
```

Now we have a **submodule repository** that we will include inside the **main repository**.

> **Important:** Normally, the submodule repository would be hosted on GitHub or another Git server, but for simplicity, we’re keeping it local.

---

## **Step 3: Add the Submodule to the Main Repository**
Now, we go back to the **main repository** and add the **submodule** inside it.

```bash
cd ../main-repo
git submodule add ../submodule-repo submodules/my-submodule
git commit -m "Added submodule"
```

### **What Just Happened?**
- We added `submodule-repo` inside `main-repo` at `submodules/my-submodule`.
- This means our **main repository now tracks the submodule as a reference to a specific commit**.
- The submodule appears as a separate repository inside the main repository.

---

## **Step 4: Cloning a Repository with a Submodule**
If someone else clones the `main-repo`, they will **not** automatically get the submodule. They need to do:

```bash
git clone --recurse-submodules <repo-url>
```

If they forget `--recurse-submodules`, they will only get an empty folder where the submodule should be. In that case, they can run:

```bash
git submodule update --init --recursive
```

---

## **Step 5: Making Changes in the Submodule**
If we want to update the **submodule-repo**, we need to go inside it:

```bash
cd submodules/my-submodule
echo "Another line in the submodule" >> submodule.txt
git add submodule.txt
git commit -m "Updated submodule content"
git push origin main  # (If it's hosted remotely)
```

Now, we have updated the **submodule repository**.

---

## **Step 6: Updating the Submodule Reference in the Main Repository**
Even though we updated the **submodule**, the **main repository does not know about it yet**. We must tell it that the submodule reference has changed:

```bash
cd ../
git add submodules/my-submodule
git commit -m "Updated submodule reference"
git push origin main
```

Now, anyone who pulls the **main repository** will get the latest submodule reference.

---

## **Step 7: Updating the Submodule in Another Clone**
If someone else has already cloned the **main-repo**, they won’t automatically see the new submodule update. They need to run:

```bash
git submodule update --remote --merge
```

---

## **Step 8: Removing a Submodule**
If we no longer want the submodule, we need to remove it properly:

1. **Unregister the submodule:**
   ```bash
   git submodule deinit -f submodules/my-submodule
   ```

2. **Remove the submodule files:**
   ```bash
   rm -rf submodules/my-submodule
   rm -rf .git/modules/submodules/my-submodule
   ```

3. **Commit the removal:**
   ```bash
   git rm -f submodules/my-submodule
   git commit -m "Removed submodule"
   ```

Now, the submodule is completely gone from the **main repository**.

---

### **Final Summary**
| Action | Command | Where? |
|---------|---------|---------|
| Initialize a main repository | `git init` | In `main-repo` |
| Initialize a submodule repository | `git init` | In `submodule-repo` |
| Add a submodule to main repository | `git submodule add <repo-url> <path>` | In `main-repo` |
| Clone a repo with submodules | `git clone --recurse-submodules <repo-url>` | Anywhere |
| Initialize submodules after cloning | `git submodule update --init --recursive` | In `main-repo` |
| Update a submodule | `git submodule update --remote --merge` | In `main-repo` |
| Remove a submodule | `git submodule deinit -f <path>` + `rm -rf <path>` | In `main-repo` |

Would you like me to explain anything in more detail?