#!/usr/bin/env python3
"""
Trusted-source feed scanner.

Pulls Atom/RSS feeds from a curated list of high-signal sources (vendor
changelogs, specific authors, conference talks) defined in
`registry/trusted-feeds.json`. For each new entry detected since the last
scan, files a GitHub issue against the `source-submission` template with
the URL prefilled and a `new-source` label so it flows through Pipeline 1
the same way human submissions do.

Per-feed seen-state lives in `registry/trusted-feeds-state.json` (separate
from the curated list so the hand-edited file stays diff-clean across runs).

Higher signal-to-noise than the broad HN/Reddit failure scrape — these are
sources we already trust, just looking for new content from them.

Standard library only (xml.etree for feed parsing) plus `requests`, to
match the existing scanner footprint (see scan-repos.py / scan-failures.py).
"""

import argparse
import json
import os
import shutil
import subprocess
import sys
import time
import xml.etree.ElementTree as ET
from datetime import datetime, timezone
from pathlib import Path

import requests

import scan_budget

GITHUB_TOKEN = os.environ.get("GITHUB_TOKEN")
REPO_URL = os.environ.get("GITHUB_REPOSITORY", "steveash/hitchhiker-guide")

FEEDS_PATH = Path(__file__).parent.parent / "registry" / "trusted-feeds.json"
STATE_PATH = Path(__file__).parent.parent / "registry" / "trusted-feeds-state.json"

# Polite defaults — these feeds are mostly small static files; we don't
# need to hammer them.
USER_AGENT = "hitchhiker-guide-trusted-scanner/1.0 (+https://github.com/steveash/hitchhiker-guide)"
REQUEST_TIMEOUT = 30
INTER_FEED_SLEEP = 2  # seconds between feeds (be polite)

# Default cap on issues filed per feed per run. Without this, adding a new
# feed would burst dozens of issues into Pipeline 1 on its first scan.
DEFAULT_MAX_PER_RUN = 3

# Atom + RSS namespace map for ElementTree.
NS = {
    "atom": "http://www.w3.org/2005/Atom",
    "content": "http://purl.org/rss/1.0/modules/content/",
    "dc": "http://purl.org/dc/elements/1.1/",
}


def load_feeds() -> dict:
    """Load the curated feed list (hand-edited)."""
    with open(FEEDS_PATH) as f:
        return json.load(f)


def load_state() -> dict:
    """Load per-feed scanning state. Empty if file does not exist yet."""
    if STATE_PATH.exists():
        with open(STATE_PATH) as f:
            return json.load(f)
    return {"feeds": {}, "last_scan": None}


def save_state(state: dict):
    """Persist per-feed scanning state."""
    STATE_PATH.parent.mkdir(parents=True, exist_ok=True)
    with open(STATE_PATH, "w") as f:
        json.dump(state, f, indent=2, default=str)


def fetch_feed(url: str) -> str | None:
    """Fetch raw feed XML. Returns None on error (logged to stderr)."""
    try:
        resp = requests.get(
            url,
            headers={"User-Agent": USER_AGENT, "Accept": "application/atom+xml, application/rss+xml, application/xml;q=0.9, */*;q=0.8"},
            timeout=REQUEST_TIMEOUT,
        )
    except requests.RequestException as e:
        print(f"  ERROR fetching {url}: {e}", file=sys.stderr)
        return None

    if resp.status_code != 200:
        print(f"  ERROR fetching {url}: HTTP {resp.status_code}", file=sys.stderr)
        return None

    return resp.text


def parse_entries(xml_text: str) -> list[dict]:
    """Parse Atom or RSS feed XML into a normalized list of entries.

    Each returned entry is {id, title, url, published}. The `id` is the
    canonical feed-provided id (Atom <id>, RSS <guid>) when present, falling
    back to the entry URL — that's what we use for dedup against state.
    """
    try:
        root = ET.fromstring(xml_text)
    except ET.ParseError as e:
        print(f"  ERROR parsing feed XML: {e}", file=sys.stderr)
        return []

    entries = []

    # Atom: <feed><entry>...
    atom_entries = root.findall("atom:entry", NS)
    if atom_entries:
        for entry in atom_entries:
            entries.append(_parse_atom_entry(entry))
        return [e for e in entries if e]

    # RSS 2.0: <rss><channel><item>...
    rss_items = root.findall(".//item")
    if rss_items:
        for item in rss_items:
            entries.append(_parse_rss_item(item))
        return [e for e in entries if e]

    print("  WARNING: feed has neither <atom:entry> nor <item> elements", file=sys.stderr)
    return []


