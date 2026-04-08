"""
Daily-cap budget + overflow queue for the discovery scanners.

The three discovery scanners (scan-repos.py, scan-failures.py, scan-trusted.py)
all file GitHub issues into the same Pipeline 1 triage funnel. Run together
on a daily schedule, they can burst dozens of issues at once — especially
when a new trusted feed adds 30 unread items, or HN search lights up after
a Hacker News thread about agent failures.

This module is the single shared rate limiter:

* `registry/scan-state.json` tracks how many issues have been filed today
  across ALL scanners. Reset automatically at the start of a new UTC day.
* `registry/scan-queue.json` holds items the scanners discovered but could
  not file because the daily cap was already hit. Each queue entry carries
  enough payload for the originating scanner to re-file it on the next run.

The default cap is 5 issues/day, overridable via the `DAILY_SCAN_CAP`
environment variable (set in the workflow).

Usage from a scanner:

    import scan_budget

    # 1. At start of main(): drain whatever this scanner queued previously.
    queued = scan_budget.pop_queued_for("trusted", scan_budget.remaining())
    for item in queued:
        ...refile from item["payload"]...
        scan_budget.record_filed(1)

    # 2. During fresh discovery: check budget before each file.
    if scan_budget.remaining() <= 0:
        scan_budget.queue_item("trusted", {"feed": feed, "entry": entry})
        continue
    file_issue(feed, entry)
    scan_budget.record_filed(1)

The module is intentionally standard-library only and lives next to the
scanners so `import scan_budget` works without any sys.path gymnastics.
"""

import json
import os
from datetime import date, datetime, timezone
from pathlib import Path

REGISTRY_DIR = Path(__file__).parent.parent / "registry"
STATE_PATH = REGISTRY_DIR / "scan-state.json"
QUEUE_PATH = REGISTRY_DIR / "scan-queue.json"

DEFAULT_DAILY_CAP = 5


def _today_str() -> str:
    """Today in UTC as YYYY-MM-DD. Use UTC so the daily reset is stable
    regardless of which runner timezone the workflow lands on."""
    return datetime.now(timezone.utc).date().isoformat()


def get_daily_cap() -> int:
    """Resolve the daily issue-filing cap.

    Resolution order: DAILY_SCAN_CAP env var → persisted state → default.
    Env var wins so the workflow can override without editing state files.
    """
    env = os.environ.get("DAILY_SCAN_CAP")
    if env:
        try:
            return int(env)
        except ValueError:
            pass
    state = _load_state()
    return state.get("daily_cap", DEFAULT_DAILY_CAP)


def _load_state() -> dict:
    if STATE_PATH.exists():
        try:
            with open(STATE_PATH) as f:
                return json.load(f)
        except (json.JSONDecodeError, OSError):
            # Corrupted/unreadable — start fresh rather than crashing the
            # whole daily run. The next save_state will overwrite cleanly.
            pass
    return {"date": None, "filed_today": 0, "daily_cap": DEFAULT_DAILY_CAP}


def _save_state(state: dict) -> None:
    REGISTRY_DIR.mkdir(parents=True, exist_ok=True)
    with open(STATE_PATH, "w") as f:
        json.dump(state, f, indent=2)


def _load_queue() -> dict:
    if QUEUE_PATH.exists():
        try:
            with open(QUEUE_PATH) as f:
                return json.load(f)
        except (json.JSONDecodeError, OSError):
            pass
    return {"items": []}


def _save_queue(queue: dict) -> None:
    REGISTRY_DIR.mkdir(parents=True, exist_ok=True)
    with open(QUEUE_PATH, "w") as f:
        json.dump(queue, f, indent=2)


def reset_if_new_day() -> None:
    """If the persisted date is not today's UTC date, reset filed_today=0.

    Safe to call repeatedly — it's a no-op once the state already matches.
    """
    state = _load_state()
    today = _today_str()
    if state.get("date") != today:
        state["date"] = today
        state["filed_today"] = 0
        state["daily_cap"] = get_daily_cap()
        _save_state(state)


def remaining() -> int:
    """How many more issues can be filed today, across all scanners."""
    reset_if_new_day()
    state = _load_state()
    cap = get_daily_cap()
    return max(0, cap - state.get("filed_today", 0))


def record_filed(n: int = 1) -> None:
    """Increment the daily counter by n. Call once per successful file_issue."""
    if n <= 0:
        return
    reset_if_new_day()
    state = _load_state()
    state["filed_today"] = state.get("filed_today", 0) + n
    # Keep daily_cap fresh so the JSON record is self-describing.
    state["daily_cap"] = get_daily_cap()
    _save_state(state)


def queue_item(scanner: str, payload: dict) -> None:
    """Append an item to the overflow queue for the next daily run.

    `scanner` identifies the originating scanner ("repos", "failures",
    "trusted") so the next run's pop_queued_for() can route items back
    to the right re-filer. `payload` is whatever JSON-serializable shape
    the originating scanner needs to reconstruct the file_issue call.
    """
    queue = _load_queue()
    queue.setdefault("items", []).append({
        "scanner": scanner,
        "queued_at": datetime.now(timezone.utc).isoformat(),
        "payload": payload,
    })
    _save_queue(queue)


def pop_queued_for(scanner: str, max_n: int) -> list:
    """Remove and return up to max_n queued items for a given scanner (FIFO).

    Items not belonging to `scanner` are left in the queue untouched, so
    each scanner only drains its own backlog and the queue is processed
    in scanner-order across the daily run.
    """
    if max_n <= 0:
        return []
    queue = _load_queue()
    items = queue.get("items", [])
    matching = [i for i, item in enumerate(items) if item.get("scanner") == scanner]
    take_indices = set(matching[:max_n])
    popped = [items[i] for i in sorted(take_indices)]
    queue["items"] = [item for i, item in enumerate(items) if i not in take_indices]
    _save_queue(queue)
    return popped


def status_summary() -> str:
    """Human-readable one-liner for scanner stdout logging."""
    reset_if_new_day()
    state = _load_state()
    queue = _load_queue()
    cap = get_daily_cap()
    return (
        f"daily-cap={cap} filed_today={state.get('filed_today', 0)} "
        f"remaining={remaining()} queued={len(queue.get('items', []))}"
    )
