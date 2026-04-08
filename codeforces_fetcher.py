"""
codeforces_fetcher.py
----------------------
Fetches your latest ACCEPTED (verdict=OK) submissions from Codeforces
using their PUBLIC REST API — no login/cookie needed!

SETUP:
Just put your Codeforces handle in config.json (see README)
"""

import requests
import json
import os
import logging
from datetime import datetime

logging.basicConfig(
    filename="logs/codeforces.log",
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s"
)

EXTENSIONS = {
    "GNU G++17 7.3.0": "cpp",
    "GNU G++14 6.4.0": "cpp",
    "GNU G++20 11.2.0 (64 bit, winlibs)": "cpp",
    "Microsoft Visual C++ 2017": "cpp",
    "Python 3.8.12": "py",
    "PyPy 3-64": "py",
    "Java 11.0.6": "java",
    "Java 17 64bit": "java",
    "JavaScript V8 4.8.0": "js",
    "Go 1.19.5": "go",
    "Rust 2021": "rs",
}

CF_API = "https://codeforces.com/api"

def run():
    print("Codeforces: feature in progress.")
    return []

def load_config():
    with open("config.json", "r") as f:
        return json.load(f)


def load_seen_ids():
    path = "logs/seen_codeforces.json"
    if os.path.exists(path):
        with open(path, "r") as f:
            return set(json.load(f))
    return set()


def save_seen_ids(seen_ids):
    with open("logs/seen_codeforces.json", "w") as f:
        json.dump(list(seen_ids), f)


def get_lang_ext(lang_name):
    """Try to get extension from known names, else guess from lang string."""
    for key, ext in EXTENSIONS.items():
        if key.lower() in lang_name.lower():
            return ext
    # Fallback guessing
    lang_lower = lang_name.lower()
    if "python" in lang_lower or "pypy" in lang_lower:
        return "py"
    if "java" in lang_lower:
        return "java"
    if "c++" in lang_lower or "g++" in lang_lower:
        return "cpp"
    if "javascript" in lang_lower:
        return "js"
    if "go" in lang_lower:
        return "go"
    if "rust" in lang_lower:
        return "rs"
    return "txt"


def fetch_accepted_submissions(handle, count=20):
    """Fetch recent AC submissions from Codeforces public API."""
    url = f"{CF_API}/user.status"
    params = {
        "handle": handle,
        "from": 1,
        "count": count
    }
    response = requests.get(url, params=params)
    response.raise_for_status()
    data = response.json()

    if data["status"] != "OK":
        raise Exception(f"Codeforces API error: {data.get('comment', 'unknown')}")

    # Filter only accepted submissions
    return [s for s in data["result"] if s.get("verdict") == "OK"]


def fetch_submission_code(contest_id, submission_id, handle):
    """
    Codeforces doesn't expose submission code via API directly.
    We scrape the submission page (allowed for your own submissions).
    Requires your JSESSIONID cookie for private contests.
    For public contests, no cookie needed.
    """
    config = load_config()
    cookies = {}
    cf_config = config.get("codeforces", {})

    if cf_config.get("jsessionid"):
        cookies["JSESSIONID"] = cf_config["jsessionid"]

    url = f"https://codeforces.com/contest/{contest_id}/submission/{submission_id}"
    headers = {"User-Agent": "Mozilla/5.0"}

    response = requests.get(url, headers=headers, cookies=cookies)
    response.raise_for_status()

    # Parse the <pre> tag that holds the code
    from html.parser import HTMLParser

    class CodeParser(HTMLParser):
        def __init__(self):
            super().__init__()
            self.in_code = False
            self.code = []

        def handle_starttag(self, tag, attrs):
            attrs_dict = dict(attrs)
            if tag == "pre" and attrs_dict.get("id") == "program-source-text":
                self.in_code = True

        def handle_endtag(self, tag):
            if tag == "pre" and self.in_code:
                self.in_code = False

        def handle_data(self, data):
            if self.in_code:
                self.code.append(data)

    parser = CodeParser()
    parser.feed(response.text)
    return "".join(parser.code)


def save_solution(submission, code):
    """Save Codeforces solution to organized folder."""
    problem = submission["problem"]
    contest_id = submission.get("contestId", "gym")
    problem_index = problem.get("index", "A")
    problem_name = problem.get("name", "Unknown")
    tags = problem.get("tags", [])
    lang = submission.get("programmingLanguage", "unknown")
    rating = problem.get("rating", "unrated")

    ext = get_lang_ext(lang)

    # Sanitize folder name
    safe_name = problem_name.replace(" ", "_").replace("/", "_").replace(":", "")
    folder_name = f"{contest_id}_{problem_index}_{safe_name}"
    folder = os.path.join("solutions", "codeforces", folder_name)
    os.makedirs(folder, exist_ok=True)

    filename = f"solution.{ext}"
    filepath = os.path.join(folder, filename)

    comment_char = "//" if ext in ["cpp", "java", "js", "go", "rs"] else "#"
    header = f"""{comment_char} Problem  : {problem_name}
{comment_char} Contest  : {contest_id} | Problem {problem_index}
{comment_char} Rating   : {rating}
{comment_char} Tags     : {', '.join(tags)}
{comment_char} URL      : https://codeforces.com/contest/{contest_id}/problem/{problem_index}
{comment_char} Language : {lang}
{comment_char} Solved on: {datetime.now().strftime('%Y-%m-%d %H:%M')}
{comment_char} {'─' * 50}

"""

    with open(filepath, "w") as f:
        f.write(header + code + "\n")

    logging.info(f"Saved: {filepath}")
    print(f"Saved: {filepath}")
    return filepath


# def run():
#     config = load_config()
#     handle = config["codeforces"]["handle"]

#     seen_ids = load_seen_ids()
#     new_files = []

#     print("Checking Codeforces for new accepted submissions...")
#     logging.info("Polling Codeforces...")

#     try:
#         submissions = fetch_accepted_submissions(handle)
#     except Exception as e:
#         logging.error(f"Failed to fetch submissions: {e}")
#         print(f"Error fetching submissions: {e}")
#         return []

#     for sub in submissions:
#         sub_id = str(sub["id"])

#         if sub_id in seen_ids:
#             continue

#         problem_name = sub["problem"].get("name", "Unknown")
#         contest_id = sub.get("contestId", "unknown")
#         print(f"New AC found: {problem_name} (Contest {contest_id})")
#         logging.info(f"New AC: {problem_name} id={sub_id}")

#         try:
#             code = fetch_submission_code(contest_id, sub_id, handle)
#             if not code.strip():
#                 logging.warning(f"Empty code for submission {sub_id}, skipping")
#                 continue

#             filepath = save_solution(sub, code)
#             new_files.append(filepath)
#             seen_ids.add(sub_id)

#         except Exception as e:
#             logging.error(f"Error processing submission {sub_id}: {e}")
#             print(f" Error: {e}")

#     save_seen_ids(seen_ids)
#     return new_files


if __name__ == "__main__":
    files = run()
    if not files:
        print("No new submissions to process.")
