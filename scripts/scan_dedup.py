"""
Deterministic URL deduplication for discovery scanners.

Before filing a new issue, scanners call `is_url_already_tracked(url)` to check
whether the URL is already known via:

1. `source_url:` frontmatter in source-notes/*.md files (local grep, instant)
2. Any open GitHub issue body (one cached `gh` call per process)

This is a cheap grep + API call — no LLM involved. Prevents the Prospector
from spending tokens triaging duplicates that the scanner already knows about.

Usage from a scanner:

    import scan_dedup

    for result in results:
        if scan_dedup.is_url_already_tracked(result['url']):
            print(f"  [dedup] already tracked: {result['url']}")
            continue
        file_issue(result)
"""

import json
import os
import shutil
import subprocess
import sys
from pathlib import Path

SOURCE_NOTES_DIR = Path(__file__).parent.parent / "source-notes"
REPO_URL = os.environ.get("GITHUB_REPOSITORY", "steveash/hitchhiker-guide")

# Caches — populated once per process on first call.
_source_notes_urls: set[str] | None = None
_open_issue_bodies: list[str] | None = None


def _load_source_notes_urls() -> set[str]:
    """Read source_url: frontmatter from all source-notes/*.md files."""
    global _source_notes_urls
    if _source_notes_urls is not None:
        return _source_notes_urls

    urls: set[str] = set()
    if not SOURCE_NOTES_DIR.is_dir():
        _source_notes_urls = urls
        return urls

    for md_file in SOURCE_NOTES_DIR.glob("*.md"):
        try:
            with open(md_file) as f:
                in_frontmatter = False
                for line in f:
                    stripped = line.strip()
                    if stripped == "---":
                        if in_frontmatter:
                            break  # end of frontmatter
                        in_frontmatter = True
                        continue
                    if in_frontmatter and stripped.startswith("source_url:"):
                        url = stripped.split(":", 1)[1].strip()
                        if url:
                            urls.add(url)
                        break
        except OSError:
            continue

    _source_notes_urls = urls
    return urls


def _load_open_issue_bodies() -> list[str]:
    """Fetch bodies of all open issues via gh CLI (cached per process)."""
    global _open_issue_bodies
    if _open_issue_bodies is not None:
        return _open_issue_bodies

    _open_issue_bodies = []
    if shutil.which("gh") is None:
        return _open_issue_bodies

    try:
        result = subprocess.run(
            [
                "gh", "issue", "list",
                "--repo", REPO_URL,
                "--state", "open",
                "--json", "body",
                "--limit", "500",
            ],
            capture_output=True,
            text=True,
            timeout=60,
        )
        if result.returncode == 0:
            issues = json.loads(result.stdout)
            _open_issue_bodies = [
                issue.get("body", "") for issue in issues
            ]
    except (subprocess.TimeoutExpired, subprocess.SubprocessError, json.JSONDecodeError) as e:
        print(f"  WARN: could not fetch open issues for dedup: {e}", file=sys.stderr)

    return _open_issue_bodies


def is_url_already_tracked(url: str) -> bool:
    """Check if a URL is already tracked in source-notes or open issues.

    Returns True if the URL should be skipped (already known).
    """
    if not url:
        return False

    # Check 1: source-notes frontmatter (local, instant)
    if url in _load_source_notes_urls():
        return True

    # Check 2: open GitHub issue bodies (cached API call)
    for body in _load_open_issue_bodies():
        if url in body:
            return True

    return False
