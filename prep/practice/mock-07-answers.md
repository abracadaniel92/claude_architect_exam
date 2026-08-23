# Mock 7 — Answer key

Mark each question right or wrong, then fill in the score sheet at the bottom. On a select-two,
**both** letters must be there for the mark; one letter scores zero, the same as a blank.

---

## Scenario A — Meridian Play (Customer Support Resolution Agent)

**1. C.** The loop reads `stop_reason` and continues only on `"tool_use"`. `refusal` is one of the
seven values and it stops the loop, exactly like `end_turn` and `max_tokens` — "not `end_turn`" (A)
is the classic wrong generalisation.

**2. D.** One user message, one `tool_result` block per `tool_use`, each carrying the matching
`tool_use_id`.

**3. A and C.** Money and identity are the two triggers for programmatic enforcement. A `PreToolUse`
hook and a prerequisite gate always run; a system prompt (B) and a tool description (D) are prompts,
which fail sometimes.

**4. B.** Most of the earlier context (promotions, retention offer) is stale; only two narrow facts
survive. That much staleness means a new session with a written summary, not `--resume`.

**5. B.** Parallel = several Task calls in one response. There is no `parallel: true` field.

**6. C.** Tool descriptions decide which tool the model picks. Improve them first, before reaching
for a forced `tool_choice` or a routing layer.

**7. B.** Several matching accounts → ask for another identifier. Never guess which one is right.

**8. C.** The API, token, and request are all fine; a plan-tier rule says no. That is `business`, not
`permission` — the subscriber has access to their account, the *policy* refuses the credit.

**9. B.** MCP resources are content catalogues that stop exploratory calls before they start.

**10. C.** A "case facts" block held outside the running summary, carried forward verbatim.

**11. B and C.** Sentiment and the model's own uncalibrated confidence are never, on their own,
grounds to escalate. A and D are two of the three things that correctly *do* trigger escalation
(explicit request, no progress possible) — the third being a policy gap.

**12. B and C.** The verified ID, the root cause, the amount, and the recommended action are the
handoff package. The raw transcript (A) and the model's own confidence (D) are not — the console
cannot see the conversation, but structured facts travel; an unedited transcript is not a summary.

---

## Scenario B — Aurora Retail (Code Generation with Claude Code)

Nine grouping questions in a row. Ask each time: **what set of files does this content govern?**

**13. C.** One folder, nothing outside it → a directory CLAUDE.md.

**14. B.** Grouped by package, maintainer picks, nothing copied → `@import`. "Decides" is the trap:
once chosen, the content governs *all* work in that package, which a skill can never do.

**15. B.** A file pattern across every package → `.claude/rules/` with `paths:`.

**16. B.** Grouped by nothing — always applies, to everyone, automatically → the root CLAUDE.md.
`~/.claude/CLAUDE.md` (A) is personal and does not reach the other 89 engineers.

**17. A.** Needed only when the upgrade starts → a skill.

**18. C.** `argument-hint` asks the developer for the missing parameter before the command runs.

**19. B and C.** `context: fork` keeps the huge output out of the main session; `allowed-tools`
limited to read-only tools stops it from ever touching the lockfile again.

**20. B.** Personal, not shared → `~/.claude/commands/`.

**21. B.** Restructuring module boundaries across 40 files, changing how components talk to each
other, is architectural. Plan mode reviews the approach before anything changes.

**22. B.** A manifest of completed packages, written as each finishes, is what survives a crash.

**23. C.** Renamed packages, a changed build tool, and a grown ticket scope are broad staleness —
start fresh with a written summary, not `--resume`.

**24. C.** Noisy discovery that does not need to stay in the main context → an Explore subagent.

---

## Scenario C — Northbridge Research (Multi-Agent Research System)

**25. C.** The coordinator's `allowedTools` must include `"Task"` to launch subagents at all.

**26. A.** Subagents receive nothing automatically. Everything the coordinator knows has to go into
the Task prompt.

