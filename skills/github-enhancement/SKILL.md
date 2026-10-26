---
name: github-enhancement
description: Automates fetching a GitHub issue and implementing a solution.
allowed-tools:
  - Write
  - Read
  - Edit
  - Bash
arguments:
  - issue
argument-hint: "<url-to-github-issue> or <github-issue-number>"
---

# Instructions
Resolve GitHub issue: $issue. Stop immediately if any bash command fails.

## Step 1: Fetch Issue
```bash
./scripts/get_issue "\$issue"
```

## Step 2: Implement Fix
1. Branch: `git checkout -b feature/<issue-number>-<short-description>`
2. Code: Locate targets via "Where to look" section or repository search. Apply minimal changes matching "Task" or description. No refactoring.
3. Commit:
```bash
git add . && git commit -m "claude: solution for issue #<issue-number>"
```
