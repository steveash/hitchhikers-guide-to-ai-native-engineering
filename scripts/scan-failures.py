#!/usr/bin/env python3
"""
Weekly failure report scanner.

Searches HN (via Algolia API, free, no key), GitHub Discussions,
and optionally Reddit for failure reports about AI coding agents.

Failure reports = "I tried X and it didn't work" — these are
first-class sources for the Hitchhiker's Guide.

When a substantial result is discovered the scanner shells out to
`gh issue create` so the issue is filed against the
`.github/ISSUE_TEMPLATE/failure-report.yml` template (labels +
structure stay aligned with what humans submit). This promotes the
scanner from passive REST poster to active driver of Pipeline 1 —
auto-filed failure reports flow through Prospector triage the same
way human submissions do.
"""

import argparse
import json
import os
import shutil
import subprocess
import sys
import time
from datetime import datetime, timezone
from pathlib import Path

import requests

GITHUB_TOKEN = os.environ.get("GITHUB_TOKEN")
REPO_URL = os.environ.get("GITHUB_REPOSITORY", "steveash/hitchhiker-guide")

# HN Algolia API (free, no key required)
HN_API = "https://hn.algolia.com/api/v1"

# Search terms for finding failure reports
FAILURE_SEARCH_TERMS = [
    "claude code doesn't work",
    "claude code frustrating",
    "claude code problem",
    "CLAUDE.md ignored",
    "AI coding agent failure",
    "cursor vs claude code",
    "switched from claude code",
    "claude code context window",
    "agentic coding mistake",
    "AI coding tool limitation",
]

# Positive-signal terms to also capture (for balance)
PRACTICE_SEARCH_TERMS = [
    "claude code workflow",
    "CLAUDE.md best practices",
    "claude code tips",
    "AI coding agent setup",
]

# Minimum engagement threshold (filters noise)
MIN_HN_POINTS = 3
MIN_HN_COMMENTS = 2


def github_headers():
    headers = {"Accept": "application/vnd.github+json"}
    if GITHUB_TOKEN:
        headers["Authorization"] = f"Bearer {GITHUB_TOKEN}"
    return headers


def search_hn(query: str, created_after: str = "2025-12-01") -> list[dict]:
    """Search HN via Algolia API. Free, no key needed."""
    # Convert date to unix timestamp
    ts = int(datetime.strptime(created_after, "%Y-%m-%d").timestamp())

    url = f"{HN_API}/search"
    params = {
        "query": query,
        "tags": "(story,comment)",
        "numericFilters": f"created_at_i>{ts},points>{MIN_HN_POINTS}",
        "hitsPerPage": 20,
    }

    resp = requests.get(url, params=params)
    if resp.status_code != 200:
        print(f"HN search failed ({resp.status_code}): {resp.text}", file=sys.stderr)
        return []

    results = []
    for hit in resp.json().get("hits", []):
        results.append({
            "source": "hn",
            "title": hit.get("title") or hit.get("story_title", ""),
            "url": hit.get("url") or f"https://news.ycombinator.com/item?id={hit['objectID']}",
            "hn_url": f"https://news.ycombinator.com/item?id={hit['objectID']}",
            "points": hit.get("points", 0),
            "num_comments": hit.get("num_comments", 0),
            "author": hit.get("author", ""),
            "created_at": hit.get("created_at", ""),
            "snippet": (hit.get("comment_text") or hit.get("story_text") or "")[:500],
        })

    return results


def search_github_discussions(query: str) -> list[dict]:
    """Search GitHub discussions in anthropics/claude-code and related repos."""
    url = "https://api.github.com/search/issues"
    params = {
        "q": f"{query} is:open type:discussion",
        "sort": "reactions",
        "per_page": 20,
    }

    resp = requests.get(url, headers=github_headers(), params=params)
    if resp.status_code != 200:
        print(f"GitHub search failed ({resp.status_code})", file=sys.stderr)
        return []

    results = []
    for item in resp.json().get("items", []):
        results.append({
            "source": "github",
            "title": item["title"],
            "url": item["html_url"],
            "reactions": item.get("reactions", {}).get("total_count", 0),
            "comments": item.get("comments", 0),
            "author": item.get("user", {}).get("login", ""),
            "created_at": item.get("created_at", ""),
            "body_snippet": (item.get("body") or "")[:500],
        })

    return results


def is_substantial(result: dict) -> bool:
    """Filter out low-quality results."""
    if result["source"] == "hn":
        if result.get("num_comments", 0) < MIN_HN_COMMENTS:
            return False
        if len(result.get("snippet", "")) < 50:
            return False

    if result["source"] == "github":
        if result.get("comments", 0) < 1 and result.get("reactions", 0) < 2:
            return False

    return True


