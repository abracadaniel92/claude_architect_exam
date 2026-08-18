# Mock 4 — Answer key and explanations

Questions: `mock-04-questions.md`. Do not open this file until you have finished and stopped the
clock.

---

## Key

| Q | Ans | Domain | | Q | Ans | Domain | | Q | Ans | Domain |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | B | D4 | | 21 | B | D3 | | 41 | D | D5 |
| 2 | A | D4 | | 22 | **C, D** | D4 | | 42 | A | D5 |
| 3 | C | D4 | | 23 | C | D3 | | 43 | C | D2 |
| 4 | D | D2 | | 24 | D | D1 | | 44 | B | D2 |
| 5 | **A, D** | D4 | | 25 | B | D1 | | 45 | **C, D** | D4 |
| 6 | B | D4 | | 26 | A | D4 | | 46 | D | D3 |
| 7 | C | D4 | | 27 | **A, C** | D2 | | 47 | B | D3 |
| 8 | A | D4 | | 28 | D | D2 | | 48 | A | D3 |
| 9 | D | D4 | | 29 | C | D1 | | 49 | C | D2 |
| 10 | B | D2 | | 30 | B | D4 | | 50 | D | D3 |
| 11 | **B, C** | D2 | | 31 | A | D1 | | 51 | **A, C** | D2 |
| 12 | A | D5 | | 32 | C | D1 | | 52 | D | D2 |
| 13 | C | D5 | | 33 | **B, D** | D1 | | 53 | B | D2 |
| 14 | D | D1 | | 34 | D | D1 | | 54 | A | D1 |
| 15 | B | D1 | | 35 | A | D1 | | 55 | C | D1 |
| 16 | A | D3 | | 36 | C | D1 | | 56 | D | D1 |
| 17 | **A, B** | D3 | | 37 | B | D1 | | 57 | **B, D** | D5 |
| 18 | C | D3 | | 38 | A | D5 | | 58 | C | D5 |
| 19 | D | D3 | | 39 | **A, B** | D5 | | 59 | B | D1 |
| 20 | A | D3 | | 40 | C | D5 | | 60 | A | D3 |

A select-two question scores 1 only if **both** letters are right. No half marks.

Answer distribution: of the 50 single-answer questions, A is correct 13 times, B 12, C 13, D 12.
Across the 10 select-two questions each letter is correct 5 times.

---

## Score sheet

| Domain | Questions | Out of | Your score | Floor (60%) |
|---|---|---|---|---|
| D1 — Agentic architecture | 14, 15, 24, 25, 29, 31, 32, 33, 34, 35, 36, 37, 54, 55, 56, 59 | 16 | | 10 |
| D2 — Tool design & MCP | 4, 10, 11, 27, 28, 43, 44, 49, 51, 52, 53 | 11 | | 7 |
| D3 — Claude Code config | 16, 17, 18, 19, 20, 21, 23, 46, 47, 48, 50, 60 | 12 | | 8 |
| D4 — Prompt & structured output | 1, 2, 3, 5, 6, 7, 8, 9, 22, 26, 30, 45 | 12 | | 8 |
| D5 — Context & reliability | 12, 13, 38, 39, 40, 41, 42, 57, 58 | 9 | | 6 |
| **Total** | | **60** | | **43 to pass** |

Also record: **how many minutes the first pass took**, and **how many questions you flagged**. Per
weak point 29 those two numbers predict the score better than any domain total.

---

## Scenario A — Structured Data Extraction

**1. B — normalisation rules in the prompt, next to the strict schema.**
This is the fifth appearance of the fact that has now been missed four times. **The schema fixes
the type; the prompt fixes the format.** A (post-processing layer) is the distractor that has taken
every one of those four marks: it needs a branch per variant and breaks on the first layout nobody
anticipated. C is the same idea with the type guarantee thrown away as well.

**2. A — mark it required.**
The source *always* contains the value: machine-generated, fixed header block. The failure is
**omission**, and `required` is the only option that forbids omission. B is the "worst of both"
answer — it does not stop fabrication and it now rejects documents that would have extracted fine.
D is B with a repair verb attached.

