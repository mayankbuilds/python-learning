# Useful Python & Git Commands

## 1. Python Version

Check Python:

```bash
python --version
```

or:

```bash
python3 --version
```

Find Python executable:

```bash
which python
```

Check pip:

```bash
pip --version
```

------------------------------------------------------------
## 2. Running Python
------------------------------------------------------------

Run a Python file:

```bash
python main.py
```

Run Python interactively:

```bash
python
```

Exit the interpreter:

```python
exit()
```

or press:

```text
Ctrl+D
```

Run a module:

```bash
python -m module_name
```

------------------------------------------------------------
## 3. Virtual Environment Commands
------------------------------------------------------------

Create:

```bash
python -m venv .venv
```

Activate on Linux/macOS:

```bash
source .venv/bin/activate
```

Check active Python:

```bash
which python
```

Deactivate:

```bash
deactivate
```

------------------------------------------------------------
## 4. pip Commands
------------------------------------------------------------

Install package:

```bash
pip install package_name
```

Install a specific version:

```bash
pip install package_name==1.2.3
```

Upgrade package:

```bash
pip install --upgrade package_name
```

Uninstall:

```bash
pip uninstall package_name
```

List packages:

```bash
pip list
```

Show package details:

```bash
pip show package_name
```

Save dependencies:

```bash
pip freeze > requirements.txt
```

Install project dependencies:

```bash
pip install -r requirements.txt
```

------------------------------------------------------------
## 5. Linux Navigation
------------------------------------------------------------

Show current directory:

```bash
pwd
```

List files:

```bash
ls
```

Detailed list:

```bash
ls -la
```

Change directory:

```bash
cd directory
```

Go up one directory:

```bash
cd ..
```

Go to home:

```bash
cd ~
```

Create directory:

```bash
mkdir directory
```

Create nested directories:

```bash
mkdir -p path/to/directory
```

Create a file:

```bash
touch file.py
```

Remove a file:

```bash
rm file.py
```

Remove an empty directory:

```bash
rmdir directory
```

Remove directory recursively:

```bash
rm -r directory
```

Be careful with `rm -r`.

------------------------------------------------------------
## 6. Useful File Commands
------------------------------------------------------------

Show file contents:

```bash
cat file.txt
```

Read a long file:

```bash
less file.txt
```

Search text:

```bash
grep "pattern" file.txt
```

Find files:

```bash
find . -name "file.py"
```

Find Python files:

```bash
find . -name "*.py"
```

Count lines/words/bytes:

```bash
wc file.txt
```

------------------------------------------------------------
## 7. Git Basics
------------------------------------------------------------

Check repository status:

```bash
git status
```

Initialize repository:

```bash
git init
```

Add a file:

```bash
git add file.py
```

Add everything:

```bash
git add .
```

Commit:

```bash
git commit -m "message"
```

View commits:

```bash
git log
```

Compact log:

```bash
git log --oneline
```

Show remotes:

```bash
git remote -v
```

------------------------------------------------------------
## 8. Git Branches
------------------------------------------------------------

Show branches:

```bash
git branch
```

Create branch:

```bash
git branch branch-name
```

Switch branch:

```bash
git switch branch-name
```

Create and switch:

```bash
git switch -c branch-name
```

------------------------------------------------------------
## 9. GitHub / Remote
------------------------------------------------------------

Add remote:

```bash
git remote add origin <repository-url>
```

Push current branch:

```bash
git push -u origin main
```

Pull changes:

```bash
git pull
```

Fetch remote changes:

```bash
git fetch
```

Clone repository:

```bash
git clone <repository-url>
```

------------------------------------------------------------
## 10. Useful Git Inspection
------------------------------------------------------------

Show changes:

```bash
git diff
```

Show staged changes:

```bash
git diff --cached
```

Show commit:

```bash
git show
```

Show tracked files:

```bash
git ls-files
```

------------------------------------------------------------
## 11. Git Undo Basics
------------------------------------------------------------

Unstage a file:

```bash
git restore --staged file.py
```

Discard changes in a working file:

```bash
git restore file.py
```

Be careful: `git restore file.py` discards uncommitted changes to that file.

------------------------------------------------------------
## 12. Project Setup
------------------------------------------------------------

Typical Python project setup:

```bash
mkdir my-project
cd my-project

python -m venv .venv
source .venv/bin/activate

touch main.py
touch requirements.txt
touch .gitignore

git init
```

Example `.gitignore`:

```text
.venv/
__pycache__/
*.py[cod]
.env
.env.*
.vscode/
.idea/
.pytest_cache/
.coverage
htmlcov/
.ipynb_checkpoints/
```

------------------------------------------------------------
## 13. Running a Project
------------------------------------------------------------

Activate environment:

```bash
source .venv/bin/activate
```

Run program:

```bash
python main.py
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Deactivate when finished:

```bash
deactivate
```

------------------------------------------------------------
## 14. Useful Python Module Commands
------------------------------------------------------------

Run a module:

```bash
python -m module_name
```

Run pip through the current Python interpreter:

```bash
python -m pip install package_name
```

This can be useful when you want to make sure `pip` belongs to the same Python installation/environment.

Check installed Python packages:

```bash
python -m pip list
```

------------------------------------------------------------
## 15. Environment Variables
------------------------------------------------------------

Set temporarily in the current shell:

```bash
export API_KEY="secret"
```

View:

```bash
echo $API_KEY
```

Python:

```python
import os

api_key = os.getenv("API_KEY")
```

Do not commit secrets.

------------------------------------------------------------
## 16. Finding Python Project Files
------------------------------------------------------------

Find all Python files:

```bash
find . -type f -name "*.py"
```

Find all Markdown files:

```bash
find . -type f -name "*.md"
```

Find empty directories:

```bash
find . -type d -empty
```

Create `.gitkeep` in empty directories:

```bash
find . -type d -empty -exec touch {}/.gitkeep \;
```

------------------------------------------------------------
## 17. Useful Terminal Shortcuts
------------------------------------------------------------

```text
Ctrl+C  -> stop running command/program
Ctrl+D  -> exit shell/Python prompt in many contexts
Ctrl+L  -> clear terminal screen
Tab     -> autocomplete
Up/Down -> command history
```

------------------------------------------------------------
## 18. Recommended Daily Workflow
------------------------------------------------------------

```bash
cd /path/to/project

source .venv/bin/activate

git status

python main.py

git status
git add .
git commit -m "describe the change"
git push
```

Deactivate when done:

```bash
deactivate
```

------------------------------------------------------------
## 19. Quick Command Reference
------------------------------------------------------------

```bash
# Python
python --version
python main.py
python -m pip list

# Virtual environment
python -m venv .venv
source .venv/bin/activate
deactivate

# pip
pip install package
pip uninstall package
pip list
pip freeze > requirements.txt
pip install -r requirements.txt

# Linux
pwd
ls -la
cd ..
mkdir -p directory
touch file
find . -name "*.py"

# Git
git status
git add .
git commit -m "message"
git log --oneline
git pull
git push
```