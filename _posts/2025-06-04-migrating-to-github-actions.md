### ⚙️ Step-by-Step Modular GitHub Actions Setup

#### ✅ **Step 1 – Trigger detection**

Create a workflow that **does nothing yet**, just detects when `books_zotero.csv` is uploaded or updated in a specific path (e.g. `assets/data/`).

#### 🛠 **Step 2 – Run `morel-generate.py`**

Create a second workflow or a job that runs the Python generation script when the trigger is detected.

#### 💾 **Step 3 – Commit output**

Only if generation succeeds, this job commits generated content to the repo (`_books`, `_authors`, etc.)

#### 🌍 **Step 4 – Deploy to GitHub Pages**

Let GitHub Pages do its thing if you’re deploying from `main`, or explicitly trigger deploy from `gh-pages`.

---

We’ll start with **Step 1**, so you can test your assumptions.

### 🔧 Step 1: Create `.github/workflows/trigger-check.yml`

This minimal workflow will just echo a message when `books_zotero.csv` changes:

```yaml
name: Step 1 – Trigger detection

on:
  push:
    paths:
      - 'assets/data/books_zotero.csv'

jobs:
  echo-update:
    runs-on: ubuntu-latest
    steps:
      - name: Checkout code
        uses: actions/checkout@v4

      - name: Echo change
        run: echo "books_zotero.csv was updated!"
```
---
Great catch. GitHub **does not** come with your Python environment or your required packages pre-installed. That first test (Step 1) doesn’t run Python yet, so we’re fine for now—but you’re 100% right that when we get to **Step 2**, we’ll need to:

1. **Set up the right Python version**
2. **Install dependencies** (e.g., `clevercsv`, `slugify`, `pandas`, etc.)
3. Then run your `morel-generate.py`

So just to be super clear:

---

### ✅ Step 1 (trigger-only)

* Just detects changes to `books_zotero.csv`
* Doesn't need Python yet

---

### 🧪 Step 2 (generate)

We’ll add something like this to the YAML:

```yaml
- name: Set up Python
  uses: actions/setup-python@v5
  with:
    python-version: '3.10'

- name: Install dependencies
  run: |
    pip install -r requirements.txt
```
---

## Note: on ´run´ and ´| run´

### 🔠 `run:` vs `run: |`

#### ✅ `run: <command>`

Use this when you're writing **a single-line command**:

```yaml
- name: Say hello
  run: echo "Hello, world"
```

#### ✅ `run: |`

Use this when you need to run **multiple commands** (a multiline script block):

```yaml
- name: Install and run
  run: |
    pip install pandas
    pip install clevercsv
    python src/morel-generate.py
```

The `|` is YAML’s way of saying “the following block is a **literal multiline string**.” So GitHub Actions will treat everything indented beneath it as part of one shell script.

### 🔁 In short:

| Syntax | Use for…  |                   |
| ------ | --------- | ----------------- |
| `run:` | One-liner |                   |
| \`run: | \`        | Multiple commands |

No need to overthink it—just use `|` whenever you’re chaining commands like `install`, `build`, and `run`.

---

## Equivalences ##

| **Step Description**                  | **Local Mode (Command Line)**                               | **GitHub Actions Mode (Online)**                                                              |
| ------------------------------------- | ----------------------------------------------------------- | --------------------------------------------------------------------------------------------- |
| 1. Prepare the repository             | Fork + `git clone` on your computer                         | Fork via GitHub UI (no clone needed)                                                          |
| 2. Place data in correct folder       | Manually move `books_zotero.csv` to `assets/data/`          | Upload `books_zotero.csv` via GitHub web interface to `assets/data/`                          |
| 3. Install dependencies               | Run `bundle install`, `pip install`, etc. locally           | GitHub Actions installs Python and packages (`pip install clevercsv pandas slugify ...`)      |
| 4. Generate the site content          | Run `python src/morel-generate.py` (and supporting scripts) | GitHub Actions automatically runs `src/morel-generate.py` when `books_zotero.csv` changes     |
| 5. View/test the result               | Run `ruby serve-local.rb` locally to preview                | (Optional) Use a preview branch or PR; or skip to auto-publish to `main`                      |
| 6. Commit the output                  | `git add .` → `git commit` → `git push`                     | GitHub Actions commits generated files automatically to the repo                              |
| 7. Publish the website                | GitHub Pages deploys from `main` or `gh-pages` after push   | GitHub Actions triggers GitHub Pages deploy automatically after committing output             |
| 8. Clean old content (optional)       | Run cleanup script manually                                 | GitHub Actions runs `cleanup_output.py` as part of the workflow                               |
| 9. Create downloadable zip (optional) | Run `compress_output.py` and send zip manually              | GitHub Actions creates `output.zip` and attaches to workflow or publishes as release/download |

Great question—and here's the key:

---

### In Online Mode (GitHub Actions), you **don’t need** `bundle install` **at all**… unless you're using **Ruby-based tools** during the workflow.

---

#### In your local setup:

You use:

```bash
bundle install
```

…to install Jekyll and other Ruby dependencies needed to serve the site **locally** (`ruby serve-local.rb`).

#### In GitHub Actions:

GitHub Pages already **builds the Jekyll site automatically** using its built-in environment. So unless your GitHub Actions workflow includes **custom Ruby steps** (like running Jekyll manually, e.g. `bundle exec jekyll build`), you can skip `bundle install`.

---

### 🧾 So in the table:

| **Step Description**     | **Local Mode (Command Line)** | **GitHub Actions Mode (Online)**                                     |
| ------------------------ | ----------------------------- | -------------------------------------------------------------------- |
| Install Ruby/Jekyll deps | `bundle install`              | **Not needed** – GitHub Pages runs Jekyll natively during deployment |

---

If at some point you **do** want to run Jekyll manually inside GitHub Actions (e.g. to build the site before committing), then you'd add:

```yaml
- name: Setup Ruby
  uses: ruby/setup-ruby@v1
  with:
    ruby-version: '3.1'

