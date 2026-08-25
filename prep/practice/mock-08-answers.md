# Mock 8 — Answer key

On a select-two, **both** letters must be there for the mark; one letter scores zero, the same as a
blank.

---

## Scenario A — Kestrel Underwriting

**1. C.** The source **may not** contain the value, so `required` forces the model to invent a
recommendation. A represents absence inside the enum but still demands a value; B and D are late
repairs of a schema problem.

**2. A.** Same rule, opposite direction. The source **always** contains it, so `required` guarantees
it cannot be omitted. D is the worst of both — it neither stops fabrication nor permits legitimate
absence.

**3. D.** Tool use with a JSON schema is *the* way to get structured output. A prompt asking for JSON
in the response text will always carry a failure rate; A, B and C all work on the symptom.

**4. B.** Tool use plus a schema removes **syntax** errors, not **semantic** ones. `calculated_total`
beside `stated_total` makes the discrepancy visible. C overwrites the evidence rather than surfacing
it.

**5. C.** The schema fixes the **type**; the prompt fixes the **format**. A post-processing layer
needs a branch per variant and breaks on the first layout nobody anticipated.

**6. B and D.** Two symptoms, two different kinds of thing: a category list that grows → enum plus
`"other"` plus a detail field; contradictory source data → `conflict_detected` recording both values
with their sources. C is not a schema change; A destroys the evidence.

**7. A and C.** The retry carries the document, the failed extraction and the **specific** errors.
And the boundary matters: a retry fixes format and structure, never information that is not in the
document. B removes what the correction must reference; D retries a deterministic failure.

**8. B and C.** `custom_id` matches requests to results, and batches cost roughly 50% less. A is
false — there is **no** latency guarantee, up to 24 hours. D is false — multi-turn tool calling is
**not** supported.

**9. A.** A 24-hour window against a 30-hour commitment means submitting every **4 hours**.

**10. B.** The type is unknown until the document is read and any of several schemas may apply, but
prose is never acceptable → `any`. `auto` permits a text reply; a forced tool welds every document
to one schema.

**11. A and D.** The high-confidence group is the one they are about to stop reviewing, so a
stratified sample of *that* group is the only number that matters — plus accuracy by type and field,
because one average can hide one broken type. B measures the group they are keeping; C is voting,
which hides real errors.

**12. D.** Confidence is usable for routing review only once **calibrated against labelled data**.
A is uncalibrated confidence, which is never an answer in any disguise.

**13. B.** Input fine, system fine, caller authorised, a rule says no → **business**,
`isRetryable: false`, with a customer-friendly explanation. Not `permission` — the broker has
access; the *policy* refuses.

**14. C.** MCP's `isError` flag makes the failure machine-recognisable instead of prose the model
reads as data. B replaces a mislabelled failure with a silent one.

**15. B and C.** Money and identity/prerequisite checks are the programmatic-enforcement triggers. A
hook and a prerequisite gate always run; A and D are prompts, which fail sometimes.

---

## Scenario B — Halden Systems

The question to ask on each grouping item: **what set of files does this content govern?**

**16. B.** A **file pattern** across services → `.claude/rules/` with `paths:`. "Six of the eight
services" describes where the files live, not what the content is grouped by.

**17. D.** Grouped **by service**, owner selects documents, nothing duplicated → `@import`. "Decides"
is the trap: once chosen the content governs **all** work in that service, which a skill can never
do.

**18. A.** One folder, everything in it, nothing outside → a **directory CLAUDE.md**. B works but the
grouping here is a folder, not a pattern.

**19. C.** Grouped by nothing — it always applies, to everyone, automatically → the **root
CLAUDE.md**. A is personal and never reaches the other 69 engineers.

**20. B.** Needed only when someone asks for it → a **skill**.

**21. D.** Personal, not shared → `~/.claude/commands/`. C is an invented feature.

**22. A.** `allowed-tools` is the configuration guarantee; B is an instruction the model may not
follow.

**23. C.** `context: fork` runs the skill in a separate context so its output does not flood the
session.

**24. B.** `argument-hint` asks for the missing parameter before the command runs.

**25. D.** `/memory` shows which memory files are actually loaded.

**26. A.** The file list is known and the criteria are fixed, so the shape is known before starting →
prompt chaining. "Audit" and "release" do not make it dynamic.

**27. C.** A few known, named files changed and everything else holds → `--resume` and name them.

**28. B.** Renamed services, a replaced build system and a twice-rescoped ticket is broad staleness →
fresh session with a written summary. Decided by **how much** is stale, not whether anything is.

**29. D.** Nothing stale, nothing crashed, findings still needed, context full → `/compact`, the
in-session relief valve.

**30. A.** Noisy discovery that need not stay in the main context → an Explore subagent.

---

## Scenario C — Thorne Analytics

**31. C.** The coordinator's `allowedTools` must include `"Task"` or no delegation can happen.

**32. A and C.** Subagents receive nothing automatically, and all messages pass through the
coordinator — subagents never talk to each other. B and D invert both facts.

