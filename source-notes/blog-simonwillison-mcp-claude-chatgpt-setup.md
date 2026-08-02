---
source_url: https://simonwillison.net/2026/Jul/29/mcp-in-claude-and-chatgpt/
source_type: blog-post
title: "Adding a custom MCP server to Claude and ChatGPT"
author: Simon Willison
date_published: 2026-07-29
date_extracted: 2026-08-02
last_checked: 2026-08-02
status: current
confidence_overall: anecdotal
issue: "#2411"
---

# Adding a custom MCP server to Claude and ChatGPT

> Simon Willison's practitioner walkthrough of connecting a custom (non-directory)
> MCP server to the Claude.ai and ChatGPT consumer web chat UIs — Claude's flow is a
> single "Add custom connector" modal, ChatGPT's requires enabling an account-wide
> "Developer mode" and navigating a non-obvious Plugins-directory button, and neither
> platform's custom MCP is reachable from ChatGPT's Advanced Voice mode.

## Source Context

- **Type**: blog-post / TIL — Simon Willison's short "Today I Learned" format. The
  simonwillison.net post (`source_url`) is a summary link; the full technical content
  lives at `https://til.simonwillison.net/llms/mcp-in-claude-and-chatgpt`. Both pages
  were read in full; all quotes and artifacts are drawn from the TIL page.
- **Author credibility**: Simon Willison — creator of Django, creator of Datasette,
  prolific AI-tooling commentator with no vendor affiliation to Anthropic or OpenAI.
  His TIL posts are first-person, reproducible practice notes grounded in a real task
  he ran (connecting his own live `datasette-mcp` server to both products).
- **Scope**: Covers only the *client-side* UI mechanics of adding a custom MCP server
  to the Claude.ai and ChatGPT consumer web chat interfaces, using one unauthenticated
  example server. Does NOT cover: MCP server-side design or implementation, MCP
  configuration in Claude Code or any CLI/agentic harness, authenticated/OAuth MCP
  setup (the author explicitly states he has not tried it), mobile-app UI flows (the
  described flows are web/desktop), or any quantitative/benchmark data. The post is
  six short paragraphs with eight annotated screenshots/GIFs; the screenshot alt text
  (verbatim UI copy) is treated as source content, not the miner's own description.

## Extracted Claims

### Claim 1: Adding a custom MCP connector to Claude.ai is a single short flow — the "+" menu next to the chat prompt, through Connectors, to "Add custom connector"

- **Evidence**: Direct first-person description of the navigation path, illustrated
  with a screenshot whose alt text spells out the exact menu items encountered:
  "Add files or photos, Take a screenshot, Add to project, Add from GitHub, Skills,
  Connectors (highlighted), Add plugins and Web search," with a "Connectors" submenu
  listing "Add connector, Manage connectors" and toggles for already-connected
  services, and an "Add connector" submenu offering "Browse connectors and Add custom
  connector."
- **Confidence**: settled (the author completed and reproduced this exact flow; UI
  copy is quoted verbatim from the alt text, not paraphrased)
- **Quote**: "Adding an MCP in Claude.ai is quite straight-forward. Start with the +
  menu next to the chat prompt and navigate through it like this:"
- **Our assessment**: This is the first source-note in the corpus documenting the
  literal menu path a Claude.ai *end user* (not a Claude Code / API developer) follows
  to attach an arbitrary MCP URL. It is consistent with the "MCP as a first-class,
  low-friction integration surface" theme already established for developer-facing
  MCP guidance (`blog-anthropic-mcp-production-agents.md`), but this is the first
  practitioner evidence at the *consumer chat UI* layer specifically.

### Claim 2: Claude's "Add custom connector" modal needs only a name and an MCP URL to complete, with authentication configuration present but optional and left untested by the author

- **Evidence**: First-person description plus screenshot alt text of the completed
  modal: name field containing "simonwillison.net", URL field containing
  "https://datasette.simonwillison.net/-/mcp", a collapsed "Advanced settings"
  section, a warning that only connectors from trusted developers should be used, and
  Cancel/Add buttons.
- **Confidence**: anecdotal (single practitioner's completed flow for one
  unauthenticated server; the author explicitly flags the auth path as untested)
