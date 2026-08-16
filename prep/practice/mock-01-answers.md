# Mock 1 — Answer key and explanations

Questions: `mock-01-questions.md`. Do not open this file until you have finished and stopped the
clock.

---

## Key

| Q | Ans | Domain | | Q | Ans | Domain | | Q | Ans | Domain |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | A | D1 | | 21 | D | D1 | | 41 | A | D3 |
| 2 | C | D1 | | 22 | A | D1 | | 42 | C | D3 |
| 3 | D | D1 | | 23 | B | D2 | | 43 | B | D3 |
| 4 | **B, D** | D1 | | 24 | D | D2 | | 44 | D | D1 |
| 5 | B | D1 | | 25 | C | D2 | | 45 | C | D1 |
| 6 | A | D1 | | 26 | A | D2 | | 46 | B | D4 |
| 7 | C | D2 | | 27 | **A, D** | D5 | | 47 | A | D4 |
| 8 | D | D2 | | 28 | B | D5 | | 48 | D | D4 |
| 9 | B | D2 | | 29 | D | D5 | | 49 | C | D4 |
| 10 | A | D2 | | 30 | A | D5 | | 50 | B | D4 |
| 11 | **A, C** | D2 | | 31 | C | D3 | | 51 | **A, C** | D4 |
| 12 | C | D2 | | 32 | B | D3 | | 52 | A | D4 |
| 13 | **B, C** | D5 | | 33 | **A, C** | D3 | | 53 | D | D4 |
| 14 | D | D5 | | 34 | A | D3 | | 54 | C | D4 |
| 15 | B | D5 | | 35 | C | D3 | | 55 | **C, D** | D4 |
| 16 | B | D1 | | 36 | D | D3 | | 56 | A | D4 |
| 17 | C | D1 | | 37 | A | D5 | | 57 | B | D4 |
| 18 | A | D1 | | 38 | **B, D** | D3 | | 58 | **A, B** | D5 |
| 19 | **B, D** | D1 | | 39 | B | D3 | | 59 | C | D5 |
| 20 | C | D1 | | 40 | D | D3 | | 60 | D | D2 |

A select-two question scores 1 only if **both** letters are right. No half marks.

Answer distribution, so you cannot pattern-guess: of the 50 single-answer questions, A is correct
13 times, B 12, C 13, D 12. Across the 10 select-two questions each letter is correct 5 times.

---

## Score sheet

| Domain | Questions | Your score | Out of | Floor (60%) |
|---|---|---|---|---|
| D1 — Agentic Architecture | 1–6, 16–22, 44, 45 | | 15 | 9 |
| D2 — Tool Design & MCP | 7–12, 23–26, 60 | | 11 | 7 |
| D3 — Claude Code Config | 31–36, 38–43 | | 12 | 8 |
| D4 — Prompt & Structured Output | 46–57 | | 12 | 8 |
| D5 — Context & Reliability | 13–15, 27–30, 37, 58, 59 | | 10 | 6 |
| **Total** | | | **60** | **43 to pass** |

Also record: finish time, and how many select-two questions you answered with only one letter.

---

## Scenario A — Customer Support Resolution Agent

**1 — A.** The loop reads `stop_reason` and nothing else. `tool_use` means continue, `end_turn`
means stop. B is the trap you took on 14 August: looking at whether the message has text is a
*proxy* for being finished, and the guide names it as one of the four wrong ways to stop. C is
another named wrong way — `end_turn` already signals completion, and the model may forget to call
an extra tool. D is fine as a safety limit, never as the mechanism.

**2 — C.** One `tool_result` per `tool_use`, each carrying the same `tool_use_id`, and all of them
sent back together in **one** user message.

**3 — D.** Money. A rule that must always hold cannot rest on prompt text, which the guide says has
a "non-zero failure rate". A, B and C are all prompt-level. A prerequisite gate is code: the model
cannot skip it.

**4 — B and D.** The human cannot see the conversation, so the summary carries the reasoning and
the proposed outcome. The guide's four elements are customer ID, root cause analysis, refund
amount, recommended action — B and D are the two of those offered here. A is sentiment, which is
never a valid signal on this exam. C dumps raw tool output that nobody trimmed.

