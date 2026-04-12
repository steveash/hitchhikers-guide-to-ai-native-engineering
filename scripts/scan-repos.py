#!/usr/bin/env python3
"""
Weekly GitHub repo scanner.

Searches for repos with AI agent configuration files (CLAUDE.md, .claude/,
AGENTS.md) and files GitHub issues for new discoveries.

Uses GitHub Search API (code search). Rate limit: 10 requests/minute.

When a NEW repo is discovered (not already in the registry), the scanner
shells out to `gh issue create` so the issue is filed against the
`.github/ISSUE_TEMPLATE/practitioner-repo.yml` template (labels +
structure stay aligned with what humans submit). The registry update
still happens — issue filing is an additional side effect that promotes
the scanner from passive data collector to active driver of Pipeline 1.
"""

import json
import os
import shutil
import subprocess
import sys
import time
from datetime import datetime, timezone
from pathlib import Path

import requests

import scan_budget
import scan_dedup

GITHUB_TOKEN = os.environ.get("GITHUB_TOKEN")
REGISTRY_PATH = Path(__file__).parent.parent / "registry" / "repos.json"
REPO_URL = os.environ.get("GITHUB_REPOSITORY", "steveash/hitchhiker-guide")

# Search queries for discovering repos with AI agent configs
SEARCH_QUERIES = [
    'filename:CLAUDE.md stars:>=5 pushed:>=2025-12-01 fork:false',
    'path:.claude/settings.json stars:>=5 pushed:>=2025-12-01 fork:false',
    'filename:AGENTS.md stars:>=5 pushed:>=2025-12-01 fork:false',
]

# Repos to always exclude (our own, Anthropic's, known tutorials)
EXCLUDE_OWNERS = {
    'anthropics',      # Vendor docs, not practitioner usage
    'steveash',        # Our own repos
}

# Keywords in repo name/description that suggest it's ABOUT Claude, not USING it
TUTORIAL_KEYWORDS = [
    'awesome-', 'list-of-', 'collection-', 'tutorial', 'guide',
    'template', 'starter', 'boilerplate', 'example-claude',
    'claude-tutorial', 'claude-guide', 'claude-template',
]


def github_headers():
    headers = {"Accept": "application/vnd.github+json"}
    if GITHUB_TOKEN:
        headers["Authorization"] = f"Bearer {GITHUB_TOKEN}"
    return headers


def search_repos(query: str, page: int = 1) -> list[dict]:
    """Search GitHub code API and return unique repos from results."""
    url = "https://api.github.com/search/code"
    params = {"q": query, "per_page": 100, "page": page}
    resp = requests.get(url, headers=github_headers(), params=params)

    if resp.status_code == 403:
        print(f"Rate limited. Waiting 60s...", file=sys.stderr)
        time.sleep(60)
        resp = requests.get(url, headers=github_headers(), params=params)

    if resp.status_code != 200:
        print(f"Search failed ({resp.status_code}): {resp.text}", file=sys.stderr)
        return []

    data = resp.json()
    repos = {}
    for item in data.get("items", []):
        repo = item["repository"]
        full_name = repo["full_name"]
        if full_name not in repos:
            repos[full_name] = {
                "full_name": full_name,
                "description": repo.get("description", ""),
                "html_url": repo["html_url"],
                "stars": repo.get("stargazers_count", 0),
                "config_files_found": [item["path"]],
            }
        else:
            repos[full_name]["config_files_found"].append(item["path"])

    return list(repos.values())


def is_excluded(repo: dict) -> bool:
    """Check if repo should be excluded based on heuristics."""
    full_name = repo["full_name"]
    owner = full_name.split("/")[0]
    name = full_name.split("/")[1].lower()
    desc = (repo.get("description") or "").lower()

    if owner in EXCLUDE_OWNERS:
        return True

    for kw in TUTORIAL_KEYWORDS:
        if kw in name or kw in desc:
            return True

    return False


def load_registry() -> dict:
    """Load existing repo registry."""
    if REGISTRY_PATH.exists():
        with open(REGISTRY_PATH) as f:
            return json.load(f)
    return {"repos": {}, "last_scan": None}


def save_registry(registry: dict):
    """Save repo registry."""
    REGISTRY_PATH.parent.mkdir(parents=True, exist_ok=True)
    with open(REGISTRY_PATH, "w") as f:
        json.dump(registry, f, indent=2, default=str)


def file_issue(repo: dict, is_update: bool = False) -> bool:
    """File a GitHub issue for a discovered repo via `gh issue create`.

    Body and labels are aligned with `.github/ISSUE_TEMPLATE/practitioner-repo.yml`
    so auto-filed issues look like the human-submitted ones and flow through the
    same triage path. Uses `gh` (not the raw REST API) so authentication picks up
    GH_TOKEN/GITHUB_TOKEN from the environment in CI and from the user's local
    `gh auth login` when run by hand.

    Returns True on successful filing, False otherwise. The boolean lets the
    caller decide whether to count the file against the daily-cap budget.
    """
    if shutil.which("gh") is None:
        print(
            "  ERROR: `gh` CLI not found — cannot file issue. "
            "Install GitHub CLI or run inside the GitHub Actions workflow.",
            file=sys.stderr,
        )
        return False

    label = "repo-updated" if is_update else "new-repo"
    title_prefix = "[repo-update]" if is_update else "[repo]"
    title = f'{title_prefix} {repo["full_name"]}'

    config_files = repo.get("config_files_found", [])
    config_files_md = (
        "\n".join(f"- `{f}`" for f in config_files) if config_files else "- (none detected)"
    )

    # Body mirrors the practitioner-repo.yml form sections so triage tooling can
    # treat auto-filed and human-filed issues the same way.
    body = f"""### Repository

{repo['full_name']}

URL: {repo['html_url']}

### AI config files present

{config_files_md}

### What makes this repo worth analyzing?

Auto-discovered by the weekly repo scanner.

- Stars: {repo.get('stars', 'unknown')}
- Description: {repo.get('description') or 'No description'}

This issue was filed automatically and needs triage by the Prospector agent.

---
*Filed by `scripts/scan-repos.py` against `.github/ISSUE_TEMPLATE/practitioner-repo.yml`*
"""

    cmd = [
        "gh", "issue", "create",
        "--repo", REPO_URL,
        "--title", title,
        "--body", body,
        "--label", label,
        "--label", "practitioner-repo",
    ]

    try:
        result = subprocess.run(cmd, check=True, capture_output=True, text=True)
        url_out = result.stdout.strip()
        print(f"  Filed issue for {repo['full_name']}: {url_out}")
        return True
    except subprocess.CalledProcessError as e:
        print(
            f"  Failed to file issue for {repo['full_name']} "
            f"(exit {e.returncode}): {e.stderr.strip()}",
            file=sys.stderr,
        )
        return False


