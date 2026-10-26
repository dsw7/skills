import json
import argparse
import subprocess


def check_auth_status() -> None:
    try:
        subprocess.run(
            ["gh", "auth", "status"],
            check=True,
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL,
        )
    except subprocess.CalledProcessError as e:
        raise SystemExit("authentication failed") from e


def print_stdout(stdout: str) -> None:
    issue_data = json.loads(stdout)

    title = issue_data["title"]
    print(f"Title:\n  {title}\n")

    print("Body:")
    for line in issue_data["body"].splitlines():
        print(f"  {line}")


def get_issue(user: str, repo: str, issue: str) -> None:
    try:
        result = subprocess.run(
            [
                "gh",
                "issue",
                "view",
                issue,
                "--json=title,body",
                f"--repo={user}/{repo}",
            ],
            check=True,
            capture_output=True,
            text=True,
        )
    except subprocess.CalledProcessError as e:
        raise SystemExit(f"failed to view issue {issue}: {e.stderr}") from e

    print_stdout(result.stdout)


def main() -> None:
    parser = argparse.ArgumentParser(description="view a GitHub issue")
    parser.add_argument("--user", required=True, help="provide GitHub user")
    parser.add_argument("--repo", required=True, help="provide GitHub repository")
    parser.add_argument("--issue", required=True, help="provide issue (URL or number)")
    args = parser.parse_args()

    check_auth_status()
    get_issue(user=args.user, repo=args.repo, issue=args.issue)


if __name__ == "__main__":
    main()