**5 — B.** Split, investigate in parallel with shared context, answer once. A pushes the work back
onto the customer, C is slow and drops shared context, D escalates a case the agent can handle.

**6 — A.** "Must never" plus money means tool call interception — the `PreToolUse` hook — which
blocks the call before it happens. B fixes the damage afterwards, which is not the same as never
issuing it. C and D are prompt-level again.

**7 — C.** "Most effective first step" plus "a single sentence" always means the descriptions. A
(merging into `lookup_entity`) is a legitimate design, but it is a bigger change than the question
asks for. D is the over-engineered routing layer the guide rejects by name.

**8 — D.** Category plus retryable flag plus a readable message. A generic string leaves the agent
unable to choose between retrying, explaining and escalating — and C only makes the generic string
longer, which changes nothing structurally. B hides the error, which is on the never list.

**9 — B.** The system worked, the input was well formed, and a rule said no. That is **business**,
not retryable, and it needs a customer-friendly explanation so the agent can explain the policy.

**10 — A.** The order of the test: did the system fail and might the same call succeed → transient
(A). B is business, C is permission, D is validation — and validation needs the *input* corrected
first, so the identical call would fail again.

**11 — A and C.** Two distinct symptoms, so two answers, one for each. Text instead of a tool call
→ `tool_choice: {"type": "any"}` forces a tool call. Wrong tool among similar tools → the
descriptions. B is the default that allows the first symptom. D does not touch either cause.

**12 — C.** 18 tools instead of 4–5 makes selection unreliable, and an agent holding tools outside
its role will use them. The fix is scoping, plus a narrow cross-role tool where one is genuinely
needed. D is the tool-granularity trap in reverse: collapsing tools into fewer tools with a `mode`
parameter is the wrong direction.

**13 — B and C.** Two symptoms, two layers. Summarisation losing facts → a case-facts block held
*outside* the summarised history. Oversized tool output → trim it to the useful fields **before**
it enters the context. A makes the first symptom worse. D is the "bigger context window" answer,
which never fixes attention or retention on this exam.

**14 — D.** The customer explicitly asked for a human. That is escalate **immediately** — do not
finish the diagnosis first. B is the correct answer to the *other* version of this question, where
the customer is frustrated but has not asked for a person.

**15 — B.** Several matches means ask for another identifier. Never guess, and do not escalate: the
agent can still resolve this itself.

---

## Scenario B — Multi-Agent Research System

**16 — B.** Every subagent worked correctly within the subtask it was given, and coverage is still
incomplete. That combination always points at the coordinator's decomposition. The question even
names it: the logs show the three subtasks.

**17 — C.** Parallel means several Task tool calls inside **one** assistant response. Separate
turns run sequentially. B is `fork_session`, which branches one shared analysis — a different
mechanism for a different purpose.

**18 — A.** No subagent starts at all → the coordinator's `allowedTools` is missing `"Task"`.

**19 — B and D.** Two symptoms again. Generic synthesis → the subagent inherits nothing, so the
earlier findings must be in its prompt. Untraceable citations → a structured format that keeps each
finding separate from its source metadata. C would let synthesis do its own searching, which is
exactly the role bleed you are trying to avoid.

**20 — C.** Hub-and-spoke: visibility, one place for error handling, control over what information
flows where. Cost is not the deciding factor.

**21 — D.** Coordinator prompts describe goals and quality standards. Step-by-step procedures stop
subagents adapting, and A makes the procedure longer rather than removing the constraint.

**22 — A.** The iterative refinement loop: read the synthesis, find the gaps, dispatch targeted
follow-ups, run synthesis again. B is voting across runs, which the guide says suppresses real
findings. C is the bigger-context answer.

**23 — B.** Least privilege applied to tools: a narrow `verify_fact` tool for the 85% of simple
checks, with the remaining 15% still routed through the coordinator. C is technically pure
hub-and-spoke but pays a coordinator round trip for every date check.

**24 — D.** MCP **resources** are content catalogues. They let the agent see what data exists
without exploratory tool calls. That is the whole point of the resource concept.