def _parse_atom_entry(entry: ET.Element) -> dict | None:
    """Extract id/title/url/published from an Atom <entry>."""
    title_el = entry.find("atom:title", NS)
    title = (title_el.text or "").strip() if title_el is not None else ""

    # Atom <link> can be rel="alternate" (the human-readable URL we want)
    # or rel="self" (feed metadata). Prefer alternate; fall back to first.
    url = ""
    for link in entry.findall("atom:link", NS):
        rel = link.get("rel", "alternate")
        if rel == "alternate":
            url = link.get("href", "")
            break
    if not url:
        first_link = entry.find("atom:link", NS)
        if first_link is not None:
            url = first_link.get("href", "")

    id_el = entry.find("atom:id", NS)
    entry_id = (id_el.text or "").strip() if id_el is not None else url

    published = ""
    for tag in ("atom:published", "atom:updated"):
        el = entry.find(tag, NS)
        if el is not None and el.text:
            published = el.text.strip()
            break

    if not entry_id and not url:
        return None
    return {"id": entry_id or url, "title": title, "url": url, "published": published}


def _parse_rss_item(item: ET.Element) -> dict | None:
    """Extract id/title/url/published from an RSS 2.0 <item>."""
    title_el = item.find("title")
    title = (title_el.text or "").strip() if title_el is not None else ""

    link_el = item.find("link")
    url = (link_el.text or "").strip() if link_el is not None else ""

    guid_el = item.find("guid")
    entry_id = (guid_el.text or "").strip() if guid_el is not None else url

    pub_el = item.find("pubDate")
    if pub_el is None:
        pub_el = item.find("dc:date", NS)
    published = (pub_el.text or "").strip() if pub_el is not None else ""

    if not entry_id and not url:
        return None
    return {"id": entry_id or url, "title": title, "url": url, "published": published}


def file_issue(feed: dict, entry: dict) -> bool:
    """File a source-submission GitHub issue for a new feed entry.

    Body mirrors `.github/ISSUE_TEMPLATE/source-submission.yml` so auto-filed
    issues look like human-submitted ones and flow through the same
    Prospector triage path. Returns True on success, False on failure.
    """
    if shutil.which("gh") is None:
        print(
            "  ERROR: `gh` CLI not found — cannot file issue. "
            "Install GitHub CLI or run inside the GitHub Actions workflow.",
            file=sys.stderr,
        )
        return False

    title_text = entry["title"] or entry["url"] or "untitled"
    title = f"[source] {title_text[:100]}"

    body = f"""### Source URL

{entry['url']}

### Source Type

{feed['source_type']}

### What's interesting about this source?

Auto-discovered from trusted feed `{feed['id']}` ({feed['description']}).

- **Feed**: {feed['url']}
- **Entry title**: {entry['title'] or '(no title)'}
- **Published**: {entry['published'] or 'unknown'}

This source comes from a curated high-signal feed, so it has already passed
the "is this author worth listening to?" bar. The Prospector still needs to
decide novelty and chapter relevance.

### Where might this be relevant?

Unknown — Prospector to determine.

### Key claims or patterns you noticed (optional)

(none — auto-filed, body has not been read)

---
*Filed by `scripts/scan-trusted.py` against `.github/ISSUE_TEMPLATE/source-submission.yml`*
"""

    cmd = [
        "gh", "issue", "create",
        "--repo", REPO_URL,
        "--title", title,
        "--body", body,
        "--label", "new-source",
        "--label", "source-submission",
        "--label", "trusted-feed",
    ]

    try:
        result = subprocess.run(cmd, check=True, capture_output=True, text=True)
        print(f"  Filed: {result.stdout.strip()}")
        return True
    except subprocess.CalledProcessError as e:
        print(
            f"  Failed to file issue for {entry['url']} "
            f"(exit {e.returncode}): {e.stderr.strip()}",
            file=sys.stderr,
        )
        return False


