#!/usr/bin/env python3
"""
Site-crawl scanner: seed-based documentation site discovery.

Given a curated list of "seed" URLs (documentation sites, knowledge bases),
this scanner discovers pages via sitemap.xml or nav-link extraction, screens
them for relevance using a fast Haiku LLM call, and files GitHub issues for
relevant pages to feed into the existing source pipeline.

Per-seed crawl state lives in `registry/site-crawl-state.json` so the
hand-edited seed list stays diff-clean across runs.

URL lifecycle in state:
  (not in state) → discovered → screened:pending | screened:rejected
  screened:pending → filed

Runs as a step in the daily-scan workflow alongside feed/failure scanners.
Shares the same daily-cap budget via scan_budget.
"""

import argparse
import json
import os
import re
import subprocess
import shutil
import sys
import time
from datetime import datetime, timezone
from pathlib import Path
from urllib.parse import urljoin, urlparse

import requests

import scan_budget
import scan_dedup

GITHUB_TOKEN = os.environ.get("GITHUB_TOKEN")
ANTHROPIC_API_KEY = os.environ.get("ANTHROPIC_API_KEY")
REPO_URL = os.environ.get("GITHUB_REPOSITORY", "steveash/hitchhiker-guide")

SEEDS_PATH = Path(__file__).parent.parent / "registry" / "site-crawl-seeds.json"
STATE_PATH = Path(__file__).parent.parent / "registry" / "site-crawl-state.json"

USER_AGENT = "hitchhiker-guide-site-crawler/1.0 (+https://github.com/steveash/hitchhiker-guide)"
REQUEST_TIMEOUT = 30
INTER_REQUEST_SLEEP = 1  # seconds between requests (be polite)

# Max issues to file per run across all seeds.
MAX_ISSUES_PER_RUN = 20

# Max new URLs to screen per seed per run (keeps Haiku costs bounded).
MAX_SCREEN_PER_SEED = 50


def load_seeds() -> dict:
    with open(SEEDS_PATH) as f:
        return json.load(f)


def load_state() -> dict:
    if STATE_PATH.exists():
        with open(STATE_PATH) as f:
            return json.load(f)
    return {}


def save_state(state: dict):
    STATE_PATH.parent.mkdir(parents=True, exist_ok=True)
    with open(STATE_PATH, "w") as f:
        json.dump(state, f, indent=2, default=str)


def get_base_url(url: str) -> str:
    """Extract scheme + netloc from a URL for same-site filtering."""
    parsed = urlparse(url)
    return f"{parsed.scheme}://{parsed.netloc}"


def get_site_prefix(url: str) -> str:
    """Get the URL path prefix for scoping crawls to the same site section.

    Walks up from the seed URL path to find a sensible project root.
    For https://example.com/gh-aw/introduction/overview/ → /gh-aw
    For https://example.com/docs/guide/ → /docs
    Uses the first two non-empty path segments as the root.
    """
    parsed = urlparse(url)
    segments = [s for s in parsed.path.split("/") if s]
    # Use the first path segment as the project root (e.g. "gh-aw")
    if segments:
        root = "/" + segments[0]
    else:
        root = "/"
    return f"{parsed.scheme}://{parsed.netloc}{root}"


def discover_from_sitemap(seed_url: str) -> list[str] | None:
    """Try to fetch and parse sitemap.xml. Returns URLs or None if no sitemap."""
    base = get_base_url(seed_url)
    sitemap_urls = [
        f"{base}/sitemap.xml",
        f"{base}/sitemap_index.xml",
    ]

    for sitemap_url in sitemap_urls:
        try:
            resp = requests.get(
                sitemap_url,
                headers={"User-Agent": USER_AGENT},
                timeout=REQUEST_TIMEOUT,
            )
            if resp.status_code != 200:
                continue

            # Parse sitemap XML
            import xml.etree.ElementTree as ET
            root = ET.fromstring(resp.text)

            # Handle sitemap index (contains <sitemap><loc>) or
            # urlset (contains <url><loc>)
            ns = {"sm": "http://www.sitemaps.org/schemas/sitemap/0.9"}
            urls = []

            # Try urlset first
            for url_el in root.findall(".//sm:url/sm:loc", ns):
                if url_el.text:
                    urls.append(url_el.text.strip())

            # Try without namespace (some sitemaps don't use it)
            if not urls:
                for url_el in root.findall(".//url/loc"):
                    if url_el.text:
                        urls.append(url_el.text.strip())

            if urls:
                print(f"  Found sitemap at {sitemap_url} with {len(urls)} URLs")
                return urls

        except Exception as e:
            print(f"  Sitemap {sitemap_url}: {e}", file=sys.stderr)
            continue

    return None


