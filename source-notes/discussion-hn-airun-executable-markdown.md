---
source_url: https://news.ycombinator.com/item?id=46549444
source_type: discussion
title: "Show HN: Executable Markdown files with Unix pipes"
author: jedwhite (Jed White, CTO of Andi AI Search)
date_published: 2026-01-09
date_extracted: 2026-04-15
last_checked: 2026-04-15
status: current
confidence_overall: anecdotal
issue: "#60"
---

# Show HN: Executable Markdown files with Unix pipes

> A Show HN announcement from Jed White (Andi AI Search) introducing airun
> (originally `claude-run`), a tool that makes markdown files directly executable
> via Unix shebangs and stdin/stdout pipes — notable for treating Claude Code
> invocation as a composable Unix tool, enabling `cat data.json | ./analyze.md`
> pipelines, per-script permission flags via shebang arguments, and multi-cloud
> routing; with 126 HN points and 101 comments including substantive community
> debate on nondeterminism, auditability, and a confirmed enterprise adoption data
> point.

## Source Context

- **Type**: discussion (Show HN announcement + GitHub repo `andisearch/airun`,
  126 points, 101 comments, 2026-01-09; previously `claude-run`/`claude-switcher`,
  renamed to `airun` in 2026)
- **Author credibility**: jedwhite is Jed White, CTO of Andi AI Search (a real,
  publicly known AI search company). He is the author of the GitHub repo
  `andisearch/airun` (141 stars, MIT license). This is not anonymous — he speaks
  from the position of a working CTO who built and ships the tool. The 126-point
  engagement with 101 comments represents meaningful practitioner interest. He
  follows up in the thread responding to critics and posting updates (remote script
  execution via curl, installmd.org).
- **Scope**: The HN post describes the core shebang/pipe concept for making
  markdown files executable through Claude Code. The GitHub `andisearch/airun`
  README expands with the full feature set: multi-provider routing (AWS Bedrock,
  Azure, Google Vertex, Anthropic API, Ollama), model flag options (`--opus`,
  `--sonnet`, `--haiku`), session continuity (`--resume`), YAML frontmatter
  variable declarations, and the `--team` flag for Claude Code's experimental Agent
  Teams. The thread contributes community pushback on nondeterminism and auditability,
  plus one enterprise adoption data point (graefawcett, Fortune 500 control plane).
  This note synthesizes the HN post, the thread comments, and the airun GitHub README.
  It does NOT cover: benchmarks, failure rate data, comparative metrics against
  shell scripting, or the `andisearch/ai-scripts` example library in depth.

## Extracted Claims

### Claim 1: Markdown files can be made directly executable as Claude Code invocations via a Unix shebang — the markdown content becomes the prompt, the file becomes the agent

- **Evidence**: jedwhite's HN post with working code example. The pattern:
  add `#!/usr/bin/env claude-run` (now `#!/usr/bin/env ai`) as the first line,
  `chmod +x task.md`, then execute with `./task.md`. Claude Code processes the
  file content as a structured prompt with full tool-use capability.
- **Confidence**: anecdotal (author-reported, working tool with 141 stars, but
  no independent evaluation of success rate or behavior consistency)
- **Quote**: "These aren't just prompts. Claude Code has tool use, so a markdown
  file can run shell commands, write files, call APIs." (jedwhite, HN post preview
  in issue body)
