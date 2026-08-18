# Mock 3 — Answer key and explanations

Questions: `mock-03-questions.md`. Do not open this file until you have finished and stopped the
clock.

---

## Key

| Q | Ans | Domain | | Q | Ans | Domain | | Q | Ans | Domain |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | A | D1 | | 21 | A | D3 | | 41 | A | D4 |
| 2 | C | D1 | | 22 | D | D3 | | 42 | **B, C** | D5 |
| 3 | B | D1 | | 23 | B | D3 | | 43 | C | D2 |
| 4 | D | D1 | | 24 | C | D3 | | 44 | B | D2 |
| 5 | **A, D** | D1 | | 25 | B | D3 | | 45 | **A, B** | D5 |
| 6 | B | D1 | | 26 | D | D3 | | 46 | D | D2 |
| 7 | A | D5 | | 27 | **A, C** | D5 | | 47 | B | D2 |
| 8 | C | D5 | | 28 | A | D5 | | 48 | A | D2 |
| 9 | B | D2 | | 29 | C | D4 | | 49 | D | D2 |
| 10 | C | D2 | | 30 | D | D4 | | 50 | C | D2 |
| 11 | D | D1 | | 31 | A | D3 | | 51 | A | D2 |
| 12 | C | D1 | | 32 | D | D4 | | 52 | D | D2 |
| 13 | A | D5 | | 33 | B | D4 | | 53 | **B, D** | D1 |
| 14 | **A, D** | D1 | | 34 | **B, D** | D4 | | 54 | C | D1 |
| 15 | D | D1 | | 35 | A | D4 | | 55 | A | D1 |
| 16 | B | D3 | | 36 | C | D4 | | 56 | B | D1 |
| 17 | A | D3 | | 37 | D | D4 | | 57 | D | D5 |
| 18 | C | D3 | | 38 | B | D4 | | 58 | **C, D** | D5 |
| 19 | B | D3 | | 39 | **B, C** | D4 | | 59 | B | D1 |
| 20 | C | D3 | | 40 | D | D4 | | 60 | **A, C** | D1 |

A select-two question scores 1 only if **both** letters are right. No half marks.

Answer distribution: of the 50 single-answer questions, A is correct 12 times, B 13, C 12, D 13.
Across the 10 select-two questions each letter is correct 5 times.

---

## Score sheet

| Domain | Questions | Your score | Out of | Floor (60%) |
|---|---|---|---|---|
| D1 — Agentic Architecture | 1–6, 11, 12, 14, 15, 53–56, 59, 60 | | 16 | 10 |
| D2 — Tool Design & MCP | 9, 10, 43, 44, 46–52 | | 11 | 7 |
| D3 — Claude Code Config | 16–26, 31 | | 12 | 8 |
| D4 — Prompt & Structured Output | 29, 30, 32–41 | | 12 | 8 |
| D5 — Context & Reliability | 7, 8, 13, 27, 28, 42, 45, 57, 58 | | 9 | 6 |
| **Total** | | | **60** | **43 to pass** |

Also record: **finish time of the first pass**, and how many questions you flagged and returned to.
On this paper those two numbers matter as much as the score.

---

## Scenario A — Multi-Agent Research System

**1 — A.** The loop reads `stop_reason` and nothing else: `"tool_use"` → run the tools and repeat.
B is the trap from the "not `end_turn`" family — it looks equivalent but it keeps looping on
`max_tokens`, `refusal` and the rest. C (inspecting block types) and D (`task_complete`) are two of
the four named wrong ways to stop.

**2 — C.** Every `tool_use` needs one `tool_result` with the same `tool_use_id`, **failures
included**, and all results from one assistant message go back in **one** user message. A replaces a
result with prose; B splits them; D defers one.

**3 — B.** Parallel means several Task tool calls **in one assistant response**. There is no flag,
no config key and no setting — A is the invented feature, and step 2 of the method deletes it on
sight. `fork_session` branches one analysis; it does not run subagents.

**4 — D.** Coverage is incomplete and every subagent worked correctly inside its assigned scope, so
the fault is upstream, in how the coordinator split the topic. Every answer blaming a component the
question says was correct is wrong by construction.

**5 — A and D.** Two symptoms, two layers. Re-establishing known facts → put them in each subagent's
prompt, because subagents inherit nothing. Findings lost between subagents → all messages go
**through the coordinator**; subagents never talk to each other. B is an invented flag, C is the
architecture the guide rules out.