**33. B.** Parallel = several Task calls in **one response**. There is no `parallel: true` field.

**34. D.** `fork_session` branches several approaches from one shared analysis without re-collecting
the evidence.

**35. A.** Every subagent succeeded against its own brief, so the gap is in how the coordinator
divided the work — not in execution, and not in synthesis.

**36. B.** Goal-and-criteria prompts let the subagent adapt; a rigid script fails on the first case
that does not fit it.

**37. C.** An iterative refinement loop: evaluate for gaps, re-delegate targeted follow-ups,
re-synthesise until coverage is sufficient.

**38. D.** One user message, one `tool_result` block per `tool_use`, each with its matching
`tool_use_id`.

**39. A.** Scope each agent's tools to its role — 4–5 relevant tools beat 19, and out-of-role tools
invite misuse.

**40. B.** MCP resources are content catalogues; they stop exploratory calls before they start.

**41. C.** One small cross-role tool and nothing else from the research set.

**42. C and D.** A 503 is transient and retriable, and the subagent fixes transient failures itself,
reporting upward only what it cannot resolve. B is hiding an error as success.

**43. D.** Record both figures with their sources — and dates, so a stale figure is not mistaken for
a contradiction. Never pick one, never average.

**44. A and B.** Date, source location and methodology are what a subagent must record because
nothing downstream can recover them. C and D are the two documented downstream repairs, both wrong.

**45. A.** Manifests written as work completes are what survives a crash. C stops findings decaying
but does not resume a run.

---

## Scenario D — Lumen Mobile

**46. B.** The loop continues only on `tool_use`. `max_tokens` stops it, exactly like `end_turn` and
`refusal` — "not `end_turn`" is the wrong generalisation.

**47. C.** Problems arriving in one message and sharing customer context are decomposed, investigated
together, and answered once.

**48. D.** Money plus "must never" → programmatic enforcement, and it must block the call **before**
it happens. A reverses a payment already made.

**49. A.** `PostToolUse` changes tool **results** before the model reads them — the documented use for
normalising differing data shapes. `PreToolUse` blocks outgoing **calls**.

**50. C.** No agreed name, and the candidate words return nothing — that is the definition of having
no string to search for. Semantic search.

**51. B.** The exact string is printed in the question → `Grep`.

**52. D.** Tool **descriptions** decide which tool the model picks. Improve them first, before
forcing `tool_choice` or removing a working tool.

**53. A.** A `mode` enum means split into purpose-specific tools, each with its own contract. **B is
the documented wrong answer** — fewer modes keeps the overloaded design.

**54. B.** A standard, uncustomised integration → the community server. A team's own workflow →
build it.

**55. C.** An explicit request for a human is honoured **immediately**, without finishing the
diagnosis first — and the handoff carries a structured summary because the console cannot see the
conversation.

**56. B and D.** Two different problems: precise facts dissolving in summarisation → a "case facts"
block outside the summary; verbose tool results filling context → trim before they enter it. A
intensifies the first failure; C asks the model to report a loss rather than preventing it.

**57. D.** Personal, machine-local, not shared → `~/.claude/CLAUDE.md`. C is an invented file.

**58. A and D.** `CLAUDE_HEADLESS=true` and `--no-interactive` do not exist. `-p` and
`--output-format json` are both real.

**59. A.** Two to four examples, aimed at the **unclear** cases — not the ones already handled well.

**60. B.** Two or three concrete input/output examples are the documented way to show an expected
transformation when prose has failed.

---

## Score sheet

| Domain | Questions | Score |
|---|---|---|
| D1 — Agentic Architecture | 15, 26, 27, 28, 31, 32, 33, 34, 35, 36, 37, 38, 46, 47, 48, 49 (16) | ___/16 |
| D2 — Tool Design & MCP | 13, 14, 39, 40, 41, 42, 50, 51, 52, 53, 54 (11) | ___/11 |
| D3 — Claude Code Configuration | 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 57, 58 (12) | ___/12 |
| D4 — Prompt Eng. & Structured Output | 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 59, 60 (12) | ___/12 |
| D5 — Context & Reliability | 11, 12, 29, 30, 43, 44, 45, 55, 56 (9) | ___/9 |
| **Total** | | **___/60** |

**Select-two questions (10):** 6, 7, 8, 11, 15, 32, 42, 44, 56, 58.

**Key balance check.** Singles: A 12 · B 14 · C 12 · D 12. Select-twos: each letter appears 5×. No
positional rotation — verify by reading the singles down each scenario, they do not cycle.

**Length-tell check.** The correct answer is the **shortest** option on questions 1, 2, 3, 5, 10, 12,
14, 19, 20, 21, 23, 24, 25, 29, 30, 31, 33, 39, 41, 43, 45, 46, 51, 53, 55, 57, 59 and 60 — 28 of the
50 singles. If you scored well by picking the option that explains itself, this paper would have
punished it.