- **Quote**: "The \"Add custom connector\" modal then contains the necessary fields to
  add the MCP URL, and optionally configure authentication (I haven't tried this
  yet):"
- **Our assessment**: The minimal required fields (name + URL) confirm that Claude.ai
  treats a bare, unauthenticated MCP endpoint as a first-class connector target — no
  registration, no directory listing, and no OAuth are prerequisites for a user to
  attach it. The "trusted developers" warning shown in the modal is the platform's
  only stated safeguard against a user pointing Claude at an arbitrary, unvetted URL;
  the author does not test what technical controls (if any) back that warning.

### Claim 3: Once added, a custom Claude.ai connector can be toggled on and off per-session from the same Connectors menu used to add it

- **Evidence**: First-person description referring back to the menu shown in Claim 1's
  screenshot, which lists toggles for already-connected services (Descript, Gmail,
  Google Calendar, and simonwillison.net after setup).
- **Confidence**: settled (directly observed, reproducible UI behavior)
- **Quote**: "You can then toggle the new MCP on and off in the Connectors menu, shown
  above."
- **Our assessment**: Per-session toggling is a lightweight, user-controlled way to
  limit which MCP tools are exposed to Claude in a given conversation — a manual,
  UI-level analogue to the `enabledMcpjsonServers` project-scoping mechanism
  documented for Claude Code in `blog-simonwillison-cloudflare-mcp-api-fallback.md`
  Claim 1, but operating on a single global connector list rather than per-project
  config files.

### Claim 4: Adding a custom MCP server to ChatGPT first requires enabling an account-wide "Developer mode" toggle, explicitly labeled "ELEVATED RISK"

- **Evidence**: First-person description plus screenshot alt text: the Developer mode
  toggle is "switched on, described as allowing unverified connectors that could
  modify or erase data permanently," alongside a separate "Enforce CSP in developer
  mode" toggle (left off) and, in the same Security and login panel, "Sessions and
  Advanced security sections including a Lockdown mode toggle."
- **Confidence**: settled (directly observed account setting and its own displayed
  risk description)
- **Quote**: "ChatGPT is a whole lot more complicated. First, you need to enable
  \"Developer mode\" for your account in the Security and login panel:"
- **Our assessment**: This is a materially higher-friction and higher-stated-risk
  gate than Claude's flow (Claim 2's single "trusted developers" advisory warning).
  ChatGPT's own UI copy warns that Developer mode permits connectors that "could
  modify or erase data permanently" — a data-integrity risk disclosure, not merely a
  provenance-trust reminder. Notably, this Developer mode toggle sits in the same
  settings panel as the "Lockdown mode" toggle documented in
  `blog-simonwillison-openai-lockdown-mode.md` (OpenAI's deterministic,
  non-AI-evaluated network-restriction defense against prompt-injection data
  exfiltration) — the two toggles pull in opposite directions: Lockdown mode
  *restricts* what ChatGPT can reach over the network, while Developer mode
  *expands* it to arbitrary unverified MCP servers. A user who enables Developer mode
  for custom-MCP experimentation is, by ChatGPT's own account-settings taxonomy,
  operating in a materially different security posture than one running Lockdown
  mode.

### Claim 5: The button to add a new MCP server in ChatGPT is hard to find — a "+" icon in the top-right corner of the ChatGPT Plugins directory page

- **Evidence**: First-person description of locating the control, plus screenshot alt
  text: "The ChatGPT Plugins page, subtitled \"Work with ChatGPT across your favorite
  tools\", with a row of installed plugin icons. A red arrow points at the + button in
  the top right next to the plugin search box."
- **Confidence**: anecdotal (subjective "hard to find" judgment from a single
  practitioner, though the described UI location is a directly observed fact)
- **Quote**: "Having done that, you can add your new MCP. The button for that is hard
  to find - it's the \"+\" icon on the top right of the ChatGPT Plugins directory
  page:"
- **Our assessment**: The author felt the need to add a red arrow annotation to his
  own screenshot to point out the control — itself evidence the affordance is not
  visually prominent in ChatGPT's UI. Combined with Claim 4, ChatGPT's custom-MCP
  setup path is both gated (Developer mode) and non-discoverable (an easy-to-miss
  icon on a secondary settings page), a materially different UX posture from Claude's
  single, prominently-placed "+" menu next to the chat box.

