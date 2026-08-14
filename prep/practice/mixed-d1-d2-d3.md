# Mixed Set — Domains 1, 2 and 3 (20 questions)

**Purpose:** confirm all three completed domains together, before Mock 1 on 16 Aug. Built 14 August.

Weighted like the blueprint ratio between these three domains (27 : 18 : 20):
**8 × Domain 1, 6 × Domain 2, 6 × Domain 3.**
Four questions ask for **two answers** — one in five, matching the real exam.

All questions are new. None appear in the drills, the D1+D2 mixed set, or Set 1.

Several questions deliberately target the traps on your repeat-miss list: `@import` (missed
twice), tool granularity (missed twice), Grep vs semantic search (missed four times — this time
from the *other* direction), `tool_choice` values, and the select-two counting habit.
**The answer key is balanced** — A, B, C and D are each correct four times among the sixteen
single-answer questions.

**The questions use exam-level English.** The explanations are in simple English.

Time: 40 minutes. Answers below — cover them while you work.

> **Before you start, apply the exam-day rule from the log:** for every question, first check
> whether it says "select two". If it does, count the symptoms in the scenario and match one
> answer to each symptom.

---

### Scenario: Billing & Subscriptions Support Agent

**Q1.** An engineer proposes terminating the agentic loop with an explicit `task_complete` tool:
the system prompt instructs the model to call it when the customer's issue is resolved, and the
loop exits when that call appears. In testing, a fraction of sessions run until the safety
iteration cap because the model answers the customer but never calls the tool. What should
replace this design?

A. Retain the tool but strengthen the instruction to "you MUST call `task_complete` before ending".
B. Exit when `stop_reason` is `"end_turn"` — the API already signals completion, and the extra tool is redundant and skippable.
C. Exit when a response contains a text block and no `tool_use` blocks.
D. Lower the iteration cap so hung sessions terminate sooner.

---

**Q2.** A customer requests cancellation with a full refund of an annual plan, 200 days into the
term. Policy permits full refunds only within the first 30 days. The request parameters are
well-formed and the billing service is healthy. What should the `cancel_subscription` tool
return?

A. `errorCategory: "transient"`, `isRetryable: true` — the outcome could differ on a later attempt.
B. `errorCategory: "validation"`, `isRetryable: false` — the request was not acceptable as submitted.
C. `errorCategory: "business"`, `isRetryable: false`, with a customer-friendly explanation of the 30-day policy that the agent can relay.
D. `errorCategory: "permission"`, `isRetryable: false` — the agent is not authorised to issue refunds of this size.

---

**Q3.** To reduce latency, a teammate proposes letting the billing subagent forward its findings
directly to the communications subagent, bypassing the coordinator. What is the strongest reason
to keep the hub-and-spoke arrangement instead?

A. Routing everything through the coordinator preserves visibility into what moves between agents, provides a single place for error handling, and keeps control over what information flows where.
B. Subagents are technically incapable of invoking one another, so the proposal cannot be implemented.
C. Direct subagent messaging is acceptable only when both subagents run the same model version.
D. Hub-and-spoke is a development-time convenience for debugging and can safely be dropped in production.

---

**Q4.** Your agent extracts structured data from uploaded invoices, receipts and purchase orders,
using three schema-specific extraction tools. With `tool_choice: {"type": "auto"}`, the model
frequently replies with a prose summary of the document instead of calling any extraction tool.
You still need the model to select which schema fits each document. Which setting is correct?

A. Keep `{"type": "auto"}` and add a system prompt instruction forbidding prose answers.
B. Force `{"type": "tool", "name": "extract_invoice"}`, since invoices are the most common type.
C. Use `{"type": "none"}` and parse the structured data out of the model's text reply.
D. Use `{"type": "any"}` — the model must call some tool, but chooses which one.

---

**Q5.** Two incidents are reported in the same week. First, the agent issued a €900 goodwill
credit although the system prompt states a €100 cap. Second, case timelines are unreliable
because one billing service reports amounts in cents and another in euros with decimals, and the
model confuses them mid-reasoning. Which two changes address these? **(Select two.)**

A. Enforce the cap with tool call interception (`PreToolUse`): block any credit above €100 and route it to human escalation.
B. Move the cap statement to the top of the system prompt and repeat it in every user turn.
C. Add a `PostToolUse` hook that normalises all monetary amounts to a single unit before the model reads the results.
D. Ask the two billing services to standardise their units before the agent ships.