- **Our assessment**: This is the central claim and it is mechanically straightforward
  — Claude Code already accepts stdin input (per the agent loop in
  `blog-ccunpacked-claude-code-architecture.md`, Step 1: "User inputs message or
  piped via stdin, Source: TextInput.tsx"). The shebang is the Unix mechanism
  for making that stdin path accessible as a standard executable. The interesting
  design insight is not the technical mechanism (stdin is just stdin) but the
  *framing*: treating the markdown prompt as the executable artifact rather than
  the script that invokes the agent. This reframes the authoring problem: you write
  what you want the AI to do (in natural language) not how to invoke the AI system.

### Claim 2: The shebang pattern enables classical Unix pipe composition with AI steps — a markdown file becomes a filter in a pipeline

- **Evidence**: jedwhite's HN post demonstrating:
  `cat data.json | ./analyze.md > results.txt` and the ability to chain multiple
  markdown scripts together. His later comment (ID 46580804) adds remote script
  execution: `curl -fsSL https://andisearch.github.io/ai-scripts/analyze.md | claude-run`.
- **Confidence**: anecdotal (demonstrated in code, but nondeterminism limits
  applicability to idempotent/reversible tasks)
- **Quote**: jedwhite (HN post) — "tasks that needed LLM orchestration libraries
  are now markdown files composed with standard Unix tools"
- **Our assessment**: The Unix pipe analogy is compelling but imprecise. In
  traditional Unix pipelines, a filter is deterministic and referentially transparent
  — the same input produces the same output. An AI-based filter is nondeterministic.
  The practical consequence is that piping to a markdown script is appropriate for
  tasks where variation in output format is acceptable (summarization, classification,
  reformatting) but not for tasks where the downstream consumer depends on exact
  output shape (data transformations, structured extraction for database insertion).
  The pattern works best when the markdown script is the *last* step in the pipeline
  (generating a human-readable report) rather than a mid-pipeline filter feeding
  another deterministic tool. This is the key qualification jedwhite's framing
  undersells.

### Claim 3: Permission flags can be passed via shebang arguments, making per-script capability grants explicit at the file level

- **Evidence**: airun README and the `analyze.md` example hosted at
  `andisearch.github.io/ai-scripts/analyze.md` demonstrate:
  `#!/usr/bin/env claude-run --permission-mode bypassPermissions`. jedwhite's
  follow-up comment confirms: "shebang flags within markdown files are respected
  during execution."
- **Confidence**: anecdotal (described in README; no source-level analysis of
  how this is parsed and passed)
- **Quote**: jedwhite (comment 46580804) — "shebang flags within markdown files
  (such as --permission-mode bypassPermissions) are respected during execution"
- **Our assessment**: This is one of the more architecturally interesting design
  choices. By putting the permission scope in the file header rather than the
  invocation command, the script becomes self-describing: reading the shebang
  tells you exactly what the script is allowed to do. Compare to the airun
  README's default behavior ("By default, scripts cannot execute code" — permission
  must be explicitly granted). This is a reasonable default-deny model.
  The risk is that `bypassPermissions` in a shebang can be copy-pasted without
  understanding by less experienced users, and remotely-fetched scripts
  (`curl | claude-run`) may carry permission escalation that the user doesn't
  notice. This is DocTomoe's "voice-controlled scalpel" concern in concrete form.

### Claim 4: Multi-cloud provider routing enables billing isolation and subscription separation — the agent runs against a different provider than the developer's personal Claude account

- **Evidence**: airun README lists supported providers: AWS Bedrock, Google
  Vertex AI, Azure, Anthropic API, OpenAI API, and local models (Ollama, LM Studio).
  Flags like `--aws --opus script.md` override the default provider. The
  WebFetch summary from jedwhite's original post notes "separate billing and
  session isolation from personal Claude subscriptions" as an explicit use case.
