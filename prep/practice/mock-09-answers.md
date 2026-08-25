# Mock 9 — Answer key

On a select-two, **both** letters must be there for the mark; one letter scores zero, the same as a
blank.

---

## Scenario A — Calderwood Rail

**1. C.** File **paths** by pattern → `Glob`. `Grep` searches contents, not paths.

**2. A.** The exact string is printed in the question → `Grep`.

**3. D.** No agreed name, the original authors are gone, and none of the candidate words appears
anywhere — that is the definition of having no literal to search for. **Semantic search.** A and C
grep for strings the question has already said are absent; B widens a pattern, which is a description
of not having one.

**4. B.** `Edit` needs a unique anchor; when the file defeats that, `Read` + `Write` is the documented
fallback. C mutilates the file to satisfy the tool.

**5. C.** Incremental exploration: search for entry points first, then read selectively along the
traced paths.

**6. B and D.** Shared server in `.mcp.json` with `${VAR}` so no secret is committed; personal server
in `~/.claude.json`. A commits a live token; C unshares team tooling.

**7. A.** Direct execution for the well-scoped single-function fix; plan mode where scale and
competing approaches make design-before-commitment worthwhile.

**8. D.** `/memory` shows which memory files a session has loaded.

**9. B.** Shared with everyone on clone → `.claude/commands/`. `~/.claude/commands/` is personal.

**10. C.** User-level configuration never travels through version control; team standards belong at
project level.

**11. A.** The scope and shape are unknown → **dynamic decomposition**: map first, then plan from the
map. "Every remaining use" does not make it a fixed list — nobody knows what the list is.

**12. D.** `fork_session` branches independent explorations from one shared analysis without
re-deriving it.

**13. B.** A replaced build system, merged modules and a rewritten ticket is broad staleness → fresh
session with a written summary. Decided by **how much** is stale, not whether anything is.

**14. C.** Answering from "typical patterns" instead of specific findings is context degradation →
**scratchpad files**. B is the documented non-fix: a bigger window does not cure attention dilution.

**15. C.** Crash recovery → **manifests**, written as work completes and loaded on resume. `--resume`
does not survive a machine restart mid-run, and a scratchpad addresses decay, not recovery.

---

## Scenario B — Brightwell Financial

**16. C.** `-p` / `--print` runs non-interactively, so the step stops waiting for input.

**17. B.** `--output-format json` makes the output machine-readable; `--json-schema` makes it conform
to the shape the gate expects. Neither alone is enough, and D is not a real setting.

**18. A and C.** `--no-interactive` and `CLAUDE_HEADLESS=true` do not exist.

**19. D.** In CI, **CLAUDE.md is how Claude Code learns the project** — testing standards, fixture
conventions, review criteria.

**20. A.** Give the reviewer its prior findings and ask for deltas: new issues plus unresolved
carryovers.

**21. B.** Supply the **existing test files**, so it can see what is already covered. C gives a number,
not the content — a percentage cannot tell the model which scenarios exist.

**22. D.** Vague conservatism does not transfer; explicit categorical criteria with concrete
boundaries do. B is self-reported confidence used as a sort key, which is uncalibrated confidence in
a thin disguise.

**23. C.** Disable the offending category, keep the accurate ones, fix the prompt, re-enable. A high
false-positive category is contagious — it teaches developers to dismiss everything.

**24. A.** Concrete code examples per severity level give the classifier something to match against.
C is voting, which launders an unanchored judgement rather than anchoring it.

**25. B.** The generating session carries the reasoning that produced the code and will not question
it. Review in an independent instance without that context.

**26. D.** **Voting across runs hides real bugs** — a genuine defect surfaced by one run is discarded
on exactly the same rule as a false positive. B is a real cost objection but not the reason the design
is wrong.

**27. B and C.** Latency-tolerant work suits batch; blocking checks stay synchronous because a batch
may take up to 24 hours with **no** latency guarantee. A and D are both false — no guaranteed window,
and no multi-turn tool calling.

**28. A and D.** Two to four examples aimed at the genuinely unclear cases, plus examples demonstrating
the exact output shape. B is volume over targeting; C is false — examples complement explicit
criteria, they do not replace them.

**29. A.** Known file list, fixed criteria → prompt chaining: one pass per file, then one across files.

**30. D.** A coverage gap is **declared in the output the reader sees**, next to the findings. C files
it somewhere the reader of the report will never look, which is the same miss as hiding it.

---

## Scenario C — Aldergate Policy Institute

**31. B.** The Task tool is the spawning mechanism; without `"Task"` in `allowedTools` no delegation is
possible regardless of what the prompt says.

**32. C.** Subagents inherit nothing. Everything they need goes into the Task prompt.

**33. A.** Parallel = several Task calls in **one response**. There is no `parallel: true` field and no
concurrency setting.

**34. D.** Every subagent succeeded against its own brief, so the omission is in how the coordinator
divided the work.

**35. B.** Goal-and-criteria prompts let the subagent adapt; a fixed script fails on the first case it
does not anticipate.

**36. A.** An iterative refinement loop: evaluate for gaps, re-delegate targeted follow-ups,
re-synthesise until coverage is sufficient.

**37. C.** The loop continues **only** on `tool_use`. `refusal` stops it, exactly like `end_turn` and
`max_tokens` — "not `end_turn`" is the wrong generalisation, and D treats a stop value as a continue
value.

**38. D.** One user message, one `tool_result` block per `tool_use`, each carrying its matching
`tool_use_id`.

