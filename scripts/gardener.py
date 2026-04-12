#!/usr/bin/env python3
"""Weekly Gardener: staleness sweep for source notes + guide claims.

Walks every source note in ``source-notes/``, checks its front-matter date,
and tags notes whose ``last_checked`` is more than 90 days old as
``status: stale``. Then walks the guide chapters, finds inline citations to
those stale sources, and demotes the confidence grade one step on this
ladder::

    settled  -> emerging
    emerging -> stale
    stale    -> stale          (floor)
    anecdotal -> anecdotal     (off-ladder; never demoted)
    editorial -> editorial     (off-ladder; never demoted)

``anecdotal`` and ``editorial`` are deliberately off the ladder. They
already encode "weak evidence" / "guide opinion"; demoting them to
``stale`` would lose that distinction.

Demotion runs every week against the *full* set of currently-stale source
notes (not just notes newly tagged this run), so a citation that was at
``[settled]`` ratchets through ``[emerging]`` -> ``[stale]`` over two
consecutive weekly runs without anyone re-checking the source in between.
Once a citation reaches ``[stale]`` it is at the floor and the gardener
stops touching it.

File mutations land in-place. The caller (a GitHub Actions workflow) is
responsible for opening a PR labeled ``guide-update`` so the Assayer can
re-grade the demoted claims before the changes merge.

Per ``agents/GARDENER.md`` this run tags at most 20 newly-stale notes
(oldest ``last_checked`` first) so a single weekly pass cannot demote
everything in one go.
"""

from __future__ import annotations

import argparse
import re
import sys
from datetime import date, datetime, timezone
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
SOURCE_NOTES_DIR = REPO_ROOT / "source-notes"
GUIDE_DIR = REPO_ROOT / "guide"
STICKY_NOTES_DIR = REPO_ROOT / "sticky-notes"

STALENESS_DAYS = 90
WEEKLY_TAGGING_BUDGET = 20
STICKY_STALE_DAYS = 90
STICKY_ARCHIVE_DAYS = 30

# Demotion ladder. Off-ladder grades (anecdotal, editorial) are passthrough --
# see module docstring.
DEMOTE: dict[str, str] = {
    "settled": "emerging",
    "emerging": "stale",
    "stale": "stale",
}

GRADES = ("settled", "emerging", "anecdotal", "editorial", "stale")

# `[source: foo, bar] [grade]` -- captures the source list and the grade
# separately so we can rewrite the grade in place.
CITATION_RE = re.compile(
    r"\[source:\s*([^\]]+?)\]\s*\[(" + "|".join(GRADES) + r")\]"
)


# ---------------------------------------------------------------------------
# Front-matter parsing
# ---------------------------------------------------------------------------


def parse_frontmatter(text: str) -> tuple[dict[str, str], int]:
    """Return ``(frontmatter dict, fm_end_line_index)``.

    Returns ``({}, -1)`` if there is no ``---``-delimited frontmatter block.
    The parser is intentionally simple: only ``key: value`` lines are
    recognized -- which is all the source notes in this repo use.
    """
    lines = text.splitlines()
    if not lines or lines[0].strip() != "---":
        return {}, -1
    end = -1
    for i in range(1, len(lines)):
        if lines[i].strip() == "---":
            end = i
            break
    if end == -1:
        return {}, -1
    fm: dict[str, str] = {}
    for line in lines[1:end]:
        if ":" not in line:
            continue
        k, _, v = line.partition(":")
        fm[k.strip()] = v.strip()
    return fm, end


def render_frontmatter(
    updates: dict[str, str], original_lines: list[str], fm_end: int
) -> list[str]:
    """Rewrite the frontmatter, replacing only the values in ``updates``.

    Lines that aren't ``key: value`` (e.g. blank lines, comments) are
    preserved verbatim so a Gardener edit produces a minimal diff.
    """
    out = ["---"]
    seen: set[str] = set()
    for line in original_lines[1:fm_end]:
        if ":" in line:
            k = line.split(":", 1)[0].strip()
            if k in updates and k not in seen:
                out.append(f"{k}: {updates[k]}")
                seen.add(k)
                continue
        out.append(line)
    # Append any keys the gardener wants to add that didn't exist yet.
    for k, v in updates.items():
        if k not in seen:
            out.append(f"{k}: {v}")
    out.append("---")
    return out


