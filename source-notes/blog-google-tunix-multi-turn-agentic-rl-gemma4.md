---
source_url: https://developers.googleblog.com/multi-turn-agentic-reinforcement-learning-with-tunix-and-gemma-4-on-google-tpus/
source_type: blog-post
title: "Multi-Turn Agentic Reinforcement Learning with Tunix and Gemma 4 on Google TPUs"
author: "Wei Wei, Developer Advocate (Google)"
date_published: 2026-11-19
date_extracted: 2026-11-21
last_checked: 2026-11-21
status: current
confidence_overall: anecdotal
issue: "#4879"
---

# Multi-Turn Agentic Reinforcement Learning with Tunix and Gemma 4 on Google TPUs

> A worked, single-game example (Plane Strike) of RL-training a tool-using agent: env/tool-parser/agent/learner split, a stop-token trick that keeps one assistant turn open across tool responses, and an admitted credit-assignment limit of trajectory-level reward.

## Source Context

- **Type**: blog-post (tutorial with code; companion repo `planestrike-gemma4-rl`)
- **Author credibility**: Wei Wei is a Google Developer Advocate and author of two earlier Tunix posts. This is vendor tutorial content promoting Tunix/TPUs, not an independent evaluation.
- **Scope**: One toy environment (6x6 Plane Strike), one model (Gemma 4 E2B, thinking mode), one run on a single TPU v6e-8 host. No baselines other than the untrained model, no cost/throughput data, no ablations of the settings used. This is RL post-training of the model, not practitioner workflow for using agents; relevance to the guide is peripheral (harness plumbing, reward/verification design).

## Extracted Claims

### Claim 1: Agentic RL pipeline decomposes into four modular components
- **Evidence**: Code walkthrough with a file per component (`env.py`, `strike_tool.py`, `agent.py`, `trajectory_utils.py`/`train_planestrike.py`).
- **Confidence**: emerging
- **Quote**: "We set up the multi-turn RL pipeline in four modular components:"
- **Our assessment**: A clean separation (environment, tool + chat-template parser, conversation agent, collection engine + learner) that mirrors the harness split in agent engineering generally. It is a design description, not a tested claim.

### Claim 2: The environment fixes a seed so all rollouts in a GRPO group play the identical hidden board
- **Evidence**: `PlaneStrikeEnv` code takes `entry["seed"]` and the post states all 8 rollouts share the board.
- **Confidence**: emerging
- **Quote**: "Each environment instance receives a task dictionary with a seed that fixes the hidden plane position so all 8 rollouts in a GRPO group play the exact same board:"
- **Our assessment**: Sensible: group-relative advantages only compare like with like when the task instance is the same. The analogue for agent evals is controlling task state when comparing runs. No evidence offered that it matters empirically.

### Claim 3: Env step returns observation/reward/done/info; per-step rewards are summed into one trajectory-level reward
- **Evidence**: Description of `_step_impl` returning `EnvStepResult(observation, reward, done, info)`.
- **Confidence**: emerging
- **Quote**: "computes the step reward (summed into the trajectory-level reward over the episode), and returns EnvStepResult(observation, reward, done, info)."
- **Our assessment**: Standard RL interface. Notable mainly because Claim 8 depends on it.