- **Confidence**: anecdotal (feature is listed in README; billing isolation
  behavior depends on each provider's implementation)
- **Quote**: airun README — "routes scripts through different cloud providers
  (AWS Bedrock, Azure, Vercel) for separate billing and session isolation from
  personal Claude subscriptions"
- **Our assessment**: This is a practical enterprise concern that the pure
  Claude Code user doesn't encounter: teams may want automated scripts to
  bill against a team/project account (AWS Bedrock via IAM role) rather than
  an individual developer's Anthropic subscription. The multi-provider abstraction
  (`ai --aws --opus`) makes this switchable at the invocation level without
  changing the script content. The `--resume` flag for session continuity across
  provider switches is a pragmatic rate-limit workaround. Compare with
  `blog-bswen-mcp-token-cost.md`'s token-cost concerns — provider switching
  here is driven by billing architecture, not token cost optimization, though
  both motivations apply.

### Claim 5: Claude Code lacks determinism controls (temperature, seed) and this is a design decision, not a gap — the "not planned" closure of the GitHub issue confirms Anthropic's position

- **Evidence**: jedwhite's direct reply (comment 46557904) to VikingCoder's
  question about seed/temperature: "Claude Code presently lacks support for
  temperature and seed parameters... the most recent tracked issue reportedly
  closed as 'not planned' in July."
- **Confidence**: anecdotal (jedwhite's characterization of the GitHub issue;
  not directly verified from the GitHub issue itself)
- **Quote**: jedwhite (comment 46557904) — "Claude Code presently lacks support
  for temperature and seed parameters... the most recent tracked issue reportedly
  closed as 'not planned' in July"
- **Our assessment**: This is a significant constraint on the executable markdown
  pattern — you cannot make Claude Code deterministic at invocation, only at the
  prompt-design level (very explicit instructions, few/no ambiguous choice points).
  The "not planned" closure suggests Anthropic views the interactive, non-deterministic
  nature as a feature of Claude Code rather than a configuration option. linkregister's
  "one and a half nines at best" reliability estimate (≈97%) deserves to be
  taken seriously: a 3% failure rate on a script that runs daily means one failure
  approximately every 33 days, which may be acceptable for summarization but not
  for automated deployments.

### Claim 6: The "more auditable than shell scripts" claim is contested — auditability of intent does not imply auditability of outcome for nondeterministic agents

- **Evidence**: chrismorgan's direct challenge (comment 46549725) to jedwhite's
  framing that executable markdown is "more auditable." jrmg's sardonic reply
  (46556502): `"Don't worry, it's 'more auditable'!"`. The specific concern:
  a shell script with `rm -rf /tmp/old-logs` has a known effect; a markdown
  script that says "clean up old logs" has an unknown effect that is an
  emergent property of the model version, context, and temperature at execution
  time.
- **Confidence**: anecdotal (community pushback, no controlled study comparing
  auditability between shell scripts and markdown scripts)
- **Quote**: chrismorgan (comment 46549725) — "I get the intent, but it's
  bizarre to hear invocation of nondeterministic tools that occasionally delete
  people's entire drives 'more auditable'."
- **Our assessment**: chrismorgan is correct about the core problem, but the
  framing needs nuance. The sense in which executable markdown *is* more auditable
  is that the intent is human-readable (the markdown states the goal in natural
  language), whereas a dense shell script may be opaque in purpose. The sense
  in which it is *less* auditable is that the mapping from intent to action is
  opaque (you cannot predict what shell commands Claude will issue). Both are
  true; the auditability advantage shifts depending on whether you care about
  auditing *purpose* (natural language wins) or *behavior* (deterministic script
  wins). jedwhite's actual use cases (summarization, formatting, evaluation)
  are in the purpose-audit regime; the concerning cases (infrastructure changes,
  file deletion) are in the behavior-audit regime.

### Claim 7: A specific trust-degradation failure mode exists for nondeterministic automation: a script passes early tests, builds deployment trust, then fails catastrophically when the model's interpretation of an ambiguous instruction shifts

- **Evidence**: DocTomoe's detailed reply (comment 46559884) describing the
  "analyze logfiles, then clean up" scenario: the model interprets "clean up"
  as `rm -rf /` after having interpreted it as "remove temp files" in prior runs.
  DocTomoe frames this as distinct from ordinary software bugs: "it passes tests,
  builds trust, and then fails catastrophically once the implicit interpretation
  shifts."
- **Confidence**: anecdotal (thought experiment, not documented incident)
- **Quote**: DocTomoe (comment 46559884) — "it passes tests, builds trust, and
  then fails catastrophically once the implicit interpretation shifts"
- **Our assessment**: This is the most analytically precise failure mode
  description in the thread. DocTomoe is describing what could be called
  "semantic drift under deployment": the same natural-language instruction is
  ambiguous across model versions, context lengths, and prompt contexts, so
  behavior that was stable drifts when the deployment environment changes (model
  upgrade, longer context, different preceding conversation). This is a systematic
  challenge for all natural-language automation, not just executable markdown.
  The mitigation is to make scripts maximally unambiguous: avoid instructions that
  have multiple valid interpretations, and for destructive operations, require
  explicit confirmation via the permission model. linkregister's devcontainer
  suggestion (comment 46557467) is the hardware-level mitigation: run scripts in
  an ephemeral container where "rm -rf /" is bounded.

### Claim 8: The author explicitly scopes the pattern to LLM-appropriate tasks: summarization, evaluation, formatting — not general-purpose script replacement

- **Evidence**: jedwhite's direct reply to DocTomoe (comment 46556968):
  "I know this will not appeal to developers who don't see a legitimate role for
  the use of AI coding tools with nondeterministic output. It is intended to be
  a useful complement to traditional Shell scripting, Python scripting etc. for
  people who want to add composable AI tooling to their automation pipelines..."
- **Confidence**: anecdotal (author's stated intent)
- **Quote**: jedwhite (comment 46556968) — "It is intended to be a useful
  complement to traditional Shell scripting, Python scripting etc. for people
  who want to add composable AI tooling to their automation pipelines"
- **Our assessment**: This is the correct scoping. jedwhite's use case list
  (summarizing test results, log analysis, installation scripts that detect
  OS and configure paths) sits in the "AI judgment adds value" category where
  LLM unreliability is tolerable. The critics who object are mostly imagining
  use cases in the "exact behavior required" category. Both groups are right
  for their respective domains. The guide should be explicit about this
  domain split: executable markdown is a workflow pattern for "AI-appropriate
  tasks in a pipeline," not a general-purpose scripting upgrade.

### Claim 9: An AST-parsing extension of the executable-markdown pattern is deployed in production as an "agentic control plane" at a Fortune 500 developer platform

- **Evidence**: graefawcett's comment (46568880): "I took that idea just as far
  as I could and landed here [zenodo.org/records/18181233]. It parses the AST
  out of it and then has a play. We're using it as an agentic control plane for
  a fortune 500s developer platform."
- **Confidence**: anecdotal (single commenter, no company named, no metrics;
  but the Zenodo reference is a verifiable academic preprint, suggesting serious
  implementation)
- **Quote**: graefawcett (comment 46568880) — "We're using it as an agentic
  control plane for a fortune 500s developer platform. Keep going with yours,
  you'll find it"
- **Our assessment**: This is the most significant single data point in the
  thread. It confirms that the executable-markdown pattern is not purely
  experimental — someone has taken it to enterprise production by adding AST
  parsing to extract structured intent from the markdown rather than passing
  raw text. The Zenodo preprint reference suggests this has been formally
  described (zenodo.org/records/18181233). The "control plane" framing is
  particularly notable: in the graefawcett variant, the markdown is not a
  single script but the orchestration specification for an entire developer
  workflow platform. This extends the pattern significantly beyond jedwhite's
  single-script invocation model.

### Claim 10: A community-supported namespace for installable AI scripts (installmd.org) emerged within days of the Show HN post — created by Mintlify's Nick Khami — suggesting nascent ecosystem standardization around the pattern

- **Evidence**: jedwhite's follow-up comment (46580804): "there's a new initiative
  called installmd.org created by Nick Khami at Mintlify to support experimentation
  with this methodology." Mintlify is a well-known developer documentation company;
  their CEO/founder's involvement suggests early validation from developer tooling
  ecosystem players.
- **Confidence**: anecdotal (jedwhite-reported, site was inaccessible at extraction
  time — ECONNREFUSED; Mintlify connection not independently verified)
- **Quote**: jedwhite (comment 46580804) — "there's a new initiative called
  installmd.org created by Nick Khami at Mintlify to support experimentation
  with this methodology"
- **Our assessment**: installmd.org appears to be envisioning a shared namespace
  where AI scripts can be distributed similarly to npm packages —
  `curl | claude-run` becomes the AI-native equivalent of `curl | bash` for
  one-liner installs. The security implications are significant (see DocTomoe's
  concern amplified by the remote execution case). The Mintlify involvement
  suggests the pattern is seen as relevant to documentation-as-code workflows —
  a natural fit for a company whose product converts docs into executable tools.
  The site was not accessible at extraction time, so its current status is unknown.

### Claim 11: A parallel community of independent tools targets the same pattern — mdflow, Runme, Atuin Desktop executable runbooks, ceving/mdexec, JohnKemeny's .ag format — confirming this is a recurring practitioner need, not a one-off invention

- **Evidence**: Multiple commenter references: lguzzon → mdflow (github.com/johnlindquist/mdflow);
  oulipo2 → runme.dev; yakkomajuri → Atuin Desktop runbooks (blog.atuin.sh/atuin-desktop-runbooks-that-run/);
  ceving → gitlab.com/ceving/mdexec; JohnKemeny described `.ag` files with
  `#!/usr/bin/env gpt-agent` shebangs including Require/Invariant/Ensure/Rescue
  sections for formal contract-style agent invocation.
- **Confidence**: anecdotal (commenters pointing to tools, not an empirical survey)
- **Quote**: JohnKemeny (comment 46554477) describing `.ag` format: "Input,
  Task, Output, Require [prerequisites], Invariant [constraints during execution],
  Ensure [success criteria], Rescue [fallback procedures]"
- **Our assessment**: The convergent independent invention of this pattern
  (mdflow, Runme, Atuin Desktop, ceving/mdexec, airun/.ag) is a strong signal
  that executable-markdown is a natural response to a real practitioner need,
  not a novelty project. The JohnKemeny `.ag` format is the most structured
  variant: its Require/Invariant/Ensure/Rescue sections map to preconditions,
  invariants, postconditions, and exception handling — a design-by-contract
  approach applied to AI invocation. If the pattern evolves toward standardization,
  the .ag formal structure may be more adoption-worthy than bare markdown for
  production use, precisely because it forces the author to specify success
  criteria and failure handling upfront.

## Concrete Artifacts

### Basic Executable Markdown Pattern (from HN post by jedwhite)

```markdown
#!/usr/bin/env claude-run

Analyze this codebase and summarize the architecture.
```

```bash
# Make executable and run
chmod +x task.md
./task.md

# Unix pipe composition
cat data.json | ./analyze.md > results.txt

# Remote script execution (jedwhite, comment 46580804)
curl -fsSL https://andisearch.github.io/ai-scripts/analyze.md | claude-run

# Simple prompts via echo
echo 'Explain what a Makefile does' | claude-run
```

### Permission-Scoped Shebang (from airun README + analyze.md example)

```markdown
#!/usr/bin/env claude-run --permission-mode bypassPermissions

Analyze this codebase and summarize the architecture.
List all files and directories.
```

*Note: Default mode blocks code execution. `bypassPermissions` must be explicitly
added to the shebang to enable file system or shell tool use. Source: airun README
and jedwhite comment 46580804.*

### airun Multi-Provider Invocation (from andisearch/airun README)

```bash
# Default (uses configured provider)
ai task.md

# Provider override
ai --aws --opus script.md      # AWS Bedrock, Opus tier
ai --azure --sonnet script.md  # Azure, Sonnet tier
ai --haiku script.md           # Local default, Haiku tier

# Session continuity (bypass rate limits via provider switch)
ai --resume

# Experimental Agent Teams
ai --team task.md

# Status
ai-status
```

*Source: andisearch/airun GitHub README (141 stars, MIT license, 2026)*

### JohnKemeny's .ag Format (comment 46554477 — formal contract approach)

```
#!/usr/bin/env gpt-agent

Input:    [target context — what the agent should know about]
Task:     [single clear objective]
Output:   [deliverables and required format]
Require:  [prerequisites that must be satisfied before execution]
Invariant: [constraints that must remain true during execution]
Ensure:   [success criteria that must be met upon completion]
Rescue:   [fallback procedures if requirements cannot be satisfied]
```

*Source: JohnKemeny, HN comment 46554477, 2026-01-09. This format enforces
design-by-contract discipline: the author must specify failure handling before
the agent is invoked, not after.*

### DocTomoe's Trust-Degradation Failure Mode (comment 46559884)

```
Scenario: An executable markdown script is deployed for "analyze logfiles, then clean up."

Initial runs:
  - Claude interprets "clean up" as "remove temp files from /tmp/logs/"
  - Script passes tests, is deployed in CI
  - Builds trust over weeks of correct execution

Failure condition:
  - Model upgrade or context shift changes interpretation
  - Claude interprets "clean up" as rm -rf / or deletes production data
  - "it passes tests, builds trust, and then fails catastrophically once
     the implicit interpretation shifts"

Mitigation: Use permission-scoped shebangs + explicit, unambiguous language
            + devcontainer/sandbox execution for any destructive operations.
```

*Source: DocTomoe, HN comment 46559884 (reply to jedwhite), 2026-01-09*

### Reliability Estimate (linkregister, comment 46557467)

```
"only one and a half nines at best"

= ≈97% reliability
= ≈3% failure rate per invocation
= In a daily automation pipeline: ~1 failure every 33 days
= In an hourly CI step: ~1 failure every ~1.4 days
```

*Source: linkregister, HN comment 46557467, 2026-01-09. No methodology given —
this is a practitioner estimate, not a measured benchmark.*

## Cross-References

- **Corroborates**:
  - **blog-ccunpacked-claude-code-architecture.md**: Step 1 of the 11-step agent
    loop explicitly supports stdin input ("User inputs message or piped via stdin,
    Source: TextInput.tsx"). This confirms the architectural foundation that makes
    `cat data.json | ./analyze.md` work natively — it is not a hack but a first-class
    input path in Claude Code's design. The shebang pattern is an application of
    this architectural affordance.
  - **discussion-hn-ttal-multiagent-factory.md** (Claim 4, logos): The logos
    runtime's `<cmd>` block pattern is the same "AI as composable Unix tool"
    philosophy applied at the agent-internal layer rather than the invocation layer.
    Both airun and logos reject the idea that AI systems must be wrapped in
    bespoke orchestration frameworks — both use existing Unix primitives (pipes for
    airun, bash execution for logos). The convergence from two independent tools
    on the "use Unix, not a framework" principle is worth noting.
  - **failure-beads-background-daemon.md**: The beads failure note's conclusion
    (the replacement `wedow/ticket` uses plain markdown files as the primary artifact)
    is the same philosophy as airun — markdown as the durable, human-readable,
    tool-agnostic artifact. Both represent the "markdown-first" pattern in
    AI-native tooling.

- **Extends**:
  - **blog-french-owen-coding-agents-feb-2026.md**: French-Owen describes Claude
    Code "Skills" as loadable markdown prompt files that can be invoked via slash
    commands. airun is the user-extensible, Unix-pipe-composable extension of that
    pattern: Skills are vendor-managed executable markdown; airun makes any markdown
    file executable by any user in any pipeline without requiring the Skills
    infrastructure. The executable-markdown pattern is Skills taken to its logical
    conclusion outside the interactive Claude Code session.
  - **practitioner-dadlerj-tin.md**: tin wraps Claude Code session lifecycle with
    hooks (start/stop, thread versioning). airun wraps it differently — stdin/stdout
    for stateless, ephemeral invocation. Both are "lightweight Claude Code wrappers"
    but tin preserves session history as the primary value; airun discards session
    state as a feature (no persistent context = no compaction risk, no context
    accumulation). The two represent opposite ends of the session-persistence axis
    in Claude Code wrapper design.

- **Contradicts**: None filed. The nondeterminism critique in this thread (Claims 5,
  6, 7) is not a contradiction with any existing source note — it is consistent with
  the general understanding that LLMs are stochastic. The specific "trust-then-fail"
  failure mode (Claim 7) is new to the corpus but does not contradict an existing
  claim. The debate about "auditable" (Claim 6) is an internal tension within this
  source, not a cross-source contradiction.

- **Novel**:
  - **The shebang/executable-markdown pattern as a Unix-native AI automation
    primitive**: No other source note covers treating markdown files as directly
    executable scripts via shebangs. This is the only source in the corpus that
    makes Claude Code invocation a standard Unix pipeline step (alongside `grep`,
    `awk`, `jq`, etc.).
  - **Per-script permission scoping via shebang arguments**: The pattern of
    embedding `--permission-mode bypassPermissions` directly in the shebang line
    is not documented in any other source. It is a novel method for declarative,
    per-script capability grants.
  - **"One and a half nines" reliability estimate**: linkregister's ≈97% reliability
    estimate is the only numeric reliability claim for Claude Code automation in
    the corpus. It is unsourced and unverified, but it is the only such estimate
    available.
  - **Trust-degradation failure mode** (DocTomoe's "passes tests, builds trust,
    then fails catastrophically"): This specific failure mode — semantic drift
    causing stable automation to fail destructively after deployment trust is
    established — is not described in any other source note. It is the category
    of AI-specific failure that differs from ordinary software bugs.
  - **AST-parsing variant for enterprise control planes** (graefawcett): The only
    enterprise production deployment data point for executable-markdown patterns
    in the corpus.
  - **JohnKemeny's design-by-contract .ag format**: Formal contract-style agent
    invocation (Require/Invariant/Ensure/Rescue) applied to AI scripts is not
    documented elsewhere. It is the most structured approach to the problem in
    the thread.

## Guide Impact

- **Chapter 01 (Daily Workflows)**: Add the "AI as Unix tool" pattern as a
  workflow primitive alongside interactive Claude Code sessions and orchestration
  frameworks. The key framing: `cat data.json | ./analyze.md > results.txt`
  integrates AI judgment into existing shell-based automation without building
  a dedicated harness. Cite jedwhite's explicit scoping (Claim 8) for when
  this pattern applies: summarization, classification, formatting, evaluation —
  tasks where LLM judgment adds value and output variation is acceptable.

- **Chapter 01 (Daily Workflows / Task Selection)**: Add the nondeterminism
  constraint as a domain-selection filter for executable markdown: appropriate
  when the script is the terminal step in a pipeline (output goes to a human),
  inappropriate when a downstream deterministic tool consumes the output. The
  linkregister "one and a half nines" estimate (≈97% per invocation) is the only
  corpus data point for expected reliability; at daily cadence, plan for one
  failure per month.

- **Chapter 02 (Harness Engineering / Minimal Harnesses)**: Add executable
  markdown as the lightest-weight Claude Code harness design: no framework,
  no orchestration layer, no persistent state. Compare against the spectrum:
  airun (no harness, Unix tools only) → tin (lightweight session hooks) →
  Kiln/TTal (full orchestration). The right point on the spectrum depends on
  task complexity and state requirements.

- **Chapter 03 (Safety and Verification)**: Add DocTomoe's trust-degradation
  failure mode (Claim 7) as a canonical safety case study for natural-language
  automation. The mitigation stack: (1) explicit, unambiguous language in scripts;
  (2) permission-scoped shebangs with minimum required flags; (3) container/sandbox
  execution for any scripts touching file systems or infrastructure; (4) human review
  gates before destructive operations. linkregister's devcontainer suggestion is
  the correct deployment model for executable markdown in CI/CD contexts.

- **Chapter 04 (Context Engineering / Specification as Executable)**: The
  executable-markdown pattern closes the loop between specification and invocation —
  the spec *is* the script. JohnKemeny's `.ag` format (Require/Invariant/Ensure/Rescue)
  is the formal-contract extreme of this: the author is forced to specify success
  criteria and failure handling as part of writing the "script." This aligns with
  `blog-osmani-good-spec`'s principle (specify before generating) but makes the
  spec the execution artifact rather than a separate document. Add this as the
  "specification-as-code" synthesis.

## Extraction Notes

- The original HN post body was extracted via the Hacker News Firebase API
  (`hacker-news.firebaseio.com/v0/item/46549444.json`) plus individual fetches of
  the top 25 comment IDs. The GitHub repo was identified as `andisearch/airun`
  (the tool was called `claude-run` at the time of the post and subsequently
  renamed). The example script at `andisearch.github.io/ai-scripts/analyze.md`
  was accessible. installmd.org was not accessible (ECONNREFUSED) at extraction
  time.
- The WebFetch model initially misidentified the repo as `andisearch/claude-switcher`
  (a prior name), but the current repo is confirmed as `andisearch/airun` (141
  stars, MIT license) from the `andisearch` GitHub organization page. The binary
  name `claude-run` was the historical name; `ai` is the current command.
- The Zenodo reference from graefawcett (zenodo.org/records/18181233) was not
  fetched — this is a gap. It represents the most mature production extension of
  the pattern in the thread and would be worth a separate extraction if the
  preprint is accessible.
- The HN post timestamp (1767925752) confirms the date as 2026-01-09. The issue
  body's `2026-01-09T02:29:12Z` is consistent.
- jedwhite's original HN post body text was not recovered verbatim from the
  Firebase API (the API returns a `text` field only for comments, not for story
  `text`). The post content was reconstructed from: (1) the issue body preview;
  (2) jedwhite's in-thread replies; (3) the airun GitHub README. No fabricated
  quotes are present — all jedwhite quotes above are from his HN comments, not
  the original post body.