---

**Q6.** Compliance requires that `update_payout_account` is never executed before the customer's
identity has been verified. Today this lives as a system prompt instruction, and an audit has
flagged several near-misses where the model almost skipped verification. What is the correct fix?

A. Add few-shot examples demonstrating the verification-first sequence.
B. Move the instruction to the first line of the system prompt and set it in capital letters.
C. Instruct the model to re-state the verification status in its reasoning before each tool call.
D. Add a prerequisite gate that programmatically blocks `update_payout_account` until `verify_identity` has returned a verified customer ID.

---

**Q7.** The agent chooses between `lookup_subscription` and `lookup_invoice`, whose one-line
descriptions are nearly identical, and it picks the wrong one roughly a third of the time. What
is the most effective first step?

A. Merge both into a single `lookup_billing_record` tool with a `record_type` parameter.
B. Expand each description to state accepted input formats, example queries, edge cases, and when to use it instead of the other tool.
C. Classify each request upstream and force `tool_choice` to the correct tool.
D. Split each tool further, by billing period, so the boundaries are unambiguous.

---

### Scenario: Multi-Agent Codebase Analysis Platform

**Q8.** Your coordinator dispatches five independent module analyses, but each Task call is issued
in its own turn after the previous subagent finishes, so total wall-clock time equals the sum of
all five runs. What is the correct change?

A. Issue all five Task calls in a single response, so the subagents run in parallel.
B. Raise each subagent's tool-call budget so individual runs finish faster.
C. Configure the subagents with a smaller model to reduce per-run latency.
D. Set `parallel: true` on the Task tool definition.

---

**Q9.** You must find every place in the service that emits the exact log line
`"payment declined: code 4021"`. Which search approach fits?

A. Semantic search — declined-payment handling is a concept spread across the codebase.
B. `Glob` for `**/*payment*`, then read the matching files.
C. `Grep` for the literal string — the exact text is known and can be spelled out.
D. `Read` the entry-point files and follow imports until the logging call appears.

---

**Q10.** Review of an audit run shows two problems. Two research subagents each analysed the same
three shared libraries, duplicating effort. And the final report says nothing about the
message-queue modules, although they were in scope — while every subagent completed its own
assignment correctly. Which two changes address these? **(Select two.)**

A. Share a live scratchpad between subagents so they can see each other's progress and self-coordinate.
B. Partition the scope explicitly so each subagent receives a distinct, non-overlapping set of modules.
C. Increase each subagent's context window so it can cover more modules per run.
D. Widen the coordinator's task decomposition so the message-queue modules are assigned — incomplete coverage with correctly-working agents points at the split.

---

**Q11.** Three weeks ago, a session named `arch-review` analysed a service in depth. Since then a
framework upgrade has rewritten most of the files it inspected — imports, configuration and
routing all changed. You now need to continue the architectural work. What is the reliable
approach?

A. Start a new session seeded with a structured written summary of the conclusions that still hold — most of the old tool results are stale.
B. `--resume arch-review` and name the changed files, so only those are re-read.
C. `--resume arch-review` as-is; Claude re-reads any file whose contents changed.
D. Use `fork_session` to branch the old analysis into a fresh line of work.

---

**Q12.** A customer writes one message containing three unrelated problems: a wrong plan price, a
broken data export, and a support ticket nobody answered. What is the correct handling?

A. Address them strictly in priority order, sending the customer a reply after each is resolved.
B. Ask the customer which of the three they want fixed first.
C. Split the message into separate items, investigate each in parallel using shared context, and combine the results into one answer.
D. Route the whole message to a human agent, since multi-issue messages exceed single-agent scope.

---

**Q13.** A `run_analysis` tool takes a `mode` enum with six values — lint, complexity, security,
dependency, coverage, style. Its description documents every mode in detail, yet the agent still
regularly runs the wrong analysis for the request. What is the recommended redesign?

A. Merge related modes so the enum offers three broader choices.
B. Add an `auto` mode that inspects the request and infers the intended analysis.
C. Classify requests upstream and force `tool_choice` to `run_analysis` with the mode pre-filled.
D. Split it into purpose-specific tools, each with its own defined input and output contract.

---

**Q14.** Two symptoms appear in production. Every failure from your MCP tools reads
`"Operation failed"`, and the agent responds by retrying everything — including policy denials —
until the retry cap. Separately, when a document search legitimately matches nothing, the agent
treats it as an outage and retries that too. Which two changes are correct? **(Select two.)**

