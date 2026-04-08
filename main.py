"""
main.py
--------
Runs the fetchers and commits new solutions to GitHub.
Set this up as a cron job to run every 10 minutes.

python main.py                  # both platforms
python main.py --platform lc    # only LeetCode
python main.py --platform cf    # only Codeforces
python main.py --no-push        # don't push to GitHub
"""

import argparse
import os
import sys
from datetime import datetime

os.chdir(os.path.dirname(os.path.abspath(__file__)))

import leetcode_fetcher
import codeforces_fetcher
import git_committer


def parse_args():
    parser = argparse.ArgumentParser(
        description="Auto-commit competitive programming solutions to GitHub"
    )
    parser.add_argument(
        "--platform",
        choices=["lc", "cf", "both"],
        default="both",
        help="Which platform to check (lc=LeetCode, cf=Codeforces, both=default)"
    )
    parser.add_argument(
        "--no-push",
        action="store_true",
        help="Save files locally but skip git commit/push"
    )
    return parser.parse_args()


def main():
    args = parse_args()
    print(f"\n{'='*55}")
    print(f"  Auto-Commit Solutions — {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print(f"{'='*55}\n")

    all_new_files = []

    if args.platform in ("lc", "both"):
        try:
            lc_files = leetcode_fetcher.run()
            all_new_files.extend(lc_files)
        except FileNotFoundError:
            print("  [WARNING] config.json not found.")
        except KeyError as e:
            print(f"  [WARNING] Missing config key: {e}")
        except Exception as e:
            print(f"  [ERROR] LeetCode: {e}")

    if args.platform in ("cf", "both"):
        try:
            cf_files = codeforces_fetcher.run()
            all_new_files.extend(cf_files)
        except FileNotFoundError:
            print("  [WARNING] config.json not found.")
        except KeyError as e:
            print(f"  [WARNING] Missing config key: {e}")
        except Exception as e:
            print(f"  [ERROR] Codeforces: {e}")

    if all_new_files and not args.no_push:
        git_committer.commit_and_push(all_new_files)
    elif all_new_files and args.no_push:
        print(f"\n  {len(all_new_files)} file(s) saved locally (--no-push mode)")
    else:
        print("\n  Everything is up to date.")

    print(f"\n{'='*55}\n")


if __name__ == "__main__":
    main()