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

STALENESS_DAYS = 90
WEEKLY_TAGGING_BUDGET = 20

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
# Reporting
# ---------------------------------------------------------------------------


def write_markdown_summary(
    newly_tagged: dict[str, dict],
    all_stale: dict[str, dict],
    demotions: list[dict],
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

    if args.report_file is not None:
        args.report_file.parent.mkdir(parents=True, exist_ok=True)
        with args.report_file.open("w") as fp:
            write_markdown_summary(newly_tagged, all_stale, demotions, today, fp)
        print(f"Report written to {args.report_file}", file=sys.stderr)

    return 0


if __name__ == "__main__":
    sys.exit(main())