**25 — C.** Standard integration → community server. Build custom only for workflows specific to
the team.

**26 — A.** The agent prefers a built-in tool because it does not understand what the MCP tool
does. Improve the description first. C removes a useful capability, and B forces a tool on turns
where it may be wrong.

**27 — A and D.** Two failures described: the error is generic, and one subagent's failure stops
everything. So: structured error context (failure type, query attempted, partial results,
alternatives) **and** continue with the rest, marking the affected topics as coverage gaps. B hides
the error and makes the report look complete when it is not. C retries blindly.

**28 — B.** This is the upstream-versus-downstream rule. The information was lost at the moment the
subagent recorded the finding without its date, so that is where it must be fixed: require dates,
source location and methodology in the subagent's structured output. A re-fetches at synthesis
time, C guesses at credibility, D records the symptom in the final schema. All three are
defensible engineering and all three are late.

**29 — D.** Two credible sources disagree → record both with their sources, clearly marked, and let
the coordinator decide before synthesis. Never pick one, never take a majority vote, never drop the
figure.

**30 — A.** Lost in the middle. Key findings first, then details under clear section headings.

---

## Scenario C — Code Generation with Claude Code

**31 — C.** Everyone else has it, one person does not, same repository → the instructions live in a
user-level file, which version control does not carry.

**32 — B.** `@import`. The discriminator is **who chooses and when**: the package maintainer
chooses once, when writing the file, and the content then loads **always**. A skill is chosen at
run time and loads only when invoked, so it can never hold standards that must apply to all work in
the package. C duplicates nothing but forces the model to guess which heading applies. D would work
mechanically but organises by directory rather than by document, and re-lists the same globs in
four files — the question asks for no duplication.

**33 — A and C.** Two complaints, two layers. Contractor gets nothing → the conventions are in user
scope and must move into the repository. Irrelevant instructions load every session → split by
topic into `.claude/rules/` with `paths` globs so each loads only for matching files. B keeps the
loading problem, D requires invocation.

**34 — A.** Project scope, in the repository: `.claude/commands/`. `.claude/config.json` with a
`commands` array does not exist.

**35 — C.** `context: fork` runs the skill in a separate context so its noisy output never reaches
the main conversation.

**36 — D.** `paths` belongs to `.claude/rules/`, not to SKILL.md. The three SKILL.md keys the exam
tests are `context`, `allowed-tools` and `argument-hint`.

**37 — A.** "Typical patterns" instead of the specific classes it read is the named symptom of
context degradation. The direct fix is scratchpad files. B is the bigger-context answer, which the
guide rejects for attention and retention problems.

**38 — B and D.** Two defects, two flags. Hanging → `-p` / `--print` for non-interactive mode.
Unparseable output → `--output-format json` with `--json-schema`. A and C are the invented options:
`CLAUDE_HEADLESS` and `--batch` do not exist.

**39 — B.** 45 files plus three call sites needing redesign = many files plus architectural
decisions = plan mode. C is the standard trap: the complexity is already described in the
requirements, so there is nothing to discover later.

**40 — D.** `/memory` shows which memory files are loaded. That is the diagnostic when behaviour
differs between sessions.

**41 — A.** Two or three concrete input/output examples. The guide calls this the most effective
way to communicate an expected transformation when prose is producing inconsistent results.

**42 — C.** Include the earlier findings and instruct the reviewer to report only new or
still-unfixed issues. A misses unfixed issues in untouched files; B is a fragile string match; D
gives up the value of re-review.

**43 — B.** Personal scope, different name: `~/.claude/skills/`. C is inside the repository, so
teammates get it.

**44 — D.** Resume or fresh is decided by **how much** is stale, not by how long ago it was. Three
known files inside a 40-file analysis means most of the context is still correct: resume and name
the three. A and B over-apply the "stale tool results" rule.

**45 — C.** The discriminator is: do I know the shape of the work before I start? Here the module
boundaries, dependencies and risky areas are all unknown, so the steps must be decided from
findings — dynamic decomposition. A is the one-pass-per-file pattern, which is correct for a large
review with a known file list, and wrong here. Note that words like *legacy* and *whole service* do
not decide this; only the known-shape test does.

