# Mock 5 — Answer key and explanations

Questions: `mock-05-questions.md`. Do not open this file until you have finished and stopped the
clock. **Write the first-pass time down first** — weak point 45.

---

## Key

| Q | Ans | Domain | | Q | Ans | Domain | | Q | Ans | Domain |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | **A, C** | D3 | | 21 | C | D4 | | 41 | D | D2 |
| 2 | C | D3 | | 22 | D | D4 | | 42 | B | D2 |
| 3 | B | D3 | | 23 | A | D4 | | 43 | A | D2 |
| 4 | D | D3 | | 24 | C | D4 | | 44 | C | D1 |
| 5 | A | D3 | | 25 | **B, D** | D4 | | 45 | D | D1 |
| 6 | B | D3 | | 26 | D | D2 | | 46 | B | D1 |
| 7 | C | D3 | | 27 | A | D2 | | 47 | A | D1 |
| 8 | A | D3 | | 28 | **A, B** | D2 | | 48 | **B, C** | D1 |
| 9 | D | D3 | | 29 | **C, D** | D5 | | 49 | C | D1 |
| 10 | B | D3 | | 30 | B | D5 | | 50 | D | D1 |
| 11 | C | D3 | | 31 | A | D5 | | 51 | B | D1 |
| 12 | A | D3 | | 32 | C | D5 | | 52 | A | D1 |
| 13 | D | D1 | | 33 | D | D5 | | 53 | C | D1 |
| 14 | B | D4 | | 34 | **A, D** | D5 | | 54 | D | D2 |
| 15 | A | D4 | | 35 | **B, C** | D1 | | 55 | A | D2 |
| 16 | C | D4 | | 36 | **A, B** | D1 | | 56 | **A, D** | D5 |
| 17 | D | D4 | | 37 | B | D1 | | 57 | C | D5 |
| 18 | A | D4 | | 38 | A | D1 | | 58 | B | D5 |
| 19 | B | D4 | | 39 | **C, D** | D2 | | 59 | D | D1 |
| 20 | B | D4 | | 40 | C | D2 | | 60 | C | D2 |

A select-two question scores 1 only if **both** letters are right. No half marks.

Answer distribution: of the 50 single-answer questions, A is correct 13 times, B 12, C 13, D 12.
Across the 10 select-two questions each letter is correct 5 times.

---

## Score sheet

| Domain | Questions | Yours | Floor (60%) |
|---|---|---|---|
| D1 — Agentic architecture (16) | 13, 35, 36, 37, 38, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 59 | | 10 |
| D2 — Tool design & MCP (11) | 26, 27, 28, 39, 40, 41, 42, 43, 54, 55, 60 | | 7 |
| D3 — Claude Code config (12) | 1–12 | | 8 |
| D4 — Prompts & structured output (12) | 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25 | | 8 |
| D5 — Context & reliability (9) | 29, 30, 31, 32, 33, 34, 56, 57, 58 | | 6 |
| **Total** | **60** | | **43 to pass** |

**Also record:** first-pass start time, first-pass end time, how many questions you flagged, and
how many flagged answers you changed on the second pass. That is the measurement this paper exists
for.

---

## Explanations

Questions marked ★ test one of the thirteen facts that no earlier repo paper covered.

### Scenario A — Claude Code in Continuous Integration

**1. A, C.** `-p` / `--print` is non-interactive mode and is the documented fix for a pipeline that
hangs; `--output-format json` gives a script something it can read. B and D are invented — there is
no `CLAUDE_HEADLESS` variable and no `--no-interactive` flag.

**2. C.** `--json-schema` forces the output to follow a schema. A gives you JSON with no guarantee
about the fields; B is invented; D is the repair verb — validating afterwards does not make the
shape reliable.

**3. B.** In CI, CLAUDE.md is how Claude Code learns the project: testing standards, fixture
conventions, review criteria. Appending them to the pipeline prompt (A) is the documented wrong
answer. C would only load when a matching file is edited, and the standards are not a file-type
convention.

**4. D.** Give it the existing test files and it stops proposing what is already covered. A is a
prompt where a fact is needed; B tells it the number, not the content.

**5. A ★** (re-review duplicate findings). Include the earlier findings and ask for only new or
still-unfixed issues. C is the repair verb — de-duplicating comments after posting them is a
downstream fix for missing context upstream.

**6. B ★** (personal command placement). `~/.claude/commands/` is personal and never shared through
version control. Anything under `.claude/` is shared, whatever the filename says. D is invented.

**7. C.** `argument-hint` is for a missing parameter. `paths` (A) is a `.claude/rules/` key and not a
SKILL.md key at all.

**8. A ★** (`allowed-tools`). It limits which tools the skill may use — the guide's example is
exactly preventing destructive actions. B is a prompt where a guarantee is required. D mixes the
rules key into SKILL.md.

