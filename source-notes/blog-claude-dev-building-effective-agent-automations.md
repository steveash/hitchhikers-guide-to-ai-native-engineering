---
source_url: https://claude.dev/blog/building-effective-agent-automations/
source_type: blog-post
title: "Building effective agent automations"
author: Lance Martin and CJ Avilla (Anthropic, claude.dev blog)
date_published: 2026-10-08
date_extracted: 2026-10-12
last_checked: 2026-10-12
status: current
confidence_overall: emerging
issue: "#4068"
---

# Building effective agent automations

> Anthropic's reference "daily brief" scheduled agent on Claude Managed Agents distills six operating rules (bookmarks, loud failed reads, re-verify before posting, confirm-before-record, fresh read-only preferences, read-only access plus spend caps) that keep an unattended agent from failing silently.

## Source Context

- **Type**: blog-post (vendor reference-implementation walkthrough, claude.dev blog, "A reference implementation walkthrough with common failure modes", 9 min read)
- **Author credibility**: Lance Martin and CJ Avilla write for Anthropic, the platform vendor, so they are authoritative on how Managed Agents behaves (e.g., what happens when an MCP server is down, how budget caps stop a run). The rules come from one template and are design guidance; the post reports no metrics, failure rates, or cost data.
- **Scope**: Covers one reference implementation (`daily-brief`: reads Slack channels and GitHub PRs on a weekday cron, posts a brief to Slack) across six components: sources, destination, agent, schedule, memory, guardrails. Does NOT cover: evaluation of brief quality, multi-destination fan-out, non-Slack sinks, measured reliability, or actual cost numbers (the $5.00 cap in the YAML is an example value). The full eight run steps live in the repo (`anthropics/claude-quickstarts`, `managed-agents/daily-brief`) and were not available in the post; only steps 4 and 5 are quoted.

## Extracted Claims

### Claim 1: Read each source from a per-source bookmark, not a fixed "last 24 hours" window
- **Evidence**: Design rule with a stated failure mode and mechanism: the agent writes the newest-item timestamp per source to `bookmarks.json` (e.g. `"slack": "2026-09-14T13:02:11Z"`) in a read-write memory store; the next run starts from there. No measurements.
- **Confidence**: emerging
- **Quote**: "A late run leaves a gap and an early run repeats items."
- **Our assessment**: Strong, cheap, and generalizable: a high-water mark per source makes the window elastic. Standard in ETL/stream-processing practice, but a useful explicit statement for LLM agents, which default to time-window prompts. Caveat: it assumes the newest-item timestamp is monotonic and the source returns everything since it (the post itself notes a source that "returns only the newest 50 items" as a note-worthy quirk).

### Claim 2: A failed source read looks identical to a quiet day, so it must be reported as unreadable and its bookmark must not advance
- **Evidence**: Platform behavior described: if an MCP server is down or token expired, the run still starts without that server's tools, the session logs an error, and the agent sees nothing. Mitigation is three rules in `agent.md`: keep the bookmark, write from other sources, end the brief with a line naming what could not be read.
- **Confidence**: emerging
- **Quote**: "If an MCP server is down or its token has expired, the run still starts, just without that server's tools."
- **Our assessment**: The most valuable claim for harness design. It names a silent-degradation mode (missing tools, not an error the model sees) that is easy to miss in unattended agents. Holding the bookmark means the next run backfills, so a transient outage costs delay, not data. Generalizes: any unattended agent should have an explicit "what I could not check" channel.

### Claim 3: Count a post as sent only on Slack `"ok": true` plus a message ts, update ledger/bookmarks only after confirmation, and use a "maybe posted" state for unclear results
- **Evidence**: Three `agent.md` rules plus a run record (`runs/<date>.md`) marked "posting" before the send, then "posted" with message ID or "maybe posted". Failure modes named: recording a post that never landed (items never reported) or re-posting out of uncertainty (duplicate brief).
- **Confidence**: emerging
- **Quote**: "Third, the agent updates the ledger and bookmarks only after that confirmation."
- **Our assessment**: This is a write-ahead-log / commit-after-effect pattern applied to an agent. The choice to bias toward "change nothing else" on ambiguity trades a possible missed or repeated item for no lost state. Note it relies on the model faithfully following prose rules; the post gives no enforcement (hook or code check) beyond instructions.

