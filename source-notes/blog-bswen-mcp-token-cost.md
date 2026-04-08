---
source_url: https://docs.bswen.com/blog/2026-03-23-mcp-token-optimization-claude-code/
source_type: blog-post
title: "How to Stop MCP Servers From Eating Your Claude Context Tokens (with companion: How Claude Code Counts Tokens)"
author: Cowrie (Dev @ Bswen)
date_published: 2026-03-23
date_extracted: 2026-04-08
last_checked: 2026-04-08
status: current
confidence_overall: emerging
issue: "hi-e93.2"
---

# Bswen on MCP Token Cost (and the Bswen Token Counting Companion)

> A practitioner failure-then-fix report: the author noticed their fresh
> Claude Code session was 100k tokens deep before they typed anything,
> traced it to MCP server tool definitions loaded into the system prompt,
> and pruned 15 servers down to 4. Includes server-count → token-count
> measurements and a `/context` breakdown showing where the budget actually
> goes. Companion piece adds CLAUDE.md sizing guidance.

## Source Context

- **Type**: blog-post (practitioner failure-then-fix arc) — synthesized from
  two related posts:
  1. Mar 23, 2026: "How to Stop MCP Servers From Eating Your Claude Context Tokens?"
  2. Mar 25, 2026: "How Claude Code Counts Tokens: A Complete Guide"
- **Author credibility**: Cowrie writes the developer blog at docs.bswen.com,
  publishing technical practitioner posts. Not a vendor; not a researcher;
  a working dev sharing a workflow discovery. The posts are concrete and
  measurement-based, which is what we need.
- **Scope**: Specifically how MCP server count translates to token consumption
  in the Claude Code system prompt, what categories of context are loaded
  before user input, and how to keep the baseline overhead bounded. Does NOT
  cover MCP server quality, which servers are actually useful, or the
  performance impact of context bloat (only the budget impact).

## Extracted Claims

### Claim 1: Every MCP server loads its full tool definitions before you type anything
- **Evidence**: Author's own `/context` inspection.
- **Confidence**: settled (this is how the MCP protocol works; mechanism is
  documented in Claude Code source and Anthropic MCP docs)
- **Quote**: "Every MCP server you connect loads all its tool definitions into
  Claude's system prompt. Not when you use them—**before you even start
  working**."
- **Our assessment**: This is the load-bearing mechanism for the entire post
  and for the broader "tool choice and context cost" argument. MCP servers
  are not pay-per-use; they are pay-per-installed. The cost of an unused
  MCP server is the same as the cost of a heavily used one.

### Claim 2: MCP server count maps roughly linearly to token cost
- **Evidence**: Author's measured table from their own configuration.
- **Confidence**: emerging (single user, single configuration set, but
  reproducible by anyone running `/context`)
- **Quote**: "15 servers: ~100k tokens; 8 servers: ~50k tokens; 6 servers:
  ~30k tokens; 3 servers: ~15k tokens."
- **Our assessment**: The ~5-7k tokens per server slope is the right order of
  magnitude based on typical MCP server schemas (5-30 tools per server,
  100-500 tokens per tool definition). The exact slope depends on which
  servers you load — a single complex server like `puppeteer` or
  `playwright` can dominate. Treat the table as illustrative; the principle
  (linear in server count, large absolute numbers) is solid.

### Claim 3: 100k of MCP overhead halves your effective context window
- **Evidence**: Direct math from Claim 2 + standard 200k Claude window.
- **Confidence**: settled (arithmetic)
- **Quote**: "If you have a 200k context window and burn 100k on tool
  definitions, you've already lost half your capacity."
- **Our assessment**: Pair this with French-Owen's "smart half" rule
  (separate source) for a brutal conclusion: a heavy-MCP user has burned
  their entire smart-half budget on tool definitions before they say hello.
  This is the cleanest single argument for MCP discipline.

### Claim 4: Recommended MCP budget: 3-6 servers, "be ruthless about necessity"
- **Evidence**: Author's recommendation after pruning his own setup.
- **Confidence**: anecdotal (one practitioner's preferred limit)
- **Quote**: "Limit to 3-6 essential servers — Be ruthless about necessity."
  Final kept list: Context7, GitHub, PostgreSQL, Filesystem.
- **Our assessment**: 3-6 servers is consistent with French-Owen's
  observation that Skills are 50-100 tokens vs MCP's thousands — if MCP is
  expensive, fewer is better. Use this as the prescriptive recommendation
  in Ch04, with the caveat that the right number depends on your work
  (a database engineer probably wants the SQL MCP regardless of token cost).

### Claim 5: "MCP eats tons of tokens for things that should be bash scripts"
- **Evidence**: Reddit quote the author cites approvingly.
- **Confidence**: emerging (reflects practitioner consensus visible in
  multiple HN/Reddit threads)
- **Quote**: "MCP eats tons of tokens for things that should be bash scripts."
- **Our assessment**: This is the practitioner critique of MCP in one line.
  Many MCP servers wrap CLIs that the agent could call directly via Bash for
  free. The wrapper is convenient but expensive. Cite as the rule of thumb:
  "Before adding an MCP server, ask whether a bash command and a slash
  command would do the same job." Sentry's settings.json approach (separate
  source: practitioner-getsentry-sentry) is the structural alternative.

### Claim 6: System prompts and system tools dominate the baseline context budget
- **Evidence**: Author's `/context` breakdown from companion piece (Mar 25).
- **Confidence**: emerging (single snapshot; percentages will vary by setup)
- **Quote** (companion): "System prompts: 35% | System tools: 28% | MCP tools:
  12% | Memory files: 5% | Conversation: 4%"