def parse_iso_date(value: str) -> date | None:
    """Parse ``YYYY-MM-DD``; return None if value is missing or unparseable."""
    if not value:
        return None
    value = value.strip().strip('"').strip("'")
    try:
        return datetime.strptime(value, "%Y-%m-%d").date()
    except ValueError:
        return None


def days_old(d: date, today: date) -> int:
    return (today - d).days


# ---------------------------------------------------------------------------
# Sticky-note helpers
# ---------------------------------------------------------------------------


def slugify(heading: str) -> str:
    """Convert a Markdown heading to a slug for §-reference matching.

    Example: ``'Verification Over Generation'`` → ``'verification-over-generation'``
    """
    text = heading.strip().lower()
    text = re.sub(r"[^\w\s-]", "", text)
    text = re.sub(r"[\s]+", "-", text)
    return text.strip("-")


def sticky_to_guide_path(sticky_path: Path) -> Path:
    """Map ``sticky-notes/chNN-name.md`` → ``guide/NN-name.md``."""
    return GUIDE_DIR / sticky_path.name[2:]


def get_chapter_headings(chapter_path: Path) -> set[str]:
    """Return the set of slugified headings from a guide chapter."""
    if not chapter_path.exists():
        return set()
    headings: set[str] = set()
    for line in chapter_path.read_text().splitlines():
        m = re.match(r"^#{1,6}\s+(.+)$", line)
        if m:
            headings.add(slugify(m.group(1)))
    return headings


_SN_HEADING_RE = re.compile(r"^##\s+(SN-\d{2}-\d{3}):\s+(.+)$")
_SN_META_RE = re.compile(r"^-\s+\*\*(\w[\w\s]*?)\*\*:\s*(.+)$")


def parse_sticky_file(text: str) -> list[dict]:
    """Parse individual sticky notes from a chapter file.

    Returns a list of dicts with keys: ``id``, ``title``, ``start_line``,
    ``end_line``, ``created``, ``status``, ``section``, ``type``,
    ``resolved_date``, ``in_archive``.
    """
    lines = text.splitlines()
    notes: list[dict] = []
    current: dict | None = None
    in_archive = False

    for i, line in enumerate(lines):
        # Detect ## Archive boundary.
        if line.strip() == "## Archive":
            in_archive = True
            if current is not None:
                current["end_line"] = i
                notes.append(current)
                current = None
            continue

        heading = _SN_HEADING_RE.match(line)
        if heading:
            if current is not None:
                current["end_line"] = i
                notes.append(current)
            current = {
                "id": heading.group(1),
                "title": heading.group(2),
                "start_line": i,
                "end_line": len(lines),
                "created": None,
                "status": None,
                "section": None,
                "type": None,
                "resolved_date": None,
                "in_archive": in_archive,
            }
            continue

        # Any non-SN ## heading terminates the current note.
        if line.startswith("## ") and current is not None:
            current["end_line"] = i
            notes.append(current)
            current = None
            continue

        if current is None:
            continue

        meta = _SN_META_RE.match(line)
        if meta is None:
            continue

        key, val = meta.group(1).strip(), meta.group(2).strip()
        if key == "Created":
            current["created"] = val
        elif key == "Status":
            current["status"] = val
        elif key == "Section":
            sec = re.search(r"§([\w-]+)", val)
            if sec:
                current["section"] = sec.group(1)
        elif key == "Type":
            current["type"] = val
        elif key == "Resolved":
            dm = re.match(r"(\d{4}-\d{2}-\d{2})", val)
            if dm:
                current["resolved_date"] = dm.group(1)

    if current is not None:
        notes.append(current)

    return notes


# ---------------------------------------------------------------------------
# Source-note staleness pass
# ---------------------------------------------------------------------------