**6 — B.** One shared analysis, two branches to compare → `fork_session`. Parallel Task calls would
start two subagents that inherit none of the review.

**7 — A.** Provenance travels as **structure from the agent that held the source**: publication date,
source location, methodology. B and C are the two classic late fixes — re-fetching finds today's
page, not the one the claim came from, and "weigh credibility" asks the synthesis agent to weigh
information it cannot see. D annotates after the judgement it was needed for.

**8 — C.** Sources were unavailable, so the report must **declare** which findings are well supported
and where the gaps are. A blocks delivery on systems that may never answer; B and D hide the gap
from the reader. A coverage gap is something to declare, never something to remove.

**9 — B.** A small cross-role tool for a frequent need — the guide's own example is `verify_fact` for
the synthesis agent. A hands it a toolset outside its job, which it will misuse.

**10 — C.** MCP **resources** are content catalogues — issue lists, documentation structures, database
schemas — and they exist precisely to stop exploratory calls. B adds a tool that returns everything;
D describes a structure that will drift.

**11 — D.** You do not know where the relevant text is, how much of it there is, or what the next step
should be until the current one returns. That is dynamic decomposition. The corpus being large does
not decide this — a known list of 900 filings with fixed criteria would be chaining.

**12 — C.** An iteration cap is a legitimate **safety limit**, but promoting it to the termination
mechanism is one of the four named wrong ways to stop. `stop_reason` drives the loop.

**13 — A.** Conflicting sources → record both, with source **and date**. Never choose, never average.
The date is what stops a 2021 figure and a 2026 figure being read as a contradiction.

**14 — A and D.** Two problems, two layers. Crash recovery → manifests: each agent writes state to a
known location and the coordinator loads it on resume. No context left for the final agent → the
**earlier** agents return structured findings instead of prose. B is context hygiene, not crash
recovery; C is the bigger-window answer, which never fixes attention or context economics here.

**15 — D.** A good coordinator selects subagents by the complexity of the request. A makes five
unnecessary subagents faster; B throws away specialisation; C only helps on repeats.

---

## Scenario B — Code Generation with Claude Code

**16 — B.** Shared with everyone who clones → project scope, `.claude/commands/`. Anything starting
`~/` is personal and never travels through version control.

**17 — A.** Personal, not shared → `~/.claude/CLAUDE.md`. B and C would push one engineer's
preferences onto the whole team.

**18 — C.** The grouping is **file type across many folders** (`**/*.test.ts`), which is the one case
`.claude/rules/` with `paths:` is for. It loads only when a matching file is edited.

**19 — B.** The grouping is **one folder, everything in it, nothing outside** → a CLAUDE.md inside
`packages/checkout/`. A is the reflex answer and would apply checkout's conventions to every `.tsx`
file in the monorepo.

**20 — C.** Two requirements in one question. Always applies → the root CLAUDE.md. The **maintainer
chooses** which shared documents apply, with no duplication → `@import`. Skills must be invoked, so
they can never hold standards that always apply; B duplicates text, which the question forbids.

Read 18, 19 and 20 together: three questions, three mechanisms, chosen by **what the content is
grouped by** and nothing else. That grouping test is the whole of Domain 3's mechanism table.

**21 — A.** `allowed-tools` limits which tools a skill may use. `paths` is not a SKILL.md key at all.

**22 — D.** `context: fork` runs the skill in a separate context, keeping long output out of the main
conversation.

**23 — B.** `argument-hint` asks the developer for a missing parameter.

**24 — C.** `--output-format json` is real. `--batch`, `--no-interactive` and a `commands` list in
`.claude/config.json` are all invented options this exam reuses.

**25 — B.** Forty files, six packages, an architectural boundary being moved → plan mode. C is
attractive but the exploration is not the hard part here; the sequencing of the change is.

**26 — D.** Noisy discovery that fills the context with material of no later use → an Explore
subagent. A does the damage and then repairs it; C is the bigger-window answer.

**27 — A and C.** Two distinct causes. Talking about "typical patterns" instead of the specific
classes it found is context **degradation** → scratchpad files. Forty-field tool responses are tool
results **filling** the context → trim the output before it enters. B is the never-list answer; D is
progressive summarisation, which loses the details you are trying to keep.