def discover_from_nav(seed_url: str) -> list[str]:
    """Fetch the seed page and extract internal links."""
    try:
        resp = requests.get(
            seed_url,
            headers={"User-Agent": USER_AGENT},
            timeout=REQUEST_TIMEOUT,
        )
        if resp.status_code != 200:
            print(f"  ERROR fetching seed {seed_url}: HTTP {resp.status_code}", file=sys.stderr)
            return []
    except requests.RequestException as e:
        print(f"  ERROR fetching seed {seed_url}: {e}", file=sys.stderr)
        return []

    # Extract all href links from the HTML
    hrefs = re.findall(r'href=["\']([^"\']+)["\']', resp.text)

    base = get_base_url(seed_url)
    prefix = get_site_prefix(seed_url)
    urls = set()

    for href in hrefs:
        # Resolve relative URLs
        full_url = urljoin(seed_url, href)
        # Strip fragments
        full_url = full_url.split("#")[0]
        # Strip trailing slash for consistency
        full_url = full_url.rstrip("/")

        # Only keep same-site URLs under the same path prefix
        if full_url.startswith(prefix) and full_url != seed_url.rstrip("/"):
            # Skip common non-content paths
            skip_patterns = [
                "/api/", "/assets/", "/static/", "/css/", "/js/",
                "/images/", "/fonts/", ".css", ".js", ".png", ".jpg",
                ".svg", ".ico", ".xml", ".json",
            ]
            if not any(p in full_url.lower() for p in skip_patterns):
                urls.add(full_url)

    print(f"  Extracted {len(urls)} internal links from seed page")
    return sorted(urls)


def screen_urls_with_haiku(urls: list[str], seed: dict) -> dict[str, str]:
    """Batch-screen URLs for relevance using Haiku.

    Returns {url: "relevant"|"rejected"} with a one-line reason for each.
    """
    if not ANTHROPIC_API_KEY:
        print("  WARNING: ANTHROPIC_API_KEY not set — marking all URLs as pending", file=sys.stderr)
        return {url: "pending" for url in urls}

    # Build a compact list for Haiku
    url_list = "\n".join(f"- {url}" for url in urls)

    prompt = f"""You are a fast relevance screener for the Hitchhiker's Guide to AI-Native Engineering.

Given these URLs from a documentation site, decide which pages are likely to contain
practitioner insights relevant to AI-native software engineering (agent patterns,
tool integration, workflow design, failure modes, team adoption).

Scope hint from the curator: {seed.get('scope', 'no specific scope')}

URLs to screen:
{url_list}

For each URL, respond with exactly one line in this format:
URL | RELEVANT | one-line reason
URL | REJECT | one-line reason

Base your decision on the URL path structure and page name — you cannot read the pages.
Reject API reference pages, changelog/release-note pages, installation/setup guides
that are purely mechanical, and pages that are clearly not about AI coding practices.
When in doubt, mark as RELEVANT — the Prospector will do the deep evaluation later."""

    try:
        resp = requests.post(
            "https://api.anthropic.com/v1/messages",
            headers={
                "x-api-key": ANTHROPIC_API_KEY,
                "anthropic-version": "2023-06-01",
                "content-type": "application/json",
            },
            json={
                "model": "claude-haiku-4-5-20251001",
                "max_tokens": 4096,
                "messages": [{"role": "user", "content": prompt}],
            },
            timeout=60,
        )
        resp.raise_for_status()
        result = resp.json()
        text = result["content"][0]["text"]
    except Exception as e:
        print(f"  ERROR calling Haiku for screening: {e}", file=sys.stderr)
        return {url: "pending" for url in urls}

    # Parse the response
    verdicts = {}
    for line in text.strip().split("\n"):
        line = line.strip()
        if not line or "|" not in line:
            continue
        parts = [p.strip() for p in line.split("|", 2)]
        if len(parts) < 2:
            continue
        url = parts[0]
        verdict = parts[1].upper()
        # Match URL back to our list (Haiku might slightly mangle URLs)
        matched_url = None
        for u in urls:
            if u in url or url in u:
                matched_url = u
                break
        if matched_url:
            if "RELEV" in verdict:
                verdicts[matched_url] = "pending"
            else:
                verdicts[matched_url] = "rejected"

    # Any URL not in the response defaults to pending (screen again next time)
    for url in urls:
        if url not in verdicts:
            verdicts[url] = "pending"

    relevant = sum(1 for v in verdicts.values() if v == "pending")
    rejected = sum(1 for v in verdicts.values() if v == "rejected")
    print(f"  Haiku screening: {relevant} relevant, {rejected} rejected")

    return verdicts