**3. C — optional and nullable.**
Same rule, opposite direction. The source **may not** contain the clause, so a required field
forces the model to produce something and it **invents**. Both directions are correct answers on
this exam; decide it from the source, never from which failure you saw most recently.

**4. D — business.**
Run the test in order: system healthy and a retry would not help → not transient. Payload
well-formed → not validation. Caller authorised → not permission. A rule says no → **business**,
`isRetryable: false`, with a readable explanation. A policy limit is not an access problem.

**5. A, D.**
Two distinct symptoms, one answer each. Arithmetic that does not add up → extract
`calculated_total` next to `stated_total` so the comparison is in the data. Contradictory source
values → `conflict_detected` plus both readings **with their sources**. B is the repair verb again;
C throws away documents rather than recording what they say.

**6. B — the document, the failed extraction, and the specific errors.**
All three. A omits the document, C omits the errors, D changes nothing about the request. Retries
fix wrong format and wrong structure; they never conjure information that is not in the document.

**7. C — 50% cheaper, up to 24 hours, no speed guarantee.**
B is the trap: the window is a ceiling, not a promise. D invents `--batch`, which step 2 of the
30-second method deletes on sight.

**8. A — multi-turn tool calling is not supported.**
Straight from the batch table. Schemas work (so B is false), `custom_id` matches results back (C is
false), and there is no one-document limit (D).

**9. D — schema enforcement removes syntax errors, not semantic ones.**
A swapped consignee and shipper is a perfectly valid document that means the wrong thing. Nothing
about types or required fields catches it.

**10. B — split into purpose-specific tools.**
A `mode` enum is the textbook overloaded tool. **C is the documented wrong answer:** merging eight
modes into three keeps the overloaded design and only reduces the number of ways to be wrong. A is
level 4 force applied to a level 1 problem.

**11. B, C.**
Symptom one is tool results filling the context → **trim the output before it enters the context**.
Symptom two is exploratory calls to discover what exists → **an MCP resource catalogue**, which is
exactly what resources are for. A is on the never-list (a bigger window does not fix dilution) and
D treats the symptom after the damage.

**12. A — an access failure was reported as an empty successful result.**
On the never-list, and chosen once before on Mock 2 Q30. An access failure is not an empty result;
zero matches genuinely is a success (so C is wrong), one failure does not stop the workflow (B),
and infinite retries are not a policy (D).

**13. C — a stratified random sample of the high-confidence extractions, analysed by type and field.**
Why that group: it is the group review is about to **stop covering**, so its true error rate is the
only number that matters. A tells you nothing about it; B and D re-examine the group already being
looked at. This was a three-paper repeat miss, closed on 17 Aug — it is here to confirm that holds.

**14. D — a `PreToolUse` hook.**
Money plus "must never" → programmatic enforcement, and specifically the interception hook that
blocks the outgoing call. A and B are prompting, which fails sometimes. C detects it after the
declaration has already been filed.

**15. B — a `PostToolUse` hook.**
Read this against Q1, which is the point of putting both in one paper. **Prompt rules normalise the
formats in the source document; a `PostToolUse` hook normalises the results a tool returns before
the model reads them.** C is the right answer to Q1 and the wrong answer here. A rewrites the
outgoing request, which is not where the inconsistency lives.

---

## Scenario B — Developer Productivity with Claude

**16. A — `.claude/rules/` with `paths: "**/*.tsx"`.**
The noun trap: the question says *twelve of the fourteen packages*, and the content governs a
**file pattern**. Ask only "what set of files does this content govern?" — every `.tsx` file,
wherever it lives. B is the `@import` answer this question is dressed to attract.

**17. A, B.**
Two documents, two mechanisms. Central document, maintainer selects it, no duplication, and once
selected it applies to all work in that service → **`@import`**. A long procedure run four times a
year → **a skill**. C is duplication, which the question rules out. D is the reflex answer.

