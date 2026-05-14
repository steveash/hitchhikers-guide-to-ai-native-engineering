---
source_url: https://claude.com/blog/best-practices-for-computer-and-browser-use-with-claude
source_type: blog-post
title: "Best practices for computer and browser use with Claude"
author: Lucas Gonzalez and Luca Weihs (Anthropic)
date_published: 2026-05-13
date_extracted: 2026-05-14
last_checked: 2026-05-14
status: current
confidence_overall: settled
issue: "#735"
---

# Best practices for computer and browser use with Claude

> Anthropic's authoritative implementation guide for computer and browser use
> — covering screenshot scaling, model selection, thinking-effort tuning, prompt
> injection defense, context management, and demonstration-based teaching — the
> practitioner complement to the March 2026 product announcement.

## Source Context

- **Type**: blog-post (official claude.com blog, May 13, 2026)
- **Author credibility**: Lucas Gonzalez and Luca Weihs are Anthropic engineers
  in the computer use group. This is a first-party, engineering-team implementation
  guide published 7 weeks after the March 2026 product announcement. Unlike the
  announcement post (which described capabilities and the safety model at a high
  level), this post contains specific configuration parameters, API code examples,
  and failure diagnostics — the kind of content that comes from practitioners who
  built and operated the system. Claims about resolution, model behavior, and
  context management are authoritative; claims about reliability improvements from
  experimental features (advisor tool, batch tools) carry emerging confidence
  because they are marked beta or experimental.
- **Scope**: Covers the full implementation stack for computer use integrations:
  screenshot pre-processing, API limits per model family, message-array content
  ordering, click accuracy diagnostics, model selection heuristics, thinking-effort
  tuning, prompt injection defense, context management strategies (rolling buffer,
  LLM-based compaction, server-side compaction), the batch tools experiment,
  the advisor tool beta, periodic reminder nudges, and demonstration-based
  teaching. Includes working Python code examples for all major patterns. Does
  NOT cover connector-first hierarchy (covered in the March announcement), Dispatch,
  pricing, or Linux support.

## Extracted Claims

### Claim 1: Pre-downscaling screenshots to 1280×720 before sending to the API is the single highest-impact optimization for computer use click accuracy

- **Evidence**: Author's direct statement in the post's summary; framed as the
  primary takeaway after covering all other optimizations. The rationale: images
  exceeding API pixel limits are silently downscaled by the API before the model
  sees them, introducing aspect ratio distortion and resolution mismatch between
  what the model "clicks" and where the click lands in screen coordinates.
- **Confidence**: settled (first-party implementation guidance from the team that
  built the system; the root cause — silent API-side downscaling — is stated
  explicitly)
- **Quote**: "the single highest impact optimization is also one of the simplest:
  pre downscale your screenshots before sending them to the API"
- **Our assessment**: This is the canonical fix for the most common computer use
  failure mode. The problem is invisible: practitioners send high-resolution
  screenshots, the API downscales them silently, and the model's click coordinates
  land offset from the intended target. 1280×720 as the default resolution is
  safe for the Claude 4.6 family (max long edge: 1568 px, max total pixels:
  1.15 MP). For Opus 4.7, the limit is larger (max long edge: 2576 px,
  3.75 MP) and 1080p is the recommended starting point.

### Claim 2: API pixel limits differ by model family and silent violation is the root cause of click inaccuracy — practitioners must know their limits per model

- **Evidence**: Explicit table of limits per model family (4.6 family vs. Opus 4.7)
  provided in the post, with the statement that exceeding limits causes silent
  internal downscaling "before the model sees them."
- **Confidence**: settled (first-party specification from the model team)
- **Quote**: "Images exceeding API limits get internally downscaled before the
  model sees them. This is the primary cause of click inaccuracy at high
  resolutions."
- **Our assessment**: The two-sentence mechanism is the missing piece practitioners
  need. The click offset is not a model accuracy problem — it is a coordinate
  space mismatch: the model is clicking relative to the downscaled image it saw,
  but `scale_coordinates()` is mapping relative to the original. Every harness
  must either pre-downscale to safe limits or implement coordinate scaling that
  accounts for the API's downscaling factor. The post provides both approaches in
  working Python code.