### Claim 6: ChatGPT surfaces MCP servers to end users under the label "Plugin," not "MCP" — the add-server dialog is titled "New Plugin," and custom/unauthenticated servers are configured there via a "No Auth" setting with an explicit unreviewed-risk warning

- **Evidence**: First-person observation plus screenshot alt text of the "New Plugin"
  modal: "Name is set to simonwillison.net, Description is empty, Connection is set
  to Server URL with https://datasette.simonwillison.net/-/mcp, and Authentication is
  No Auth. An orange warning says \"Custom MCP servers introduce risk\" and a checked
  box confirms \"I understand and want to continue\", noting OpenAI hasn't reviewed
  the MCP server."
- **Confidence**: settled (directly observed UI terminology and warning copy)
- **Quote**: "This gives you the \"New Plugin\" modal. Apparently an MCP is a
  \"Plugin\" in the user-facing ChatGPT UI." / "Be sure to set authentication to \"No
  Auth\" if the plugin does not need OAuth configured:"
- **Our assessment**: The Plugin/MCP terminology mismatch is a concrete, practitioner-
  discovered UX detail with no prior corpus documentation — ChatGPT's underlying
  connector mechanism is MCP, but the consumer-facing label is the pre-existing
  "Plugin" concept, which could confuse a user who has read about "MCP" but never
  encountered ChatGPT's plugin system. The explicit per-connector "OpenAI hasn't
  reviewed the MCP server" disclosure is a second, connector-specific risk warning
  layered on top of the account-level Developer mode warning from Claim 4 — ChatGPT
  warns about unverified custom MCP servers at two separate points in the setup flow,
  where Claude warns once (Claim 2).

### Claim 7: Activating an already-added custom MCP/plugin inside a ChatGPT conversation requires a separate manual step each time — clicking "+" next to the chat box, typing the connector's name to search for it, and selecting it before a prompt can use it

- **Evidence**: First-person description of the activation flow, plus an animated
  screenshot (GIF) whose alt text confirms: "Animated demo showing clicking plus,
  typing simonwillison, selecting the MCP and running the prompt \"count the
  tables\"."
- **Confidence**: anecdotal (author's own experience navigating the web UI; explicitly
  scoped as "On web")
- **Quote**: "Activating the MCP is difficult as well. On web I found I had to click
  the + icon next to the chat and then type the name of the MCP to search for it,
  then select it so I could run a prompt:"
- **Our assessment**: Unlike Claude's connector, which is toggled on/off in a
  persistent Connectors menu (Claim 3), ChatGPT's activation is framed by the author
  as a per-use, search-and-select action rather than a standing toggle — a third
  compounding friction point on top of Developer mode (Claim 4) and the
  hard-to-find add button (Claim 5). This is a self-reported difficulty judgment,
  not a benchmarked comparison, so it is flagged anecdotal despite the underlying
  mechanical steps being directly observed.

### Claim 8: The first time a ChatGPT conversation actually invokes a newly-connected custom MCP tool, the platform interrupts with a two-stage consent flow — an in-chat "Connect" prompt followed by a modal confirming the connection

- **Evidence**: Screenshot alt text for both stages: a chat card headed "Connect
  simonwillison.net" stating "ChatGPT needs access to simonwillison.net to help with
  this request," with "Not now" and "Connect" buttons; followed by a modal headed
  "Add simonwillison.net to ChatGPT" with three notes — "Permissions always
  respected," "You're in control," and "Connectors may introduce risk" (the last
  warning that sites may attempt to steal your data) — and a "Connect" button.
- **Confidence**: settled (directly observed, screenshotted two-stage UI flow)
- **Quote**: "The first time you do this it will prompt you to enable the MCP:" /
  "Then show you this more visually impressive splash screen:"