def gardener_source_pass(
    today: date, dry_run: bool
) -> tuple[dict[str, dict], dict[str, dict]]:
    """Tag newly-stale source notes and return (newly_tagged, all_stale).

    ``newly_tagged`` is the set of notes whose status flipped to ``stale``
    on this run (subject to the WEEKLY_TAGGING_BUDGET cap). ``all_stale``
    is the set of notes that are stale *after* this pass -- whether tagged
    by this run or a previous one. The guide-demotion pass uses
    ``all_stale`` so a citation grade can ratchet down across multiple
    weekly runs.
    """
    candidates: list[tuple[date, Path, dict[str, str], list[str], int]] = []
    all_stale: dict[str, dict] = {}

    for note_path in sorted(SOURCE_NOTES_DIR.glob("*.md")):
        # Skip dotfile templates (`.template-*.md`) -- not real source notes.
        if note_path.name.startswith("."):
            continue
        text = note_path.read_text()
        fm, fm_end = parse_frontmatter(text)
        if fm_end == -1:
            print(f"  skip (no frontmatter): {note_path.name}", file=sys.stderr)
            continue

        # Prefer last_checked, fall back to date_extracted.
        ref_date = parse_iso_date(fm.get("last_checked", "")) or parse_iso_date(
            fm.get("date_extracted", "")
        )
        if ref_date is None:
            print(f"  skip (no usable date): {note_path.name}", file=sys.stderr)
            continue

        age = days_old(ref_date, today)
        already_stale = fm.get("status", "current") == "stale"

        if already_stale:
            all_stale[note_path.stem] = {
                "path": str(note_path.relative_to(REPO_ROOT)),
                "last_checked": ref_date.isoformat(),
                "age_days": age,
                "newly_tagged": False,
            }
            continue

        if age > STALENESS_DAYS:
            candidates.append((ref_date, note_path, fm, text.splitlines(), fm_end))

    # Oldest first; cap to weekly budget.
    candidates.sort(key=lambda c: c[0])
    deferred = max(0, len(candidates) - WEEKLY_TAGGING_BUDGET)
    capped = candidates[:WEEKLY_TAGGING_BUDGET]

    newly_tagged: dict[str, dict] = {}
    for ref_date, note_path, fm, lines, fm_end in capped:
        fm["status"] = "stale"
        new_fm_lines = render_frontmatter(fm, lines, fm_end)
        # Reassemble: new frontmatter + body. ``lines`` came from splitlines()
        # so it has no trailing newline; we add one if the original had one.
        original_text = note_path.read_text()
        body = lines[fm_end + 1 :]
        new_text = "\n".join(new_fm_lines + body)
        if original_text.endswith("\n") and not new_text.endswith("\n"):
            new_text += "\n"
        if not dry_run:
            note_path.write_text(new_text)

        record = {
            "path": str(note_path.relative_to(REPO_ROOT)),
            "last_checked": ref_date.isoformat(),
            "age_days": days_old(ref_date, today),
            "newly_tagged": True,
        }
        newly_tagged[note_path.stem] = record
        all_stale[note_path.stem] = record
        print(
            f"  STALE: {note_path.name} "
            f"(last_checked={ref_date.isoformat()}, {record['age_days']}d old)"
        )

    if deferred:
        print(
            f"  (deferred {deferred} more newly-stale note(s) to next weekly run; "
            f"budget={WEEKLY_TAGGING_BUDGET})"
        )

    return newly_tagged, all_stale


# ---------------------------------------------------------------------------
# Guide-claim demotion pass
# ---------------------------------------------------------------------------


def collect_source_note_names() -> set[str]:
    """Filenames (without ``.md``) of every source note on disk."""
    return {
        p.stem
        for p in SOURCE_NOTES_DIR.glob("*.md")
        if not p.name.startswith(".")
    }


def extract_source_names(citation_body: str, known_notes: set[str]) -> list[str]:
    """From the inside of ``[source: ...]``, return note names that exist.

    A citation body looks like ``foo-note, bar-note, Claim 5`` or
    ``foo-note, Linked Source 6 (Comprehension Debt)``. We split on commas,
    strip trailing parenthetical qualifiers, and keep only the tokens that
    match a real source-note filename. Qualifiers like "Claim 5" or
    "Linked Source 6" naturally fall away because they aren't files.
    """
    parts = [p.strip() for p in citation_body.split(",")]
    names: list[str] = []
    for p in parts:
        p = re.sub(r"\s*\(.*\)\s*$", "", p)
        if p in known_notes:
            names.append(p)
    return names