**9. D.** `context: fork` runs the skill in a separate context, keeping long or exploratory output
out of the main conversation. A and B manage the symptom after the output has already landed.

**10. B.** The content governs `**/*.stories.tsx` wherever it lives — a file pattern, so
`.claude/rules/` with `paths:`. "Eleven of the twelve services" is the noun trap: the grouping is
the file type, not the package.

**11. C.** Shared documents, maintainer picks which apply, nothing copied, and once picked they
govern everything in that service → `@import`. A skill (A) would have to be invoked every time. D
duplicates.

**12. A.** One folder and nothing outside it → a CLAUDE.md inside that folder. B is the reflex
answer; `.claude/rules/` is correct only when the grouping is a file pattern.

**13. D.** Known file list plus fixed criteria → prompt chaining: one pass per file, then one pass
across files. The number of files does not decide it — whether you know the shape does.

**14. B ★** (severity consistency). Define each severity level with concrete code examples. A and C
are the confidence and voting traps; voting across runs hides real findings.

**15. A.** Turn off the noisy category, keep the accurate ones running, fix its prompt, turn it back
on. B and C are the "be conservative" and confidence-filter answers, which the guide says do not
improve precision.

### Scenario B — Structured Data Extraction

**16. C ★** (plain-text JSON → tool use). Tool use with a JSON schema is the reliable way to get
structured output; it removes JSON syntax errors. A is few-shot for a problem that has a structural
fix; B is the repair verb; D leaves the failure mode in place.

**17. D.** A strict schema removes **syntax** errors, not **semantic** ones. `calculated_total` next
to `stated_total` is the documented way to catch totals that do not add up. C is the false claim the
exam tests. B overwrites the evidence you need.

**18. A.** The source always contains it and the failure is **omission** → `required`. B is the worst
of both worlds: it does not stop fabrication and it now rejects documents that would have extracted
fine.

**19. B.** The source may not contain it and the failure is **fabrication** → optional and nullable.
Both directions of this rule are correct answers on this exam; decide from the source, not from
whichever failure you saw last.

**20. B.** The schema fixes the **type**; the prompt fixes the **format**. C is the post-processing
distractor that has cost four marks in this repo — a branch per variant breaks on the first layout
you did not anticipate.

**21. C ★** (`tool_choice` values). Several schemas and the document type unknown → `any`: the model
must call a tool and picks which. `auto` (A) permits a text reply.

**22. D ★.** Forcing one named tool is `{"type": "tool", "name": "..."}` on that turn, then continue
in later turns. `any` would satisfy the "must call something" half only. A retries around the
problem instead of removing it.

**23. A.** A retry fixes format and structure. It cannot fix information that is not in the document
(B), was never supplied (C), or cannot be read (D).

**24. C ★** (batch resubmission). Results are matched to requests by `custom_id`, so resubmit only
the failures. A pays twice; B abandons the 50% saving for work nobody is waiting on; D is invented —
the window is up to 24 hours and there is no speed guarantee to extend.

**25. B, D.** Two to four examples, aimed at the **unclear** cases. A is too many; C picks the
obvious documents, which teaches nothing.

**26. D.** Healthy API, well-formed payload, authorised caller, and a rule says no → **business**,
`isRetryable: false`. This is the Mock 4 Q52 miss: transient additionally implies that a retry could
succeed, and here it never will.

**27. A.** The caller lacks the access it needs → **permission**. Run the test in order: system
failure → transient; malformed input → validation; rule says no → business; lacks access →
permission.

**28. A, B.** Every error returns `errorCategory`, `isRetryable`, and a readable message. C leaks
internals; D is the generic message the guide names as never acceptable.

**29. C, D.** A 97% average can hide one broken document type, so analyse by type and by field, and
sample the **high-confidence** group — the group review is about to stop covering, whose true error
rate is the only number that matters. A tells you nothing about that group; B samples what the model
already doubted.

**30. B.** Coverage annotations: state which findings are well supported and which topics have gaps.
A delays, C hides the gap by omission, D is an error dressed as success.

### Scenario C — Customer Support Resolution Agent

**31. A ★** (escalation, positive direction). An explicit request for a human → escalate
**immediately**. Finishing the diagnosis first (B) is the documented wrong answer, however helpful
it sounds.

**32. C ★** (escalation, the other direction). Frustrated but solvable → acknowledge, offer to
solve, escalate only if they ask again. A is sentiment, which is never a reason.

**33. D.** The policy does not cover the request — a policy gap, which is one of the three valid
reasons to escalate. B invents a rule; A refuses a case a human could grant.

**34. A, D.** Sentiment and the model's own uncalibrated confidence are the two signals that are
always wrong. B and C are two of the three valid reasons.

**35. B, C ★** (handoff package contents). The human cannot see the conversation, so the summary
carries the customer ID, the root cause, the refund amount and the recommended action. A dumps the
transcript instead of the analysis; D is confidence again.

