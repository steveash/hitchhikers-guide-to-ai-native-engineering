---
source_url: https://github.blog/changelog/2026-04-22-bring-your-own-language-model-key-in-vs-code-now-available
source_type: docs
title: "Bring your own language model key in VS Code now available"
author: GitHub (official changelog)
date_published: 2026-04-22
date_extracted: 2026-05-10
last_checked: 2026-05-10
status: current
confidence_overall: settled
issue: "#346"
---

# Bring Your Own Language Model Key in VS Code Now Available

> GitHub's April 2026 announcement that Copilot Business and Enterprise users can now
> configure external provider API keys directly in VS Code Chat — bypassing Copilot
> request quotas, expanding the model roster to hundreds of non-Copilot models, and
> introducing a default-on governance surface that enterprise AI policies must explicitly
> account for.

## Source Context

- **Type**: docs (GitHub official product changelog, ~200 words, April 22 2026; supplemented
  by the linked VS Code documentation page at
  `https://code.visualstudio.com/docs/copilot/customization/language-models#_bring-your-own-language-model-key`)
- **Author credibility**: GitHub engineering team announcing a production feature change.
  Authoritative for the fact that this feature exists, which plans can use it, which providers
  are supported, and what the admin policy controls are. The linked VS Code docs are the
  canonical reference for configuration steps and safety caveats. Neither source provides
  empirical data on task quality, cost comparisons with Copilot-managed models, or real-world
  adoption patterns.
- **Scope**: The BYOK feature in VS Code for Copilot Business and Enterprise subscribers.
  Covers: supported providers, available contexts within VS Code (chat vs. completions),
  billing model, and admin policy controls. Does NOT cover: individual Copilot plan access
  to BYOK (not addressed in the changelog — VS Code docs suggest a Copilot plan is still
  required); how BYOK interacts with Copilot CLI auto routing; specific model IDs supported
  per provider; cost comparison between provider-direct billing and Copilot request quotas;
  or how BYOK integrates with agent harness configuration files (CLAUDE.md, AGENTS.md).

## Extracted Claims

### Claim 1: BYOK is now generally available for Copilot Business and Enterprise users in VS Code

- **Evidence**: Official GitHub product changelog announcing general availability: "Copilot
  Business and Enterprise users can now use bring your own language model key (BYOK) in
  Visual Studio Code."
- **Confidence**: settled (product fact — the feature exists and is documented)
- **Quote**: "Copilot Business and Enterprise users can now use bring your own language model
  key (BYOK) in Visual Studio Code."
- **Our assessment**: This is a Business/Enterprise-only feature as announced in the changelog.
  Individual plan users (Free, Pro, Pro+) are not mentioned. For Ch02: BYOK is a new
  configuration surface that exists exclusively in the Business/Enterprise tier. Teams on
  those plans now have a path to models outside Copilot's managed pool without switching tools.
  Contrast with `docs-github-copilot-individual-plan-changes.md` Claim 5/6, which shows
  Opus access being narrowed for individual plans — BYOK provides an alternative path for
  Business/Enterprise users specifically.

### Claim 2: BYOK supports major cloud providers and local model runtimes as model sources

- **Evidence**: Official changelog enumerates providers explicitly: Anthropic, Gemini, OpenAI,
  OpenRouter, Azure, Ollama, and Foundry Local.
- **Confidence**: settled (definitional list stated in official changelog)
- **Quote**: "BYOK lets teams reuse their API keys to access models from providers like
  Anthropic, Gemini, OpenAI, OpenRouter, and Azure, as well as locally running models
  through Ollama and Foundry Local."
- **Our assessment**: The provider list is notable on two dimensions. First, it includes
  Anthropic — meaning a team with a Copilot Business subscription can now access Claude
  models via their own Anthropic API key within VS Code Chat, separate from GitHub's managed
  Claude agent integration. Second, local model support (Ollama, Foundry Local) enables
  air-gapped or privacy-sensitive use cases within the VS Code interface. For Ch02: document
  BYOK as the mechanism to extend VS Code Chat's model footprint beyond Copilot's managed
  pool, including to models from providers that may not be available in GitHub's managed tier.

### Claim 3: BYOK models are available throughout VS Code Chat — in the built-in plan agent and custom agents — but explicitly not in code completions

- **Evidence**: Official changelog states both the availability and the explicit exclusion:
  "Once configured, BYOK models are available anywhere in VS Code Chat, including the
  built-in plan agent and custom agents. BYOK does not apply to code completions."