**18. C — a CLAUDE.md inside `services/payments/`.**
Second noun trap: *the payments lead decides* is not the same as *invoking*. The content governs one
folder and nothing outside it → a directory CLAUDE.md. A is the near-miss that has cost marks in the
other direction — a glob is for a file type across folders, not a single subtree — and B is the
skills trap that has now returned three times.

**19. D — the root CLAUDE.md.**
Grouped by nothing; it always applies. A looks equivalent but is not: a `paths` rule loads when a
matching **file is edited**, so it does not apply to a task that edits nothing. C makes a universal
standard personal and unshared.

**20. A — `argument-hint` and `context: fork`.**
`argument-hint` asks for the missing parameter; `context: fork` keeps long output out of the main
conversation. **`paths:` is a `.claude/rules/` key, not a SKILL.md key** — that is the single most
common Domain 3 mistake, and it is planted in three of the four options here.

**21. B — `~/.claude/CLAUDE.md`.**
Anything under `~/` is personal and is not shared through version control. Everything else on the
list is a project file, git-ignored or not.

**22. C, D.**
A category with many false alarms damages trust in the good ones → **turn it off while you fix it**.
Prose that gives inconsistent results → **two or three concrete input/output examples**, which the
guide calls the most effective way to show an expected transformation. A ("be conservative") and B
(voting across runs, which hides real bugs) are both on the never-list.

**23. C — `.claude/commands/` with `argument-hint`.**
Shared, so not `~/`. A command, not a skill. And `argument-hint` is precisely the key for a
parameter developers keep omitting. D invents `.claude/config.json` with a `commands` list.

**24. D — prompt chaining.**
The shape is known before starting: a fixed list of 22 packages, fixed criteria. One pass per
package plus one across packages. The words "dependency upgrade" and the package count do not make
it dynamic.

**25. B — dynamic decomposition.**
The shape is unknown — nobody knows where configuration is loaded or how many patterns exist. Map
first, then plan from the map. A is the trap: "audit", "large" and "comprehensive" do **not** decide
this. Q24 and Q25 are the same rule in opposite directions, in the same scenario.

**26. A — the interview pattern.**
Unfamiliar domain and you do not know what to specify → let Claude ask the questions first, so it
raises invalidation and failure modes. **Not plan mode:** plan mode designs against a specification
you do not yet have. This fact cost a mark on Mock 2 and was in neither file at the time.

**27. A, C.**
Wrong tool chosen → **improve the descriptions** (inputs, example queries, edge cases, when to use
this one instead of that one). Tools outside the agent's job being misused → **remove them**. B
climbs to forced `tool_choice` for a description-level problem, and D is the overloaded-tool
anti-pattern from Q10.

**28. D — semantic search.**
The question says there is no agreed name and several candidates return nothing. **If you cannot
spell the string, it is semantic.** "Widen the pattern until something matches" is a description of
not having a string to search for.

**29. C — a fresh session with a written summary.**
Decided by **how much** is stale, not by how old the session is. Most of the context is stale here,
so `--resume` carries wrong assumptions forward. A is correct only when a few known files changed.

**30. B — two to four examples, aimed at the unclear cases.**
Both halves matter: the count and the targeting. Clear cases already work, so examples of them
teach nothing.

---

## Scenario C — Multi-Agent Research System

**31. A — continue only on `"tool_use"`.**
Weak point 38's exact row, and B is the answer that has been chosen twice before. "Not `end_turn`"
would keep looping on `max_tokens` and `refusal`, which is why it is wrong rather than merely
imprecise. C inspects block types — a proxy the guide names as a wrong way to stop. D invents a
completion tool.

**32. C — one user message, four `tool_result` blocks, matching `tool_use_id`s, the failure carried
as an error.**
All of it in one user message. A failed tool still gets a `tool_result`; it carries the error.