- **Our assessment**: This is a fourth, distinct friction/warning point in ChatGPT's
  custom-MCP flow (after Developer mode, the hard-to-find add button, and per-use
  activation), and it is the first point where the platform explicitly names the data
  exfiltration risk ("sites may attempt to steal your data") to the end user in plain
  language, rather than the more abstract "introduces risk" / "hasn't reviewed"
  phrasing used earlier in setup. This consent-at-first-use pattern is functionally
  similar in intent to the "Claude will ask for permission before using one of your
  connected tools" gate documented for Claude's voice mode in
  `blog-anthropic-voice-mode-tools-multilingual.md` Claim 4, though that source
  describes a single permission prompt rather than ChatGPT's stacked, multi-stage
  warning sequence.

### Claim 9: Despite the multi-step setup, the custom MCP connection ultimately works end-to-end in ChatGPT once configured

- **Evidence**: Direct first-person confirmation following the full setup sequence
  described in Claims 4-8, and a screenshot alt text showing a live exchange: prompt
  "list tables" sent to the simonwillison.net plugin, with ChatGPT replying "I'll
  inspect the connected Simon Willison database and return its table names."
- **Confidence**: anecdotal (single practitioner's one-time confirmation; no
  reliability or repeat-session data given)
- **Quote**: "After all of this... it works!"
- **Our assessment**: The "After all of this" framing is the author's own summary
  judgment on the cumulative friction documented in Claims 4-8 — five distinct steps
  (enable Developer mode, find the add button, configure the No-Auth plugin, activate
  per-conversation, complete two-stage consent) versus Claude's three steps (open +
  menu, fill in name/URL, toggle on). The claim that it works is not itself contested
  anywhere in the source; the contrast is entirely about setup friction, not end
  functionality.

### Claim 10: Custom MCP tools connected to ChatGPT are not accessible from ChatGPT's Advanced Voice mode — a working text-chat MCP connector cannot be invoked while a voice conversation is running

- **Evidence**: Direct first-person report of an attempted use case (driving the MCP
  purely by voice) that failed, stated as a discovery rather than an expected result.
- **Confidence**: anecdotal (single practitioner's observation at one point in time;
  no confirmation from OpenAI documentation that this is a permanent or intentional
  limitation)
- **Quote**: "Sadly I was not able to access MCPs from ChatGPT Advanced Voice mode - I
  was hoping I could connect them to a regular chat and then start voice mode and
  drive an MCP purely through voice commands, but it looks like they are not
  available as tools while the voice mode conversation is running."
- **Our assessment**: This is a direct, product-specific contrast with Claude's voice
  mode, which — per `blog-anthropic-voice-mode-tools-multilingual.md` Claim 4 — "reaches
  the tools you've connected like Gmail and Slack" and executes actions behind a
  permission gate, i.e., Claude's voice mode *does* reach connected tools. This is not
  the same underlying claim being contradicted (one source is about Claude's own
  first-party connectors like Gmail/Slack surfaced through Claude's connector system;
  this source is about a third-party custom MCP server surfaced through ChatGPT's
  plugin system), so it is not filed as a corpus contradiction — it is a genuine
  product-capability difference between two vendors' voice-mode architectures rather
  than two sources disagreeing about the same fact. It is, however, a concrete data
  point for any guide section comparing voice-mode tool-use maturity across vendors:
  as of the two respective July 2026 sources, Claude's voice mode reaches connected
  tools with a permission gate, while ChatGPT's Advanced Voice mode does not expose
  custom MCP tools at all.

## Concrete Artifacts

### Example MCP server used throughout the walkthrough

```
Unauthenticated MCP server: https://datasette.simonwillison.net/-/mcp
Built with: https://github.com/datasette/datasette-mcp
Capability: read-only SQL query execution against a copy of the author's
            blog database (simonwillison.net)

Source: "I'm using my new unauthenticated MCP for my blog -
https://datasette.simonwillison.net/-/mcp - which uses
https://github.com/datasette/datasette-mcp to allow the execution of
read-only SQL queries against a copy of my site's database."
```

### Claude.ai custom connector flow (verbatim screenshot alt text)

