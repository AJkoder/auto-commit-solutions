"""
git_committer.py
-----------------
Takes a list of new solution files and auto-commits + pushes them to GitHub.
Uses subprocess to run git commands — standard Python from Phase 1!
"""

import subprocess
import logging
import os
from datetime import datetime

logging.basicConfig(
    filename="logs/git.log",
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s"
)


def run_git(args, cwd=None):
    """Run a git command and return output. Raises on failure."""
    cmd = ["git"] + args
    result = subprocess.run(
        cmd,
        cwd=cwd or os.getcwd(),
        capture_output=True,
        text=True
    )
    if result.returncode != 0:
        raise Exception(f"Git error: {result.stderr.strip()}")
    return result.stdout.strip()


def commit_and_push(new_files):
    """
    Stage all new files, make a descriptive commit, and push to origin/main.
    
    Args:
        new_files: list of file paths that were just saved
    """
    if not new_files:
        print("No files to commit.")
        return

    print(f"\nCommitting {len(new_files)} new solution(s) to Git...")

    try:
        # 1. Stage all new/modified files in solutions/
        run_git(["add", "solutions/"])
        logging.info(f"Staged: {new_files}")

        # 2. Build a meaningful commit message
        today = datetime.now().strftime("%Y-%m-%d")
        if len(new_files) == 1:
            # Extract problem name from path for a nice message
            # e.g. solutions/leetcode/two-sum/solution.py → "two-sum"
            parts = new_files[0].replace("\\", "/").split("/")
            problem = parts[2] if len(parts) >= 3 else "solution"
            platform = parts[1] if len(parts) >= 2 else "platform"
            msg = f"[{today}] Solved: {problem} ({platform})"
        else:
            platforms = set()
            for f in new_files:
                parts = f.replace("\\", "/").split("/")
                if len(parts) >= 2:
                    platforms.add(parts[1])
            msg = f"[{today}] Added {len(new_files)} solutions ({', '.join(platforms)})"

        # 3. Commit
        run_git(["commit", "-m", msg])
        print(f" Committed: {msg}")
        logging.info(f"Committed: {msg}")

        # 4. Push to remote
        run_git(["push", "origin", "main"])
        print("Pushed to GitHub!")
        logging.info("Pushed to origin/main")

    except Exception as e:
        logging.error(f"Git operation failed: {e}")
        print(f"Git error: {e}")
        print("Tip: Make sure git remote is set up and you have push access.")
