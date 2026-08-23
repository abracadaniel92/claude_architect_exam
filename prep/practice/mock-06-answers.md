# Mock 6 — Answer key

Mark each question right or wrong, then fill in the score sheet at the bottom. On a select-two,
**both** letters must be there for the mark; one letter scores zero, the same as a blank.

---

## Scenario A — Claims intake at a motor insurer

**1. C.** Tool use with a JSON schema is *the* way to get structured output. A prompt asking for
"JSON in your response" will always have a failure rate. A adds examples (missed 20 Aug this way),
B repairs symptoms downstream, D does not make text output a contract.

**2. A.** The source **may not** contain the value, so `required` would force the model to invent a
liability opinion. D is the 14 Aug trap: nullable plus a rule rejecting null is the worst of both —
it neither stops fabrication nor allows the legitimate absence.

**3. D.** Same rule, opposite direction. The source **always** contains it, so `required` guarantees
it cannot be omitted. Decide from the *source*, never from the failure you saw last.

**4. B.** The schema fixes the **type**; the prompt fixes the **format**. A post-processing layer
needs a branch per variant and breaks on the first layout nobody anticipated.

**5. A.** `calculated_total` next to `stated_total` is the documented pattern for totals that do not
add up. B asks the model to assert a conclusion instead of showing both numbers.

**6. B and D.** Two symptoms, two different kinds of thing: contradictory source data →
`conflict_detected` recording both values with their sources; a category list that grows → enum plus
`"other"` plus a detail string. A destroys the evidence; C is not a schema change.

**7. C.** Resubmit only the failures, found by `custom_id`. That is what `custom_id` is for.

**8. B.** The loop reads `stop_reason` and nothing else. A and C are the block-inspection proxies
the guide names as wrong; D makes a counter the primary mechanism.

**9. D.** Every `tool_use` needs one `tool_result` with the same `tool_use_id`, and all results from
one Claude message go back in **one** user message. C sends them in the wrong role.

**10. A.** The file list is known and the criteria are fixed, so the shape is known before starting:
prompt chaining, one pass per document plus one across documents. "Large" and "quarterly" do not
make it dynamic.

**11. A and C.** Money and identity are the two programmatic-enforcement triggers. A hook and a
prerequisite gate always run; B and D are prompts, which fail sometimes.

**12. B.** Input fine, system fine, a rule says no → **business**, `isRetryable: false`, with a
customer-friendly explanation. Not `permission` — the caller has access; the *policy* refuses.

**13. C.** A `mode` enum means split into purpose-specific tools, each with its own contract.
**B is the documented wrong answer** — fewer modes keeps the overloaded design.

**14. D.** A coverage gap is **declared**, not removed. A retries it away, B hides it, C tells the
pipeline log instead of the reader.

**15. A and C.** The high-confidence group is the one they are about to stop reviewing, so a
stratified random sample of *that* group is the only number that matters — plus accuracy by document
type and field, because a 97% average can hide one broken type. B measures the group they are
keeping; D is voting, which hides real errors.

---

## Scenario B — A platform team standardising a monorepo

Ten grouping questions in a row. The question to ask each time: **what set of files does this
content govern?**

**16. C.** A **file pattern** across every package → `.claude/rules/` with `paths:`. "They exist in
all nine packages" is the sentence that made this a miss on 17 Aug — the packages are where the
files live, not what the content is grouped by.

**17. B.** Grouped **by package**, with the maintainer selecting documents and nothing duplicated →
`@import`. The word "decides" is the trap: after the choice is made, the content applies to **all**
work in that package, which a skill can never do.

**18. D.** One folder, everything in it, nothing outside → a **directory CLAUDE.md**. A works but is
the reflex answer; the grouping here is a folder, not a pattern.

**19. A.** Needed only when someone asks for it → a **skill**.

**20. B.** Grouped by nothing — it always applies → the **root CLAUDE.md**. A is personal and not
shared; C fakes always-on with a pattern; D must be invoked.