def file_issue(seed: dict, url: str) -> int | None:
    """File a source-submission issue for a discovered page. Returns issue number or None."""
    if shutil.which("gh") is None:
        print("  ERROR: `gh` CLI not found", file=sys.stderr)
        return None

    # Extract a readable title from the URL path
    parsed = urlparse(url)
    path_parts = [p for p in parsed.path.split("/") if p]
    title_slug = " ".join(path_parts[-2:]) if len(path_parts) >= 2 else path_parts[-1] if path_parts else "untitled"
    title = f"[source] {seed['id']}: {title_slug}"[:100]

    body = f"""### Source URL

{url}

### Source Type

{seed['source_type']}

### What's interesting about this source?

Auto-discovered from site-crawl seed `{seed['id']}`.

- **Seed URL**: {seed['url']}
- **Scope**: {seed.get('scope', 'none specified')}

This page was discovered via sitemap/nav-link crawling and passed a
Haiku relevance screen. The Prospector still needs to evaluate novelty
and chapter relevance.

### Where might this be relevant?

Unknown — Prospector to determine.

### Key claims or patterns you noticed (optional)

(none — auto-filed, page has not been deep-read)

---
*Filed by `scripts/scan-sites.py` from site-crawl seed `{seed['id']}`*
"""

    cmd = [
        "gh", "issue", "create",
        "--repo", REPO_URL,
        "--title", title,
        "--body", body,
        "--label", "new-source",
        "--label", "source-submission",
    ]

    try:
        result = subprocess.run(cmd, check=True, capture_output=True, text=True)
        issue_url = result.stdout.strip()
        print(f"  Filed: {issue_url}")
        # Extract issue number from URL
        match = re.search(r"/issues/(\d+)", issue_url)
        return int(match.group(1)) if match else None
    except subprocess.CalledProcessError as e:
        print(f"  Failed to file issue for {url} (exit {e.returncode}): {e.stderr.strip()}", file=sys.stderr)
        return None


def scan_seed(seed: dict, state: dict, dry_run: bool = False) -> tuple[int, int, int]:
    """Scan one seed. Returns (new_urls_found, issues_filed, pending_count)."""
    seed_id = seed["id"]
    print(f"\nScanning seed: {seed_id} ({seed['url']})")

    seed_state = state.setdefault(seed_id, {"urls": {}, "last_scan": None})
    known_urls = seed_state["urls"]

    # Phase 1: Discover URLs
    urls = discover_from_sitemap(seed["url"])
    if urls is None:
        print("  No sitemap found, falling back to nav-link extraction")
        urls = discover_from_nav(seed["url"])

    if not urls:
        print("  No URLs discovered")
        return (0, 0, 0)

    # Filter to new URLs only
    new_urls = [u for u in urls if u not in known_urls]
    print(f"  {len(new_urls)} new URLs (of {len(urls)} total)")

    if not new_urls:
        seed_state["last_scan"] = datetime.now(timezone.utc).isoformat()
        return (0, 0, sum(1 for v in known_urls.values() if isinstance(v, dict) and v.get("status") == "pending"))

    # Cap screening per run
    to_screen = new_urls[:MAX_SCREEN_PER_SEED]
    if len(new_urls) > MAX_SCREEN_PER_SEED:
        print(f"  Capping screening at {MAX_SCREEN_PER_SEED}; remaining {len(new_urls) - MAX_SCREEN_PER_SEED} next run")

    # Phase 2: Haiku screening
    if not dry_run:
        verdicts = screen_urls_with_haiku(to_screen, seed)
    else:
        verdicts = {url: "pending" for url in to_screen}
        print(f"  [DRY-RUN] skipping Haiku screening, marking all as pending")

    # Update state with screening results
    for url, verdict in verdicts.items():
        known_urls[url] = {
            "status": verdict,
            "screened_at": datetime.now(timezone.utc).isoformat(),
        }

    seed_state["last_scan"] = datetime.now(timezone.utc).isoformat()

    new_found = len(new_urls)
    pending = sum(1 for v in known_urls.values() if isinstance(v, dict) and v.get("status") == "pending")
    return (new_found, 0, pending)