def scan_feed(feed: dict, state: dict, dry_run: bool = False) -> tuple[int, int, int]:
    """Scan one feed. Returns (new_entries_found, issues_filed, items_queued).

    The third element is items pushed to the global scan-queue.json because
    the daily-cap budget was exhausted before we got to them. Per-feed cap
    excess is *not* queued — it stays unread in the per-feed state and
    drains naturally on subsequent runs (existing behavior).
    """
    feed_id = feed["id"]
    print(f"\nFetching {feed_id}: {feed['url']}")

    xml_text = fetch_feed(feed["url"])
    if xml_text is None:
        return (0, 0, 0)

    entries = parse_entries(xml_text)
    print(f"  Parsed {len(entries)} entries")

    feed_state = state["feeds"].setdefault(feed_id, {"seen": [], "last_scan": None})
    seen_set = set(feed_state.get("seen", []))

    # New entries appear in the feed in newest-first order; we want to file
    # in chronological order so the oldest unread becomes the lowest-numbered
    # issue. Reverse before iterating.
    new_entries = [e for e in entries if e["id"] not in seen_set]
    new_entries.reverse()
    print(f"  {len(new_entries)} new since last scan")

    max_per_run = feed.get("max_per_run", DEFAULT_MAX_PER_RUN)
    to_file = new_entries[:max_per_run]
    if len(new_entries) > max_per_run:
        print(f"  Capping at {max_per_run}/run; remaining {len(new_entries) - max_per_run} will be picked up next run")

    filed = 0
    queued = 0
    for entry in to_file:
        # Check the global daily cap before each file. If exhausted, push
        # to the overflow queue instead of filing — the next daily run will
        # drain it via pop_queued_for("trusted", ...). We still mark the
        # entry as seen so the per-feed state doesn't re-discover it; the
        # queue is now the canonical home for that work item.
        if not dry_run and scan_budget.remaining() <= 0:
            scan_budget.queue_item("trusted", {"feed": feed, "entry": entry})
            queued += 1
            print(f"  [queued] daily cap reached: {entry['title'][:80]}")
            seen_set.add(entry["id"])
            continue

        if dry_run:
            print(f"  [DRY-RUN] would file: {entry['title'][:80]}  ({entry['url']})")
            filed += 1
        else:
            if file_issue(feed, entry):
                filed += 1
                scan_budget.record_filed(1)
        # Mark seen even if filing failed — we don't want to retry forever
        # against a known-broken entry. The dry-run path also marks seen so
        # repeated dry runs don't duplicate output; pass --reset-state if
        # you need to re-run.
        seen_set.add(entry["id"])

    feed_state["seen"] = sorted(seen_set)
    feed_state["last_scan"] = datetime.now(timezone.utc).isoformat()
    return (len(new_entries), filed, queued)


def drain_queue(dry_run: bool = False) -> int:
    """File items previously queued by this scanner. Returns count filed.

    Called at the start of main(), before any feed fetching, so that
    backlog from prior days flushes first while there's still budget.
    """
    budget = scan_budget.remaining()
    if budget <= 0:
        return 0

    queued_items = scan_budget.pop_queued_for("trusted", budget)
    if not queued_items:
        return 0

    print(f"Draining {len(queued_items)} queued trusted-feed item(s) from prior runs...")
    filed = 0
    for item in queued_items:
        payload = item.get("payload", {})
        feed = payload.get("feed", {})
        entry = payload.get("entry", {})
        if not feed or not entry:
            print(f"  WARN: skipping malformed queue item: {item}", file=sys.stderr)
            continue
        if dry_run:
            print(f"  [DRY-RUN] would refile from queue: {entry.get('title', '')[:80]}")
            filed += 1
            continue
        if file_issue(feed, entry):
            filed += 1
            scan_budget.record_filed(1)
    return filed


def main():
    parser = argparse.ArgumentParser(description="Scan curated trusted feeds for new entries.")
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Parse feeds and report what would be filed, without calling `gh`.",
    )
    parser.add_argument(
        "--feed",
        help="Only scan the feed with this id (for debugging a single source).",
    )
    args = parser.parse_args()

    feeds_data = load_feeds()
    state = load_state()

    feeds = feeds_data.get("feeds", [])
    if args.feed:
        feeds = [f for f in feeds if f["id"] == args.feed]
        if not feeds:
            print(f"ERROR: no feed with id={args.feed} in {FEEDS_PATH}", file=sys.stderr)
            sys.exit(1)

    print(f"scan-trusted starting: {scan_budget.status_summary()}")

    # Drain any backlog this scanner queued in previous runs first, so the
    # oldest unread entries get filed before we discover anything new today.
    drained = drain_queue(dry_run=args.dry_run)
    if drained:
        print(f"Refiled {drained} item(s) from queue. {scan_budget.status_summary()}")

    print(f"Scanning {len(feeds)} trusted feed(s)...")

    total_new = 0
    total_filed = 0
    total_queued = 0
    for i, feed in enumerate(feeds):
        try:
            new, filed, queued = scan_feed(feed, state, dry_run=args.dry_run)
            total_new += new
            total_filed += filed
            total_queued += queued
        except Exception as e:
            # Don't let one bad feed kill the whole scan.
            print(f"  ERROR scanning {feed.get('id', '?')}: {e}", file=sys.stderr)
        if i < len(feeds) - 1:
            time.sleep(INTER_FEED_SLEEP)

    state["last_scan"] = datetime.now(timezone.utc).isoformat()
    if not args.dry_run:
        save_state(state)

    print(
        f"\nScan complete: {total_new} new entries across {len(feeds)} feed(s), "
        f"{total_filed} issue(s) filed, {total_queued} queued for next run"
    )
    print(f"Final budget: {scan_budget.status_summary()}")


if __name__ == "__main__":
    main()