**28 — A.** A few named files changed and the rest of the analysis still holds → `--resume`, naming
them. B is correct only when **most** of the earlier context is stale. The discriminator is *how
much* is stale, never *how long ago* it was.

**29 — C.** A prose description giving inconsistent results → two or three concrete input/output
examples. The guide calls this the most effective way to show an expected transformation. A is the
skill answer, which is one level too high for an inconsistency problem.

**30 — D.** The interview pattern: unfamiliar domain, no specification yet, so let Claude ask the
questions and surface what you had not considered. Plan mode designs **against** a specification —
which is exactly what the engineer does not have.

---

## Scenario C — Claude Code in CI

**31 — A.** A pipeline hanging on input needs non-interactive mode: `-p` / `--print`.
`CLAUDE_HEADLESS` and `--no-interactive` do not exist.

**32 — D.** A vague instruction producing false alarms → explicit, testable criteria. "Report only
high-confidence findings" and confidence thresholds do not improve precision, and a classifier is
level 5 before prompt work has been tried.

**33 — B.** A session that wrote the code remembers why, so it does not question its own decisions →
an independent instance. D is voting across runs, which suppresses real findings.

**34 — B and D.** Two complaints, two fixes. One noisy category destroying trust in the others →
turn that category off while its criteria are rewritten, keep the rest running. Inconsistent
severity labels → define each level with concrete code examples. A reduces everything including the
findings you want; C moves the work to developers.

**35 — A.** A person is waiting and the merge is blocked → real-time. Batch is 50% cheaper with **no
speed guarantee**, which is disqualifying whenever anyone is waiting.

**36 — C.** Worst case = the gap between submissions plus up to 24 hours of processing. A 30-hour
commitment allows a gap of at most 6 hours, so every 4 hours works (28 worst case). Every 12 gives
36, every 24 gives 48, every 30 gives 54.

**37 — D.** The source **may not** contain the value, and the failure is a fabricated one → optional
and nullable. A required field forces the model to produce something.

**38 — B.** The source **always** contains the value and the failure is **omission** → `required`,
which is the guarantee you want. A is the long-running trap: it keeps the fabrication risk and adds
rejections on top. Read 37 and 38 together — same rule, opposite directions, both correct answers
on this exam. Decide it from the **source**, never from which failure you saw last.

**39 — B and C.** Two symptoms of attention dilution on a large review: depth varying by file, and
contradictory judgements between files. The fix is both halves — one pass per file **and** one pass
across files, which is where cross-file data flow and contradictions are found. A is the
bigger-window answer; D hides real bugs.

**40 — D.** Resubmit **only** the failures, identified by `custom_id`, splitting the over-long inputs
first. A wastes 95% of the work; B abandons the cost saving for work nobody is waiting on; C retries
failures whose cause has not changed.

**41 — A.** Inconsistent handling of unclear cases is the textbook few-shot problem: two to four
examples aimed at the **borderline** cases. B over-shoots the count — examples are there to
generalise, not to enumerate.

**42 — B and C.** Two failures. A silent empty result marked successful → return structured error
context: failure type, what was attempted, partial results, alternatives. One tool failure aborting
everything → continue with the remaining checks and mark what was not covered. A and D are both on
the never-list: hiding an error as success, and stopping the whole workflow.

**43 — C.** The caller lacks the required scope → **permission**. Not retryable; escalate or explain.

**44 — B.** The system failed and a retry may well succeed once the redeploy finishes → **transient**.
The only retryable category.

**45 — A and B.** A high overall figure can hide one category or one file type failing badly →
analyse by segment. And sample the **high-confidence** group specifically, because that is the group
review would stop covering, so its true error rate is the only number that matters. C samples harder
without learning anything about that group; D trusts the very scores under question, and uncalibrated
confidence is never an answer in any disguise.

---

## Scenario D — Customer Support

**46 — D.** A `mode` enum is an overloaded tool → split into purpose-specific tools, each with its
own contract. A keeps the overloaded design and only shrinks the number of wrong choices, which is
the designed trap here.

**47 — B.** `any` = must call a tool, model chooses which. `auto` permits a text reply, which is the
behaviour being complained about. C forces one specific tool, removing the choice the question
requires.