def file_pending(state: dict, seeds_by_id: dict, dry_run: bool = False) -> int:
    """File issues for pending URLs across all seeds. Returns count filed."""
    filed = 0

    for seed_id, seed_state in state.items():
        if seed_id not in seeds_by_id:
            continue
        seed = seeds_by_id[seed_id]

        for url, info in list(seed_state.get("urls", {}).items()):
            if not isinstance(info, dict) or info.get("status") != "pending":
                continue
            if filed >= MAX_ISSUES_PER_RUN:
                print(f"\n  Hit per-run cap of {MAX_ISSUES_PER_RUN} issues. Remaining pending URLs will be filed next run.")
                return filed
            if scan_budget.remaining() <= 0:
                print(f"\n  Daily budget exhausted. Remaining pending URLs will be filed next run.")
                return filed

            if not dry_run and scan_dedup.is_url_already_tracked(url):
                print(f"  [dedup] already tracked: {url}")
                info["status"] = "deduped"
                continue

            if dry_run:
                print(f"  [DRY-RUN] would file: {url}")
                filed += 1
            else:
                issue_num = file_issue(seed, url)
                if issue_num is not None:
                    info["status"] = "filed"
                    info["issue"] = issue_num
                    info["filed_at"] = datetime.now(timezone.utc).isoformat()
                    filed += 1
                    scan_budget.record_filed(1)
                else:
                    # Don't retry failed filings forever
                    info["status"] = "file_failed"

            time.sleep(INTER_REQUEST_SLEEP)

    return filed


def main():
    parser = argparse.ArgumentParser(description="Scan documentation site seeds for new relevant pages.")
    parser.add_argument("--dry-run", action="store_true", help="Discover and screen but don't file issues.")
    parser.add_argument("--seed", help="Only scan the seed with this id.")
    args = parser.parse_args()

    seeds_data = load_seeds()
    state = load_state()

    seeds = seeds_data.get("seeds", [])
    if args.seed:
        seeds = [s for s in seeds if s["id"] == args.seed]
        if not seeds:
            print(f"ERROR: no seed with id={args.seed} in {SEEDS_PATH}", file=sys.stderr)
            sys.exit(1)

    seeds_by_id = {s["id"]: s for s in seeds_data.get("seeds", [])}

    print(f"scan-sites starting: {len(seeds)} seed(s), {scan_budget.status_summary()}")

    # Phase 1+2: Discover and screen new URLs
    total_new = 0
    total_pending = 0
    for i, seed in enumerate(seeds):
        try:
            new, _, pending = scan_seed(seed, state, dry_run=args.dry_run)
            total_new += new
            total_pending += pending
        except Exception as e:
            print(f"  ERROR scanning seed {seed.get('id', '?')}: {e}", file=sys.stderr)
        if i < len(seeds) - 1:
            time.sleep(INTER_REQUEST_SLEEP)

    # Phase 3: File issues from pending queue
    print(f"\nFiling issues from pending queue ({total_pending} pending)...")
    filed = file_pending(state, seeds_by_id, dry_run=args.dry_run)

    if not args.dry_run:
        save_state(state)

    print(f"\nScan complete: {total_new} new URLs discovered, {filed} issue(s) filed, "
          f"{total_pending - filed} still pending")
    print(f"Final budget: {scan_budget.status_summary()}")


if __name__ == "__main__":
    main()