- **Our assessment**: Most striking finding from the breakdown: in this
  configuration, the **conversation itself was only 4%**. The remaining 96%
  was harness boilerplate, system tool definitions, MCP tools, and memory
  files. This is the clearest demonstration we have that "context engineering"
  is mostly about minimizing the boilerplate, not about being efficient with
  the chat. Use as the reframing quote for Ch04.

### Claim 7: Recommended CLAUDE.md size: 100-300 lines, hard cap ~500
- **Evidence**: Author's recommendation in companion piece.
- **Confidence**: anecdotal (single practitioner's heuristic; broadly
  consistent with HumanLayer's "conditional important tags" pattern in
  failure-claudemd-ignored-compaction)
- **Quote** (companion): "Good: 100-300 lines, focused instructions. Bad:
  1000+ lines, everything including the kitchen sink. Keep under 500 lines."
- **Our assessment**: Reasonable rule of thumb. Aligns with the failure
  report finding (separate source) that long CLAUDE.md files are followed
  less reliably. Pair the two findings: long CLAUDE.md is both expensive (this
  post) AND ineffective (failure report). 100-300 lines is a defensible
  upper bound to recommend.

### Claim 8: Cached prompt reads cost 0.1x base
- **Evidence**: Author's stated economics in companion piece.
- **Confidence**: settled (matches Anthropic's published prompt-caching pricing)
- **Quote** (companion): "Cache read costs 0.1x compared to base input."
- **Our assessment**: Useful for the "what does compaction actually cost"
  argument. Cached prefix is cheap (0.1x), but compaction destroys the cache,
  so the next turn pays full price (1.0x) for the entire summarized prefix.
  This is the mechanism behind the wasnotwas $0.40 / 21-turn finding
  (separate source).

## Concrete Artifacts

The post does not include specific configuration files, but the author's
methodology is reproducible:

```
# Diagnosis: count tokens in your fresh context
/context

# Look for: System prompts, System tools, MCP tools, Memory files
# Each line shows percentage of total budget

# Action: prune your ~/.claude.json or .mcp.json server list
# Target: 3-6 essential servers
```

The companion piece's category breakdown is the most quotable single
artifact:

| Category       | Share of context |
|----------------|------------------|
| System prompts | 35%              |
| System tools   | 28%              |
| MCP tools      | 12%              |
| Memory files   |  5%              |
| Conversation   |  4%              |
| Free / unused  | 16% (computed)   |

## Cross-References

- **Corroborates**: blog-french-owen-coding-agents-feb-2026 (French-Owen says
  Skills are 50-100 tokens vs MCP's "thousands"; Bswen measures the
  thousands as ~5-7k per server)
- **Corroborates**: failure-claudemd-ignored-compaction (long CLAUDE.md is
  ignored more often; this post adds that it is also more expensive)
- **Corroborates**: practitioner-getsentry-sentry (Sentry's 60+ command
  prefixes in settings.json achieve fine-grained control without the
  per-server token tax of MCP — Bswen's recommendation to prefer bash
  scripts is structurally aligned)
- **Extends**: research-wasnotwas-context-compaction (wasnotwas measures
  the cost of compaction in dollars; Bswen measures the cost of MCP in
  baseline tokens. Together they cover both the floor and the recurring cost
  of context.)
- **Novel**: The 100k baseline + 4% conversation breakdown is the most
  shocking single number in our Ch04 corpus. No other source quantifies how
  small the conversation actually is.

## Guide Impact

- **Chapter 04 (Tool choice and context cost)**: This is the primary source
  for the section, alongside French-Owen. Lead with Claim 6 (the 96%
  boilerplate breakdown), then Claim 1 (mechanism: MCP loads upfront), then
  Claim 2 (server-count → token table), then Claim 4 (recommendation: 3-6
  servers).

- **Chapter 04 (Context as budget)**: Pair Claim 3 ("100k on tool definitions
  loses half your capacity") with French-Owen's "smart half" rule. Together
  they make the budget argument concrete: heavy MCP users have burned their
  entire usable window before saying hello.

- **Chapter 02 (Harness Engineering)**: Cite Claim 7 (CLAUDE.md size cap)
  as a sizing rule. Currently Ch02 lacks a recommended file size; this post
  gives us 100-300 lines with a 500-line hard cap.

- **Chapter 02 (Harness Engineering)**: Add the "MCP server count budget"
  as a recommended discipline. Cite Bswen's methodology (run `/context`,
  prune to essentials).

- **Chapter 02 (Anti-patterns)**: Add "Convenience MCP servers for things
  that should be bash" as an anti-pattern, citing Claim 5. The cost of
  convenience is several thousand tokens of permanent overhead.

## Extraction Notes

- The Mar 23 post (MCP token optimization) is the primary source. The Mar 25
  companion (Claude Code Counts Tokens) provides supporting metrics that
  strengthen several claims and is treated as part of the same source note.
- The companion piece's "5,000 tokens / 96% used" `/init` observation looks
  contradictory — 5k is way too low to be 96% of any useful context window.
  We suspect the screenshot was from a constrained context (e.g., the
  /init evaluation context) rather than a normal session, and have NOT
  cited it as a claim. The category breakdown in the same post is the
  reliable artifact.
- The Reddit quote ("MCP eats tons of tokens for things that should be bash
  scripts") is pulled from a thread the author cites; we did not chase the
  original Reddit comment for attribution. Treat the source as "approvingly
  quoted" rather than "first-person."
- The author does not measure performance degradation as a function of MCP
  count, only token consumption. The performance link is implicit and should
  be made explicit in Ch04 by cross-referencing French-Owen's "smart half"
  argument.
- Cowrie's other posts on docs.bswen.com cover related material (HANDOFF.md
  patterns, compaction recovery). We have NOT pulled them into this source
  note but they may be worth a separate note if Ch04 needs more depth on
  multi-session handoff coordination.
