#!/usr/bin/env python3
"""Regenerate registry/sources.json from source-note front-matter.

The registry is a derived index, not a hand-edited file. Every miner used to
append its own entry to this single shared file, which made every parallel
miner PR conflict on it (the entire 54-PR backlog of 2026-06 was jammed on
this). Instead, miners now only add their own unique `source-notes/<slug>.md`,
and this script rebuilds the index deterministically from the front-matter of
every note. Run in CI on any push to main that touches source-notes/.

Usage:
  python3 scripts/build_registry.py            # rewrite registry/sources.json
  python3 scripts/build_registry.py --check     # exit 1 if out of date (CI guard)

Field mapping (front-matter -> registry entry), matching the historical format:
  slug                = basename without .md
  title, source_url, source_type, date_published, date_extracted,
  confidence_overall, status, issue   = copied verbatim from front-matter
  author              = front-matter author with any trailing "(...)" stripped
  file                = source-notes/<slug>.md
"""
import glob
import json
import os
import re
import sys

import yaml

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
NOTES_DIR = os.path.join(ROOT, "source-notes")
REGISTRY = os.path.join(ROOT, "registry", "sources.json")

# Order of keys in each emitted entry — matches the historical registry so the
# generated file is a stable, reviewable diff.
ENTRY_KEYS = [
    "slug", "title", "source_url", "source_type", "author",
    "date_published", "date_extracted", "issue", "file",
    "confidence_overall", "status",
]


def _line_parse(block):
    """Fallback flat parser for front-matter that isn't valid YAML.

    Some notes have an unquoted `author:` (or similar) whose value contains a
    bare colon, which YAML rejects. The front-matter here is always flat
    `key: value` lines, so split on the FIRST colon and strip surrounding
    quotes. This keeps such notes in the index instead of dropping them.
    """
    out = {}
    for line in block.splitlines():
        if not line.strip() or line.lstrip().startswith("#"):
            continue
        m = re.match(r"^([A-Za-z_][\w-]*):\s?(.*)$", line)
        if not m:
            continue
        key, val = m.group(1), m.group(2).strip()
        if len(val) >= 2 and val[0] == val[-1] and val[0] in "\"'":
            val = val[1:-1]
        out[key] = val
    return out


def parse_front_matter(path):
    """Return the front-matter dict for a note, or None if absent."""
    with open(path, encoding="utf-8") as f:
        text = f.read()
    if not text.startswith("---"):
        return None
    end = text.find("\n---", 3)
    if end == -1:
        return None
    block = text[3:end]
    try:
        loaded = yaml.safe_load(block)
        if isinstance(loaded, dict):
            return loaded
    except yaml.YAMLError:
        pass
    # YAML failed (e.g. unquoted value with a bare colon) — fall back so the
    # note is still indexed. These notes should be fixed to quote the value.
    return _line_parse(block)


def normalize_author(value):
    if not value:
        return value
    # Drop a trailing parenthetical qualifier, e.g.
    # "Harrison Chase (LangChain CEO)" -> "Harrison Chase".
    return re.sub(r"\s*\([^)]*\)\s*$", "", str(value)).strip()


def build():
    sources = {}
    for path in sorted(glob.glob(os.path.join(NOTES_DIR, "*.md"))):
        slug = os.path.basename(path)[:-3]
        if slug.startswith("."):  # skip .template-* and dotfiles
            continue
        fm = parse_front_matter(path)
        if fm is None:
            print(f"WARN: no parseable front-matter in {path}", file=sys.stderr)
            continue
        entry = {
            "slug": slug,
            "title": fm.get("title"),
            "source_url": fm.get("source_url"),
            "source_type": fm.get("source_type"),
            "author": normalize_author(fm.get("author")),
            "date_published": fm.get("date_published"),
            "date_extracted": fm.get("date_extracted"),
            "issue": fm.get("issue"),
            "file": f"source-notes/{slug}.md",
            "confidence_overall": fm.get("confidence_overall"),
            "status": fm.get("status"),
        }
        # Stringify dates (yaml may parse them as date objects) and drop Nones
        # to keys we have, preserving key order.
        ordered = {}
        for k in ENTRY_KEYS:
            v = entry.get(k)
            if v is None:
                continue
            ordered[k] = str(v) if not isinstance(v, str) else v
        sources[slug] = ordered
    return {"sources": sources}


def main():
    check = "--check" in sys.argv
    new = build()
    new_text = json.dumps(new, indent=2, ensure_ascii=False) + "\n"
    if check:
        try:
            cur = open(REGISTRY, encoding="utf-8").read()
        except FileNotFoundError:
            cur = ""
        if cur != new_text:
            print("registry/sources.json is OUT OF DATE — run scripts/build_registry.py",
                  file=sys.stderr)
            return 1
        print("registry/sources.json is up to date.")
        return 0
    with open(REGISTRY, "w", encoding="utf-8") as f:
        f.write(new_text)
    print(f"Wrote {REGISTRY} with {len(new['sources'])} entries.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