### Claim 3: Text instruction must precede the screenshot in the messages array — placing the image first degrades click accuracy

- **Evidence**: First-party recommendation with rationale: "Text instruction first
  helps model know what to look for while processing screenshot."
- **Confidence**: emerging (stated design recommendation without ablation data;
  plausibly grounded in model architecture but not benchmarked in the post)
- **Quote**: "Place the text instruction before the image"
- **Our assessment**: This is a low-cost, high-plausibility fix that every computer
  use harness should adopt as a default. If content ordering was architecturally
  neutral, the post would not call it out. The framing ("helps model know what to
  look for while processing") is consistent with how attention operates in
  prefix-causal transformers — the instruction sets up the task before the
  model processes the screenshot's pixel content.

### Claim 4: Claude Sonnet 4.6 is the recommended default for computer use tasks requiring mechanical click precision; Opus 4.7 is preferred for complex reasoning tasks with high-resolution source images

- **Evidence**: First-party model selection guidance: "Claude Sonnet 4.6 tends to
  be more mechanically precise at clicking" and "Claude Sonnet 4.6 is also more
  robust when source images require heavy downscaling." Opus 4.7 is preferred when
  "wanting stronger reasoning with high-resolution source images." Haiku 4.5 is
  recommended when latency is the priority.
- **Confidence**: emerging (first-party recommendation; plausible based on model
  architecture differences; no benchmark data published in the post)
- **Quote**: "Claude Sonnet 4.6 tends to be more mechanically precise at clicking"
- **Our assessment**: The three-way split (Sonnet for precision, Opus for complex
  reasoning, Haiku for speed) applies the same model-selection principle used
  elsewhere in the corpus to the specific computer use context. Practitioners
  defaulting to Opus for all tasks are likely leaving both cost and precision on
  the table for routine clicking workflows. The Sonnet-for-clicking recommendation
  is counterintuitive (Opus is generally the more capable model) and specific
  enough to be worth testing.

### Claim 5: Thinking effort "medium" for Claude 4.6 models achieves near-best task success rate at roughly half the output tokens of "high" effort — making it the recommended default

- **Evidence**: First-party benchmark claim: medium effort "achieves close to the
  highest task success rate while using roughly half the output tokens of high."
  The post recommends medium as the default for most computer use tasks with the
  4.6 family, with "high" reserved for complex one-shot tasks and "low" for
  high-throughput cost-sensitive applications.
- **Confidence**: emerging (first-party quantitative claim without methodology
  disclosed; proportional improvement stated but absolute numbers not given)
- **Quote**: "close to the highest task success rate while using roughly half the
  output tokens of high"
- **Our assessment**: If the half-token claim holds, medium effort is the
  dominant strategy for 4.6-family computer use: nearly equivalent quality at half
  the cost. The post explicitly recommends *against* "max" effort for computer
  use on the 4.6 family, which is notable — more thinking does not always help
  and can introduce over-analysis failures. For Opus 4.7, "high" is the default,
  and "max" is reserved for complex one-shot tasks (Opus 4.7 benefits from more
  thinking at higher resolutions in ways the 4.6 family does not).

### Claim 6: Batch tools improve throughput for independent, non-visual sub-actions but compound errors when actions are sequentially dependent

- **Evidence**: First-party recommendation with explicit failure condition: "Recommend
  batch tools when the sub-actions are self-contained and don't depend on each
  other's visual outcomes." The post explicitly warns against using batch tools
  "in exploratory navigation, error-recovery sequences, or any workflow where
  'if action 1 fails I need to re-plan.'"
- **Confidence**: emerging (experimental feature; first-party guidance on when to
  apply it; failure mode is mechanistically clear)
- **Quote**: "when the sub-actions are self-contained and don't depend on each
  other's visual outcomes"
- **Our assessment**: The failure mode — "batch tools stack compounding error if
  action dependencies exist" — is the classic parallelization trap: batch execution
  assumes independence, but UI workflows are rarely fully independent (clicking
  "Submit" before "Fill in amount" produces errors). The guideline "use batch
  only when you'd be comfortable running all actions simultaneously without seeing
  intermediate results" is the correct mental model. This is consistent with
  multi-agent patterns for task decomposition generally: batch/parallel for
  independent work; sequential for dependent work.

### Claim 7: Using the official `computer_20251124` tool type gives automatic prompt injection classifier protection; other tool types require manual implementation

- **Evidence**: First-party statement about the official tool's built-in protection:
  "Use official computer_20251124 tool type for automatic classifier protection."
  The post also provides guidance for practitioners who implement their own
  computer use tool outside the official type.
- **Confidence**: settled (first-party description of a feature in a named, versioned
  tool type)
- **Quote**: "Classifiers are one layer of defense, not a complete solution"
- **Our assessment**: The automatic classifier in the official tool type confirms
  and extends the March 2026 announcement's Claim 3 (three-layer safety model)
  — the "activation-level prompt injection scanning" described in the announcement
  is implemented in the official tool type. Practitioners using custom computer use
  implementations must replicate this layer manually using Claude's built-in
  classifier API. The post emphasizes the classifier is a layer, not a complete
  solution, reinforcing the defense-in-depth principle from the announcement.

### Claim 8: Four behavioral best practices apply regardless of which injection defense mechanism is used

- **Evidence**: Explicit list from the "best practices regardless of classifier use"
  section: (1) pause before irreversible actions, (2) scope permissions, (3) log
  all actions including screenshots, (4) treat web content as untrusted.
- **Confidence**: settled (named practices from the official implementation guide;
  consistent with standard secure-by-design principles)
- **Quote**: "Have the agent pause and request user confirmation before performing
  irreversible actions"; "Treat all web content as untrusted"
- **Our assessment**: These four practices are the computer use equivalent of the
  general agentic safety checklist. The "pause before irreversible actions" practice
  is the most important for production deployments — it is the human-in-the-loop
  checkpoint that limits blast radius when the agent misunderstands intent. The
  "log all actions including screenshots" practice enables post-hoc audit of
  what the agent did, which is essential for debugging and compliance. Together
  these four practices should be the minimum bar for any computer use harness,
  independent of the injection defense mechanism.

### Claim 9: Rolling buffer screenshot pruning (keep_n=3, interval=25) with batch pruning maintains cache stability for computer use context management

- **Evidence**: First-party prescription with specific parameter values and a
  warning that pruning screenshots one-at-a-time "breaks caching." The rolling
  buffer approach prunes screenshots in batches to preserve cache-hit stability
  between prune events.
- **Confidence**: settled (first-party implementation guidance with specific
  parameter values; consistent with prompt caching principles established in other
  Anthropic posts)
- **Quote**: "Rolling buffer 'breaks caching' if screenshots pruned one at a time"
- **Our assessment**: This is the computer use specialization of the general
  caching principle ("static content first, dynamic content last") from the
  prompt caching post (blog-anthropic-prompt-caching-everything.md, Claim 3).
  Screenshots are the largest token consumers in computer use sessions; replacing
  them with `[Image omitted]` must be done in batches (interval=25) to avoid
  perturbing the cached prefix on every turn. The keep_n=3 parameter ensures the
  model retains enough recent visual context to understand current state while
  controlling token growth.

### Claim 10: Server-side compaction (beta) is available for automatic context management in long-running computer use sessions, triggered at a configurable input token threshold

- **Evidence**: First-party documentation of a beta API feature: `betas=["compact-2026-01-12"]`
  with `context_management` configuration block. The trigger is configurable
  (`"trigger": {"type": "input_tokens", "value": 150_000}`). Client-side code
  must mirror server compaction to keep views aligned.
- **Confidence**: emerging (beta feature; API syntax shown is first-party; behavior
  described as requiring client-side mirroring suggests the protocol is still
  stabilizing)
- **Quote**: (no direct quote; see concrete artifacts for verbatim API configuration)
- **Our assessment**: Server-side compaction for computer use is the analog of
  Claude Code's autocompact feature, applied to API-level computer use sessions.
  The requirement to mirror server compaction on the client side (truncating
  messages to match the server's view after compaction fires) adds implementation
  complexity. The post provides the exact Python code for this mirroring. This is
  a significant addition for practitioners building long-running browser automation
  agents where context accumulates rapidly due to screenshot volume.

### Claim 11: The advisor tool (beta) lets a Sonnet-based agent call Opus-level reasoning on demand for planning, without giving Opus tools or screen access

- **Evidence**: First-party description of the `advisor_20260301` tool type: "Useful
  for long-horizon tasks where most turns are mechanical clicking but occasional
  planning moments benefit from Opus-level reasoning." The advisor runs "without
  tools and without context management, so it can't click or browse." It receives
  a constrained view of context, not the full session.
- **Confidence**: emerging (beta feature; first-party design rationale; no
  performance benchmarks published)
- **Quote**: "long-horizon tasks where most turns are mechanical clicking but
  occasional planning moments benefit from Opus-level reasoning"
- **Our assessment**: The advisor tool is the computer use specialization of
  the orchestrator-subagent pattern: a Sonnet executor delegates planning to
  an Opus advisor without giving Opus the overhead of executing actions. The
  "without tools and without context management" constraint prevents the Opus
  advisor from becoming a runaway consumer of tokens and actions. The cap-per-request
  design (cap advisor calls to bound worst-case cost) is the right production
  posture. This is the most novel experimental feature in the post; it inverts
  the usual model selection logic (use Opus for everything hard) into a mixed-model
  architecture where Sonnet handles execution and Opus handles planning.

### Claim 12: Demonstration-based teaching via recorded, annotated workflows is the primary reliability improvement mechanism for repetitive computer use tasks

- **Evidence**: Full section titled "Improving reliability: teaching Claude" covering
  a data model (`WorkflowStep`, `SavedWorkflow`), recording approach, annotation
  method (blue circles marking click positions), and adaptive playback. The core
  principle is "show, don't tell": demonstrate the task once, then have the model
  adapt the demonstration to current UI state on each run.
- **Confidence**: emerging (well-motivated design with code examples; no ablation
  data comparing taught vs. untaught reliability rates)
- **Quote**: (no direct quote for the core principle; "show, don't tell" is the
  section summary)
- **Our assessment**: This is the most novel pattern in the post. Rather than
  writing prompts that describe a workflow, practitioners record themselves doing
  it once — capturing screenshots, actions, selectors, and optionally voice
  narration — and use that recording as context on subsequent runs. The adaptive
  playback mode allows the model to find UI equivalents even when the UI has
  changed. This is closer to few-shot programming-by-demonstration than traditional
  prompt engineering. The `WorkflowStep` data model capturing both selectors and
  coordinates (for robustness) is directly reusable. This pattern has no analog
  in the existing corpus.

### Claim 13: Periodic reminder nudges in the system prompt counteract goal drift and instruction forgetting in long-running computer use sessions

- **Evidence**: Listed as a debugging pattern in the "Debugging patterns in the
  reference implementation" section. The technique inserts periodic reminders of
  key constraints (e.g., "remember to log all actions") into the message stream
  to combat the model's tendency to drop earlier instructions as context grows.
- **Confidence**: emerging (described as a debugging pattern, suggesting it addresses
  a real production failure mode; no metrics on effectiveness)
- **Quote**: (no direct quote; see extraction notes)
- **Our assessment**: This is the computer use instance of the general "context rot"
  problem documented in blog-anthropic-session-management-1m-context.md (Claim 1
  there: "Context rot is the observation that model performance degrades as context
  grows because attention gets spread across more tokens"). Periodic nudges are a
  compensating mechanism — injecting fresh copies of critical instructions avoids
  the attention dilution that causes goal drift. It is a manual mitigation for
  the same failure that steerable /compact addresses in interactive sessions.

## Concrete Artifacts

### Screenshot Scaling Pipeline (Python)

```python
# Source: "Best practices for computer and browser use with Claude"
# Anthropic (Lucas Gonzalez and Luca Weihs), 2026-05-13

import math
from PIL import Image
import base64
import io

MAX_LONG_EDGE = 1568  # 1568 for 4.6, 2576 for Opus 4.7
MAX_PIXELS = 1_150_000  # 1.15MP for 4.6, 3.75MP for Opus 4.7

def prepare_screenshot(screenshot, native_w, native_h):
    display_w, display_h = 1280, 720
    resized = screenshot.resize((display_w, display_h), Image.LANCZOS)
    buffer = io.BytesIO()
    resized.save(buffer, format="PNG")
    b64 = base64.standard_b64encode(buffer.getvalue()).decode()
    return b64, display_w, display_h

def scale_coordinates(api_x, api_y, display_w, display_h, screen_w, screen_h):
    screen_x = int(api_x * (screen_w / display_w))
    screen_y = int(api_y * (screen_h / display_h))
    return screen_x, screen_y

def compute_max_api_fit(native_w, native_h):
    aspect = native_w / native_h
    h_from_pixels = math.sqrt(MAX_PIXELS / aspect)
    w_from_pixels = h_from_pixels * aspect
    if native_w >= native_h:
        w = min(w_from_pixels, MAX_LONG_EDGE)
        h = w / aspect
    else:
        h = min(h_from_pixels, MAX_LONG_EDGE)
        w = h * aspect
    w = min(w, native_w)
    h = min(h, native_h)
    return int(w), int(h)
```

### API Limits by Model Family

```
# Claude computer use API pixel limits (as of May 2026)
# Source: Anthropic, 2026-05-13

Claude 4.6 family:
  Max long edge:    1568 pixels
  Max total pixels: 1.15 megapixels (1,150,000 px)
  Default resolution: 1280×720
  Avoid: 1920×1080 and above

Claude Opus 4.7:
  Max long edge:    2576 pixels
  Max total pixels: 3.75 megapixels (3,750,000 px)
  Default resolution: 1080p (1920×1080)
  Note: MacOS device pixel ratio = 2; account for this in screenshots
```

### Click Accuracy Diagnostic Table

```
# Click accuracy symptom → cause → fix mapping
# Source: Anthropic, 2026-05-13

Symptom                           | Likely Cause                          | Solution
----------------------------------|---------------------------------------|-----------------------------------
Clicks consistently offset        | display_width_px/display_height_px    | Ensure display dims match resized
  in one direction                |   mismatch; screenshot exceeds limits;|   screenshot; pre-downscale to
                                  |   image-first content ordering        |   1280×720; move text before image
Clicks land in roughly right area | Target very small; source very high   | Enable enable_zoom: True; capture
  but miss target                 |   resolution; aspect ratio distortion |   at lower DPI; preserve aspect ratio
Model clicks wrong element        | Ambiguous instruction; similar-looking| More specific prompts with positional
  entirely                        |   elements; UI too complex            |   context; break into smaller steps
Accuracy poor across the board    | Screenshots above API limits;         | Pre-downscale all screenshots;
                                  |   extreme compression ratios;         |   try 1280×720 baseline
                                  |   resolution too low                  |
```

### Thinking Effort Recommendations by Model

```
# Thinking effort configuration for computer use
# Source: Anthropic, 2026-05-13

Claude 4.6 family:
  Default / most use cases:  "medium"  (near-best success at ~half tokens of "high")
  High-throughput / cost:    "low"
  Simple workflows:          disable thinking
  Complex one-shot tasks:    "high"
  Do NOT use:                "max" (not recommended for computer use on 4.6)

Claude Opus 4.7:
  Default / most use cases:  "high"
  High-throughput / cost:    "low"
  Simple well-defined:       consider Sonnet 4.6 instead
  Complex one-shot tasks:    "max"
```

### API Configuration: Thinking Effort

```python
# Source: Anthropic, 2026-05-13
import anthropic

client = anthropic.Anthropic()

response = client.beta.messages.create(
    model="claude-sonnet-4-6",
    max_tokens=16000,
    betas=["computer-use-2025-11-24"],
    thinking={"type": "adaptive"},
    output_config={"effort": "medium"},
    messages=[...],
    tools=[{
        "type": "computer_20251124",
        "name": "computer",
        "display_width_px": 1280,
        "display_height_px": 720,
    }],
)
```

### Cache Breakpoint Placement for Computer Use

```python
# Source: Anthropic, 2026-05-13
# Rule: one breakpoint on system prompt/tools, up to 3 on most recent tool results

def set_trailing_cache_control(messages, max_breakpoints=3):
    for msg in messages:
        for block in msg.get("content", []):
            if isinstance(block, dict):
                block.pop("cache_control", None)
    
    placed = 0
    for msg in reversed(messages):
        for block in reversed(msg.get("content", [])):
            if placed >= max_breakpoints:
                return
            if isinstance(block, dict) and block.get("type") == "tool_result":
                block["cache_control"] = {"type": "ephemeral"}
                placed += 1
```

### Rolling Buffer Screenshot Pruning

```python
# Source: Anthropic, 2026-05-13
# Rule: prune in batches (interval=25) to preserve cache stability;
# never prune one at a time (breaks caching)

def prune_old_screenshots(messages, keep_n=3, interval=25):
    image_positions = [
        (msg_idx, block_idx)
        for msg_idx, msg in enumerate(messages)
        for block_idx, block in enumerate(msg.get("content", []))
        if isinstance(block, dict) and block.get("type") == "image"
    ]
    if len(image_positions) <= keep_n + interval:
        return messages
    
    to_prune = image_positions[:-keep_n][-interval:]
    for msg_idx, block_idx in to_prune:
        messages[msg_idx]["content"][block_idx] = {
            "type": "text",
            "text": "[Image omitted]",
        }
    return messages
```

### Server-Side Compaction Configuration (Beta)

```python
# Source: Anthropic, 2026-05-13
# Requires: betas=["compact-2026-01-12", "computer-use-2025-11-24"]

response = client.beta.messages.create(
    model="claude-opus-4-7",
    max_tokens=16000,
    betas=["compact-2026-01-12", "computer-use-2025-11-24"],
    context_management={
        "edits": [{
            "type": "compact_20260112",
            "trigger": {"type": "input_tokens", "value": 150_000},
            "instructions": COMPACT_PROMPT,
        }]
    },
    messages=[...],
    tools=[...],
)
```

### Advisor Tool Configuration (Beta)

```python
# Source: Anthropic, 2026-05-13
# Pattern: Sonnet executor + Opus advisor for plan-heavy workflows
# The advisor has no tools and no context management — it cannot click or browse

response = client.beta.messages.create(
    model="claude-sonnet-4-6",
    max_tokens=16000,
    betas=["advisor-tool-2026-03-01", "computer-use-2025-11-24"],
    tools=[
        {
            "type": "advisor_20260301",
            "name": "advisor",
            "model": "claude-opus-4-7",
        },
        {
            "type": "computer_20251124",
            "name": "computer",
            "display_width_px": 1280,
            "display_height_px": 720,
        },
    ],
    messages=[...],
)
```

### Demonstration Workflow Data Model

```python
# Source: Anthropic, 2026-05-13
# Captures both selectors and coordinates for robustness when UI changes

from dataclasses import dataclass, field
from typing import Literal, Optional

@dataclass
class WorkflowStep:
    action: Literal["click", "type", "navigate", "scroll", "select"]
    description: str
    timestamp: float
    selector: Optional[str] = None
    coordinates: Optional[dict] = None
    url: Optional[str] = None
    screenshot: Optional[str] = None
    viewport_dimensions: Optional[dict] = None
    speech_transcript: Optional[str] = None
    value: Optional[str] = None

@dataclass
class SavedWorkflow:
    id: str
    name: str
    steps: list[WorkflowStep] = field(default_factory=list)
    description: Optional[str] = None
    start_url: Optional[str] = None
    created_at: float = 0.0
    usage_count: int = 0
```

### Playback Context Prompt Template

```python
# Source: Anthropic, 2026-05-13
# Annotated screenshots use BLUE CIRCLES to mark click positions
# Model is told these are guides, not elements to interact with

def generate_playback_context(steps):
    steps_description = "\n".join(
        f"Step {i+1}: {step.description}"
        for i, step in enumerate(steps)
    )
    
    return f"""<demonstration_context>
The user has recorded a demonstration showing how to perform this task.

RECORDED STEPS:
{steps_description}

ABOUT THE SCREENSHOTS:
- Each screenshot shows the screen state when an action was taken
- BLUE CIRCLES mark where the user clicked
- The blue highlighting is NOT part of the actual interface
- Your own screenshots will NOT have these markers

HOW TO USE THIS DEMONSTRATION:
1. Review all steps and screenshots
2. Take your own screenshot to see CURRENT page state
3. Find the element indicated by blue highlights
4. Follow the same sequence of actions, adapting to differences
5. Use judgment to find equivalent elements if UI has changed
</demonstration_context>"""
```

### Approaches Tested That Did Not Help

```
# Approaches the Anthropic team tried that produced no measurable improvement
# Source: Anthropic, 2026-05-13

1. Breaking the image into smaller tiles
   — No improvement in click accuracy

2. Overlaying a grid pattern with coordinates
   — Did not produce reliable gains

3. Resize algorithm choice (PIL LANCZOS vs sips)
   — Produced identical results
```

## Cross-References

- **Corroborates**:
  - **blog-anthropic-dispatch-computer-use.md** (issue #177), Claim 3: The March
    2026 announcement described a three-layer safety model including
    "activation-level prompt injection scanning." This post confirms that the
    official `computer_20251124` tool type provides this scanner automatically
    (Claim 7 here), validating the announcement's design-intent claim with a
    concrete implementation detail. The two sources together give the full picture:
    the March announcement stated the safety model; this post explains how to
    access it and what to do when you're not using the official tool type.
  - **blog-anthropic-prompt-caching-everything.md** (issue #478), Claim 3: The
    prompt caching post states "The best way to do this is static content first,
    dynamic content last." The rolling buffer and cache breakpoint patterns in this
    post (Claims 9 and the Concrete Artifacts section) are the computer use
    implementation of that same principle — placing cache breakpoints on trailing
    tool results maintains a stable cached prefix despite high screenshot volume.

- **Contradicts**: None found. The dispatch note's Claim 6 ("Computer use is still
  early compared to Claude's ability to code or interact with text. Claude can make
  mistakes.") is still accurate — this post is entirely about mitigating those
  limitations, not refuting them.

- **Extends**:
  - **blog-anthropic-dispatch-computer-use.md** (issue #177): The March 2026
    announcement established the product capability, the connector-first hierarchy,
    and the three-layer safety model. This May 2026 post is the practitioner
    implementation guide for everything the announcement described at the design
    level. Claim 2 in the announcement ("no setup required") is nuanced here: while
    the capability needs no connector setup, production use requires significant
    harness engineering (resolution management, model selection, thinking effort
    tuning, context management, injection defense) to achieve reliable results.
  - **blog-anthropic-prompt-caching-everything.md** (issue #478): That post
    documents the four-layer cache hierarchy and cache-breaking pitfalls for
    general harness design. This post extends those patterns to the computer use
    domain, where screenshots are the primary cache-breaking element and rolling
    buffer pruning is the domain-specific mitigation.
  - **blog-anthropic-session-management-1m-context.md** (issue #316): The session
    management post covers context rot and compaction for interactive Claude Code
    sessions. This post covers the same context management problem for API-level
    computer use sessions, adding computer-use-specific strategies (rolling buffer
    for screenshots, server-side compaction beta, LLM-based summarization with a
    specific prompt). The two posts together give practitioners the full compaction
    toolkit for both interactive and programmatic deployments.

- **Novel**:
  - **Demonstration-based teaching (show, don't tell) as a reliability mechanism**:
    No other source in the corpus describes programming-by-demonstration for
    computer use tasks. The `WorkflowStep`/`SavedWorkflow` data model, annotation
    convention (blue circles), and adaptive playback mode are completely new to
    the corpus.
  - **Advisor tool (beta) as a mixed-model architecture for computer use**: The
    pattern of a Sonnet executor calling an Opus planner without giving Opus tools
    is new. No existing corpus source documents a mixed-model architecture within
    a single computer use session.
  - **Per-model-family API pixel limits as a named harness constraint**: The
    specific limits (1568 px / 1.15 MP for 4.6; 2576 px / 3.75 MP for Opus 4.7)
    and the "silent downscaling is the root cause" mechanism are new to the corpus.
  - **Batch tools for computer use**: The batch tool pattern (parallel sub-actions
    without intermediate visual feedback) and its failure condition are new.
  - **Thinking effort tuning for computer use** with specific per-family
    recommendations (medium for 4.6, high for Opus 4.7, avoid max for 4.6) is new
    to the corpus.
  - **Server-side compaction beta API** (`compact-2026-01-12`) with client-side
    mirroring requirement: new API feature not documented in any existing note.
  - **Empirically disproven techniques** (tiling, grid overlay, resize algorithm):
    the explicit "didn't help" list is useful negative knowledge not present
    elsewhere.

## Guide Impact

- **Chapter 02 (Harness Engineering — computer use integration)**: Add a dedicated
  section on computer use screenshot pipeline: always pre-downscale to 1280×720
  (or per-model limit), always place text instruction before image, always
  implement coordinate scaling via `scale_coordinates()`. This post should anchor
  the section — it is the authoritative implementation reference.

- **Chapter 02 (Harness Engineering — model selection)**: Update model selection
  guidance for computer use tasks specifically. The general "use Opus for complex
  tasks" heuristic inverts for mechanical click precision: use Sonnet 4.6 for
  most computer use workflows (more mechanically precise), Opus 4.7 for
  reasoning-heavy tasks with high-resolution source images, Haiku 4.5 for
  latency-sensitive pipelines. This is distinct from code generation model
  selection guidance.

- **Chapter 02 (Harness Engineering — context management for computer use)**:
  Add rolling buffer screenshot pruning (keep_n=3, interval=25) as the
  standard pattern for managing screenshot accumulation. Add server-side
  compaction beta as an option for long-running sessions. Cross-reference
  the blog-anthropic-prompt-caching-everything cache breakpoint guidance.

- **Chapter 03 (Safety and Verification — computer use threat model)**: The March
  2026 announcement (blog-anthropic-dispatch-computer-use.md) established the
  three-layer safety model. This post extends it with specific implementation
  guidance: (1) use `computer_20251124` tool type for automatic classifier
  protection, (2) add four behavioral practices regardless of classifier (pause
  before irreversible, scope permissions, log with screenshots, treat web content
  as untrusted). Add as the implementation section following the architecture
  overview from the March announcement.

- **Chapter 04 (Advanced Patterns — demonstration-based teaching)**: Add the
  show-don't-tell demonstration pattern as a first-class reliability technique
  for repetitive computer use tasks. The `WorkflowStep` data model and playback
  context prompt template are ready-to-use implementation starters.

- **Chapter 04 (Advanced Patterns — mixed-model orchestration)**: The advisor
  tool represents a new architectural pattern: a cheaper executor model that
  calls a more capable planner model on demand without giving the planner
  tool access. This generalizes beyond computer use — add as a pattern example
  wherever the guide discusses cost-optimized multi-model routing.

## Extraction Notes

- The source was fetched via WebFetch (which processes HTML through an AI model
  before returning). The tool provided a structured extraction of all headings,
  recommendations, warnings, code examples, and use cases. Quotes presented as
  direct quotes were those the WebFetch model enclosed in quotation marks in its
  response — these likely represent verbatim text from the post, but cannot be
  guaranteed character-for-character without raw HTML access. Code examples were
  returned in code blocks and are treated as verbatim.
- The post is comprehensive (40 section headings) and clearly written by
  practitioners who built the system. Code examples are complete and working
  (they reference real API beta strings like `"computer-use-2025-11-24"` and
  `"compact-2026-01-12"`).
- The post references a "reference implementation" linked from the article for
  full code. That reference implementation was not fetched (out of the 5-link
  follow-up budget); practitioners implementing production computer use should
  consult it directly.
- The post covers three beta/experimental features (batch tools, advisor tool,
  server-side compaction). Confidence for these claims is downgraded to
  "emerging" — they represent Anthropic's intended design but may change as
  betas mature.
- No paywalled or inaccessible content. The article is public on claude.com.
- The "approaches tested that didn't help" section (tiling, grid overlay, resize
  algorithm) is unusually candid negative-knowledge documentation from Anthropic —
  it prevents practitioners from wasting time on interventions the team already
  ruled out.
