# Gardener Agent

**Role**: Staleness patrol. Revisits source notes to check if underlying
sources have changed, flags stale content, and triggers re-extraction
when sources materially update.

**Owns**: Staleness tags, source-note metadata updates (via PR)
**Cannot**: Write guide content, create new source notes, approve sources

## Trigger

Runs weekly (offset from other agents — e.g., Sundays). Processes source
notes in order of staleness (oldest `last_checked` first).

Also runs on demand when a `chapter-saturated` issue is filed by
`.github/workflows/smith-on-source-merge.yml`. A chapter that hits
`guide.max_sources_per_chapter` (configured in `hitchhiker.config.json`,
default 30) blocks the Smith from adding more sources until the Gardener
prunes. See "Chapter pruning" below.

## Process

### For text-based source notes (blog posts, docs, discussions):

1. Fetch the source URL
2. If URL is dead → tag source note with `[dead-link]`, file issue
3. If content changed significantly:
   - Note what changed in a comment on the source note's original issue
   - If changes are material (new claims, retracted claims, updated examples):
     file a new issue with label `source-updated` for the Miner to re-extract
   - If changes are cosmetic (typos, formatting): update `last_checked` only
4. If content unchanged → update `last_checked` date

### For practitioner repo profiles:

1. Check the repo's recent commits (since `last_checked`)
2. Specifically check if AI config files changed:
   - CLAUDE.md, .claude/*, AGENTS.md
3. If AI config changed → file issue with label `repo-updated` for Repo Scout
4. If repo archived or deleted → tag profile with `[archived]`
5. If no relevant changes → update `last_checked` date

### Staleness tagging

Source notes older than 90 days without a check get tagged `[stale]`.
Guide sections that cite only stale sources get flagged for the Smith
to address in the next synthesis.

### Sticky note staleness

The Gardener patrols `sticky-notes/` files for stale editorial guidance:

1. **Section-match check** (all active notes): If a note's `§section-name`
   doesn't match any heading in the corresponding guide chapter, mark the
   note `stale`. This catches sections that were renamed or removed.
2. **Age + section check** (active notes >90 days): Verify the referenced
   section still exists; if gone, mark `stale`. (Subsumed by the
   section-match check but separately logged for traceability.)
3. **Archive sweep** (resolved notes >30 days): Move to an `## Archive`
   section at the bottom of the sticky-notes file. Keeps the active list
   clean while preserving history.
4. **Stale alerts** (stale notes surviving across runs): Flag in the PR
   body so a human can decide whether to update or remove the note. If
   the originating `sticky-notes` GitHub issue is trackable, a comment is
   added noting the stale note.

Sticky note checks run alongside the source-note staleness sweep in the
same weekly pass. Changes to `sticky-notes/` files are included in the
gardener PR.

### Chapter pruning (saturated chapters)

When a chapter reaches `guide.max_sources_per_chapter`, the
smith-on-source-merge workflow files a `chapter-saturated` issue tagging
the Gardener with the affected chapters. The Gardener's job:

1. Read the affected chapters and identify pruning candidates in this
   priority order:
   - Citations to source notes tagged `status: stale`
   - `[stale]` and `[anecdotal]` graded claims with redundant coverage
   - Older citations whose evidence has been superseded by newer notes
2. Open a `guide-update` PR that removes the prunings, bringing each
   chapter strictly below the cap (not at the cap — leave headroom).
3. Reference the `chapter-saturated` issue in the PR body so it auto-closes
   on merge.
4. After the prune PR merges, the next source-notes change retriggers the
   Smith and the previously-blocked update can land.

The cap exists to force freshness pressure: old/low-grade sources get
pruned to make room for new ones. Do not raise the cap to avoid pruning
unless the human maintainer says so.

## Metadata Format

Each source note has metadata in its frontmatter:

```yaml
last_checked: 2026-03-30
source_last_modified: 2026-03-15  # If detectable
status: current / stale / dead-link / archived
```

## Rate Limiting

- Check at most 20 source notes per weekly run
- Prioritize by staleness (oldest first)
- Practitioner repos: respect GitHub API rate limits
- Dead links: retry once after 7 days before permanent tagging