**48 — A.** Short, similar descriptions are the named cause, so the fix is level 1: expand them with
inputs, example queries, edge cases, and when to use each instead of the other. B and D climb the
ladder for a problem the cheapest rung solves; C merges two clean tools into an overloaded one.

**49 — D.** Personal MCP servers live in `~/.claude.json`. A ships a server the team should not have;
C invents a scheme where a documented location already exists.

**50 — C.** `${VAR}` expansion is what keeps secrets out of a committed `.mcp.json`.

**51 — A.** Community server for the standard integration, custom only for the team's own workflow.
That split is the guide's rule, and the question sets up both halves.

**52 — D.** Input is valid, the system is healthy, and a **rule** says no → **business**: not
retryable, explain the policy. C is the trap — permission is when the *caller lacks access*, not when
a policy limit is exceeded.

**53 — B and D.** Two requirements, two hooks. Money plus "must never" → `PreToolUse` interception on
the outgoing call. Several services returning different formats → `PostToolUse` normalisation
**before the model reads them**. A puts a money rule in a prompt, which has a non-zero failure rate;
C reverses damage after it is done.

**54 — C.** No money, no identity, no policy limit — this is style and judgement, which is what prompt
guidance plus two to four examples is for. A, B and D apply programmatic enforcement where nothing
requires it.

**55 — A.** Identity plus "must never" → a prerequisite gate blocking step B until step A returns.
D repairs the damage after the refund has left.

**56 — B.** The question names the cause: the coordinator sent only the customer ID, and the subagent's
output was correct for what it received. Every answer blaming the subagent is wrong by construction.

**57 — D.** The customer **explicitly asked** for a person → escalate immediately, do not finish the
diagnosis first. Contrast with the frustrated customer whose problem you can solve now: there you
offer to resolve it and escalate only if they ask.

**58 — C and D.** Two problems, two answers. No usable context for the human → a structured handoff
summary (customer ID, root cause, amount, recommended action). The agent deciding matters the policy
does not cover → escalate on the **policy gap** instead of inventing policy. A is a raw dump, not a
summary; B escalates on sentiment, which is never a valid signal.

**59 — B.** The coordinator dispatches subagents with the Task tool, so its `allowedTools` must
include `"Task"`. D is the invented `parallel` field again — delete it on sight.

**60 — A and C.** Two symptoms. Sequential independent checks → issue the Task calls in a **single**
response. Running all three when one is needed → the coordinator selects by what the case requires.
B is the invented flag; D throws away the specialisation.

---

## What this set is testing

Mock 3 was built from the LOG's repeat-miss list rather than from the blueprint alone. Each of the
five facts below has been missed twice or more, and each appears **twice** here.

| The fact | Where it appears | What the wrong answer looked like before |
|---|---|---|
| Parallel = several Task calls in one response | Q3, Q60 | a `parallel: true` field that does not exist |
| Domain 3 mechanism, chosen by grouping | Q16–20, Q23, Q31 | `.claude/rules/` as the reflex answer to any scoping question |
| Coverage annotations | Q8, Q42 | "retry until the sources respond", "summarise more aggressively" |
| Stratified sample of the high-confidence group | Q45 | analysing by segment and stopping there |
| Required vs nullable, both directions | Q37, Q38 | "nullable, plus a rule rejecting nulls" |

Three question shapes recur, in the proportions the last two papers suggest you need.

1. **The defensible late fix** — Q7, Q8, Q37, Q38, Q53, Q55. Before choosing any answer that
   repairs, validates, post-processes, reconciles or re-fetches: name the component that was holding
   the information at the moment it was lost. If your preferred answer is not that component, it is
   the distractor.
2. **The plausible feature that does not exist** — Q3, Q5, Q24, Q31, Q59, Q60. Six questions, and
   deleting these options costs no knowledge of the subject at all.
3. **The rule running backwards** — Q11 (dynamic, not chaining), Q28 (resume, not fresh), Q37 and
   Q38 (nullable *and* required), Q47 (`any`, not `auto`), Q52 (business, not permission), Q57
   (escalate at once). If you learned the shape rather than the rule, this is where it shows.

And four never-list answers are offered as the most reasonable-looking option on the page: Q34 A
(threshold as a filter), Q42 A (empty result marked successful), Q45 D (uncalibrated confidence),
Q58 B (sentiment). All four were correct on one mock and missed on the other. They are a
stop-and-check problem, not a knowledge problem.
