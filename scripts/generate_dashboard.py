#!/usr/bin/env python3
"""Daily DASHBOARD.md generator — content-derived guide metrics.

Reads ``source-notes/`` frontmatter, ``guide/*.md`` markdown, and the local
git history to compute four metrics per chapter that GitHub Projects can't
show natively:

1. **Source count vs cap** — number of unique source-note slugs cited in the
   chapter, against ``guide.max_sources_per_chapter`` from
   ``hitchhiker.config.json``. Mirrors ``check_chapter_source_cap.py``.
2. **Oldest source** — earliest ``date_published`` among the chapter's cited
   source notes. Surfaces decay candidates for the Gardener.
3. **Staleness percentage** — fraction of cited source notes whose
   ``last_checked`` is more than 90 days old (matches the ``[stale]`` tag
   semantics in README.md).
4. **Weekly line-count delta** — chapter line count today vs. the most recent
   commit from at least 7 days ago. Cheap proxy for "is this chapter
   actively churning."

Run by ``.github/workflows/daily-scan.yml`` once per UTC day; the workflow
commits the regenerated ``DASHBOARD.md`` alongside the registry/state diff.
Linked from README.md alongside the GitHub Project link. See bead hi-4yk.18.
"""

from __future__ import annotations

import json
import re
import subprocess
import sys
from datetime import date, datetime, timezone
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
GUIDE_DIR = REPO_ROOT / "guide"
SOURCE_NOTES_DIR = REPO_ROOT / "source-notes"
CONFIG_PATH = REPO_ROOT / "hitchhiker.config.json"
DASHBOARD_PATH = REPO_ROOT / "DASHBOARD.md"

# Citation regex matches ``[source: foo, bar (Claim 5)] [grade]``. Kept in
# sync with scripts/check_chapter_source_cap.py and scripts/gardener.py.
GRADES = ("settled", "emerging", "anecdotal", "editorial", "stale")
CITATION_RE = re.compile(
    r"\[source:\s*([^\]]+?)\]\s*\[(" + "|".join(GRADES) + r")\]"
)
DATE_PUBLISHED_RE = re.compile(r"^date_published:\s*(\d{4}-\d{2}-\d{2})", re.M)
LAST_CHECKED_RE = re.compile(r"^last_checked:\s*(\d{4}-\d{2}-\d{2})", re.M)

# Matches the README.md trust-model definition of `[stale]`: source is older
# than 90 days and hasn't been re-verified.
STALE_DAYS = 90


def load_cap() -> int:
    return int(json.loads(CONFIG_PATH.read_text())["guide"]["max_sources_per_chapter"])


def parse_frontmatter_date(path: Path, regex: re.Pattern[str]) -> date | None:
    """Pull a YYYY-MM-DD date out of a source-note's YAML frontmatter.

    Returns ``None`` if the file has no frontmatter or the field is missing
    — both are real cases (a few practitioner profiles ship without YAML).
    """
    text = path.read_text()
    if not text.startswith("---\n"):
        return None
    end = text.find("\n---\n", 4)
    if end == -1:
        return None
    match = regex.search(text[:end])
    if not match:
        return None
    try:
        return datetime.strptime(match.group(1), "%Y-%m-%d").date()
    except ValueError:
        return None


def collect_source_notes() -> dict[str, tuple[date | None, date | None]]:
    """Map ``slug -> (date_published, last_checked)`` for every source note."""
    notes: dict[str, tuple[date | None, date | None]] = {}
    for path in SOURCE_NOTES_DIR.glob("*.md"):
        if path.name.startswith("."):
            continue
        notes[path.stem] = (
            parse_frontmatter_date(path, DATE_PUBLISHED_RE),
            parse_frontmatter_date(path, LAST_CHECKED_RE),
        )
    return notes


def chapter_sources(chapter: Path, known: set[str]) -> set[str]:
    """Return the set of source-note slugs cited in ``chapter``.

    Splits on commas inside ``[source: ...]`` and strips trailing
    parenthetical qualifiers like ``(Claim 5)`` so the leftover token can be
    matched against actual filenames on disk. Identical extraction logic to
    check_chapter_source_cap.py.
    """
    found: set[str] = set()
    for match in CITATION_RE.finditer(chapter.read_text()):
        for part in match.group(1).split(","):
            cleaned = re.sub(r"\s*\(.*\)\s*$", "", part.strip())
            if cleaned in known:
                found.add(cleaned)
    return found