- **Confidence**: settled (both availability and exclusion stated directly in official changelog)
- **Quote**: "Once configured, BYOK models are available anywhere in VS Code Chat, including
  the built-in plan agent and custom agents. BYOK does not apply to code completions."
- **Our assessment**: The code-completions exclusion is the most operationally limiting
  constraint. Inline code suggestions (the autocomplete feature) still use Copilot's managed
  model infrastructure; BYOK applies only to the chat interface. For practitioners who
  primarily use chat-based agentic workflows (e.g., Claude for complex multi-step tasks via
  VS Code Chat), this is not a significant limitation. For practitioners who depend on the
  inline completion quality of a specific external model, BYOK cannot help. For Ch02:
  be explicit that BYOK expands the chat model roster but leaves completions unchanged.

### Claim 4: BYOK usage is billed directly by the chosen provider and does not consume GitHub Copilot request quotas

- **Evidence**: Official changelog: "Usage is billed directly by your chosen provider and
  does not count against GitHub Copilot request quotas."
- **Confidence**: settled (stated directly in official changelog)
- **Quote**: "Usage is billed directly by your chosen provider and does not count against
  GitHub Copilot request quotas."
- **Our assessment**: This is the most significant operational implication of BYOK. Using
  an external provider model via BYOK is financially completely separate from the Copilot
  subscription. Teams at or near their Copilot request quota limits can use BYOK as a quota
  bypass — switching to provider-direct models for heavy-use scenarios while preserving
  quota for other uses. The cost trade-off: provider-direct billing may be higher per
  token than the Copilot premium request rate depending on the plan and model, but removes
  the quota ceiling entirely. For Ch04 (cost management): document BYOK as a quota-bypass
  pattern for teams hitting Copilot request limits, noting that total cost depends on the
  specific provider's pricing relative to Copilot's request multiplier.

### Claim 5: The BYOK policy is enabled by default — organization members can add external models without admin action unless the admin explicitly disables the policy

- **Evidence**: Official changelog: "The policy is enabled by default. Organization members
  can add models from built-in providers or install language model provider extensions. To
  disable BYOK for your organization, an administrator must disable the 'Bring Your Own
  Language Model Key in VS Code' policy in the Copilot policy settings on github.com."
- **Confidence**: settled (default-on policy stated directly in official changelog)
- **Quote**: "The policy is enabled by default."
- **Our assessment**: Default-on is a significant governance signal. Unlike the model
  selection feature for cloud agents (`docs-github-copilot-agent-model-selection.md`
  Claim 5, where admin must explicitly enable the policy), BYOK is active without any
  admin action. Organization members can immediately add external provider models to their
  VS Code Chat — including models outside any Responsible AI framework GitHub applies to
  its managed models. For Ch05 (enterprise governance): BYOK is an ungoverned configuration
  surface by default. Organizations with AI governance policies that restrict which models
  or providers can be used must actively disable this policy; relying on inaction preserves
  an open configuration surface.

### Claim 6: BYOK provides access to hundreds of non-built-in models and enables bypassing Copilot's built-in rate limits

- **Evidence**: VS Code documentation linked from the changelog:
  "access hundreds of models from different providers, beyond the built-in models" and
  "bypass the standard rate limits and restrictions imposed on the built-in models."
- **Confidence**: settled (stated in official VS Code documentation)
- **Quote**: "access hundreds of models from different providers, beyond the built-in models"
- **Our assessment**: The "hundreds of models" framing is marketing language, but the
  underlying capability is real: any model exposed by a provider via an OpenAI-compatible
  API (or a dedicated extension) can theoretically be surfaced through BYOK. The rate-limit
  bypass is specifically important for teams that hit Copilot's per-model rate ceilings —
  BYOK routes through the provider's own API, which has its own rate limits but is
  independent of Copilot's quota system. For Ch02: BYOK is the mechanism to access
  niche or specialized models (e.g., fine-tuned domain models, early-access models from
  a provider) that GitHub does not surface in its managed pool.

### Claim 7: Local models accessed via BYOK still require the Copilot service and internet connectivity — fully offline use is not supported

- **Evidence**: VS Code documentation: "Currently, using a locally hosted models still
  requires the Copilot service" and "You need to be online."
- **Confidence**: settled (stated in official VS Code documentation)
- **Quote**: "Currently, using a locally hosted models still requires the Copilot service"
- **Our assessment**: The "local model" framing in the changelog (Ollama, Foundry Local)
  implies offline/air-gapped operation, but the VS Code docs clarify that the Copilot
  service is still involved even when the model runs locally. For privacy-sensitive teams
  hoping to use BYOK for truly offline local model inference: this is not currently
  supported. The "currently" qualifier suggests this may change. For Ch02: when
  documenting local model support via BYOK, include the caveat that network and Copilot
  service connectivity are still required.