- name: Install Jekyll dependencies
  run: bundle install
```

But for now, your current workflow *doesn’t require it*—you only need Python for generation, and GitHub Pages handles the rest.

However, given the current `Test Jekyll Build` workflow you pasted, yes: **you are indeed using `bundle install` in the online mode**, because you're running **Jekyll manually** inside GitHub Actions rather than relying on GitHub Pages’ native build.

So to revise and clarify:

---

### ✅ In *your current GitHub Actions setup*, the `bundle install` step **does exist**, because:

1. You're using `ruby/setup-ruby` to install Ruby
2. You're installing gems manually:

   ```yaml
   gem install bundler
   bundle install
   ```
3. You're manually building the site with:

   ```yaml
   bundle exec jekyll build
   ```

This gives you **more control** over the Jekyll build (e.g., useful if you're using custom plugins not supported by GitHub Pages' native builder).

---

### 📝 So the table now reads:

| **Step Description**     | **Local Mode (Command Line)** | **GitHub Actions Mode (Online)**         |
| ------------------------ | ----------------------------- | ---------------------------------------- |
| Install Ruby/Jekyll deps | `bundle install`              | `gem install bundler` + `bundle install` |

If in the future you decide to go *back* to GitHub Pages’ built-in Jekyll engine (using Pages from `main` or `gh-pages`), you could remove those Ruby steps. But right now, you’re doing it fully manually—and that’s a solid choice for flexibility.

---

Perfect. Here’s the updated, final version of the table with **Step 9 (Create downloadable zip)** removed:

---

### ✅ Clean Final Table – Local vs. GitHub Actions (Aligned with Your Docs)

| **Step (based on current docs)**   | **Local Mode (Command Line)**                 | **GitHub Actions Mode (Online)**                                                 |
| ---------------------------------- | --------------------------------------------- | -------------------------------------------------------------------------------- |
| 1. Fork the repository             | Fork on GitHub and `git clone`                | Fork via GitHub web interface only                                               |
| 2. Open terminal in working folder | (User opens terminal)                         | N/A                                                                              |
| 3. Clone the repository            | `git clone`                                   | N/A                                                                              |
| 4. Navigate into folder            | `cd morel-theme-generator`                    | N/A                                                                              |
| 5. Install Ruby dependencies       | `bundle install` (after installing Ruby)      | `gem install bundler` + `bundle install` (via GitHub Actions)                    |
| 6. Run the local server            | `ruby serve-local.rb`                         | (Skipped in online mode) GitHub Actions builds directly; no local preview needed |
| 7. Upload Zotero export            | Move `books_zotero.csv` to `assets/data/`     | Upload `books_zotero.csv` via GitHub web interface to `assets/data/`             |
| 8. Generate the site content       | Run `python src/morel-generate.py`            | GitHub Actions job runs `python src/morel-generate.py`                           |
| 9. Commit & push changes           | `git add`, `git commit`, `git push`           | GitHub Actions commits and pushes generated files                                |
| 10. Deploy to GitHub Pages         | GitHub auto-deploys from `main` or `gh-pages` | `peaceiris/actions-gh-pages@v3` handles deployment from `_site`