**33. B, D.**
Sequential execution → **issue the Task calls in a single response**. There is no flag: A invents
`parallel: true` and C invents `shared_memory`. Direct subagent-to-subagent messaging → **everything
goes through the coordinator**. That second letter is the one omitted twice in earlier papers.

**34. D — `allowedTools` must include `"Task"`.**
Subagents are started with the Task tool; without it in the coordinator's allowed set nothing is
delegated. B is an invented field again.

**35. A — subagents inherit nothing; put it in the prompt.**
C is the plausible-mechanism trap: `fork_session` branches from a shared analysis when you ask it
to, it is not an inheritance setting for delegated subagents.

**36. C — the coordinator's decomposition.**
Every subagent did its subtask completely and correctly, so step 3 of the method removes A, B and D
— they blame parts the question says are working. Incomplete coverage with all agents working means
the split was too narrow.

**37. B — `fork_session`, twice.**
That is exactly what it is for: branch from one shared analysis to compare approaches without
redoing the work. A repeats the analysis, which the question forbids.

**38. A — subagents record dates, source location and methodology.**
Provenance travels as structure from the agent that held the source. B and D are downstream repairs
(what you re-fetch later is not reliably where the claim came from) and C asks the synthesis agent
to weigh what it cannot see. This is step 6 in its purest form.

**39. A, B.**
Unavailable sources → **coverage annotations**: say which findings are well supported and which
jurisdictions have gaps. C and D are the two documented wrong answers — both treat a gap as
something to remove rather than something to declare. Rate limit → **the subagent fixes transient
failures itself** and reports upward only what it cannot resolve; halting the run is on the
never-list.

**40. C — key findings at the beginning, plus a case-facts block outside the summary.**
Two of the three named context problems: lost-in-the-middle, and progressive summarisation losing
details. A is on the never-list, B is the cause rather than the fix, D is not a mechanism.

**41. D — manifests the coordinator loads on resume.**
**Crash recovery = manifests.** This has been missed twice with two different wrong answers, which
is the signature of a fact that is simply absent. B is the near-miss: a scratchpad stops findings
decaying inside a live session; it is not a resume mechanism. A shrinks a live context. Note that A,
B and the Explore subagent are each the *correct* answer to another question in this paper — Q42,
Q57 and Q42 respectively — so matching by feel cannot separate them.

**42. A — an Explore subagent, returning only the shortlist.**
Noisy discovery that must not fill the main context. Not `/compact`, which cleans up after the
damage, and not a scratchpad you then keep in context anyway.

**43. C — failure type, what was attempted, partial results, possible alternatives.**
All four. A is the generic message on the never-list; D hides a partial result as a complete
finding.

**44. B — an existing community MCP server.**
Standard integration with a documented, widely used API → community server. Build custom only for
your team's own workflows. C is the general-tool anti-pattern.

**45. C, D.**
Conflicting sources → **record both, with sources and dates**; B silently picks one, which is what
the question is complaining about. Self-review is weak because the model remembers its own
reasoning → **an independent instance**. A is voting across runs, on the never-list.

---

## Scenario D — Code Generation with Claude Code

**46. D — `-p` / `--print`.**
Non-interactive mode is the documented fix for a CI job that hangs. A and B are invented
(`CLAUDE_HEADLESS`, `--no-interactive`); both are on the "these do not exist" list.

**47. B — `--output-format json` with `--json-schema`.**
One flag makes the output machine-readable, the other forces the shape. C invents `--batch` and D
invents `.claude/config.json`. Four questions in this paper contain an invented feature; this
scenario holds three of them.

**48. A — standards in CLAUDE.md, plus the existing test files.**
In CI, **CLAUDE.md is how Claude Code learns the project**: testing standards, fixture conventions,
review criteria. Appending them to the pipeline's prompt string (B) is the documented wrong answer.
And supplying the existing tests is what stops duplicates — both halves are needed here.

**49. C — `~/.claude.json`.**
Personal MCP servers live in `~/.claude.json`; `.mcp.json` is the shared, committed one. A is the
invented "disabled by default" answer that cost a mark on Mock 3 Q49. D fights the file's purpose.