def demote_guide_claims(
    stale_notes: set[str], dry_run: bool
) -> list[dict]:
    """Walk ``guide/*.md`` and demote citations whose source list intersects
    ``stale_notes``. Returns a list of demotion records for the PR body."""
    demotions: list[dict] = []
    if not stale_notes:
        return demotions

    known_notes = collect_source_note_names()

    for guide_path in sorted(GUIDE_DIR.glob("*.md")):
        original = guide_path.read_text()
        new_lines: list[str] = []
        changed = False

        for line_no, line in enumerate(original.splitlines(), start=1):
            new_line = line
            # Track how much earlier rewrites on the same line have shifted
            # subsequent match positions.
            offset = 0
            for m in CITATION_RE.finditer(line):
                cited = extract_source_names(m.group(1), known_notes)
                if not any(name in stale_notes for name in cited):
                    continue
                old_grade = m.group(2)
                new_grade = DEMOTE.get(old_grade, old_grade)
                if new_grade == old_grade:
                    continue  # already at floor or off-ladder
                start = m.start(2) + offset
                end = m.end(2) + offset
                new_line = new_line[:start] + new_grade + new_line[end:]
                offset += len(new_grade) - len(old_grade)
                changed = True
                demotions.append(
                    {
                        "file": str(guide_path.relative_to(REPO_ROOT)),
                        "line": line_no,
                        "sources": cited,
                        "from": old_grade,
                        "to": new_grade,
                    }
                )
            new_lines.append(new_line)

        if changed and not dry_run:
            new_text = "\n".join(new_lines)
            if original.endswith("\n"):
                new_text += "\n"
            guide_path.write_text(new_text)

    return demotions


# ---------------------------------------------------------------------------
# Sticky-note staleness pass
# ---------------------------------------------------------------------------


def _apply_archives(
    lines: list[str], notes_to_archive: list[dict]
) -> list[str]:
    """Move archived note blocks to an ``## Archive`` section at the bottom."""
    archive_blocks: list[list[str]] = []
    # Process from bottom to top so earlier indices stay valid.
    ranges = sorted(
        [(n["start_line"], n["end_line"]) for n in notes_to_archive],
        reverse=True,
    )
    for start, end in ranges:
        archive_blocks.insert(0, lines[start:end])
        del lines[start:end]

    # Ensure ## Archive heading exists.
    if not any(line.strip() == "## Archive" for line in lines):
        lines.append("")
        lines.append("## Archive")

    # Append archived notes at the very end.
    for block in archive_blocks:
        lines.append("")
        lines.extend(block)

    return lines