**39. A and C.** Subagents never talk to each other — everything routes through the coordinator — and
each AgentDefinition carries its own description, system prompt and tool restrictions. B and D invert
both facts; restrictions are configuration, not advice.

**40. B.** Scope each agent's tools to its role. Agents choose reliably among four or five relevant
tools and unreliably among 22, and out-of-role tools get misused precisely because they are there.

**41. B and D.** Transient and retriable — and the **subagent retries it itself**, passing upward only
what it cannot resolve, with what was attempted and any partial results. A halts on a recoverable
failure; C hides an error as success.

**42. A.** MCP **resources** are content catalogues; they turn discovery into a lookup.

**43. C.** Provenance survives only as structure: claim-source mappings travel as data through every
hop. A invents citations, which is worse than none in an evidence review.

**44. A and D.** Record both figures with their sources and surface the disagreement, and require dates
so that figures measuring different moments are not misread as contradictions. B and C both resolve a
conflict the system has no basis to resolve.

**45. B.** Return the findings actually obtained, **marked as partial**. Partial results are one of the
four required parts of a subagent report. C is the forbidden one — success with an empty set.

---

## Scenario D — Oakhill Property

**46. A.** Tool use with a JSON schema is *the* way to get structured output; a prompt asking for JSON
in the response text always carries a failure rate.

**47. C.** The source **may not** contain the value, so `required` forces fabrication. D still demands
a value; A pits an instruction against a structural requirement.

**48. B.** Two symptoms, one schema answer each: a growing category list → enum plus `"other"` plus a
detail field; genuinely ambiguous readings → an `"unclear"` value. C and D are downstream repairs, and
C additionally leans on uncalibrated confidence.

**49. D.** A retry fixes **format and structure**; it cannot produce information that is not in the
document supplied. A, B and C are all structural or placement errors the model can correct when shown
the errors.

**50. A.** `custom_id` identifies the failures; resubmit only those, fixing what caused each — chunking
the oversized bundles before they go back.

**51. B and C.** Money/registration limits and identity verification are the programmatic-enforcement
triggers. A hook and a prerequisite gate always run; A and D are prompts, which fail sometimes.

**52. C.** Known list, fixed criteria, shape known before starting → prompt chaining. "Compliance" and
"quarterly" do not make it dynamic.

**53. A.** `PostToolUse` changes tool **results** before the model reads them — the documented use for
normalising differing data shapes. `PreToolUse` blocks outgoing **calls**.

**54. D.** The caller lacks the access the operation needs → **permission**. Not `business`: no policy
rule refused the operation, the token simply lacked the scope.

**55. B.** An `action`/`mode` enum means split into purpose-specific tools, each with its own contract.
**C is the documented wrong answer** — fewer actions keeps the overloaded design.

**56. A.** Universal and always-relevant → CLAUDE.md. Occasional and task-specific → a skill.

**57. C and D.** `allowed-tools` limited to read operations makes the write impossible; `context: fork`
keeps the output out of the main session. A and B address neither symptom.

**58. A and B.** The high-confidence group is the one about to stop being reviewed, so a stratified
sample of *that* group is the only number that matters — plus segmentation by type and field, because
one average can hide one broken type. C measures the group they are keeping; D is voting.

**59. B.** Confidence is usable for routing review only once **calibrated against labelled data**.

**60. D.** Trim the tool result to the fields actually used **before it enters the context**. A asks
the model to ignore what it has already been made to read; B compresses after the damage.

---

## Score sheet

| Domain | Questions | Score |
|---|---|---|
| D1 — Agentic Architecture | 11, 12, 13, 29, 31, 32, 33, 34, 35, 36, 37, 38, 39, 51, 52, 53 (16) | ___/16 |
| D2 — Tool Design & MCP | 1, 2, 3, 4, 5, 6, 40, 41, 42, 54, 55 (11) | ___/11 |
| D3 — Claude Code Configuration | 7, 8, 9, 10, 16, 17, 18, 19, 20, 21, 56, 57 (12) | ___/12 |
| D4 — Prompt Eng. & Structured Output | 22, 23, 24, 25, 26, 27, 28, 46, 47, 48, 49, 50 (12) | ___/12 |
| D5 — Context & Reliability | 14, 15, 30, 43, 44, 45, 58, 59, 60 (9) | ___/9 |
| **Total** | | **___/60** |

**Select-two questions (10):** 6, 18, 27, 28, 39, 41, 44, 51, 57, 58.

**Completeness check.** Sixty answers. Ten of them are two letters. If your list is shorter than
sixty lines, find the gap before you mark anything.

**Key balance.** Singles: A 12 · B 13 · C 13 · D 12, no positional rotation. Select-twos: each letter
5×.

**Length-tell check — this is the point of the paper.** The correct answer is the **longest** option
on Q3, Q5, Q11, Q17, Q22, Q23, Q25, Q26, Q30, Q36, Q39, Q41, Q43, Q44, Q48, Q51 and Q57. It is the
**shortest** on Q1, Q2, Q8, Q12, Q15, Q16, Q19, Q29, Q32, Q37, Q42, Q45, Q47, Q53, Q55, Q59 and Q60.
Neither shape predicts anything. If your misses cluster in one of those two lists, the heuristic is
doing more work than you think it is.

**The three facts this paper re-tests without saying so.** Q41 is the subagent-retry rule omitted on
both Mock 5 Q39 and Mock 8 Q42 — same select-two position, third appearance. Q59 is the confidence
calibration missed on Mock 8 Q12. Q37 is `stop_reason: "refusal"`, missed on Mock 7 Q1. Check those
three first when marking.