A. Return structured errors carrying `errorCategory` and `isRetryable`, so only transient failures are retried.
B. Lower the retry cap to one attempt.
C. Make the search tool distinguish a valid empty result — success with zero matches — from an access failure.
D. Add a system prompt rule telling the agent to retry each tool at most once.

---

### Scenario: Platform Team Rollout of Claude Code

**Q15.** Your monorepo hosts six services. Nine shared standards documents live in
`docs/standards/`, and each service's lead should decide which of them apply to their service —
with no document ever copied. Which mechanism is correct?

A. Skills in `.claude/skills/`, one per standards document, invoked when relevant.
B. A CLAUDE.md in each service directory that uses `@import` to reference only the standards files that apply.
C. `.claude/rules/` files with `paths:` globs scoped to each service directory.
D. Copy the applicable standards into each service's CLAUDE.md so they are self-contained.

---

**Q16.** Database migration files ending in `.sql` sit inside each of roughly thirty service
folders. One set of conventions applies to all of them, wherever they live, and should load
automatically only when such a file is being edited. What do you create?

A. A section in the root CLAUDE.md headed "Migration conventions".
B. A CLAUDE.md in each of the thirty service folders.
C. A skill containing the conventions, invoked before writing migrations.
D. A `.claude/rules/` file with YAML frontmatter `paths: ["**/*.sql"]`.

---

**Q17.** The requirements for a payment-provider integration already describe two viable
approaches — webhooks versus polling — with different infrastructure implications, touching many
modules. A teammate suggests starting with direct execution and switching to plan mode if
unexpected complexity appears. What is the correct approach?

A. Plan mode first — the complexity is already described in the requirements, not something that might appear later — then direct execution to implement the chosen plan.
B. The teammate's approach: direct execution, escalating to plan mode on demand.
C. Direct execution, backed by a sufficiently detailed upfront specification.
D. Plan mode throughout, including the implementation itself.

---

**Q18.** A brainstorming skill produces pages of exploratory options each time it runs. After
using it, the main conversation loses track of the task it was working on. Which SKILL.md
frontmatter option addresses this?

A. `allowed-tools`
B. `argument-hint`
C. `context: fork`
D. `paths:`

---

**Q19.** You have described, in words, how changelog entries should be turned into release notes.
Across runs, the output format keeps varying. According to the guide, what is the most effective
technique?

A. The interview pattern — let Claude ask clarifying questions before starting.
B. Provide two to three concrete input/output examples of the expected transformation.
C. Test-driven iteration — write failing format tests first, then share the failures.
D. Split the request into several smaller messages, one per formatting rule.

---

**Q20.** A CI job runs `claude "Audit the changed files for missing tests"`. It hangs waiting for
interactive input. In an earlier trial run it did complete, but the comment-posting script could
not parse the prose output. Which two flags fix this job? **(Select two.)**

A. `--batch`
B. `-p` / `--print`
C. `CLAUDE_HEADLESS=true`
D. `--output-format json`

---
---

# Answers

**Q1 — B** · Domain 1

`stop_reason: "end_turn"` already signals completion. An explicit `task_complete` tool is the
fourth named wrong way to stop the loop: it is redundant, and the model may simply forget to call
it — which is exactly the hang described.

- **A** — prompt instructions have a non-zero failure rate. Strengthening the wording does not
  change the mechanism, and the mechanism is the problem.
- **C** — "check whether the response contains text" is another of the named wrong ways to stop.
  Text and tool calls often appear together.
- **D** — the iteration cap is a safety limit, not a stopping mechanism. Lowering it hides the
  bug and cuts off legitimate long sessions.

**Q2 — C** · Domain 2

Run the four-way test in order. Could a retry succeed? No — the policy will answer the same way
forever. Is the input malformed? No — the parameters are well-formed. Input and system are both
fine, but a rule says no → **business**. A business error carries `isRetryable: false` plus a
customer-friendly explanation, so the agent can explain the policy instead of retrying.

- **A** — nothing here is temporary. Retrying a policy decision wastes calls.
- **B** — validation means the *input* was malformed. It was not; the rule rejected it.
- **D** — permission means the *caller* lacks access. The agent is allowed to call the tool; the
  operation is denied by policy, which is a different category.

**Q3 — A** · Domain 1

The reasons for hub-and-spoke are exactly these three: visibility into what moves between agents,
one place for error handling, and control over what information flows where. Cutting the
coordinator out trades all three for a little latency.