**21. C.** Personal commands live in `~/.claude/commands/`. Anything starting with `~/` is personal
and is not shared through version control. D does not exist.

**22. A.** Personal MCP servers → `~/.claude.json`. Shared servers → `.mcp.json`.

**23. B and C.** Two symptoms, two keys: output flooding the session → `context: fork`; a skill that
edited when it should only read → `allowed-tools`. **A is the classic Domain 3 mistake** — `paths:`
is a `.claude/rules/` key, not a SKILL.md key.

**24. D.** `/memory` shows which memory files are loaded.

**25. B and D.** Inverse direction — the question asks which two **do not exist**.
`CLAUDE_HEADLESS=true` and `--no-interactive` are invented. `-p`/`--print` and
`--output-format json` are real, which is exactly why answering the ordinary way costs both marks.

**26. A.** A few known files changed → `--resume` and name them. The `--resume` fact in the
**positive** direction.

**27. C.** Most of the earlier context is stale → a **new** session with a written summary. Decided
by **how much** is stale, not by how long ago it was.

**28. B.** Parallel = several Task calls in **one response**. `parallel: true` does not exist;
consecutive turns run sequentially.

**29. D.** Four candidate names, none confirmed, and no string to search for → **semantic search**.
"Widen the pattern until something matches" is a description of not having a string.

**30. A.** `${VAR}` in `.mcp.json` keeps secrets out of the repository.

---

## Scenario C — A legal research system built from subagents

**31. C.** The coordinator `allowedTools` must include `"Task"`, or it cannot launch subagents.

**32. A.** Subagents receive **nothing** automatically. Everything they need goes in the prompt.

**33. B.** `fork_session` branches from one shared analysis so approaches can be compared. Separate
Task calls or separate sessions do not share the reading.

**34. D.** Coverage incomplete but every agent worked → the **coordinator split was too narrow**.
Blaming synthesis or a silent truncation contradicts what the question says is fine.

**35. C.** The structure is unknown, so **dynamic decomposition**: map first, then plan. 900
documents does not make it chaining, and 34 known documents in Q10 did not make it dynamic.

**36. A.** Goal-oriented prompts — objective plus success criteria — instead of a rigid procedure the
subagent follows off a cliff. B and C patch the script; D removes the subagent autonomy entirely.

**37. B and D.** Inverse direction again: which two are **never valid**. A `task_complete` tool and
"the response contains a text block" are two of the four documented wrong ways to stop. A and C are
both readings of `stop_reason`, which is the mechanism.

**38. C.** Progressive summarization loses details → a "case facts" block **outside** the summary.

**39. A and C.** Two symptoms, two fixes: lost in the middle → key findings at the **beginning**;
the model talking about typical patterns instead of what it found is context degradation →
**scratchpad files**. B is the "bigger window" answer, which does not fix attention dilution.

**40. B.** Trim tool output **before it enters the context**. 46 fields where five matter is the
guide example.

**41. D.** Provenance travels as structure from the agent that held the source: date, source
location, methodology. A and B are the two documented late fixes — the synthesis agent cannot weigh
what it cannot see, and a re-fetch is not reliably where the claim came from.

**42. A.** Crash recovery = **manifests**, loaded by the coordinator when work resumes.

**43. C.** MCP **resources** are content catalogues, and they exist to stop exploratory calls.

**44. B.** A small cross-role tool — `verify_fact` — for a common need. An agent given tools outside
its job will misuse them, so A cannot hold; the fix is the tool surface, not the instruction.

**45. D.** Shared slash commands live in `.claude/commands/`. A is the personal path.

---

## Scenario D — A telecom customer support agent

**46. A.** The caller lacks access → **permission**, not retriable. The token scope is too narrow;
nothing about the request or the service is wrong.