### Claim 4: Check the destination for today's edition before posting, to prevent duplicates after retries
- **Evidence**: Rule in `agent.md`: look for today's title in the channel's recent messages; the deployment's first message fixes the title format ("Daily brief, <weekday> <month> <day>").
- **Confidence**: emerging
- **Quote**: "First, the agent looks for today's title in the channel's recent messages and doesn't post if the edition is already there."
- **Our assessment**: A practical idempotency key built from a deterministic title. Pairs with Claim 3: the "maybe posted" state is resolved on the next run by this existence check. Works only if the title is deterministic and the bot can read channel history.

### Claim 5: Re-verify each item against its live source immediately before posting; assert the status or drop the item, never hedge
- **Evidence**: `agent.md` step 5 (quoted in full under Concrete Artifacts). Unconfirmable items are dropped and listed in the run record's "cuts". Links are copied from the source's own link field, never hand-assembled.
- **Confidence**: emerging
- **Quote**: "One stale "still waiting on you" costs more trust than ten missing items, so never hedge an item's status: assert it or drop it."
- **Our assessment**: Good trust-calibration principle: precision over recall for proactive notifications. The "cuts" list keeps drops auditable. The claim that one stale item costs more than ten missing is the authors' judgment, not measured.

### Claim 6: Keep the output short: an item earns a line only if the reader would act on it today; counts are not items; still-open ledger items are carried as one marked line
- **Evidence**: `agent.md` step 4 text (quoted under Concrete Artifacts). No data on reader behavior.
- **Confidence**: anecdotal
- **Quote**: "When unsure, leave it out. Most days that is a few items, sometimes none."
- **Our assessment**: Reasonable editorial rule for digest agents, expressed as an actionability filter plus a ledger-based dedupe ("still waiting, day 3"). Unvalidated; useful as a prompt pattern rather than a finding.

### Claim 7: Split memory into a read-only preferences store (human-edited) and a read-write state store (agent-owned); re-read preferences fresh every run and stop if they cannot be read
- **Evidence**: Two stores mounted under `/mnt/memory/`; `deployment.md` sets `access: read_only` for preferences with the instruction "Never write here." State holds bookmarks, ledger, run records, proposed preference changes, and per-source behavior notes.
- **Confidence**: emerging
- **Quote**: "If it can't read the file, it should stop and say so instead of running on defaults."
- **Our assessment**: Same fail-loud principle as Claim 2 applied to configuration. The "proposals" file lets the agent suggest preference changes without being able to apply them, a clean human-in-the-loop boundary. The post also warns about the opposite failure: preferences baked into the prompt "keep applying rules you've already changed".

### Claim 8: Stale agent memory is itself a failure mode (reporting resolved items as waiting, or dropping open items as "already reported")
- **Evidence**: Stated as a risk of the ledger/state design; mitigation is the re-verify step (Claim 5) plus ledger entries holding a stable ID and last known status.
- **Confidence**: emerging
- **Quote**: "However, stale memory can confuse the agent: it reports an item as still waiting after it was resolved, or drops one that's still open because it was "already reported.""
- **Our assessment**: Honest acknowledgement that memory adds a correctness hazard, not only value. The design treats the ledger as a hint to be verified against live sources, not as truth. Relevant counterweight to memory-positive vendor notes.

### Claim 9: Give the agent scoped credentials held in a vault; the sandbox holds only an opaque placeholder that the platform swaps for the real token on allowlisted hosts
- **Evidence**: Two paths described: MCP via a proxy outside the sandbox matching vault credential URL; shell via `$SLACK_BOT_TOKEN` placeholder swapped at egress. Vault credential created with `networking: { type: "limited", allowed_hosts: ["slack.com"] }`.
- **Confidence**: emerging
- **Quote**: "The sandbox only holds an opaque placeholder, $SLACK_BOT_TOKEN."
- **Our assessment**: Concrete worked example of the vault pattern that earlier Anthropic notes announce. Credential never entering the sandbox is a real architectural property; the host allowlist binds the secret to a destination, limiting exfiltration by a manipulated agent.