def gardener_sticky_pass(
    today: date, dry_run: bool
) -> dict[str, list[dict]]:
    """Run sticky-note staleness checks.

    Checks performed (per ``agents/GARDENER.md``):

    1. Active notes >90 days old whose ``§section-name`` no longer matches a
       heading in the guide chapter → mark ``stale``.
    2. Any active note whose ``§section-name`` doesn't match a heading →
       mark ``stale`` (regardless of age).
    3. Resolved notes >30 days old → move to ``## Archive``.
    4. Already-stale notes (from a prior run) → flag for attention.

    Returns ``{"marked_stale": [...], "archived": [...], "stale_alerts": [...]}``.
    """
    marked_stale: list[dict] = []
    archived: list[dict] = []
    stale_alerts: list[dict] = []
    result: dict[str, list[dict]] = {
        "marked_stale": marked_stale,
        "archived": archived,
        "stale_alerts": stale_alerts,
    }

    if not STICKY_NOTES_DIR.exists():
        return result

    for sn_path in sorted(STICKY_NOTES_DIR.glob("ch*.md")):
        text = sn_path.read_text()
        notes = parse_sticky_file(text)
        if not notes:
            continue

        guide_path = sticky_to_guide_path(sn_path)
        headings = get_chapter_headings(guide_path)
        lines = text.splitlines()
        changed = False
        to_archive: list[dict] = []
        newly_stale_ids: set[str] = set()

        for note in notes:
            if note["in_archive"]:
                continue

            status = note["status"]
            created = parse_iso_date(note["created"] or "")

            if status == "active":
                # Checks 1 & 2: §section must match a chapter heading.
                section = note.get("section")
                if section and section not in headings:
                    age_str = (
                        f", {days_old(created, today)}d old" if created else ""
                    )
                    reason = f"§{section} not found in {guide_path.name}{age_str}"
                    for li in range(note["start_line"], note["end_line"]):
                        if "**Status**:" in lines[li] and "active" in lines[li]:
                            lines[li] = lines[li].replace("active", "stale")
                            changed = True
                            break
                    newly_stale_ids.add(note["id"])
                    marked_stale.append(
                        {
                            "file": sn_path.name,
                            "id": note["id"],
                            "title": note["title"],
                            "section": section,
                            "reason": reason,
                        }
                    )
                    print(
                        f"  STALE: {note['id']} in {sn_path.name} — {reason}"
                    )

            elif status == "resolved":
                # Check 3: resolved >30 days → archive.
                resolved = parse_iso_date(note.get("resolved_date") or "")
                if resolved and days_old(resolved, today) > STICKY_ARCHIVE_DAYS:
                    to_archive.append(note)
                    archived.append(
                        {
                            "file": sn_path.name,
                            "id": note["id"],
                            "title": note["title"],
                        }
                    )
                    print(
                        f"  ARCHIVE: {note['id']} in {sn_path.name} "
                        f"(resolved {note['resolved_date']})"
                    )

            elif status == "stale" and note["id"] not in newly_stale_ids:
                # Check 4: already-stale notes → flag for attention.
                stale_alerts.append(
                    {
                        "file": sn_path.name,
                        "id": note["id"],
                        "title": note["title"],
                    }
                )

        if to_archive:
            lines = _apply_archives(lines, to_archive)
            changed = True

        if changed and not dry_run:
            new_text = "\n".join(lines)
            if text.endswith("\n") and not new_text.endswith("\n"):
                new_text += "\n"
            sn_path.write_text(new_text)

    return result


# ---------------------------------------------------------------------------
# Reporting
# ---------------------------------------------------------------------------