# Map our internal source identifier to the human label used by the
# failure-report.yml template's "Where was this reported?" dropdown.
PLATFORM_LABELS = {
    "hn": "Hacker News",
    "github": "GitHub Issue / Discussion",
    "reddit": "Reddit (r/ClaudeCode, r/ChatGPT, etc.)",
}


def file_issue(result: dict):
    """File a GitHub issue for a discovered failure report via `gh issue create`.

    Body and labels are aligned with `.github/ISSUE_TEMPLATE/failure-report.yml`
    so auto-filed issues look like the human-submitted ones and flow through the
    same Prospector triage path. Uses `gh` (not the raw REST API) so authentication
    picks up GH_TOKEN/GITHUB_TOKEN from the environment in CI and from the user's
    local `gh auth login` when run by hand.
    """
    if shutil.which("gh") is None:
        print(
            "  ERROR: `gh` CLI not found — cannot file issue. "
            "Install GitHub CLI or run inside the GitHub Actions workflow.",
            file=sys.stderr,
        )
        return

    source_label = f"source-{result['source']}"
    platform = PLATFORM_LABELS.get(result["source"], "Other")
    preview = result.get("snippet") or result.get("body_snippet") or "(no preview available)"

    title = f"[failure] {result['title'][:80]}"

    # Body mirrors the failure-report.yml form sections so triage tooling can
    # treat auto-filed and human-filed issues the same way.
    body = f"""### Source URL

{result['url']}

### Where was this reported?

{platform}

### What failed?

Auto-discovered by the weekly failure scanner. Preview of the source content
below — the Prospector / Miner should fetch the URL above for the full text.

- **Author**: {result.get('author', 'unknown')}
- **Date**: {result.get('created_at', 'unknown')}
- **Engagement**: {_engagement_summary(result)}

> {preview}

### Why is this failure report valuable?

Unknown — needs Prospector triage. The scanner only knows that this content
matched one of the failure-mode search terms with enough engagement to clear
the noise floor; it has not read the body. The Prospector decides whether the
failure is concrete enough to extract actionable lessons, relevant to current
AI agent tooling, and substantive (not just venting).

---
*Filed by `scripts/scan-failures.py` against `.github/ISSUE_TEMPLATE/failure-report.yml`*
"""

    cmd = [
        "gh", "issue", "create",
        "--repo", REPO_URL,
        "--title", title,
        "--body", body,
        "--label", "new-failure",
        "--label", "failure-report",
        "--label", source_label,
    ]

    try:
        proc = subprocess.run(cmd, check=True, capture_output=True, text=True)
        url_out = proc.stdout.strip()
        print(f"  Filed: {title} → {url_out}")
    except subprocess.CalledProcessError as e:
        print(
            f"  Failed to file issue for {result['url']} "
            f"(exit {e.returncode}): {e.stderr.strip()}",
            file=sys.stderr,
        )


def _engagement_summary(result: dict) -> str:
    if result["source"] == "hn":
        return f"{result.get('points', 0)} points, {result.get('num_comments', 0)} comments"
    elif result["source"] == "github":
        return f"{result.get('reactions', 0)} reactions, {result.get('comments', 0)} comments"
    return "unknown"


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--source", choices=["hn", "github", "reddit", "all"],
                        default="all")
    parser.add_argument("--since", default="2025-12-01",
                        help="Only find content after this date (YYYY-MM-DD)")
    args = parser.parse_args()

    all_results = []

    if args.source in ("hn", "all"):
        print("Scanning Hacker News...")
        for term in FAILURE_SEARCH_TERMS + PRACTICE_SEARCH_TERMS:
            results = search_hn(term, created_after=args.since)
            all_results.extend(results)
            print(f"  '{term}': {len(results)} results")
            time.sleep(1)  # Be polite to Algolia

    if args.source in ("github", "all"):
        print("\nScanning GitHub Discussions...")
        for term in FAILURE_SEARCH_TERMS[:5]:  # Fewer queries, rate limits
            results = search_github_discussions(term)
            all_results.extend(results)
            print(f"  '{term}': {len(results)} results")
            time.sleep(2)  # GitHub rate limits

    if args.source in ("reddit", "all"):
        print("\nReddit scanning requires API credentials (not yet configured)")
        # TODO: Add Reddit scanning when credentials are available

    # Deduplicate by URL
    seen_urls = set()
    unique_results = []
    for r in all_results:
        if r["url"] not in seen_urls:
            seen_urls.add(r["url"])
            unique_results.append(r)

    # Filter for substance
    substantial = [r for r in unique_results if is_substantial(r)]

    print(f"\n{len(all_results)} total → {len(unique_results)} unique → "
          f"{len(substantial)} substantial")

    for result in substantial:
        file_issue(result)

    print(f"\nDone. Filed {len(substantial)} issues.")


if __name__ == "__main__":
    main()