- **B** — factually wrong reasoning. The design rule exists because direct links are a bad idea,
  not because they are impossible.
- **C** — model versions have nothing to do with it.
- **D** — the guide treats hub-and-spoke as the production architecture, not a debugging aid.

**Q4 — D** · Domain 2

`{"type": "any"}` forces the model to call *some* tool while leaving the choice of tool to the
model — exactly what you need when the schema depends on the document type. This is the guide's
own use case for `any`: the model keeps replying with text instead of extracting.

- **A** — a prompt instruction against a behaviour that `tool_choice` can simply eliminate.
- **B** — forcing one named tool breaks the requirement that the model select the schema.
- **C** — `none` forbids tool use entirely — the opposite direction.

**Q5 — A and C** · Domain 1 *(select two — two symptoms, one answer each)*

Symptom 1 is a policy cap being broken: money plus "must always hold" means programmatic
enforcement, and the blocking mechanism is tool call interception (`PreToolUse`) — block the call
and escalate. Symptom 2 is inconsistent data formats confusing the model: the fix is a
`PostToolUse` hook that normalises the formats before the model reads the results.

- **B** — prompt placement does not remove the non-zero failure rate, and money is involved.
- **D** — asking upstream services to change is out of your control and does not fix the agent.

**Q6 — D** · Domain 1

Identity verification before a money-affecting operation is the textbook case for a prerequisite
gate: programmatically block `update_payout_account` until `verify_identity` has returned a
verified customer ID. If the question involves money or compliance, any answer built on prompts
or examples is wrong.

- **A, B, C** — all three are prompt-based guidance in different costumes. Each fails sometimes,
  and "sometimes" is what the audit already found.

**Q7 — B** · Domain 2

Tool descriptions are the main way the model chooses a tool. When two similar tools get confused,
the *most effective first step* is to expand the descriptions: input formats, example queries,
edge cases, and when to use this tool instead of the similar one.

- **A** — merging into one general tool is a valid design, but it is the expensive option, not
  the first step.
- **C** — building an upstream classifier is more machinery than the problem needs, and it gives
  up on the model's own routing.
- **D** — splitting further multiplies the tools without fixing why they are confused.

**Q8 — A** · Domain 1

Parallel subagents require several Task calls **in one single response**. Issued across separate
turns, they always run sequentially — which is precisely the symptom.

- **B, C** — both speed up individual runs but leave the runs sequential. The structure is the
  problem, not the per-run speed.
- **D** — there is no `parallel: true` option. Parallelism comes from how the calls are issued.

**Q9 — C** · Domain 2

The exact string is printed in the question. **If you can spell the text you are looking for, it
is Grep.** (Note the direction: four earlier misses were "no literal exists → semantic". This one
is the mirror image.)

- **A** — semantic search is for concepts with no literal to match. Here the literal is given.
- **B** — Glob matches file *paths*, and nothing says the string lives in payment-named files.
- **D** — reading and tracing works, but it is the slow way to find a string Grep finds at once.

**Q10 — B and D** · Domain 1 *(select two — two symptoms, one answer each)*

Duplicated effort is a **scope partitioning** failure: give each subagent a distinct,
non-overlapping slice. Missing modules while every agent worked correctly is the signature of
**too-narrow task decomposition**: the coordinator never assigned them.

- **A** — subagents coordinating through a shared scratchpad breaks hub-and-spoke; coordination
  is the coordinator's job.
- **C** — context size has nothing to do with either symptom.

**Q11 — A** · Domain 1

"How much is stale?" is the deciding question. Here *most* of the analysed files were rewritten,
so resumption would be built on stale tool results. Start fresh, seeded with a structured summary
of the conclusions that survive.

- **B** — resume-and-name-the-files is for the opposite case: a few known files changed inside a
  mostly-valid analysis.
- **C** — no such automatic re-reading exists; the stale results stay in context either way.
- **D** — `fork_session` branches from a *valid* shared baseline. This baseline is invalid.

**Q12 — C** · Domain 1

The guide's handling for multi-problem messages: split into separate items, investigate in
parallel with shared context, and return **one** combined answer.

- **A** — sequential handling is named as the wrong approach; the customer waits three times.
- **B** — asking the customer to choose is also explicitly wrong. All three are the agent's job.
- **D** — nothing here needs a human; the customer did not ask for one, and each problem is
  within the agent's capability.

**Q13 — D** · Domain 2