---

## Scenario D — Structured Data Extraction

**46 — B.** Tool use with a JSON schema is the reliable way to guarantee schema-conforming output.
It removes JSON syntax errors outright. A, C and D all try to make a text response more likely to
parse.

**47 — A.** The reverse direction of the nullable rule, and the one that costs people marks. The
source **always** contains this value, and the failure is the field being **omitted** — so
`required` is the guarantee you want. B produces exactly the failure mode of required with none of
the guarantee: the model still has to put something there, and now null is rejected too.

**48 — D.** Here the source **may not** contain the value, and the model is inventing one. Optional
and nullable. Read 47 and 48 together — the same rule, both directions, and the exam uses both as
correct answers.

**49 — C.** Several schemas, document type unknown, and the model sometimes answers with prose:
`tool_choice: {"type": "any"}` forces a tool call while letting the model pick which. A is the
default that permits the prose. B forces one specific schema on documents whose type is unknown.

**50 — B.** One named tool must run first → forced tool selection on the first turn, then continue
in later turns. Declaration order in the tools array guarantees nothing.

**51 — A and C.** Two groups, two treatments. Structurally wrong output → retry with the original
document, the failed extraction, and the **specific** validation errors. Value absent from the
source → no retry can find it; route it to a human. B and D both retry a problem retrying cannot
solve.

**52 — A.** Valid JSON with wrong content is a **semantic** error, and tool use does not prevent
those — which is why D is wrong. Extract `calculated_total` next to `stated_total` and compare.

**53 — D.** The schema fixes the **type**; the prompt fixes the **format**. Normalisation rules
belong in the prompt, next to the strict schema. B is the same late fix in a different place: it
repairs the output instead of getting it right at the point of extraction.

**54 — C.** Nobody is waiting on the nightly run and it has until morning → batch. Somebody is
watching the screen during the pre-approval check → real-time.

**55 — C and D.** Results come back in any order, so match by `custom_id`, never by position. And
one batch request cannot run a multi-turn tool-calling loop. A is wrong twice over: batch is up to
24 hours with **no** speed guarantee. B inverts the price — batch is roughly 50% cheaper.

**56 — A.** With a 24-hour processing window and a 30-hour SLA, the gap between submissions can be
at most 6 hours. Submitting every 4 hours keeps the worst case at 28 hours. B leaves a 24-hour gap
plus 24 hours of processing, which breaks the SLA.

**57 — B.** An enum that will grow needs an `"other"` value plus a detail string, and ambiguous
cases need an `"unclear"` value. A throws away the enum's value; C forces a wrong category; D
rejects work the pipeline should handle.

**58 — A and B.** A 97% average can hide one document type or one field failing badly, so check by
type and by field. And sample the **high-confidence** group specifically, because that is the group
you are about to stop reviewing. C assumes the confidence scores are trustworthy, which is what you
are trying to establish. D keeps averaging.

**59 — C.** Confidence is usable for routing review, but only when it is **calibrated against
labelled data** — plus the documents that are ambiguous or contradict themselves. A is raw
self-reported confidence, which is never the answer on this exam.

**60 — D.** An access failure is not an empty result. Nothing found is a successful search; an
unreachable store is a transient error the agent may retry. Returning the same thing for both is
the failure the question describes.

---

## After marking

1. Fill in the score sheet, then add the row to `LOG.md` with the per-domain split.
2. Count how many of your misses are already on the weak point list. Those matter more than the
   total.
3. Questions aimed at your repeat misses: **32** (`@import`, 4th appearance), **44** (resume vs
   fresh), **45** (chaining vs dynamic decomposition), **12** (tool granularity), **1** (stopping
   the loop), **47 and 48** (required vs nullable, both directions), **53** (format normalisation),
   **28** (upstream vs downstream fix). If any of these are wrong, that fact has now been missed
   often enough to belong on the revision card, not the cheat sheet.
4. Ten select-two questions: 4, 11, 13, 19, 27, 33, 38, 51, 55, 58. Count how many you answered
   with a single letter. That is weak point 6, and it is measured separately from whether the
   content was right.
