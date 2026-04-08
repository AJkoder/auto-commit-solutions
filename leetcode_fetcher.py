"""
leetcode_fetcher.py
--------------------
Fetches your latest ACCEPTED submissions from LeetCode
and saves them as files in the solutions/leetcode/ folder.

SETUP:
1. Log into leetcode.com in your browser
2. Open DevTools → Application → Cookies → copy 'LEETCODE_SESSION' value
3. Paste it in config.json (see README)
"""

import requests
import json
import os
import logging
from datetime import datetime

# ── Logging setup (you learned this in Phase 1!) ──────────────────────────────
logging.basicConfig(
    filename="logs/leetcode.log",
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s"
)

# ── Language → file extension map ─────────────────────────────────────────────
EXTENSIONS = {
    "python3": "py",
    "python": "py",
    "cpp": "cpp",
    "java": "java",
    "javascript": "js",
    "typescript": "ts",
    "c": "c",
    "go": "go",
    "rust": "rs",
    "kotlin": "kt",
    "swift": "swift",
    "scala": "scala",
    "ruby": "rb",
    "php": "php",
}

# ── GraphQL query to fetch recent accepted submissions ────────────────────────
GRAPHQL_QUERY = """
query recentAcSubmissions($username: String!, $limit: Int!) {
  recentAcSubmissionList(username: $username, limit: $limit) {
    id
    title
    titleSlug
    timestamp
    lang
  }
}
"""

# ── GraphQL query to fetch actual code of a submission ────────────────────────
SUBMISSION_DETAIL_QUERY = """
query submissionDetails($submissionId: Int!) {
  submissionDetails(submissionId: $submissionId) {
    code
    lang {
      name
    }
    question {
      title
      titleSlug
      difficulty
      topicTags {
        name
      }
    }
  }
}
"""


def load_config():
    """Load config.json which has your session cookie and username."""
    with open("config.json", "r") as f:
        return json.load(f)


def load_seen_ids():
    """Load the set of submission IDs we've already committed."""
    path = "logs/seen_leetcode.json"
    if os.path.exists(path):
        with open(path, "r") as f:
            return set(json.load(f))
    return set()


def save_seen_ids(seen_ids):
    """Save updated seen submission IDs."""
    with open("logs/seen_leetcode.json", "w") as f:
        json.dump(list(seen_ids), f)


def fetch_recent_accepted(username, session_cookie, limit=10):
    """Call LeetCode GraphQL API to get recent accepted submissions."""
    url = "https://leetcode.com/graphql"
    headers = {
        "Content-Type": "application/json",
        "Cookie": f"LEETCODE_SESSION={session_cookie}",
        "Referer": "https://leetcode.com",
        "User-Agent": "Mozilla/5.0",
        "x-csrftoken": "none",  # required header
    }
    payload = {
        "query": GRAPHQL_QUERY,
        "variables": {"username": username, "limit": limit}
    }

    response = requests.post(url, json=payload, headers=headers)
    response.raise_for_status()
    data = response.json()
    return data["data"]["recentAcSubmissionList"]


def fetch_submission_code(submission_id, session_cookie):
    """Fetch the actual code + metadata for a specific submission."""
    url = "https://leetcode.com/graphql"
    headers = {
        "Content-Type": "application/json",
        "Cookie": f"LEETCODE_SESSION={session_cookie}",
        "Referer": "https://leetcode.com",
        "User-Agent": "Mozilla/5.0",
        "x-csrftoken": "none",
    }
    payload = {
        "query": SUBMISSION_DETAIL_QUERY,
        "variables": {"submissionId": int(submission_id)}
    }

    response = requests.post(url, json=payload, headers=headers)
    response.raise_for_status()
    data = response.json()
    return data["data"]["submissionDetails"]


def save_solution(detail, submission_id):
    """Save solution to file with a nice header comment."""
    question = detail["question"]
    title = question["title"]
    slug = question["titleSlug"]
    difficulty = question["difficulty"]
    tags = [t["name"] for t in question["topicTags"]]
    lang = detail["lang"]["name"].lower()
    code = detail["code"]

    ext = EXTENSIONS.get(lang, "txt")

    # folder: solutions/leetcode/two-sum/
    folder = os.path.join("solutions", "leetcode")
    os.makedirs(folder, exist_ok=True)

    filename = f"solution.{ext}"
    filepath = os.path.join(folder, f"{slug}.{ext}")

    # Build a nice file header
    header_lines = [
        f"Problem  : {title}",
        f"Difficulty: {difficulty}",
        f"Tags     : {', '.join(tags)}",
        f"URL      : https://leetcode.com/problems/{slug}/",
        f"Solved on: {datetime.now().strftime('%Y-%m-%d %H:%M')}",
    ]

    comment_char = "//" if ext in ["cpp", "java", "js", "ts", "c", "go", "rs", "kt"] else "#"
    header = "\n".join(f"{comment_char} {line}" for line in header_lines)
    header += f"\n{comment_char} " + "─" * 50 + "\n\n"

    with open(filepath, "w", encoding="utf-8") as f:
        f.write(header + code + "\n")

    logging.info(f"Saved: {filepath}")
    print(f"Saved: {filepath}")
    return filepath


def run():
    config = load_config()
    username = config["leetcode"]["username"]
    session_cookie = config["leetcode"]["session_cookie"]

    seen_ids = load_seen_ids()
    new_files = []

    print("Checking LeetCode for new accepted submissions...")
    logging.info("Polling LeetCode...")

    try:
        submissions = fetch_recent_accepted(username, session_cookie)
    except Exception as e:
        logging.error(f"Failed to fetch submissions: {e}")
        print(f" Error fetching submissions: {e}")
        return []

    for sub in submissions:
        sub_id = sub["id"]

        if sub_id in seen_ids:
            continue  # already processed

        print(f"New submission found: {sub['title']} ({sub['lang']})")
        logging.info(f"New submission: {sub['title']} id={sub_id}")

        try:
            detail = fetch_submission_code(sub_id, session_cookie)
            if detail is None:
                logging.warning(f"Could not fetch detail for submission {sub_id}")
                continue

            filepath = save_solution(detail, sub_id)
            new_files.append(filepath)
            seen_ids.add(sub_id)

        except Exception as e:
            logging.error(f"Error processing submission {sub_id}: {e}")
            print(f"Error: {e}")

    save_seen_ids(seen_ids)
    return new_files


if __name__ == "__main__":
    files = run()
    if not files:
        print("No new submissions to process.")
