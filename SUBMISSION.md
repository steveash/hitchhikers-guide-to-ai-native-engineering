# Submit a Source to the Hitchhiker's Guide

Found something useful about AI-native engineering? We want it.

## What We're Looking For

- **Practitioner repos** with real CLAUDE.md files, .claude/ configs, or AGENTS.md
- **Failure reports** — "I tried X and it broke" is extremely valuable
- **Workflow patterns** — concrete approaches that worked in practice
- **Tool comparisons** — measured, not vibes-based
- **Counter-evidence** — something that contradicts the current guide

## What We're NOT Looking For

- Vendor marketing or product announcements
- Pure opinion without experience to back it up
- Tutorials that haven't been battle-tested
- Anything from before December 2025 (the landscape was too different)

## How to Submit

### Option 1: Use the Issue Template (preferred)

1. Go to [Issues → New Issue](../../issues/new/choose)
2. Select **"Source Submission"**
3. Fill in:
   - **Source URL** — the link to the repo, post, discussion, etc.
   - **Source type** — practitioner-repo, failure-report, blog-post, discussion, paper
   - **What's interesting** — in your own words, what did you find valuable?
   - **Where it's relevant** — which part of the guide might this affect?
4. Submit. The agent pipeline will pick it up.

### Option 2: Quick Issue (no template)

Create an issue with the title format:

```
[source] Brief description of what you found
```

Include at minimum:
- The URL
- One paragraph on why it matters

### What Happens Next

Your submission enters the same pipeline as automated discoveries:

1. **Prospector** triages it — is it novel? relevant? credible?
2. **Miner** (or **Repo Scout** for repos) does a deep extraction
3. **Assayer** reviews the extraction for depth and accuracy
4. If it passes review, the source note merges and the **Smith** considers
   it for the next guide update

You'll see progress on your issue as it moves through the pipeline.
Labels track the state: `new` → `triaged` → `mining` → `review` → `integrated`.

## The Same Bar Applies

Community submissions are processed with the same editorial rigor as
automated discoveries. That means:

- Shallow sources get rejected (with an explanation)
- Claims get evidence-graded, not taken at face value
- If your source contradicts the guide, that's a feature, not a problem
- The extraction may emphasize different aspects than you expected

This isn't gatekeeping — it's quality control. The guide is only useful
if every claim in it is properly sourced and graded.