### Claim 8: BYOK removes GitHub's Responsible AI filtering guarantees when using non-built-in models

- **Evidence**: VS Code documentation: "There is no guarantee that responsible AI filtering
  is applied" when using BYOK.
- **Confidence**: settled (stated as a specific caveat in official VS Code documentation)
- **Quote**: "There is no guarantee that responsible AI filtering is applied"
- **Our assessment**: This is the key safety caveat for enterprise deployments. GitHub's
  managed model pool applies safety filters before model outputs reach users; BYOK models
  communicate directly with the provider's API, bypassing that filtering layer. For Ch05:
  organizations that rely on Copilot's responsible AI filtering as part of their enterprise
  AI governance should treat BYOK as an exception surface — by default, any organization
  member on a Business/Enterprise plan can configure a BYOK model that operates without
  GitHub's safety filtering. The default-on policy (Claim 5) compounds this: the
  ungoverned model surface is active without any admin action.

### Claim 9: Configuration uses either built-in provider integrations or VS Code extension-based providers from the Marketplace

- **Evidence**: VS Code documentation describes two configuration paths: "Built-in providers"
  (direct API key entry) and "Extension-based providers" (install from VS Marketplace,
  e.g., "AI Toolkit for VS Code with Foundry Local").
- **Confidence**: settled (configuration methods described in official VS Code documentation)
- **Quote**: (no direct quote for the two-path model; see paraphrase in Our assessment)
- **Our assessment**: The extension-based path is significant: it means any VS Code extension
  author can become a BYOK-compatible model provider. This extends the practical provider
  universe beyond the named set (Anthropic, Gemini, etc.) to any provider who ships a
  VS Code extension. For Ch02: practitioners who need a model not in the built-in provider
  list should search the VS Code Marketplace with the `language-models` tag
  (`https://marketplace.visualstudio.com/search?term=tag%3Alanguage-models`). The extension
  path also means the governance surface expands to include any extension the developer
  installs — another BYOK governance consideration for enterprise teams.

## Concrete Artifacts

### BYOK Supported Providers (as of April 22, 2026, from official changelog)

```
GitHub Copilot BYOK — Supported Providers in VS Code

CLOUD PROVIDERS (API key required):
  Anthropic       — Claude model family
  Gemini          — Google AI models
  OpenAI          — GPT model family
  OpenRouter      — Multi-provider proxy
  Azure           — Azure AI / Azure OpenAI

LOCAL RUNTIMES:
  Ollama          — Local model server (e.g., Llama, Phi-4)
  Foundry Local   — Microsoft AI Foundry local runtime

EXTENSION-BASED (via VS Code Marketplace):
  Any VS Code extension tagged "language-models"
  e.g., "AI Toolkit for VS Code with Foundry Local"

CONSTRAINT:
  Local runtimes still require Copilot service + internet connection.
  "Currently, using a locally hosted models still requires the Copilot service"
  "You need to be online"
```

### BYOK Availability and Exclusions

```
GitHub Copilot BYOK — Availability Matrix

PLAN:           Copilot Business or Enterprise (only — individuals not mentioned)
APPLIES TO:     VS Code Chat (all contexts)
                  ✓ Inline chat
                  ✓ Built-in plan agent
                  ✓ Custom agents
EXCLUDED FROM:  Code completions (inline suggestions unchanged)

BILLING:
  → Provider-direct: billed by chosen provider, NOT against Copilot quotas
  → Provider rate limits apply; Copilot request quota does not

SAFETY:
  → GitHub Responsible AI filtering: NOT guaranteed for BYOK models
  → Provider's own safety measures apply (varies by provider)
```

### BYOK Policy and Governance Configuration

```
GitHub Copilot BYOK — Policy Default and Controls

DEFAULT STATE:   Enabled for all Copilot Business/Enterprise organizations
                 (no admin action required to activate)

ADMIN DISABLE:
  Path:          GitHub.com > org Settings > Copilot > Policies
  Policy name:   "Bring Your Own Language Model Key in VS Code"
  Action:        Disable to prevent org members from adding BYOK models

CONTRAST with cloud agent model selection (docs-github-copilot-agent-model-selection.md):
  Agent model selection:  Admin must ENABLE (opt-in governance)
  BYOK:                   Admin must DISABLE (opt-out governance)
  → BYOK creates a default-open configuration surface requiring active governance.
```