```
Screenshot 1 (+ menu):
"The Claude prompt box with the + menu open, showing Add files or photos,
Take a screenshot, Add to project, Add from GitHub, Skills, Connectors
(highlighted), Add plugins and Web search. The Connectors submenu lists
Add connector, Manage connectors and toggles for Descript, Gmail, Google
Calendar and simonwillison.net. The Add connector submenu offers Browse
connectors and Add custom connector."

Screenshot 2 (Add custom connector modal):
"Claude's "Add custom connector" modal. The name field contains
simonwillison.net and the URL field contains
https://datasette.simonwillison.net/-/mcp. Below is a collapsed Advanced
settings section, a warning that only connectors from trusted developers
should be used, and Cancel and Add buttons."

Source: til.simonwillison.net/llms/mcp-in-claude-and-chatgpt
```

### ChatGPT custom MCP flow (verbatim screenshot alt text)

```
Screenshot 3 (Developer mode setting):
"ChatGPT settings on the Security and login tab. The Developer mode
section shows a Developer mode toggle marked "ELEVATED RISK" switched on,
described as allowing unverified connectors that could modify or erase
data permanently, plus an "Enforce CSP in developer mode" toggle that is
off. Above it are Sessions and Advanced security sections including a
Lockdown mode toggle."

Screenshot 4 (Plugins page add button):
"The ChatGPT Plugins page, subtitled "Work with ChatGPT across your
favorite tools", with a row of installed plugin icons. A red arrow points
at the + button in the top right next to the plugin search box."

Screenshot 5 (New Plugin modal):
"ChatGPT's "New Plugin" modal. Name is set to simonwillison.net,
Description is empty, Connection is set to Server URL with
https://datasette.simonwillison.net/-/mcp, and Authentication is No Auth.
An orange warning says "Custom MCP servers introduce risk" and a checked
box confirms "I understand and want to continue", noting OpenAI hasn't
reviewed the MCP server. A Create button sits in the bottom right."

Screenshot 6 (activation GIF):
"Animated demo showing clicking plus, typing simonwillison, selecting the
MCP and running the prompt "count the tables"."

Screenshot 7 (in-chat connect prompt):
"A ChatGPT conversation where the prompt "list tables" was sent to the
simonwillison.net plugin. ChatGPT replies "I'll inspect the connected
Simon Willison database and return its table names" and shows a card
headed "Connect simonwillison.net" saying ChatGPT needs access to
simonwillison.net to help with this request, with "Not now" and "Connect"
buttons."

Screenshot 8 (consent modal):
"A ChatGPT modal headed "Add simonwillison.net to ChatGPT" with the site
icon next to the OpenAI logo and a Connect button on a blue gradient.
Below are three notes: "Permissions always respected", "You're in
control" and "Connectors may introduce risk", the last warning that sites
may attempt to steal your data."

Source: til.simonwillison.net/llms/mcp-in-claude-and-chatgpt
```

### Step-count comparison (derived from the claims above, not stated verbatim by the source)

```
Claude.ai:  1. Open + menu -> Connectors -> Add custom connector
            2. Fill in name + URL, click Add
            3. Toggle connector on in Connectors menu
            (3 steps; one warning shown)

ChatGPT:    1. Enable "Developer mode" (ELEVATED RISK) in account security settings
            2. Find "+" on ChatGPT Plugins directory page (author notes it's hard to find)
            3. Fill in New Plugin modal, set Authentication to "No Auth", accept
               "Custom MCP servers introduce risk" warning
            4. Per-conversation: click + next to chat, search connector name, select it
            5. First use: accept in-chat "Connect" prompt, then accept consent modal
               warning that "Connectors may introduce risk" / sites may steal data
            (5 steps across 2 warning/consent stages; not available in Advanced Voice mode)
```

## Cross-References

