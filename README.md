# Local Python Environment Setup

```bash

brew install direnv  # install direnv (if not installed)
echo 'eval "$(direnv hook zsh)"' >> ~/.zshrc && source ~/.zshrc  # enable direnv in Zsh if not already so

# Pull the repo, navigate to the folder
direnv allow .  # allow direnv to auto-activate venv
pip install -r requirements.txt  # install dependencies
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

## (re)Install Dependencies

```sh
pip install pandas
```

To save installed packages for future use:

```sh
pip freeze > requirements.txt
```

To reinstall packages later, activate the environment and run:

```sh
pip install -r requirements.txt
```