**36. A, B ★** (multi-issue single messages). Split the message into items, investigate them in
parallel over shared context, and return **one** combined answer. C and D are the two documented
wrong answers.

**37. B.** Money plus "must never" → programmatic enforcement, and the interception hook is
`PreToolUse`, which blocks the outgoing call. C reverses the refund after it has been made; A and D
are prompts.

**38. A.** A prerequisite gate blocking `process_refund` until `get_customer` has returned a verified
ID. This is the guide's standard example. C forces a tool on every turn — level 4 for a level 1
problem, and it does not enforce ordering.

**39. C, D.** A 503 is a system failure a retry may fix → transient, `isRetryable: true`. Subagents
fix transient failures themselves and only report what they cannot fix. B is the error-as-success
answer, which is never correct.

**40. C.** One tool with a `mode` enum → split into purpose-specific tools, each with its own
contract. A merges modes, which keeps the overloaded design and only reduces how many wrong choices
exist. B documents the same design more thoroughly.

**41. D.** Tool descriptions decide which tool the model picks, and this is the weakest fix that
meets the requirement: inputs, example queries, and when to use each instead of the other. A is the
strength ladder overshoot — nothing here says guaranteed, must or never.

**42. B.** MCP resources are content catalogues, and they exist to stop exploratory calls. A keeps
the call and makes it unconditional; C bloats every conversation with a list that changes.

**43. A.** Community server for a standard integration, custom only for your team's own workflow. D
also makes them personal, which is not what was asked.

**44. C.** The loop continues on `tool_use` and on nothing else. `max_tokens` stops it — which is
exactly why "anything other than `end_turn`" (A) is wrong rather than merely imprecise.

**45. D.** One `tool_result` block per `tool_use`, each with the matching `tool_use_id`, all inside
**one** user message. B is the summary answer that cost a mark on Mock 1.

### Scenario D — Multi-Agent Research System

**46. B.** Parallel means several Task calls in a single response. A and D are invented — there is no
`parallel: true` field and no concurrency setting.

**47. A.** The coordinator's `allowedTools` must include `"Task"` or it cannot start subagents at
all.

**48. B, C.** Subagents receive nothing automatically — everything goes in the Task prompt — and they
never talk to each other; all messages go through the coordinator. A and D are the inheritance
fictions.

**49. C ★** (goal-oriented vs rigid prompts). Coordinator and subagent prompts describe goals and
quality standards; step-by-step instructions stop subagents adapting. A and D add more steps to the
thing that is failing.

**50. D.** `fork_session` branches from one shared analysis, which is what comparing approaches
needs. A repeats the collection.

**51. B ★** (`--resume`, positive direction). A few known files changed → resume and name them.
Resume-or-fresh is decided by **how much** is stale, not by whether anything is.

**52. A.** The structure is unknown and each step depends on the last → dynamic decomposition, map
first. "900 documents" does not make it chaining; not knowing the shape makes it dynamic.

**53. C.** Every agent succeeded and coverage is still incomplete → the coordinator's division of
the work was too narrow. B and D blame components the question says worked.

**54. D.** No agreed name and no string that returns anything → semantic search. C is a description
of not having a string to search for. The triad is Glob / Grep / **semantic**: name the third member
before answering.

**55. A.** File paths by pattern → `Glob`.

**56. A, D.** Provenance travels as structure from the agent that held the source: dates, source
location, methodology. B and C are both downstream repairs — the synthesis agent cannot weigh what
it cannot see, and a later re-fetch is not reliably where the claim came from.

**57. C.** Crash recovery is a **manifest** of completed work, loaded when the run resumes.
Scratchpads stop findings decaying; `/compact` shrinks a live session; `--resume` returns to a
session that was not killed mid-run.

**58. B ★** (`/compact` as an answer). Nothing is stale, nothing crashed, and everything in the
session is still needed — so reduce the live context rather than restarting it. A fresh session
throws away context that is still in use; C and D solve problems the question does not have.

**59. D.** An Explore subagent keeps noisy discovery out of the main context. `fork_session` (B) is
for comparing approaches from a shared analysis, which is the swap Mock 3 Q26 tested.

**60. C.** `Edit` fails on text it cannot match unambiguously → `Read` the file and `Write` it back.
A and B retry the tool that is already failing for a reason retrying will not change.

---

## What to do with the result

1. **Write the first-pass time in the log** whatever the score is. That is the outstanding
   measurement.
2. **Any miss among the ★ questions is a genuinely new fact**, not a repeat — it belongs on the
   cheat sheet, because none of these were tested before Mock 5.
3. **Any miss outside the ★ set is a repeat**, and the log's weak-point list already explains it.
   Those are the ones to be worried about: they were all clean on Mock 4.