**50. D — `${VAR}` expansion.**
Keeps the secret out of the repository while the server definition stays shared. B puts a token in a
memory file, which is worse than committing it.

**51. A, C.**
Generic failures → **`errorCategory` + `isRetryable` + a readable message**, on every error. A
policy refusal retried eleven times → **business category, `isRetryable: false`**, with a friendly
explanation. B retries regardless of category, which is the bug; D is the generic message again.

**52. D — business, not retriable.**
The business-vs-permission trap. The token is valid, so access is not the problem; a rule about
approvals says no. Permission is when the caller **lacks access**.

**53. B — `Read` then `Write`.**
The documented fallback when `Edit` cannot identify the text unambiguously. A keeps retrying the
mechanism that is failing; D destroys work to avoid an edit.

**54. A — execute directly.**
Single file, cause and fix known. Plan mode for a one-line fix is the over-application trap from
weak point 2 (Set 1 Q12).

**55. C — a hook for `infra/`, prompt or CLAUDE.md for the export style.**
Two requirements of different kinds in one question. "Must never" plus a review-policy gate →
programmatic. A style preference → prompting. B over-enforces, D has them exactly backwards.

**56. D — stop the loop and handle the truncation.**
The second `stop_reason` question, in the disguise that matters: `max_tokens` is not `end_turn`, and
answer C is precisely the "not `end_turn`" rule failing in the wild. Only `"tool_use"` continues the
loop. B re-sends a request that will truncate again.

**57. B, D.**
"Typical patterns" instead of the specific classes it read is the documented sound of context
degradation → **scratchpad files**. Tool output crowding out the plan → **trim it before it enters
the context**. A is on the never-list, C is voting.

**58. C — a manifest of completed modules.**
Second appearance of the crash-recovery fact, deliberately. B is the scratchpad near-miss again and
D relies on a transcript that died with the runner.

**59. B — a prerequisite gate as a hook.**
"No exceptions, ever" → programmatic enforcement. A and C are prompting; D records the outcome in
the output rather than preventing the commit.

**60. A — the root CLAUDE.md.**
Applies to everything, automatically, whether or not anyone remembers → grouped by nothing → root
CLAUDE.md. B and C are the skills trap: **a skill must be invoked**, so it can never hold something
that must always apply, and `context: fork` changes where its output goes, not whether it runs. D is
the `paths` reflex; a glob rule loads on a matching file edit, not on every task.

---

## What this paper was testing, question by fact

| The fact | Where it appears | Previous misses |
|---|---|---|
| Prompt normalises format, schema fixes type | 1, and as a distractor in 2, 5, 15 | **4** — the leading repeat miss |
| Crash recovery = manifests | 41, 58 | **2**, two different wrong answers |
| D3 grouping, read off the content not the nouns | 16, 17, 18, 19, 23, 60 | **7 across three papers** |
| Loop continues only on `"tool_use"` | 31, 56 | **3** |
| Skills must be invoked | 18, 60 (and 17, where a skill is correct) | **3**, twice declared closed |
| Invented features | 7 (`--batch`), 23 (`.claude/config.json`), 34 (`parallel`), 46 (`CLAUDE_HEADLESS`, `--no-interactive`), 47, 49 | 3 |
| Never-list under speed | 12 (empty=success), 22 (voting, "be conservative"), 39 (halt the run), 45 (voting), 57 | 4 |
| Required vs nullable, both directions | 2, 3 | closed 16 Aug — confirming |
| Stratified high-confidence sample | 13 | closed 17 Aug — confirming |
| Parallel = Task calls in one response | 33 | closed 17 Aug — confirming |

**If you score 43+ but miss Q1, Q41 or Q58, the score is the less interesting number.** Those three
are the facts that have survived four papers, and they are worth more attention on 24 August than
anything you got right here.

**Before logging the result, write down the first-pass time.** A first pass under 45 minutes means
the six-step method was not run, whatever the score says.