def write_markdown_summary(
    newly_tagged: dict[str, dict],
    all_stale: dict[str, dict],
    demotions: list[dict],
    sticky_results: dict[str, list[dict]],
    today: date,
    fp,
) -> None:
    """Markdown report suitable for use as a GitHub PR body."""
    fp.write(f"## Gardener weekly run -- {today.isoformat()}\n\n")
    fp.write(
        f"_Staleness threshold: {STALENESS_DAYS} days. "
        f"Tagging budget: {WEEKLY_TAGGING_BUDGET} note(s)/week._\n\n"
    )

    fp.write("### Newly stale source notes\n\n")
    if not newly_tagged:
        fp.write("_None this week._\n\n")
    else:
        fp.write("| Source note | Last checked | Age |\n")
        fp.write("|---|---|---|\n")
        for name in sorted(newly_tagged):
            info = newly_tagged[name]
            fp.write(
                f"| `{info['path']}` | {info['last_checked']} | "
                f"{info['age_days']}d |\n"
            )
        fp.write("\n")

    carry_over = sorted(n for n in all_stale if not all_stale[n]["newly_tagged"])
    if carry_over:
        fp.write(
            f"### Carry-over stale notes (still stale from earlier runs)\n\n"
            f"{len(carry_over)} note(s) still tagged stale: "
            + ", ".join(f"`{n}`" for n in carry_over)
            + "\n\n"
        )

    fp.write("### Demoted citations\n\n")
    if not demotions:
        fp.write("_No citations were demoted this run._\n\n")
    else:
        fp.write("| File | Line | Sources cited | Demotion |\n")
        fp.write("|---|---|---|---|\n")
        for d in demotions:
            srcs = ", ".join(f"`{s}`" for s in d["sources"])
            fp.write(
                f"| `{d['file']}` | {d['line']} | {srcs} | "
                f"`[{d['from']}]` -> `[{d['to']}]` |\n"
            )
        fp.write("\n")

    # Sticky-note staleness results
    sn_stale = sticky_results.get("marked_stale", [])
    sn_archived = sticky_results.get("archived", [])
    sn_alerts = sticky_results.get("stale_alerts", [])

    if sn_stale or sn_archived or sn_alerts:
        fp.write("### Sticky-note staleness\n\n")

        if sn_stale:
            fp.write("**Marked stale** (§section no longer in chapter):\n\n")
            fp.write("| File | ID | Title | Reason |\n")
            fp.write("|---|---|---|---|\n")
            for s in sn_stale:
                fp.write(
                    f"| `{s['file']}` | {s['id']} | {s['title']} | "
                    f"{s['reason']} |\n"
                )
            fp.write("\n")

        if sn_archived:
            fp.write("**Archived** (resolved >30 days):\n\n")
            fp.write("| File | ID | Title |\n")
            fp.write("|---|---|---|\n")
            for a in sn_archived:
                fp.write(f"| `{a['file']}` | {a['id']} | {a['title']} |\n")
            fp.write("\n")

        if sn_alerts:
            fp.write(
                "**Stale notes needing attention** "
                "(stale from prior run, no human action):\n\n"
            )
            fp.write("| File | ID | Title |\n")
            fp.write("|---|---|---|\n")
            for a in sn_alerts:
                fp.write(f"| `{a['file']}` | {a['id']} | {a['title']} |\n")
            fp.write("\n")

    fp.write(
        "---\n"
        "Generated by `scripts/gardener.py`. See `agents/GARDENER.md` for the "
        "Gardener spec.\n"
    )


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Compute staleness + demotions without writing any files.",
    )
    parser.add_argument(
        "--today",
        type=str,
        default=None,
        help="Override today's date (YYYY-MM-DD). Useful for tests.",
    )
    parser.add_argument(
        "--report-file",
        type=Path,
        default=None,
        help="Write a markdown summary to this path (e.g. for a PR body).",
    )
    args = parser.parse_args(argv)

    if args.today is not None:
        today = parse_iso_date(args.today)
        if today is None:
            print(f"Invalid --today value: {args.today}", file=sys.stderr)
            return 2
    else:
        today = datetime.now(timezone.utc).date()

    print(
        f"Gardener run: today={today.isoformat()} "
        f"threshold={STALENESS_DAYS}d dry_run={args.dry_run}",
        file=sys.stderr,
    )
    print(
        f"Scanning {SOURCE_NOTES_DIR.relative_to(REPO_ROOT)}...",
        file=sys.stderr,
    )
    newly_tagged, all_stale = gardener_source_pass(today, args.dry_run)
    print(
        f"  -> {len(newly_tagged)} note(s) newly tagged stale; "
        f"{len(all_stale)} total stale",
        file=sys.stderr,
    )

    print(
        f"Scanning {GUIDE_DIR.relative_to(REPO_ROOT)} for citations to demote...",
        file=sys.stderr,
    )
    demotions = demote_guide_claims(set(all_stale.keys()), args.dry_run)
    print(f"  -> {len(demotions)} citation grade(s) demoted", file=sys.stderr)

    print(
        f"Scanning {STICKY_NOTES_DIR.relative_to(REPO_ROOT)} for sticky note "
        f"staleness...",
        file=sys.stderr,
    )
    sticky_results = gardener_sticky_pass(today, args.dry_run)
    print(
        f"  -> {len(sticky_results['marked_stale'])} note(s) marked stale; "
        f"{len(sticky_results['archived'])} archived; "
        f"{len(sticky_results['stale_alerts'])} alert(s)",
        file=sys.stderr,
    )

    if args.report_file is not None:
        args.report_file.parent.mkdir(parents=True, exist_ok=True)
        with args.report_file.open("w") as fp:
            write_markdown_summary(
                newly_tagged, all_stale, demotions, sticky_results, today, fp,
            )
        print(f"Report written to {args.report_file}", file=sys.stderr)

    return 0


if __name__ == "__main__":
    sys.exit(main())
