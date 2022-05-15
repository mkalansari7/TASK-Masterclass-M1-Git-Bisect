# Task

This project has a regression, and we want to haunt that regression down! The app should be able to work just by doing `python main.py`.

## Steps

1. Fork and clone [this repository](https://github.com/JoinCODED/TASK-Masterclass-M1-Git-Bisect).
2. Create a `virtual` environment using `python3 -m venv .venv`.
3. Activate the environment.
4. Install the requirements using `pip install -r requirements.lock`
5. Use `git bisect` to haunt down the regression.
   - Use `git log` to see the first occurrence of a good commit and bad commit.
   - Pin down the exact commit with the issue, and fix it.