**27. B.** Parallel = several Task calls in one response.

**28. B.** `fork_session` branches multiple approaches from one shared analysis, without re-collecting
the evidence.

**29. B.** A small cross-role tool, `verify_fact`, and nothing else from the research toolset — give
it only what its role needs.

**30. B.** MCP resources expose the catalogues (regions, filing types, schema) so the agent does not
have to discover them by trial and error.

**31. B.** A standard, uncustomised integration → use the community server.

**32. C.** Every subagent succeeded on its own brief; the gap is in how the coordinator divided the
work, not in execution.

**33. C.** Record both figures with their sources. Dates are required so a stale figure is not
mistaken for a contradiction.

**34. A and C.** Date and source location are two of the three things a subagent must record because
nothing downstream can recover them. Confidence (B) and after-the-fact credibility judgement (D) are
both distractors from the same family as weighing sources at synthesis time.

**35. B.** A coverage gap is declared in the output the reader sees, next to the findings — not left
implicit, not filed elsewhere, and not silently absorbed into a report that reads as complete.

**36. B.** The 60 filings actually retrieved, clearly labelled as partial. An incomplete answer that
says so is correct; a success with no results is not — and neither is silence until the job is
"finished."

---

## Scenario D — Fathom Logistics (Developer Productivity with Claude)

**37. B.** The scope and shape of the work are unknown — map first, then plan the passes.

**38. A.** A handful of known, named files changed; everything else holds. `--resume` and name them.

**39. C.** One user message, two `tool_result` blocks, each with its matching `tool_use_id`.

**40. B.** `fork_session` branches both approaches from the one shared reading, instead of reading the
module twice.

**41. A.** File paths by pattern → `Glob`.

**42. D.** No agreed name, and grepping the candidate words returns nothing — that is the definition
of not having a string to search for. Semantic search.

**43. C.** `Edit` cannot match unique text → fall back to `Read` + `Write`.

**44. C.** Improve the tool's description first — what it does, example queries, when to prefer it —
before forcing `tool_choice` or removing the built-in tool.

**45. A.** `${VAR}` references in `.mcp.json`, resolved from the environment, keep tokens out of
version control.

**46. A.** Personal, not shared → `~/.claude.json`.

**47. C.** `/memory` shows which memory files are actually loaded.

**48. A and C.** Scratchpad files stop findings decaying over a long session; moving key findings to
the beginning of the context stops them being lost in the middle. A bigger context window (B) does
not fix attention dilution, and asking for conciseness (D) does not address either symptom.

---

## Scenario E — MedPath Health (Claude Code for Continuous Integration)

**49. B.** `-p` / `--print` runs Claude Code non-interactively, so it does not hang waiting for input.

**50. B and D.** `CLAUDE_HEADLESS=true` and `--no-interactive` do not exist. `-p` and
`--output-format json` are both real.

**51. C.** `--output-format json` gives machine-readable output; `--json-schema` guarantees it
follows the exact shape the gate expects. Neither alone is enough, and a `schema:` workflow key (D)
is not a real Claude Code setting.

**52. B.** Testing standards, fixture conventions, and review criteria belong in CLAUDE.md — that is
how Claude Code learns the project in CI, not a string appended inside the pipeline script.

**53. C.** Give it the existing test files, so it can see what is already covered.

**54. A.** Include earlier findings in the context and ask for only new or still-unfixed issues.

**55. B.** A known file list with fixed review criteria is prompt chaining — one pass per file, then
one pass across files for cross-file issues.

**56. B.** Concrete code examples for each severity level in the prompt make the labelling
consistent. A confidence score (A) does not fix inconsistent labels, and majority voting (C) hides
real disagreement rather than resolving it.

**57. A.** Turn the bad category off, keep the good ones running, fix its prompt, then turn it back
on. "Be conservative" (B) is never a specific-enough instruction, and downgrading severity (D) still
leaves the wrong findings firing.

**58. B.** An independent instance, without the drafting context, catches what self-review misses —
the model remembers its own reasoning and defends it.