def drain_queue() -> int:
    """File repo entries previously queued by this scanner. Returns count filed."""
    budget = scan_budget.remaining()
    if budget <= 0:
        return 0
    queued_items = scan_budget.pop_queued_for("repos", budget)
    if not queued_items:
        return 0
    print(f"Draining {len(queued_items)} queued repo item(s) from prior runs...")
    filed = 0
    for item in queued_items:
        payload = item.get("payload", {})
        repo = payload.get("repo")
        is_update = payload.get("is_update", False)
        if not repo:
            print(f"  WARN: skipping malformed queue item: {item}", file=sys.stderr)
            continue
        if scan_dedup.is_url_already_tracked(repo.get("html_url", "")):
            print(f"  [dedup] already tracked (queued): {repo.get('full_name', '')}")
            continue
        if file_issue(repo, is_update=is_update):
            filed += 1
            scan_budget.record_filed(1)
    return filed


def _try_file_or_queue(repo: dict, is_update: bool) -> tuple[bool, bool]:
    """File a repo issue if budget allows, otherwise queue it for next run.

    Returns (filed, queued) — exactly one will be True. The repo is
    *always* recorded as known in the registry afterwards (caller's
    responsibility) so we never re-discover it tomorrow; the queue is now
    the canonical home for the unfiled work.
    """
    if scan_dedup.is_url_already_tracked(repo.get("html_url", "")):
        print(f"  [dedup] already tracked: {repo['full_name']}")
        return (False, False)
    if scan_budget.remaining() <= 0:
        scan_budget.queue_item("repos", {"repo": repo, "is_update": is_update})
        print(f"  [queued] daily cap reached: {repo['full_name']}")
        return (False, True)
    if file_issue(repo, is_update=is_update):
        scan_budget.record_filed(1)
        return (True, False)
    return (False, False)


def main():
    registry = load_registry()
    known_repos = registry.get("repos", {})
    all_discovered = {}

    print(f"scan-repos starting: {scan_budget.status_summary()}")

    # Drain repo backlog from prior runs first so the oldest discoveries
    # become Pipeline 1 issues before we go looking for fresh ones.
    drained = drain_queue()
    if drained:
        print(f"Refiled {drained} item(s) from queue. {scan_budget.status_summary()}")

    print("Starting repo scan...")

    for query in SEARCH_QUERIES:
        print(f"\nSearching: {query}")
        repos = search_repos(query)
        print(f"  Found {len(repos)} repos")

        for repo in repos:
            name = repo["full_name"]
            if name not in all_discovered:
                all_discovered[name] = repo
            else:
                # Merge config files lists
                existing_files = all_discovered[name]["config_files_found"]
                new_files = repo["config_files_found"]
                all_discovered[name]["config_files_found"] = list(
                    set(existing_files + new_files)
                )

        # Respect rate limits
        time.sleep(10)

    # Filter and process
    new_count = 0
    update_count = 0
    queued_count = 0

    for name, repo in all_discovered.items():
        if is_excluded(repo):
            print(f"  Excluded: {name}")
            continue

        if name not in known_repos:
            print(f"  NEW: {name}")
            filed, queued = _try_file_or_queue(repo, is_update=False)
            known_repos[name] = {
                "first_seen": datetime.now(timezone.utc).isoformat(),
                "last_scanned": datetime.now(timezone.utc).isoformat(),
                "config_files": repo["config_files_found"],
                "stars": repo.get("stars", 0),
            }
            if filed:
                new_count += 1
            if queued:
                queued_count += 1
        else:
            # Check if config files changed
            old_files = set(known_repos[name].get("config_files", []))
            new_files = set(repo["config_files_found"])
            if new_files != old_files:
                print(f"  UPDATED: {name} (config files changed)")
                filed, queued = _try_file_or_queue(repo, is_update=True)
                known_repos[name]["last_scanned"] = datetime.now(timezone.utc).isoformat()
                known_repos[name]["config_files"] = repo["config_files_found"]
                if filed:
                    update_count += 1
                if queued:
                    queued_count += 1
            else:
                known_repos[name]["last_scanned"] = datetime.now(timezone.utc).isoformat()

    registry["repos"] = known_repos
    registry["last_scan"] = datetime.now(timezone.utc).isoformat()
    save_registry(registry)

    print(f"\nScan complete: {new_count} new, {update_count} updated, "
          f"{queued_count} queued for next run, {len(known_repos)} total tracked")
    print(f"Final budget: {scan_budget.status_summary()}")


if __name__ == "__main__":
    main()