### Claim 10: Source text is a possible instruction channel; limit blast radius with read-only tokens, a read-only preferences store, and an egress allowlist, accepting that the brief's content can still be influenced
- **Evidence**: Reasoning plus configuration: GitHub token and preferences store read-only; environment limited to allowlisted hosts. Slack is called out as the exception because the same token reads and posts.
- **Confidence**: emerging
- **Quote**: "A planted instruction can still change what the brief says, including through the notes the agent keeps between runs."
- **Our assessment**: Candid statement of residual risk: containment, not prevention. Notably flags that agent-writable state is a persistence channel for injected content. The same-token-reads-and-posts exception is a real gap; a separate write-only posting credential would tighten it (our inference, not the post's).

### Claim 11: Set a per-run spend cap at 3-5x a normal run's cost and tighten from real data; a capped run pauses with `budget_reached`, which looks like a quiet brief
- **Evidence**: Authors' guidance and an example YAML (`max_list_cost` amount "500" cents = $5.00). No measured run costs.
- **Confidence**: anecdotal
- **Quote**: "A run that hits its cap pauses instead of failing, so a cap set too low looks like a brief that went quiet."
- **Our assessment**: The multiplier is a heuristic, not a result. The valuable point is that a safety limit can itself cause a silent failure, the same class as Claim 2; budget stops need monitoring or a visible signal.

### Claim 12: Compute dates in the reader's time zone, not the server's
- **Evidence**: Common-bug description; fix is the cron `timezone` field plus a line in the deployment's first message telling the agent which zone to use for dates.
- **Confidence**: emerging
- **Quote**: "A common bug is the agent calling this morning "yesterday" because it computes dates in the server's time zone."
- **Our assessment**: Small but real; note the two-part fix (schedule zone and explicit instruction for date arithmetic) since setting only the cron zone does not change what the agent believes "today" is.

### Claim 13: Unattended agents' tool permissions must be pre-granted because nobody is present to approve prompts
- **Evidence**: MCP toolset set to `always_allow`; built-in bash runs without approval by default; compensated by read-only GitHub token and allowlisted network.
- **Confidence**: emerging
- **Quote**: "MCP tools ask for approval by default and nobody is there to give it, so the GitHub toolset is set to always_allow and the GitHub token is read-only."
- **Our assessment**: Shows the trade explicitly: approval prompts are replaced by credential scoping. Also web_search and web_fetch are disabled in the config, shrinking the attack surface.

## Concrete Artifacts

Source's six rules (Getting started section, verbatim):

```
Read each source from a bookmark, not a fixed time window.
Report a failed read as unreadable, never as a quiet day.
Re-check every item right before posting.
Count a post as sent only when Slack confirms it, then update bookmarks and ledger.
Re-read your preferences every run, from a store the agent can't edit.
Give the agent read-only access wherever it only reads, and cap what each run can spend.
```

`agent.md` step 4 (Decide), from the post:

```
4. Decide. An item earns a line when the reader would act on it today, or it changes a decision they are about to make. When unsure, leave it out. Most days that is a few items, sometimes none. A count ("12 open reviews") is not an item; link the ones that are blocked. An item already in the ledger and still open is carried as one marked line ("still waiting, day 3"), not re-reported; a closed item is dropped without comment. Do not bring back a topic the preferences file has retired.
```

`agent.md` step 5 (Verify), from the post:

```
5. Verify. The world moved while you read. For every item you will report, re-check its live source just before posting: resolved since you read it, drop it; still open but changed, fix the line; cannot confirm, drop it and list it in the run record's cuts. One stale "still waiting on you" costs more trust than ten missing items, so never hedge an item's status: assert it or drop it. Every link is copied from the source's own link field (a pull request's html_url, a Slack permalink), never assembled by hand.
```

`deployment.md` (schedule, memory mounts, first message), from the post:

```
---
name: Daily brief
agent: ./agent.md
environment_id: ./environment.yaml
schedule:
  type: cron
  expression: "32 7 * * 1-5"
  timezone: America/New_York
vault_ids: [vlt_...]   # the vault you create under Sources
resources:
  - path: ./memory_store_preferences.yaml
    access: read_only
    instructions: The reader's preferences. Re-read them every run. Never write here.
  - path: ./memory_store_state.yaml
    access: read_write
    instructions: Your state. Bookmarks, ledger, notes, proposals, and run records.
---
Write today's brief.
The reader's time zone is America/New_York. Work out every date in that zone.
Follow your run steps in order. Today's edition is titled "Daily brief, <weekday> <month> <day>".
```

Ledger format, from the post:

```
2026-09-09 slack:C0123456789 1788963600.000100 refund thread: customer waiting on a decision
2026-09-11 github 481 review blocked, day 2 (still waiting)
2026-09-11 slack:C0234567891 1789117333.000300 enterprise escalation: owner named, in progress
```

Budget block, from the post:

```
budget:
  type: limit
  max_list_cost:
    amount: "500" # a string, in cents: "500" is $5.00
    currency: USD
```

Run-record lifecycle (paraphrased from the post, Destination section): `runs/<date>.md` is marked "posting" before the send, then "posted" with the message ID, or "maybe posted".

## Cross-References

- **Corroborates**: `blog-anthropic-managed-agents-scheduled-vaults.md` Claim 4 (vault credential injection where the sandbox only holds a placeholder) is demonstrated here end to end with a concrete Slack token and host allowlist. `blog-anthropic-claude-managed-agents-memory.md` Claim 5 (read-only vs read-write memory scopes) is applied here as preferences (read-only) vs state (read-write).
- **Contradicts**: None found. Not filed as a contradiction. Mild tension only: the memory-announcement note presents memory as a pure capability gain, while this post lists stale memory as a failure mode (Claim 8); that is a conditioning caveat, not an opposing claim.
- **Extends**: `blog-anthropic-managed-agents-scheduled-vaults.md` Claims 1-2 (scheduled deployments exist, cron, pause/resume) by supplying operating rules for what the scheduled agent must do. `blog-anthropic-claude-code-routines.md` Claim 3 (scheduled routines on practitioner cadences) with a reliability layer: bookmarks, ledger, confirm-before-record. `blog-anthropic-claude-managed-agents.md` (platform overview) with a concrete reference deployment.
- **Novel**: Per-source bookmarks replacing time windows; failed-read-as-quiet-day failure mode and its mitigation; "posting"/"posted"/"maybe posted" run states with confirm-before-record; destination existence check as idempotency; re-verify-before-post with "assert or drop"; budget cap pausing as a silent-failure mode; reader-time-zone date rule; preferences-read-only/state-read-write split with a proposals channel.

## Guide Impact

- **Chapter 02 (harness engineering)**: Add a short "unattended agent reliability" section or sidebar built on the six rules: per-source high-water marks, run records with a pre-send "posting" state, and an explicit "could not read" line. Cite this note's Claims 1-3.
- **Chapter 03 (verification)**: Add re-verify-immediately-before-reporting ("assert it or drop it") and commit-after-confirmation as verification patterns for agents with external side effects. Cite Claims 3, 5.
- **Chapter 04 (context/memory)**: Add the preferences (human-owned, read-only) vs state (agent-owned) split, plus the warning that agent memory can go stale and should be treated as a hint verified against live sources. Cite Claims 7, 8.
- **Chapter 06 (security)**: Add the worked example of placeholder-token vaults with host allowlists, read-only tokens, and the candid residual-risk statement that injected source text can still shape output and agent-written notes. Cite Claims 9, 10, 13. Also note that budget caps can mask failures (Claim 11).
- **Evidence labeling**: Present these as vendor design rules from one reference template, not measured results; spend-cap numbers are guidance only.

## Extraction Notes

- Read the full article (raw HTML fetched and stripped to text; the page was read end to end). Only the post itself was used; the linked repo (`anthropics/claude-quickstarts/managed-agents/daily-brief`) and the full eight-step `agent.md` were not fetched, so steps other than 4 and 5 are unseen.
- The post is vendor-authored, has no metrics or failure-rate data, and describes one template. Confidence is therefore `emerging` overall: the rules are specific and mechanistically explained but unmeasured.
- Quotes were copied from the extracted page text; inner quotation marks in the source are retained.
- The post's model reference in `agent.md` is `claude-sonnet-5-5`.
