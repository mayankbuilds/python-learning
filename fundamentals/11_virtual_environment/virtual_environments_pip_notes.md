# Virtual Environments & pip

## 1. Why Virtual Environments?

A **virtual environment (venv)** creates an isolated Python environment for a project.

Different projects may need different package versions. A virtual environment prevents those dependencies from interfering with each other.

Mental model:

```text
Project A
  └── .venv
      └── its dependencies

Project B
  └── .venv
      └── its dependencies
```

This keeps project dependencies isolated.

---

## 2. Creating a Virtual Environment

Inside the project directory:

```bash
python -m venv .venv
```

This creates a virtual environment named `.venv`.

Common convention:

```text
project/
├── .venv/
├── main.py
└── requirements.txt
```

The `.venv` directory should normally be excluded from Git.

Example `.gitignore`:

```text
.venv/
```

---

## 3. Activating the Virtual Environment

On Linux/macOS:

```bash
source .venv/bin/activate
```

After activation, the terminal usually shows the environment name:

```text
(.venv)
```

This means commands such as `python` and `pip` are using the virtual environment.

---

## 4. Installing Packages with pip

`pip` is used to install and manage Python packages.

Example:

```bash
pip install requests
```

You can install multiple packages:

```bash
pip install requests fastapi
```

After installation, those packages are available inside the active virtual environment.

---

## 5. Checking Installed Packages

Use:

```bash
pip list
```

This displays packages installed in the current environment.

You can also inspect package information:

```bash
pip show requests
```

---

## 6. `requirements.txt`

A `requirements.txt` file records the Python package dependencies required by a project.

Example:

```text
requests==2.32.5
fastapi==0.116.1
```

A project's dependencies can then be installed with:

```bash
pip install -r requirements.txt
```

This makes it easier to recreate the project's environment.

---

## 7. Creating `requirements.txt`

A common command is:

```bash
pip freeze > requirements.txt
```

This writes the packages installed in the current environment to `requirements.txt`.

Example:

```bash
pip freeze > requirements.txt
```

Then another environment can install them with:

```bash
pip install -r requirements.txt
```

---

## 8. Deactivating the Environment

When finished working:

```bash
deactivate
```

This leaves the virtual environment.

The `.venv` directory still exists and can be activated again later.

---

## 9. Typical Workflow

A common project workflow is:

```bash
mkdir my-project
cd my-project

python -m venv .venv
source .venv/bin/activate

pip install requests

pip freeze > requirements.txt
```

Later, after cloning the project:

```bash
cd my-project

python -m venv .venv
source .venv/bin/activate

pip install -r requirements.txt
```

---

## 10. Why This Matters for Projects

Without virtual environments, packages installed globally can affect multiple projects.

For example:

```text
Project A needs requests version X
Project B needs requests version Y
```

A separate virtual environment allows each project to maintain its own dependencies.

This is especially important for backend and AI/ML projects where dependencies can become numerous.

---

## 11. Environment Variables

Project configuration and secrets should not normally be hardcoded in source code.

Examples:

```text
DATABASE_URL
API_KEY
SECRET_KEY
```

These can be stored as environment variables.

Example:

```bash
export API_KEY="your-secret"
```

Python can read environment variables using:

```python
import os

api_key = os.getenv("API_KEY")
```

Do **not** commit secrets to Git.

A `.env` file is commonly used for local development, and it should normally be added to `.gitignore`:

```text
.env
```

---

## 12. Important Commands

### Create environment

```bash
python -m venv .venv
```

### Activate on Linux/macOS

```bash
source .venv/bin/activate
```

### Install package

```bash
pip install package_name
```

### List packages

```bash
pip list
```

### Save dependencies

```bash
pip freeze > requirements.txt
```

### Install dependencies

```bash
pip install -r requirements.txt
```

### Deactivate

```bash
deactivate
```

---

## 13. Common Mistakes

### Mistake 1: Installing packages outside the venv

Before installing project dependencies, make sure the virtual environment is activated.

Check the terminal for:

```text
(.venv)
```

---

### Mistake 2: Committing `.venv`

Do not normally commit the entire virtual environment to Git.

Use:

```text
.venv/
```

in `.gitignore`.

---

### Mistake 3: Committing secrets

Never commit API keys, passwords, or secret keys.

Use environment variables and ignore local `.env` files.

---

### Mistake 4: Forgetting `requirements.txt`

If a project depends on external packages, record those dependencies so the environment can be recreated.

---

## 14. Quick Revision

| Concept | Meaning |
|---|---|
| Virtual environment | Isolated Python environment for a project |
| `venv` | Python's built-in tool for creating virtual environments |
| `pip` | Tool for installing/managing Python packages |
| `.venv` | Common name for the project's virtual environment |
| `requirements.txt` | Records project Python dependencies |
| `pip freeze` | Lists installed packages/versions |
| `activate` | Switches terminal into the virtual environment |
| `deactivate` | Leaves the virtual environment |
| Environment variable | External configuration/value such as an API key |

## Checklist

- [x] Why virtual environments are used
- [x] Creating `.venv`
- [x] Activating `.venv`
- [x] Installing packages with pip
- [x] Checking installed packages
- [x] `requirements.txt`
- [x] `pip freeze`
- [x] Installing from requirements
- [x] Deactivating
- [x] Environment variables and secrets
- [x] Common mistakes