def commit_a_week_ago() -> str | None:
    """SHA of the most recent commit from at least 7 days before HEAD.

    Returns ``None`` if the repo is younger than a week or git is unhappy —
    callers downgrade the line-delta column to "n/a" in that case rather
    than failing the whole report.
    """
    try:
        out = subprocess.check_output(
            ["git", "-C", str(REPO_ROOT), "rev-list", "-1",
             "--before=7.days.ago", "HEAD"],
            stderr=subprocess.DEVNULL,
        )
    except (subprocess.CalledProcessError, FileNotFoundError):
        return None
    return out.decode().strip() or None


def line_count_at(chapter: Path, ref: str) -> int | None:
    """Line count of ``chapter`` at git ``ref``, or ``None`` if absent then."""
    rel = chapter.relative_to(REPO_ROOT).as_posix()
    try:
        out = subprocess.check_output(
            ["git", "-C", str(REPO_ROOT), "show", f"{ref}:{rel}"],
            stderr=subprocess.DEVNULL,
        )
    except (subprocess.CalledProcessError, FileNotFoundError):
        return None
    return out.decode().count("\n")


def render(chapters: list[Path], today: date) -> str:
    cap = load_cap()
    notes = collect_source_notes()
    known = set(notes)
    week_ref = commit_a_week_ago()

    rows = []
    for chapter in chapters:
        slugs = chapter_sources(chapter, known)
        dated = sorted((notes[s][0], s) for s in slugs if notes[s][0])
        oldest_date, oldest_slug = dated[0] if dated else (None, None)
        checked = [notes[s][1] for s in slugs if notes[s][1]]
        stale = sum(1 for d in checked if (today - d).days > STALE_DAYS)
        stale_pct = (stale * 100 // len(checked)) if checked else 0
        cur_lines = chapter.read_text().count("\n")
        prev_lines = line_count_at(chapter, week_ref) if week_ref else None
        delta = cur_lines - prev_lines if prev_lines is not None else None
        rows.append({
            "rel": chapter.relative_to(REPO_ROOT).as_posix(),
            "count": len(slugs),
            "oldest_date": oldest_date,
            "oldest_slug": oldest_slug,
            "stale_pct": stale_pct,
            "lines": cur_lines,
            "delta": delta,
        })

    out = [
        "# Guide Dashboard",
        "",
        f"_Generated {today.isoformat()} (UTC) by `scripts/generate_dashboard.py`._",
        "",
        "Content-derived metrics for the living guide. Refreshed daily by",
        "`.github/workflows/daily-scan.yml`. For workflow status (PRs, issues,",
        "scanner queues) see the GitHub Project linked from README.md.",
        "",
        "| Chapter | Sources | Oldest source | Stale % | Lines (Δ7d) |",
        "|---|---|---|---|---|",
    ]
    for r in rows:
        sat_marker = " ⚠" if r["count"] >= cap else ""
        if r["oldest_date"]:
            oldest = f"{r['oldest_date'].isoformat()} (`{r['oldest_slug']}`)"
        else:
            oldest = "—"
        if r["delta"] is None:
            delta_cell = f"{r['lines']} (n/a)"
        else:
            delta_cell = f"{r['lines']} ({r['delta']:+d})"
        out.append(
            f"| `{r['rel']}` | {r['count']}/{cap}{sat_marker} | {oldest} | "
            f"{r['stale_pct']}% | {delta_cell} |"
        )
    out += [
        "",
        f"**Source cap**: {cap} per chapter (see `hitchhiker.config.json`). ",
        f"Chapters at the cap are marked ⚠ and block new Smith additions until ",
        f"the Gardener prunes.",
        "",
        f"**Staleness**: percentage of cited source notes whose `last_checked` ",
        f"frontmatter field is more than {STALE_DAYS} days old. Matches the ",
        "`[stale]` confidence tag defined in README.md.",
        "",
        f"**Δ7d**: line-count delta vs. the most recent commit from at least 7 ",
        "days ago. `n/a` means the repo (or this chapter) is younger than a week.",
        "",
    ]
    return "\n".join(out)


def main() -> int:
    chapters = sorted(
        p for p in GUIDE_DIR.glob("*.md")
        if p.name not in ("SOURCES.md", "DASHBOARD.md")
    )
    today = datetime.now(timezone.utc).date()
    DASHBOARD_PATH.write_text(render(chapters, today))
    rel = DASHBOARD_PATH.relative_to(REPO_ROOT)
    print(f"wrote {rel} ({len(chapters)} chapters)", file=sys.stderr)
    return 0


if __name__ == "__main__":
    sys.exit(main())