**47. C.** Input fine, system fine, authorised caller, a rule says no → **business**, with
`isRetryable: false` and a customer-friendly explanation. Two adjacent questions, two categories:
run the four-category test twice rather than pattern-matching the first one.

**48. B and D.** Inverse direction. Never: a generic message, and hiding the error as success. A and
C are both correct behaviour, which is what makes reading the stem the whole question.

**49. A.** The question prints the string → `Grep`.

**50. B.** Community server for a standard integration. Build custom only for your own workflows.

**51. D.** Two to four examples, aimed at the **unclear** cases.

**52. A.** A prose description giving inconsistent results → two or three concrete input/output
examples. The guide calls this the most effective way to show an expected transformation.

**53. C.** A category with many false alarms damages trust in the good ones → turn it off while you
fix it. B is "be conservative", which does not work; D hides it inside a broader category.

**54. B.** Self-review is weak because the model remembers its own reasoning → an **independent
instance**. C is voting, which hides real problems.

**55. D.** Must call a tool, chooses which → `any`. `auto` would allow a text answer; the forced form
would remove the choice of tool.

**56. A.** Personal instructions → `~/.claude/CLAUDE.md`. Anything under `~/` is not shared.

**57. C and D.** Never escalate on **sentiment** or the **model own confidence**. A and B are two of
the three valid grounds, so answering "the valid ones" loses both marks.

**58. B.** The customer explicitly asked for a person → escalate **immediately**, with the structured
handoff summary. Having a fix in hand does not change it; A is the answer for a customer who is
frustrated but has not asked.

**59. C.** Split into items, investigate in parallel over shared context, return **one** combined
answer. A and B are the two documented wrong answers; D escalates work the agent can do.

**60. A and C.** The human cannot see the conversation, so the handoff carries the customer ID, the
root cause, the amount involved and the recommended action — that is A plus C. B dumps the transcript
instead of the analysis; D is confidence again.

---

## Score sheet

| Domain | Questions | Score |
|---|---|---|
| **D1 — Agentic architecture** (16) | 8, 9, 10, 11, 26, 27, 28, 31, 32, 33, 34, 35, 36, 37, 59, 60 | ___ / 16 |
| **D2 — Tool design and MCP** (11) | 12, 13, 29, 30, 43, 44, 46, 47, 48, 49, 50 | ___ / 11 |
| **D3 — Claude Code configuration** (12) | 16–25, 45, 56 | ___ / 12 |
| **D4 — Prompting and structured output** (12) | 1–7, 51, 52, 53, 54, 55 | ___ / 12 |
| **D5 — Context and reliability** (9) | 14, 15, 38, 39, 40, 41, 42, 57, 58 | ___ / 9 |
| **Total** | | ___ / 60 |

**Select-two questions:** 6, 11, 15, 23, 25, 37, 39, 48, 57, 60 — ___ / 10.
Count how many you answered with one letter, and how many you answered in the wrong direction
(Q25, Q37, Q48, Q57 are the inverse-direction four).

**Floors:** 43/60 overall, and no domain below 60% — D1 10, D2 7, D3 8, D4 8, D5 6.

**Answer letters, in one line, for fast marking:**
1 C · 2 A · 3 D · 4 B · 5 A · 6 BD · 7 C · 8 B · 9 D · 10 A · 11 AC · 12 B · 13 C · 14 D · 15 AC ·
16 C · 17 B · 18 D · 19 A · 20 B · 21 C · 22 A · 23 BC · 24 D · 25 BD · 26 A · 27 C · 28 B · 29 D ·
30 A · 31 C · 32 A · 33 B · 34 D · 35 C · 36 A · 37 BD · 38 C · 39 AC · 40 B · 41 D · 42 A · 43 C ·
44 B · 45 D · 46 A · 47 C · 48 BD · 49 A · 50 B · 51 D · 52 A · 53 C · 54 B · 55 D · 56 A · 57 CD ·
58 B · 59 C · 60 AC