**59. B.** Nobody is waiting, so the Message Batches API fits, at roughly half the real-time cost.
Batches do not support multi-turn tool calling (D is wrong on the mechanism, even though the
conclusion happens to match).

**60. C.** Two to four examples, aimed at the unclear, borderline cases — not the ones already
handled well.

---

## Scenario F — Harborline Customs (Structured Data Extraction)

**61. C.** Tool use with a JSON schema is *the* way to get structured output; a prompt asking for
"JSON in the response" will always have some parse failure rate.

**62. C.** The source always contains this field, so `required` guarantees it cannot be omitted.

**63. B.** The source may not contain this field, so `required` forces the model to invent a value.
Nullable and optional represent genuine absence.

**64. B.** The schema fixes the type; format normalisation rules in the prompt fix the format. A
post-processing layer needs a branch per variant and breaks on the first layout nobody anticipated.

**65. C.** The document type is not known until read, and any of several schemas might apply →
`tool_choice: "any"`.

**66. C.** Resubmit only the failed requests, matched to their results by `custom_id`.

**67. A.** A 24-hour processing window and a 30-hour SLA mean submitting every 4 hours.

**68. A and C.** `calculated_total` next to `stated_total` catches totals that do not add up;
`conflict_detected`, recording both values with their sources, catches contradictory source data.
Neither is fixed by asking the model to assert a conclusion (B) or attach a confidence score (D).

**69. B and C.** A stratified random sample of the high-confidence group — the one about to stop
being reviewed — plus accuracy broken down by document type and field, because one average can hide
one broken type. Uniform sampling (A) and voting across passes (D) tell you nothing about the group
that matters.

**70. C.** State which findings are well supported and which sections have coverage gaps — declared
in the report the reader sees, not fixed by a retry, a heavier summary, or a note left somewhere
else.

**71. B.** Returning success with an empty result set when the job did not finish is hiding the
error as success — always wrong. Returning the 3,000 records actually obtained, labelled partial
(A), is correct; so is stating the split (C) and resubmitting only what is missing (D).

**72. B.** A confidence score is only usable for routing review work once it is calibrated against
labelled data — checked against actual accuracy, not taken at face value the moment the model
produces it.

---

## Score sheet

| Domain | Questions | Score |
|---|---|---|
| D1 — Agentic Architecture | 1,2,3,4,5,25,26,27,28,37,38,39,40 (13) | ___/13 |
| D2 — Tool Design & MCP | 6,7,8,9,29,30,31,41,42,43,44 (11) | ___/11 |
| D3 — Claude Code Configuration | 13,14,15,16,17,18,19,20,21,45,46,47,49,50 (14) | ___/14 |
| D4 — Prompt Engineering & Structured Output | 51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68 (18) | ___/18 |
| D5 — Context & Reliability | 10,11,12,22,23,24,32,33,34,35,36,48,69,70,71,72 (16) | ___/16 |
| **Total** | | **___/72** |

| Scenario | Questions | Score |
|---|---|---|
| A — Meridian Play (Customer Support) | 1–12 | ___/12 |
| B — Aurora Retail (Code Generation) | 13–24 | ___/12 |
| C — Northbridge Research (Multi-Agent) | 25–36 | ___/12 |
| D — Fathom Logistics (Developer Productivity) | 37–48 | ___/12 |
| E — MedPath Health (CI) | 49–60 | ___/12 |
| F — Harborline Customs (Structured Extraction) | 61–72 | ___/12 |

**Select-two questions (9 total):** 3, 11, 12, 19, 34, 48, 50, 68, 69. Count your letters on each —
a single letter or a blank scores zero, same as a wrong answer.

**Single-answer inverse-direction questions:** Q57 and Q71 read like "select two" at a glance but
each asks for exactly **one** letter — "the correct action" and "which is never acceptable." If you
gave two letters on either, re-read the stem before marking it wrong; the extra letter is the error,
not the content.
