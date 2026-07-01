# LeetCode Auto-Commit 

A Chrome extension that **automatically commits your accepted LeetCode submissions to GitHub** the moment you hit "Accepted" — no session cookies, no cron jobs, no manual effort.

---

## Why this exists

The old approach (Python script + Task Scheduler + LeetCode session cookie) had one big problem — the session cookie expires every few weeks, breaking everything silently.

This extension fixes that permanently:
- Runs **inside your browser** where you're already logged in
- Detects "Accepted" **instantly** (no polling every 10 minutes)
- Only needs a **GitHub Personal Access Token** — set once, works forever
- Commits code directly via GitHub API — no local git, no Python, no terminal

---

## How it works

```
You submit on LeetCode
       ↓
content.js detects green "Accepted" via MutationObserver
       ↓
Reads problem title, slug, language, code from Monaco editor
       ↓
Sends to background.js (service worker)
       ↓
Checks seen list to avoid duplicate commits
       ↓
Calls GitHub Contents API → commits file to your repo
```

Your solution lands at:
```
solutions/leetcode/<problem-slug>/solution.<ext>
```

---

## Setup

### Step 1 — Get a GitHub Personal Access Token
1. Go to GitHub → Profile → Settings → Developer Settings
2. Personal access tokens → Tokens (classic) → Generate new token
3. Check the **`repo`** scope checkbox
4. Generate and copy the token (starts with `ghp_`)

### Step 2 — Load the extension in Chrome
1. Download or clone this repo
2. Open Chrome → go to `chrome://extensions`
3. Turn on **Developer mode** (top right)
4. Click **Load unpacked** → select the `lc-auto-commit` folder
5. Pin the extension from the 🧩 puzzle icon in toolbar

### Step 3 — Configure
1. Click the extension icon
2. Paste your GitHub token
3. Enter your repo as `username/repo-name` (e.g. `AJkoder/cp-solutions`)
4. Click **Save Credentials**

### Step 4 — Use it
Just solve problems on LeetCode normally. Every time you get "Accepted", the extension auto-commits within seconds.

---

## Files

```
lc-auto-commit/
├── manifest.json      ← extension config, permissions
├── content.js         ← runs on LeetCode, detects Accepted, reads code
├── background.js      ← service worker, dedupes, calls GitHub API
├── popup.html         ← settings UI
└── popup.js           ← saves/loads GitHub token and repo
```

---

## Supported languages

Python, C++, Java, JavaScript, TypeScript, Go, Rust, C, C#, Kotlin, Swift, Ruby, Scala, PHP

---

## Tech used

Chrome Extensions (Manifest V3) · MutationObserver · Monaco Editor API · GitHub Contents REST API · chrome.storage

---

## Comparison with v1 (Python script)

| | v1 Python Script | v2 Chrome Extension |
|---|---|---|
| Auth | LeetCode session cookie (expires) | GitHub PAT (set once) |
| Trigger | Polls every 10 minutes | Instant on Accepted |
| Setup | Python, pip, Task Scheduler | Just load unpacked |
| Works when | Script is running | Browser is open |
| Cookie needed | Yes, refresh regularly | No |

---

## Contributing

PRs welcome. If LeetCode updates their UI and the selector breaks, open an issue with the new element structure.