### VS Code BYOK Configuration Steps (from linked documentation)

```
BYOK Setup in VS Code (built-in providers):

1. Open VS Code Chat language model picker
2. Select "Manage Models"
3. Choose "Add Models"
4. Select a model provider from the list
5. Enter provider-specific details (API key, endpoint URL, model ID as needed)
6. Model appears in the chat model picker for selection

BYOK Setup (extension-based providers):
1. Open VS Code Marketplace
2. Search: tag:language-models
3. Install desired language model provider extension
4. Follow extension-specific configuration instructions
```

## Cross-References

- **Corroborates** `docs-github-copilot-agent-model-selection.md` (issue #171):
  That source documents explicit model selection for Business/Enterprise subscribers when
  using Claude and Codex cloud agents on github.com (Claim 1, admin-gated). This BYOK
  source documents a parallel, complementary model-expansion feature for the same plan
  tiers in VS Code Chat. Together they show GitHub expanding the Business/Enterprise model
  footprint on two distinct surfaces: managed model tier selection for cloud agents (opt-in,
  admin-enabled, curated pool) and BYOK for VS Code Chat (default-on, admin-disabled, open
  provider set). The key contrast: agent model selection uses GitHub's managed pool with
  Responsible AI filtering applied; BYOK bypasses that pool and removes the filtering
  guarantee (Claim 8 here). This is not a contradiction — they serve different purposes —
  but enterprise governance must account for both surfaces together.

- **Extends** `docs-github-copilot-cli-auto-model-selection.md` (issue #203):
  That source documents the CLI auto pool as cost-bounded to 0x–1x multiplier models (Claim
  3 there — no Opus). BYOK is the VS Code Chat complement that bypasses Copilot's quota
  system entirely by routing through provider-direct billing (Claim 4 here). Together they
  show GitHub providing two different escape valves from model constraints: CLI auto handles
  rate-limit mitigation within Copilot's cost-bounded pool; BYOK enables quota-exempt access
  to external models in VS Code Chat. They target different failure modes (rate-limit relief
  vs. quota exhaustion / model availability) and different surfaces (CLI vs. VS Code Chat).

- **Extends** `docs-github-copilot-individual-plan-changes.md` (issue #289):
  That source documented Opus model access being removed from Copilot Pro (Claim 5 there)
  and narrowed for Pro+ (Claim 7 there), showing a clear direction of constraining model
  access on individual plans. This BYOK source introduces a different path — available to
  Business/Enterprise subscribers only — that bypasses Copilot's managed model pool
  entirely. The contrast: individual plan subscribers face narrowing model access with no
  BYOK escape (the changelog does not address individual plan access to BYOK); Business/
  Enterprise subscribers can use BYOK to access any external model without Copilot quota
  impact. The diverging access paths (individual: constrained; Business/Enterprise: expanded
  via BYOK) reinforce that the two subscription tiers are on different trajectories.

- **Complements** `docs-github-copilot-vs-april-2026.md` (issue #475):
  That source covers GitHub Copilot in Visual Studio (the Windows IDE, not VS Code) and
  introduces user-level agent definitions at `%USERPROFILE%/.github/agents/` as a
  governance gap (Claim 6 there). This BYOK source introduces an analogous governance gap
  in VS Code: a default-on policy that creates an ungoverned model surface unless the admin
  actively disables it (Claim 5 here). The two together show a pattern: recent GitHub
  Copilot feature releases are creating new governance surfaces — user-level agent
  definitions (VS) and BYOK models (VS Code) — that enterprise AI policies built on
  earlier feature assumptions may not cover. The guide should note that enterprise Copilot
  governance now requires auditing beyond the CCA custom-properties API to cover these
  newer surfaces.

- **Novel**:
  - First source in corpus documenting external provider API key integration (BYOK) as a
    VS Code Chat feature — no prior source describes the pattern of substituting an external
    provider's model for Copilot's managed models within the VS Code interface.
  - First source to document a default-on governance surface in GitHub Copilot — prior
    Copilot governance features (agent model selection, CCA enablement) require admin
    opt-in; BYOK requires admin opt-out. This reversal of the default is novel and
    operationally significant.
  - First documentation that GitHub's Responsible AI filtering is not guaranteed for
    non-built-in models — prior corpus sources assume Copilot applies filtering
    consistently; this is the first explicit exception.
  - First source to document provider-direct billing as a quota bypass mechanism within
    the VS Code Copilot ecosystem. Prior cost management sources discuss Copilot's own
    billing mechanics (auto mode discounts, premium multipliers); this introduces the
    orthogonal path of bypassing those mechanics via external provider billing.

## Guide Impact

### Chapter 02: Harness Engineering / Tooling Configuration

- **BYOK as a model-roster expansion pattern**: Add a note that VS Code Chat's model
  roster can be extended via BYOK to include any provider with a direct API key or VS Code
  Marketplace extension. For teams running Copilot Business/Enterprise who need access to
  models not in GitHub's managed pool (e.g., a specific Anthropic model version, a
  specialized fine-tuned model, or a competitor provider's model), BYOK is the VS Code
  configuration path. Document the exclusion: BYOK does not affect code completions.
- **Code completions vs. chat model divergence**: When BYOK is configured, the model used
  for VS Code Chat may differ from the model used for inline completions. Teams should
  document which model handles which surface in their harness configuration documentation.

### Chapter 04: Model Selection and Cost Management

- **BYOK as a quota-bypass pattern**: For teams that hit Copilot request quota limits, BYOK
  routes VS Code Chat usage through provider-direct billing, decoupling it from the Copilot
  quota system. Add as a specific pattern: configure BYOK with a provider (e.g., direct
  Anthropic API key) for heavy-use chat workflows; reserve Copilot quota for completions
  and other Copilot-native features. Note the trade-off: provider-direct billing rates
  depend on the specific model and provider, and must be compared against Copilot's
  premium request multiplier to determine whether BYOK is more or less expensive.

### Chapter 05: Team Adoption / Enterprise Governance

- **BYOK as a default-on governance gap**: Enterprise teams that rely on GitHub Copilot's
  admin policy controls to govern model access must explicitly disable BYOK if they want to
  restrict VS Code Chat to managed models only. The default-on state means BYOK is active
  from the moment the organization is on Business/Enterprise, without any admin action —
  the opposite of most Copilot governance features. Add this to enterprise Copilot
  governance checklists alongside the CCA policy controls from
  `docs-github-copilot-agent-model-selection.md` and `docs-github-copilot-vs-april-2026.md`.
- **Responsible AI filtering caveat**: Organizations that rely on Copilot's Responsible AI
  filtering as part of their enterprise AI safety posture should note that BYOK models
  operate outside that filtering layer. If organizational AI policy requires content
  filtering on all AI model outputs, BYOK should be disabled unless equivalent filtering
  can be confirmed at the provider level.
- **Governance surface audit**: The combination of BYOK (this source) and user-level agent
  definitions (`docs-github-copilot-vs-april-2026.md` Claim 5) means enterprise AI
  governance for GitHub Copilot now requires auditing at least three surfaces: (1) CCA
  org/repo policies for cloud agents, (2) VS Code BYOK policy for chat models, and
  (3) user-level agent definitions at `%USERPROFILE%/.github/agents/`. None of the three
  are covered by the others.

## Extraction Notes

1. **Source is thin by design**: The changelog is approximately 200 words. All substantive
   claims from the changelog itself are exhausted above. The linked VS Code documentation
   page (which was followed per MINER.md §1) provides the configuration steps, safety
   caveats (no guaranteed RA filtering), and local model constraints that are not in the
   changelog itself. Claims 7, 8, and 9 draw from the documentation page.
2. **Individual plan access ambiguity**: The changelog addresses Business/Enterprise
   explicitly. The VS Code documentation notes "You need access to a Copilot plan (for
   example, Copilot Free)" when describing local models, suggesting individual plan users
   may have some BYOK access. However, the changelog announcement specifically scopes to
   Business/Enterprise. This source note follows the changelog scope and does not speculate
   on individual plan access.
3. **No contradictions to file**: BYOK's default-on governance is a new surface, not a
   contradiction of any existing claim. The Responsible AI filtering caveat (Claim 8) is
   novel, not contradictory. No prior source claims that Copilot's filtering applies to
   all VS Code Chat interactions regardless of model source. No contradiction issue required.
4. **OpenAI-compatible API note**: The VS Code documentation mentions support for
   OpenAI-compatible models (in VS Code Insiders 1.104+, or via the
   `github.copilot.chat.customOAIModels` setting). This extends the provider universe
   beyond the named providers in the changelog. Not extracted as a separate claim because
   the feature's Insiders-track status makes it premature for stable-guide advice.
5. **Extension path extends the governance surface**: Any VS Code extension tagged
   `language-models` can add a BYOK provider (Claim 9). Enterprise teams should also
   audit installed VS Code extensions for language model providers as part of BYOK
   governance, not just the built-in provider list.
