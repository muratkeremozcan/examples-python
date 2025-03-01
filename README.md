# Local Python Environment Setup

```bash
brew install direnv  # install direnv (if not installed)
echo 'eval "$(direnv hook zsh)"' >> ~/.zshrc && source ~/.zshrc  # enable direnv in Zsh if not already so

# Pull the repo, navigate to the folder
direnv allow .  # allow direnv to auto-activate venv
pip install -r requirements.txt  # install dependencies

# lint, check syntax, and type-check
make all
```

## (Preferred) Auto-Activate the Virtual Environment with `direnv`

Instead of manually activating the virtual environment every time, you can use [`direnv`](https://direnv.net/) to **auto-activate** when you `cd` into the project and **auto-deactivate** when you leave.

### One time setup

<details><summary>Details </summary>

Install `direnv`

```bash
brew install direnv
```

Enable `direnv` in Zsh

Add the following line to your `~/.zshrc`:

```bash
eval "$(direnv hook zsh)"
```

Then, restart your terminal or run:

```bash
source ~/.zshrc
```

</details>

### One time setup in python project folders: enable auto-activation for the folder

Inside the folder of choice, create a `.envrc` file:

```
echo "source venv/bin/activate" > .envrc
```

Then, allow `direnv` to manage the environment:

```
direnv allow .
```

Now, every time you `cd` into the folder, the virtual environment will **automatically activate**. When you `cd` out, it will **automatically deactivate**!

If things do not work, do:

```bash
direnv allow .  # Make sure it's allowed
direnv reload   # Force reload if needed
# if still nothing
source venv/bin/activate
```

---

## (manual, not preferred) Create a Virtual Environment

<details>

```bash
python3 -m venv venv
```

Activate the Virtual Environment

```sh
source venv/bin/activate
```

### Deactivate the Virtual Environment

When done, exit the virtual environment:

```sh
deactivate
```

Now, every time you work in this folder, activate the virtual environment before running Python scripts.

```sh
source venv/bin/activate  # (Mac/Linux)
```

Then, run your Python code as usual!

</details>

---

## Managing Dependencies

To install a new package:

```sh
pip install package_name
```

To save all installed packages to requirements.txt (after adding new ones):

```sh
pip freeze > requirements.txt
```

To reinstall all packages from requirements.txt:

```sh
pip install -r requirements.txt
```
## Type Checking with mypy

This project uses mypy for static type checking. To run type checking:

```sh
# Run the type checker on the entire codebase
make type-check

# Run on a specific file
venv/bin/python -m mypy path/to/your/file.py
```

### Adding Type Annotations

Python type annotations (similar to TypeScript) help catch errors before runtime:

```python
# Example of type annotations
def greet(name: str) -> str:
    return f"Hello, {name}!"

# Type checking will catch this error
# bad_result = greet(123)  # Error: Expected str, got int
```

The mypy configuration is stored in `mypy.ini` at the project root.

## Code Quality Tools

This project includes several tools to ensure code quality:

### Linting with flake8

Flake8 checks for syntax errors and style issues:

```sh
# Run the linter on the entire codebase
make lint

# Run directly for more options
venv/bin/python -m flake8 path/to/your/file.py
```

### Syntax Checking

Verify that all Python files can be compiled:

```sh
# Check all Python files for syntax errors
make check
```

### All-in-One

Run all code quality checks with a single command:

```sh
make all
```

This will run the linter, syntax checker, and type checker in sequence.
