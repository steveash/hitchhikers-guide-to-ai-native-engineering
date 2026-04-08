#!/usr/bin/env python3
"""Per-chapter source-cap enforcement.

Counts the unique source-note slugs cited in each ``guide/*.md`` chapter and
compares the count to ``guide.max_sources_per_chapter`` from
``hitchhiker.config.json``. The cap exists to prevent chapter bloat: when a
chapter is at the cap, the Gardener has to prune stale sources before the
Smith is allowed to add new ones. See bead ``hi-4yk.16``.

Usage::

    # Check every chapter under guide/ (excluding SOURCES.md):
    python3 scripts/check_chapter_source_cap.py

    # Check only specific chapters (paths relative to repo root):
    python3 scripts/check_chapter_source_cap.py guide/02-harness-engineering.md

    # Machine-readable output for the smith-on-source-merge workflow:
    python3 scripts/check_chapter_source_cap.py --json

Exit codes:
    0 = all chapters under cap
    1 = one or more chapters at or over cap (cap is inclusive — at the cap
        means no new sources can be added without pruning)
    2 = usage error / config error

The "at or over" semantics matter: if cap=30 and a chapter sits at 30
sources, the next Smith run must NOT add a new source until a pruning pass
brings the count below 30. Counting strictly-greater would let the Smith add
a 31st source on the run that pushes the count from 30 to 31, which defeats
the freshness pressure the cap is supposed to create.
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
CONFIG_PATH = REPO_ROOT / "hitchhiker.config.json"
SOURCE_NOTES_DIR = REPO_ROOT / "source-notes"
GUIDE_DIR = REPO_ROOT / "guide"

# Match the gardener.py grade list so the two scripts agree on what counts
# as a citation. Keep these in sync if either ever changes.
GRADES = ("settled", "emerging", "anecdotal", "editorial", "stale")
CITATION_RE = re.compile(
    r"\[source:\s*([^\]]+?)\]\s*\[(" + "|".join(GRADES) + r")\]"
)


def load_cap() -> int:
    """Read ``guide.max_sources_per_chapter`` from the project config."""
    if not CONFIG_PATH.exists():
        print(f"error: config file missing: {CONFIG_PATH}", file=sys.stderr)
        sys.exit(2)
    try:
        cfg = json.loads(CONFIG_PATH.read_text())
    except json.JSONDecodeError as exc:
        print(f"error: cannot parse {CONFIG_PATH}: {exc}", file=sys.stderr)
        sys.exit(2)
    try:
        cap = cfg["guide"]["max_sources_per_chapter"]
    except (KeyError, TypeError):
        print(
            "error: hitchhiker.config.json is missing "
            "guide.max_sources_per_chapter",
            file=sys.stderr,
        )
        sys.exit(2)
    if not isinstance(cap, int) or cap < 1:
        print(
            f"error: guide.max_sources_per_chapter must be a positive int, "
            f"got {cap!r}",
            file=sys.stderr,
        )
        sys.exit(2)
    return cap


def collect_source_note_names() -> set[str]:
    """Filenames (without ``.md``) of every source note on disk.

    Mirrors gardener.py's ``collect_source_note_names`` so the two passes
    treat the same set of slugs as "real" sources.
    """
    return {
        p.stem
        for p in SOURCE_NOTES_DIR.glob("*.md")
        if not p.name.startswith(".")
    }


def extract_unique_sources(text: str, known_notes: set[str]) -> set[str]:
    """Return the set of source-note slugs cited anywhere in ``text``.

    A citation looks like ``[source: foo, bar (Claim 5)] [settled]``. We
    split on commas, strip trailing parenthetical qualifiers, and keep only
    tokens that match a real source-note filename. Qualifiers like
    "Claim 5" naturally fall away because they aren't files. Identical to
    the extraction logic in ``scripts/gardener.py`` for consistency.
    """
    sources: set[str] = set()
    for match in CITATION_RE.finditer(text):
        for part in match.group(1).split(","):
            cleaned = re.sub(r"\s*\(.*\)\s*$", "", part.strip())
            if cleaned in known_notes:
                sources.add(cleaned)
    return sources


def count_chapter_sources(chapter: Path, known_notes: set[str]) -> int:
    return len(extract_unique_sources(chapter.read_text(), known_notes))


def resolve_chapters(args_paths: list[str]) -> list[Path]:
    """Turn CLI args into a sorted list of guide chapter paths.

    No args  -> every ``guide/*.md`` except ``guide/SOURCES.md`` (the index).
    Explicit -> only the given paths, after sanity checks. Paths outside
                ``guide/``, missing files, or ``guide/SOURCES.md`` exit 2 so
                a workflow caller can't accidentally check the wrong file.
    """
    if not args_paths:
        return sorted(
            p for p in GUIDE_DIR.glob("*.md") if p.name != "SOURCES.md"
        )

    resolved: list[Path] = []
    for raw in args_paths:
        path = (REPO_ROOT / raw).resolve() if not Path(raw).is_absolute() else Path(raw).resolve()
        try:
            rel = path.relative_to(REPO_ROOT)
        except ValueError:
            print(f"error: {raw} is outside the repo root", file=sys.stderr)
            sys.exit(2)
        if rel.parts[0] != "guide" or path.suffix != ".md":
            print(f"error: {raw} is not a guide/*.md chapter", file=sys.stderr)
            sys.exit(2)
        if path.name == "SOURCES.md":
            # SOURCES.md is the source index, not a chapter — it cites every
            # source in the corpus by design and is never gated.
            continue
        if not path.exists():
            print(f"error: {raw} does not exist", file=sys.stderr)
            sys.exit(2)
        resolved.append(path)
    return resolved


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "chapters",
        nargs="*",
        help=(
            "Chapter paths to check (relative to repo root). "
            "Default: every guide/*.md except guide/SOURCES.md."
        ),
    )
    parser.add_argument(
        "--json",
        action="store_true",
        help="Emit a machine-readable JSON report on stdout (for workflow use).",
    )
    args = parser.parse_args(argv)

    cap = load_cap()
    known_notes = collect_source_note_names()
    chapters = resolve_chapters(args.chapters)

    report = []
    for chapter in chapters:
        count = count_chapter_sources(chapter, known_notes)
        rel = str(chapter.relative_to(REPO_ROOT))
        # ``saturated`` is inclusive: at-cap means the next source pushes us
        # over, so we block here rather than waiting for cap+1. See module
        # docstring for the "why".
        saturated = count >= cap
        report.append(
            {
                "chapter": rel,
                "unique_sources": count,
                "cap": cap,
                "saturated": saturated,
            }
        )

    if args.json:
        json.dump(report, sys.stdout, indent=2)
        sys.stdout.write("\n")
    else:
        for entry in report:
            marker = "SATURATED" if entry["saturated"] else "ok"
            print(
                f"  {marker:>9}  {entry['chapter']}  "
                f"{entry['unique_sources']}/{entry['cap']} sources"
            )

    saturated = [e for e in report if e["saturated"]]
    if saturated:
        if not args.json:
            print(
                f"\n{len(saturated)} chapter(s) at or over the "
                f"{cap}-source cap. Gardener must prune before the Smith "
                f"can add new sources.",
                file=sys.stderr,
            )
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
