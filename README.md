# Auto-Commit Solutions

Automatically saves your accepted LeetCode submissions to GitHub. Solve a problem, and within 10 minutes it's committed — no manual effort.

---

## How it works

Every 10 minutes the script checks your LeetCode account for new accepted submissions, saves the solution as a file, and pushes it to GitHub automatically.

---

## Setup

**1. Install dependencies**
```bash
pip install requests
```

**2. Fill in config.json**
```json
{
  "leetcode": {
    "username": "your_username",
    "session_cookie": "paste_your_LEETCODE_SESSION_cookie_here"
  }
}
```

To get your session cookie — log into leetcode.com → F12 → Application tab → Cookies → copy the value of `LEETCODE_SESSION`

**3. Add config.json to .gitignore**
```bash
echo "config.json" >> .gitignore
echo "logs/" >> .gitignore
echo "__pycache__/" >> .gitignore
```

**4. Run manually to test**
```bash
python main.py
```

---

## Auto-run setup (Windows)

Uses Windows Task Scheduler to run every 10 minutes in the background.

- Program: `C:\path\to\project\venv\Scripts\python.exe`
- Arguments: `main.py`
- Start in: `C:\path\to\project`

---

## Usage

```bash
python main.py                # run normally
python main.py --no-push      # save files but don't push to GitHub
```

---

## Tech used

Python — `requests`, `subprocess`, `argparse`, `logging`, `json`, `os`

LeetCode GraphQL API · Git · Windows Task Scheduler

---

## Project structure

```
auto-commit-solutions/
├── main.py
├── leetcode_fetcher.py
├── git_committer.py
├── config.json              ← never commit this
└── solutions/
    └── leetcode/
        ├── two-sum.py
        └── jump-game.py
```
