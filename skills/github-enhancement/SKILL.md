---
name: github-enhancement
description: Automates fetching a GitHub issue and implementing a solution.
allowed-tools:
  - Write
  - Read
  - Edit
  - Bash
arguments:
  - user
  - repo
  - issue
argument-hint: "[github-user] [github-repo] [github-issue-number]"
---

# Instructions
Resolve GitHub issue: $issue. Stop immediately if any command fails.

## Step 1: Fetch Issue
```bash
python3 scripts/get_issue.py --user="\$user" --repo="\$repo" --issue="\$issue"
```

## Step 2: Implement Fix
1. Branch: `git checkout -b feature/<issue-number>-<short-description>`
2. Code: Locate targets via "Where to look" section or repository search. Apply minimal changes matching "Task" or description. No refactoring.
3. Commit:
```bash
git add . && git commit -m "claude: solution for issue #<issue-number>"
```