An enum-of-operations tool that keeps misfiring is the granularity problem: split it into
purpose-specific tools, each with its own defined input and output contract. The description is
already detailed, so the cheap fix is exhausted.

- **A** — merging modes is the recorded trap: fewer, broader choices make routing *less*
  precise, not more.
- **B** — an `auto` mode adds an eighth way to be wrong and hides the decision inside the tool.
- **C** — an upstream classifier duplicates what tool selection is for.

**Q14 — A and C** · Domain 2 *(select two — two symptoms, one answer each)*

Symptom 1 is the generic error: `"Operation failed"` gives the agent nothing to decide with, so
it retries policy denials. Structured errors with `errorCategory` and `isRetryable` fix that —
only transient errors are retriable. Symptom 2 is the access-failure-versus-empty-result
confusion: a search that succeeds with zero matches must be reported as success, not as an error
to retry.

- **B** — a lower cap reduces waste but the agent still cannot tell retry from explain from
  escalate.
- **D** — a prompt rule where a structured response solves it properly, and it still retries
  things that should never be retried once.

**Q15 — B** · Domain 3

Maintainer-selected, shared, never duplicated: that is `@import`. Each service's CLAUDE.md
references exactly the standards files its lead chose, and every service reads the same single
copy. *(Third appearance of this decision — the anchor: `@import` = the maintainer selects which
shared documents apply, with no duplication.)*

- **A** — skills must be **invoked**, so they cannot hold standards that must always apply.
  (This was the wrong answer chosen on 12 Aug.)
- **C** — `paths:` globs load rules by **file pattern**, not by a maintainer's judgement of
  which documents apply. (This was the wrong answer chosen on 8 Aug.)
- **D** — copying is exactly the duplication the requirement rules out.

**Q16 — D** · Domain 3

Conventions that follow a **file type across many folders** are the `paths:` glob case:
`.claude/rules/` with `paths: ["**/*.sql"]` loads them only when a matching file is edited,
wherever it lives.

- **A** — a root CLAUDE.md section forces the model to guess when the section applies, and it is
  always loaded.
- **B** — thirty copies to keep synchronised, and a directory CLAUDE.md only covers its own
  folder.
- **C** — skills must be invoked; the requirement says automatic.

**Q17 — A** · Domain 3

Two viable approaches with different infrastructure implications is the guide's own plan-mode
trigger. The teammate's suggestion is the named trap: the complexity is **already described in
the requirements**, not something that might appear later. Plan to decide, then execute the plan
directly.

- **B** — the trap answer, quoted almost verbatim from Sample Q5.
- **C** — a detailed specification does not resolve *which* of the two approaches to take.
- **D** — plan mode is for exploring and designing; implementation of a settled plan is direct
  execution.

**Q18 — C** · Domain 3

Exploratory, high-volume output displacing the main task is the `context: fork` case: the skill
runs in a separate context, and the main conversation keeps its thread.

- **A** — `allowed-tools` limits which tools a skill may use; nothing here is about safety.
- **B** — `argument-hint` asks for a missing parameter.
- **D** — `paths:` is not a SKILL.md key at all; it belongs to `.claude/rules/`.

**Q19 — B** · Domain 3

When written descriptions produce inconsistent results, the guide calls concrete input/output
examples (two to three of them) the **most effective** way to show an expected transformation.

- **A** — the interview pattern is for unfamiliar domains where you need Claude to surface
  questions, not for pinning down a format you already understand.
- **C** — test-driven iteration is a real technique, but the guide reserves "most effective for
  showing a transformation" for examples.
- **D** — splitting into messages is for independent problems; this is one problem.

**Q20 — B and D** · Domain 3 *(select two — two symptoms, one answer each)*

The hang is interactive mode: `-p` / `--print` runs non-interactively. The unparseable prose is
the output format: `--output-format json` makes it machine-readable.

- **A** — `--batch` does not exist; it is a standard wrong answer.
- **C** — `CLAUDE_HEADLESS=true` does not exist either.

---

## Scoring

| Result | Meaning |
|---|---|
| **16–20** | All three domains are holding together. Take Mock 1 on 16 Aug as planned |
| **13–15** | Above the 80% line only at the top of this band. Check *which* domain the misses cluster in before Mock 1 |
| **Below 13** | Find the pattern before Mock 1 — repeat misses go on the cheat sheet |

Log the score in `LOG.md` with the per-domain split: D1 /8 · D2 /6 · D3 /6.