- **Corroborates**:
  - `blog-anthropic-mcp-production-agents.md` Claim 5 ("Build remote servers so
    agents can use your system wherever they run"): Willison's example server
    (`https://datasette.simonwillison.net/-/mcp`) is exactly the remote,
    HTTP-accessible MCP server pattern that post recommends for production use — this
    note shows the *client-side* consumer-UI half of connecting to such a server,
    which the production-agents post does not cover.
  - `blog-simonwillison-cloudflare-mcp-api-fallback.md` Claim 5 (remote
    `type: http` MCP servers in Claude Code require only URL configuration and a
    simple OAuth flow via `/mcp`): That note documents low setup friction for remote
    MCP servers in the Claude Code CLI; this note documents comparably low friction
    (Claim 1-2: name + URL, three steps) for the same class of server in the Claude.ai
    consumer web UI — the "Claude's MCP onboarding is low-friction" pattern holds
    across both the CLI/agentic surface and the consumer chat surface.

- **Contradicts**: None filed. Claim 10 (ChatGPT's Advanced Voice mode cannot reach
  custom MCP tools) sits alongside `blog-anthropic-voice-mode-tools-multilingual.md`
  Claim 4 (Claude's voice mode does reach connected tools, behind a permission gate)
  as a genuine cross-vendor capability *difference*, not a disagreement about the same
  fact — the two sources describe different products' own connector systems at
  different points in time, so per MINER.md §4a this is a conditioning-variable
  contrast (which vendor, which connector system) rather than a contradiction
  requiring an issue.

- **Extends**:
  - `blog-anthropic-connector-observability.md`: That note covers server-side
    observability (dashboards, error rates, adoption metrics) for connectors already
    published to Anthropic's directory. This note covers the earlier, more basic
    stage of the same lifecycle — a user attaching an arbitrary *custom* MCP URL that
    is not in any directory at all, and the raw UI mechanics of doing so on both
    Claude.ai and ChatGPT. Together they span "how do I attach a URL as an end user"
    (this note) through "how do I monitor a published connector's production usage"
    (`connector-observability`).
  - `blog-anthropic-voice-mode-tools-multilingual.md`: That note documents Claude's
    July 2026 voice-mode expansion to tool execution via connected apps behind a
    permission gate. Claim 10 here adds the competitive contrast that ChatGPT's
    equivalent Advanced Voice mode, as of the same month, does not expose custom MCP
    tools at all — voice-mode tool-use maturity differs materially between the two
    vendors at this point in time.
  - `blog-simonwillison-openai-lockdown-mode.md`: That note documents OpenAI's
    Lockdown Mode as a deterministic, non-AI-evaluated network-restriction defense
    against prompt-injection data exfiltration, located in the same ChatGPT Security
    and login settings panel. Claim 4 here adds that the same settings panel also
    contains the opposite-direction "Developer mode" toggle (expanding reachable
    surface to unverified custom MCP servers) — the two notes together describe both
    ends of ChatGPT's user-configurable network/connector risk spectrum in one
    settings location.

- **Novel**:
  - **Consumer web-UI MCP onboarding mechanics for both Claude and ChatGPT**: No
    prior corpus source documents the literal click-by-click steps (with UI copy) an
    end user follows to attach a custom, non-directory MCP server in either product's
    web chat interface. All prior MCP corpus coverage addresses either server-side
    design/production deployment (`blog-anthropic-mcp-production-agents.md`) or
    Claude Code / CLI configuration
    (`blog-simonwillison-cloudflare-mcp-api-fallback.md`), not the consumer chat UI.
  - **ChatGPT's "Plugin" terminology for MCP servers**: The user-facing label
    mismatch (MCP server → "New Plugin" modal) is not documented anywhere else in the
    corpus.
  - **Quantified friction contrast between two vendors' custom-MCP onboarding**: The
    3-step / 1-warning (Claude) vs. 5-step / 2-warning-stage (ChatGPT) comparison
    derived above is new to the corpus and the first head-to-head UX comparison of
    MCP onboarding across the two dominant consumer chat products.
  - **ChatGPT Advanced Voice mode's custom-MCP blind spot**: No prior source
    documents that ChatGPT's voice interface cannot invoke a connector that works
    correctly in ChatGPT's own text chat.

## Guide Impact

- **Chapter 03 (Integrating Tools and MCPs)**: Add a concrete, side-by-side
  walkthrough of consumer-chat-UI MCP onboarding (as distinct from the existing
  Claude Code / production-server coverage), citing this source for the exact
  Claude.ai flow (Claims 1-3) and ChatGPT flow (Claims 4-9). Recommend framing it as
  "if you're demoing or personally using a custom MCP server outside a coding agent,
  here is what each platform actually requires" — useful for practitioners
  evaluating which consumer surface to point non-technical stakeholders at for an
  MCP demo, since the friction difference (3 steps vs. 5 steps across two consent
  stages) is a real onboarding-cost variable.
- **Chapter 04 (Agentic Patterns and Tool-Use Workflows / voice-triggered tool use)**:
  Add Claim 10 (ChatGPT Advanced Voice mode cannot reach custom MCP tools) as a
  concrete limitation alongside the existing coverage of Claude's voice-mode
  tool-execution capability (`blog-anthropic-voice-mode-tools-multilingual.md`).
  If the guide ever advises on voice-driven agentic workflows, it should note this
  is a per-vendor, currently-shipping limitation on ChatGPT's side, not a
  fundamental constraint of voice interfaces generally.
- **Chapter 06 (Security/Threat Model), if it covers connector trust**: Add the
  two-tier ChatGPT warning sequence (Developer-mode "ELEVATED RISK" account setting,
  Claim 4, plus the per-connector "OpenAI hasn't reviewed the MCP server" and
  "Connectors may introduce risk... sites may attempt to steal your data" warnings,
  Claims 6 and 8) as a concrete example of a vendor's own risk disclosure for
  unverified third-party MCP servers — useful as a citable baseline for what
  "informed consent" looks like in a shipped consumer product, versus Claude's
  single "trusted developers" advisory (Claim 2).

## Extraction Notes

- The `source_url` (simonwillison.net link-post) redirects/points to the full content
  at `https://til.simonwillison.net/llms/mcp-in-claude-and-chatgpt`; both were fetched.
  The simonwillison.net page itself is a thin summary/index entry; all quotes and
  concrete artifacts in this note are drawn from the TIL page, which contains the
  complete prose and all eight screenshots.
- WebFetch (AI-summarized) returned a materially shortened, paraphrased version of
  this post on the first attempt and could not access the TIL subdomain at all on a
  separate attempt against the top-level `simonwillison.net` URL. All quotes and the
  "Concrete Artifacts" screenshot descriptions in this note were instead taken from
  raw HTML fetched via `curl` against `til.simonwillison.net/llms/mcp-in-claude-and-chatgpt`,
  stripped of markup, and matched character-for-character against both the body text
  and each `<img alt="...">` attribute. The image `alt` text is itself the author's
  own written description of each screenshot (not the miner's interpretation) and is
  quoted verbatim in Concrete Artifacts and cited within claims accordingly.
- The post is short (six paragraphs, eight screenshots/GIFs) but the screenshots
  carry substantial verbatim UI copy in their alt text, which is why 10 claims were
  extractable from what reads as a brief TIL — the alt text functions as additional
  primary-source text, not decoration.
- No linked sub-pages were followed beyond the two pages noted above (simonwillison.net
  summary + the TIL itself); the `datasette-mcp` GitHub repo link and the MCP spec
  link in the opening paragraph are external references to tooling, not further
  narrative content, and were not treated as substantive linked pages per MINER.md §1.
- No contradictions were filed. The only candidate (ChatGPT's voice-mode MCP gap vs.
  Claude's voice-mode tool access, see Claim 10) was assessed against MINER.md §4a's
  filing criteria and judged to be a cross-vendor capability difference (conditioning
  variable: which vendor's own connector system) rather than two sources disagreeing
  about the same fact — see the Cross-References "Contradicts" entry for the
  reasoning.
- Cross-references were verified by re-reading each cited note in full and confirming
  claim numbers against their `### Claim N:` headings in document order before citing:
  `blog-anthropic-mcp-production-agents.md`,
  `blog-simonwillison-cloudflare-mcp-api-fallback.md`,
  `blog-anthropic-connector-observability.md`,
  `blog-anthropic-voice-mode-tools-multilingual.md`, and
  `blog-simonwillison-openai-lockdown-mode.md`.
- Confidence is `anecdotal` overall: this is a single practitioner's one-time,
  first-person walkthrough of two products' consumer UIs at one point in time (July
  2026), several of the individual mechanical steps are directly observed and
  reproducible (rated `settled` at the claim level), but the UX-friction judgments
  ("hard to find," "difficult," "a whole lot more complicated") and the voice-mode
  limitation are subjective or point-in-time observations that could change as either
  vendor updates their UI.