### Claim 4: Gemma 4 declares tools in the system prompt and a tool-calling turn ends at a native stop token, `<|tool_response>`, after which the environment's reply is injected inside the same assistant turn
- **Evidence**: Token-level format shown in the post and implemented by `Gemma4ToolChatTemplateParser` (appends tool declarations to the system message; renders `tool` messages as `response:strike{value:...}<tool_response|>`; suppresses the generation prompt when the last message is a tool message).
- **Confidence**: emerging (first-party description of the model's format)
- **Quote**: "<|tool_response> is one of Gemma 4's native stop tokens: the model pauses there and waits for response:strike{value:<|\"|>...<|\"|>}<tool_response|>, then continues generating its next thought and tool call within the same assistant turn."
- **Our assessment**: A concrete harness-level mechanic: tool use as a pause/resume of a single turn rather than a new turn. The same stop token must be listed in the rollout `eos_tokens` (see artifacts), otherwise generation would not pause. Model-specific; useful as an illustration of how tool-call plumbing differs per model family.

### Claim 5: The agent only counts a final answer with a single valid strike call; reasoning inside the thought channel is ignored
- **Evidence**: `tool_strike` behavior described in prose; `update_from_model` also records `tool_calls_per_turn` and whether the turn ended at the tool-response token.
- **Confidence**: emerging
- **Quote**: "only a final answer with a single valid strike call counts as a valid board coordinate (otherwise INVALID_ACTION is returned)."
- **Our assessment**: Strict output validation turns format violations into a distinct, countable failure (`INVALID_ACTION`), which later shows up as the `game/train/invalid` metric. Good verification hygiene.

### Claim 6: `exact_token_continuity=True` preserves token IDs across turns to avoid retokenization drift; loss is GSPO-token with RLOO advantage
- **Evidence**: Config shown (`loss_algo="gspo-token"`, `advantage_estimator="rloo"`, `exact_token_continuity=True`). No ablation.
- **Confidence**: anecdotal
- **Quote**: "exact_token_continuity=True to preserve exact token IDs across multi-turn rollouts without retokenization drift"
- **Our assessment**: Plausible and consistent with the train/inference-mismatch theme in the Zero-TIM note, but the post gives no evidence of the effect size.

### Claim 7: Async vLLM server-mode rollouts and prefix caching are used because variable-length multi-turn rollouts are the bottleneck
- **Evidence**: Config `rollout_vllm_server_mode=True`, `enable_prefix_caching=True`; actor, reference and rollout workers share the 8 chips of a v6e-8 host.
- **Confidence**: emerging
- **Quote**: "Multi-turn agentic RL is often bottlenecked by variable-length rollout generation"
- **Our assessment**: Restates the thesis of the throughput note; no measurements here.

### Claim 8: Reported result: win rate 9.4% -> 95% and average game length ~22.44 -> ~16 strikes after 100 agentic GRPO steps
- **Evidence**: Single run, 100 steps of 8 boards x 8 games; baseline stated as held-out-board performance; the final 95% is attributed to training metrics ("climbs from ~0.20 on initial training rollouts (9.4% on held-out evaluation boards) to ~0.95"). The post does not clearly say whether the final 95% is on held-out boards. No seeds, variance, or non-RL baselines (e.g., prompt tuning, SFT).
- **Confidence**: anecdotal
- **Quote**: "out of the box, it wins only 9.4% of games on held-out boards (averaging 22.44 strikes). After 100 steps of agentic GRPO with Tunix, its win rate reaches 95% while cutting the average game length to ~16 strikes."
- **Our assessment**: Directionally believable for a tiny closed game (6x6 grid, 4 orientations), but the toy setting, single run and train/held-out ambiguity mean it should not be cited as general evidence that agentic RL works. Note the 23-strike cap means the untrained average of 22.44 is near "always lose".

### Claim 9: Tool-call compliance converges before win rate
- **Evidence**: Training metrics described: tool-call rate ~100%, invalid ~0, repeats ~0.55 -> ~0.15 (curves not reproduced in text).
- **Confidence**: anecdotal
- **Quote**: "Tool calling compliance converges first: game/train/tool_call_rate quickly reaches ~100%, while game/train/invalid drops to ~0 and game/train/repeats falls from ~0.55 to ~0.15."
- **Our assessment**: Useful ordering insight: format/protocol compliance is learned first, task skill second. Suggests tracking protocol metrics separately from outcome metrics when evaluating agents.

### Claim 10: A single trajectory-level reward shared by all turns limits credit assignment (author's own admission)
- **Evidence**: Author states it in the results section; no experiment with per-turn credit.
- **Confidence**: emerging
- **Quote**: "Because all strikes in a game currently share a single trajectory-level reward, further improvements can be achieved with finer per-turn credit assignment."
- **Our assessment**: The most transferable point for Ch03: outcome-only verification of a multi-step agent run cannot tell you which step was wrong. Stated as a future-work remark rather than demonstrated.

### Claim 11: Prebuilt `ToolEnvironment`/`ToolAgent`/`ToolManager` abstractions exist for standard multi-tool agents
- **Evidence**: One sentence in the env section; custom classes were only needed for custom turn control (the in-turn tool response).
- **Confidence**: emerging
- **Quote**: "For standard multi-tool agents, tunix.rl.agentic also provides ready-to-use ToolEnvironment, ToolAgent and ToolManager abstractions out of the box"
- **Our assessment**: Corroborates the abstraction claim in the throughput note; the custom stop-token handling is the reason this example bypassed them.

## Concrete Artifacts

Attributed to the source post (Wei Wei, Google Developers Blog, 2026-11-19).

Gemma 4 tool-call turn format:
```
<|channel>thought
...model reasoning...
<channel|><|tool_call>call:strike{cell:<|"|>C5<|"|>}<tool_call|><|tool_response>
```

Agent routing of observations (excerpt):
```python
def _observation_to_messages(self, observation, reward, done, info) -> None:
    if not done:
      role = "tool" if self._awaiting_tool_response else "user"
      self._messages.append({"role": role, "content": str(observation)})
...
self._awaiting_tool_response = response.rstrip().endswith(strike_tool.TOOL_RESPONSE_START)
```

Rollout stop tokens (excerpt):
```python
eos_tokens=[tokenizer.eos_token_id, tokenizer.convert_tokens_to_ids("<turn|>"),
            tokenizer.convert_tokens_to_ids(strike_tool.TOOL_RESPONSE_START)],
rollout_vllm_server_mode=True,
rollout_vllm_kwargs={"enable_prefix_caching": True, "dtype": "bfloat16", ...},
rollout_vllm_sampling_kwargs={"skip_special_tokens": False},
```

Training launch and setup:
```
python train_planestrike.py \
  --run_dir runs/grpo_6x6_tool_thinking_100 \
  --learning_rate 2e-6 \
  --lr_end 2e-7
```
Game: 6x6 grid (A1-F6), one 8-cell plane in one of 4 orientations, cap of 23 strikes; 100 steps x (8 boards x 8 games). Model: google/gemma-4-E2B-it, thinking mode, single Cloud TPU v6e-8.

## Cross-References

- **Corroborates:** `blog-google-tunix-agentic-rl-throughput.md` Claim 7 (composable `ConversationAgentBase`/`BaseTaskEnv`/`ToolEnvironment` abstractions) and Claim 3 (inference engine keeps generating for other trajectories while one is blocked) — this post uses the same abstractions and async vLLM server mode in a concrete example. `blog-google-tunix-zero-tim-bitwise-on-policy-rl.md` Claim 8 (token IDs must be shared, not retokenized) is consistent with `exact_token_continuity=True`.
- **Contradicts:** none found; no contradiction issue filed.
- **Extends:** `blog-google-tunix-agentic-rl-throughput.md` (adds a runnable end-to-end example with measured outcomes), `blog-google-tunix-autonomous-post-training-agents.md` (which covers single-turn SFT/GRPO; this covers multi-turn tool use), and `blog-google-tunix-gemma-reasoning-hackathon.md` (single-turn GRPO).
- **Novel:** Gemma 4 native tool-call format with `<|tool_response>` as a stop token and in-turn response injection; seeded shared boards per GRPO group; the author's stated limit of trajectory-level credit assignment; observation that tool-call compliance converges before task win rate.

## Guide Impact

- **Chapter 02 (harness)**: Optional illustrative example that tool-call plumbing is model-specific (stop tokens, in-turn tool responses, tool declarations in the system prompt), citing this note. Low priority; the guide is practitioner-focused.
- **Chapter 03 (verification)**: Could cite Claims 9 and 10 for two points: track protocol/format-compliance metrics separately from outcome metrics, and outcome-only (trajectory-level) signals cannot attribute failure to a specific step. Cite as anecdotal.
- No existing chapter claim is contradicted.

## Extraction Notes

- Read the full post (fetched raw HTML and stripped tags so quotes are verbatim); no linked sub-pages followed, and the GitHub repo `planestrike-gemma4-rl` was not read, so code excerpts are only those in the post.
- Published date 2026-11-19 comes from the page.
- The first paragraph's wording suggests 95% is held-out, while the results section describes ~0.95 following training rollouts; flagged as ambiguous in Claim 8.
- Cross-reference claim numbers were checked against the cited notes' `### Claim` headings. The reasoning-hackathon note is cited without claim numbers.
