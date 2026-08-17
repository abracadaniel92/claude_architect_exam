# Mock 2 — Answer key and explanations

Questions: `mock-02-questions.md`. Do not open this file until you have finished and stopped the
clock.

---

## Key

| Q | Ans | Domain | | Q | Ans | Domain | | Q | Ans | Domain |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | C | D2 | | 21 | C | D3 | | 41 | B | D2 |
| 2 | A | D2 | | 22 | B | D3 | | 42 | D | D2 |
| 3 | D | D2 | | 23 | D | D3 | | 43 | C | D5 |
| 4 | **A, C** | D2 | | 24 | A | D4 | | 44 | A | D5 |
| 5 | B | D2 | | 25 | **B, D** | D4 | | 45 | B | D5 |
| 6 | D | D2 | | 26 | B | D4 | | 46 | D | D4 |
| 7 | B | D3 | | 27 | **A, D** | D4 | | 47 | B | D4 |
| 8 | C | D3 | | 28 | C | D4 | | 48 | C | D4 |
| 9 | A | D3 | | 29 | D | D5 | | 49 | A | D4 |
| 10 | D | D3 | | 30 | **A, B** | D5 | | 50 | **B, C** | D4 |
| 11 | B | D1 | | 31 | B | D1 | | 51 | A | D4 |
| 12 | A | D1 | | 32 | D | D1 | | 52 | D | D4 |
| 13 | C | D1 | | 33 | A | D1 | | 53 | C | D1 |
| 14 | D | D5 | | 34 | **B, C** | D1 | | 54 | **A, D** | D1 |
| 15 | **B, D** | D5 | | 35 | D | D1 | | 55 | B | D1 |
| 16 | A | D3 | | 36 | A | D1 | | 56 | A | D1 |
| 17 | C | D3 | | 37 | C | D1 | | 57 | D | D1 |
| 18 | B | D3 | | 38 | **C, D** | D1 | | 58 | C | D2 |
| 19 | D | D3 | | 39 | A | D2 | | 59 | **A, C** | D5 |
| 20 | A | D3 | | 40 | C | D2 | | 60 | B | D5 |

A select-two question scores 1 only if **both** letters are right. No half marks.

Answer distribution: of the 50 single-answer questions, A is correct 13 times, B 12, C 12, D 13.
Across the 10 select-two questions each letter is correct 5 times.

---

## Score sheet

| Domain | Questions | Your score | Out of | Floor (60%) |
|---|---|---|---|---|
| D1 — Agentic Architecture | 11–13, 31–38, 53–57 | | 16 | 10 |
| D2 — Tool Design & MCP | 1–6, 39–42, 58 | | 11 | 7 |
| D3 — Claude Code Config | 7–10, 16–23 | | 12 | 8 |
| D4 — Prompt & Structured Output | 24–28, 46–52 | | 12 | 8 |
| D5 — Context & Reliability | 14, 15, 29, 30, 43–45, 59, 60 | | 9 | 6 |
| **Total** | | | **60** | **43 to pass** |

---

## Scenario A — Developer Productivity

**1 — C.** No literal string to search for: three candidate names all failed, so the target is a
*concept*. That is semantic search. If the question had printed the string, it would be Grep.

**2 — A.** The question prints the exact string, so Grep. Glob only matches file paths, never file
contents.

**3 — D.** When Edit cannot match unique text, the answer is Read the file and Write it back. A and
B change the file by other means to make Edit work, which is more work than Write.

**4 — A and C.** Two requirements, two answers. Shared with everyone who clones → `.mcp.json` in
the repository. Secret must stay out of version control → `${JIRA_TOKEN}` expansion. The personal
experimental server belongs in `~/.claude.json`, which is why B is wrong for the *Jira* server.

**5 — B.** A `mode` enum is an overloaded tool. Split it into purpose-specific tools, each with its
own contract. A is the trap: reducing six modes to three keeps the overloaded design and only
shrinks the number of wrong choices.

**6 — D.** Grep to find entry points, Read to follow imports, repeat. Reading everything first
fills the context with material that is mostly irrelevant.

**7 — B.** The conventions apply to one folder and nothing outside it. That is exactly what a
directory-level CLAUDE.md covers. C is the trap: `paths: ["**/*.ts"]` would apply the billing
conventions to every TypeScript file in the monorepo.

**8 — C.** Two different requirements in one question. Always applies everywhere → the root
CLAUDE.md. The maintainer picks which of the rest apply, with no duplication → `@import`. Skills
must be **invoked**, so they can never hold standards that apply automatically. D duplicates the
text, which the question forbids.

**9 — A.** `argument-hint` asks the developer for a missing parameter. `paths` is not a SKILL.md
key at all — it belongs to `.claude/rules/`.

**10 — D.** `/compact` reduces context usage inside a running session. `/memory` only shows which
memory files are loaded, and both resume options would end the current session.

**11 — B.** One shared analysis, two branches to compare — that is `fork_session`. Parallel Task
calls (A) would start two subagents that inherit nothing, so neither would have the analysis.

**12 — A.** Most of the earlier context is now wrong, so resume would carry stale tool results.
Start fresh with a written structured summary. Note this is the *opposite* of the case where a few
named files changed inside an otherwise valid analysis — there, resume and name them.

**13 — C.** Subagents inherit nothing: no conversation history, no memory between calls. Anything
they need must be written into the prompt.

**14 — D.** Crash recovery is manifests: each agent writes its state to a known location, and the
coordinator loads it when work resumes. Scratchpads (C) address context degradation, which is a
different problem.

**15 — B and D.** Two symptoms, two layers. No context space left for the final agent → change the
**earlier** agents to return structured data instead of long prose. Readers cannot judge the
evidence → coverage annotations marking what is well supported and where the gaps are. A is the
bigger-window answer; C destroys more detail.

---

## Scenario B — Claude Code in CI

**16 — A.** A pipeline that hangs waiting for input needs non-interactive mode: `-p` / `--print`.
`--no-interactive` and `CLAUDE_HEADLESS` do not exist, and redirecting stdin is not the documented
fix.

**17 — C.** `--json-schema` is real. `--batch`, `CLAUDE_HEADLESS=true` and a `commands` list in
`.claude/config.json` are all invented options the exam reuses.

**18 — B.** CLAUDE.md is how Claude Code learns the project when it runs in CI: testing standards,
fixture conventions, review criteria. Supplying the existing test files is what stops it suggesting
tests that already exist. A works but re-injects the same text on every run instead of storing it
where the tool already looks.

**19 — D.** A session that wrote the code remembers why, so it does not question its own decisions.
Use an independent instance. C is voting across runs, which suppresses real findings.

**20 — A.** One file, a clear stack trace, one obvious fix — direct execution. B over-applies plan
mode; C is the "switch later" trap, which is only wrong when the complexity is already known, and
here there is none.

**21 — C.** The interview pattern: in an unfamiliar area, let Claude ask the questions first so it
raises what you had not considered. Plan mode designs against a specification, and the problem here
is that the engineer does not yet have one.

**22 — B.** Problems that affect each other go in one detailed message. Independent problems are
fixed one at a time.

**23 — D.** `allowed-tools` limits which tools a skill may use. B is invented — hooks are not
declared in skill frontmatter.

**24 — A.** Specific, testable criteria beat vague ones. "Be conservative" and confidence
thresholds do not improve precision, and a classifier is over-engineering before prompt work has
been tried.

**25 — B and D.** Two complaints, two fixes. One noisy category destroying trust in the others →
disable it while its prompt is improved, keep the rest running. Inconsistent severity labels →
define each level with concrete code examples.

**26 — B.** This is the one place confidence is allowed: reported **next to** a finding, so a human
reviewer can triage. It is not allowed as a **filter** on what gets reported (A, C) or as a licence
for the system to act alone (D).

**27 — A and D.** Two symptoms of attention dilution on a large review: inconsistent depth and
contradictory findings between files. The fix is both halves — one pass per file **and** one pass
across files. B is the bigger-window answer; C hides real bugs.

**28 — C.** `detected_pattern` records which code pattern triggered each finding, so you can later
see which patterns developers dismiss.

**29 — D.** The API is stateless. The full conversation history goes with every request. There is
no server-side session to enable.

**30 — A and B.** Two failures described. A silent empty result hides the error → return structured
error context instead. One tool failure aborting everything → continue with the remaining checks
and mark what was not covered. C is the hidden error the question is complaining about; D is
stopping the whole workflow.

---

## Scenario C — Customer Support

**31 — B.** Several services returning different formats is the textbook `PostToolUse` case: the
hook normalises every response **before the model sees it**. D fixes it after the conversation, by
which point the agent has already quoted wrong dates.

**32 — D.** No money, no identity, no policy limit — this is style and judgement, which is exactly
what prompts and examples are for. A, B and C all apply programmatic enforcement to a problem that
does not require it.

**33 — A.** Identity plus "must never" means a prerequisite gate. Prompt text has a non-zero
failure rate, and D repairs the damage after the fact instead of preventing it.

**34 — B and C.** Two symptoms. Running sequentially → issue the Task calls in a **single**
response. Re-establishing known context → put the case facts in each subagent's prompt. D is
invented; subagents share no memory.

**35 — D.** An iteration cap is fine as a safety limit, but `stop_reason` must drive the loop. A
and B promote the safety limit to the mechanism, which is one of the four named wrong ways to stop.

**36 — A.** A good coordinator chooses which subagents to invoke based on the request's complexity.
B is the tempting engineering answer, but running five unnecessary subagents faster is still
running five unnecessary subagents.

**37 — C.** The question names the cause: the coordinator sent only the order ID. Every answer
blaming the billing subagent is wrong, because the question states its output was correct for what
it received.

**38 — C and D.** Two problems, two answers. No usable context for the human → a structured summary
(customer ID, root cause, amount, recommended action). Late escalation → escalate immediately when
the customer explicitly asks. A is a raw dump rather than a summary; B is sentiment, which is never
a valid signal.

**39 — A.** The caller lacks access. That is **permission**: not retryable, escalate or explain.

**40 — C.** Subagents fix transient failures themselves and report only what they cannot fix — with
what they tried and any partial results.

**41 — B.** `auto` means the model **may** answer with text instead of calling a tool. That is why
`auto` is never the fix when the model keeps replying with prose. `any` forces a tool call.

**42 — D.** Expanded descriptions have already been tried and the tools genuinely overlap, so the
next step up the ladder is renaming and rewriting to make the boundary explicit, splitting the
general tool into purpose-specific ones.

**43 — C.** The policy does not cover the case. A policy gap is one of the three valid reasons to
escalate. Deciding it yourself (A or B) invents policy.

**44 — A.** The customer has **not** asked for a human, and the agent can solve the problem.
Acknowledge, offer to resolve, escalate only if they ask. B and C escalate on sentiment, which is
never valid — anger does not measure case difficulty.

**45 — B.** Match the format to the content: tables for financial data, prose for narrative,
structured lists for technical findings. Forcing everything into one format loses meaning.

---

## Scenario D — Structured Data Extraction

**46 — D.** The source **always** contains the value and the failure is **omission**, so `required`
is the guarantee you want. A is the classic trap — it keeps the fabrication risk and adds
rejections on top.

**47 — B.** Inconsistent handling of ambiguous cases is the textbook few-shot problem: two to four
examples, aimed at the unclear cases. C over-shoots the count; the examples are meant to let the
model generalise, not to enumerate every phrasing.

**48 — C.** "Must never" plus a regulatory threshold means programmatic enforcement. Few-shot
examples and prompt instructions are still probabilistic.

**49 — A.** Tool use with a schema removes **syntax** errors. It cannot make the content correct —
a value in the wrong field is valid JSON.

**50 — B and C.** Resubmit only the failures, found by `custom_id`, splitting the over-long
documents first. And test the revised prompt on a small sample before committing to another large
batch. A wastes 96% of the work; D abandons the cost saving for documents nobody is waiting on.

**51 — A.** Worst case is the gap between submissions plus up to 24 hours of processing. A 36-hour
SLA allows a gap of at most 12 hours. Every 8 hours gives 32 hours worst case. C gives 42 and D
gives 48.

**52 — D.** The source **may not** contain the value and the model is inventing one, so optional
and nullable. Read this together with Q46 — same rule, opposite directions, both correct answers on
this exam.

**53 — C.** The file list is known and the criteria are fixed, so the shape of the work is known
before starting: prompt chaining, one pass per file plus one pass across files. D drops the
cross-file pass, which is where data-flow issues and contradictions are found.

**54 — A and D.** Two requirements, two hooks. Different formats arriving → `PostToolUse`
normalisation before the model reads them. Must never auto-submit above a threshold → tool call
interception blocking the call. C reverses records after they reach the ERP, which is not the same
as never sending them.

**55 — B.** Quality degrading across a long single pass is attention dilution. Split into focused
passes plus one across the set. A larger context window does not improve attention quality.

**56 — A.** Every subagent extracts correctly from what it receives, and the output is still
incomplete. That combination always points at the coordinator's routing and decomposition.

**57 — D.** Every `tool_use` needs a matching `tool_result` with the same `tool_use_id`, including
failures, and all results from one assistant message go back in **one** user message.

**58 — C.** Malformed input is **validation**: correct the input, then retry. A plain retry of the
identical call would fail again, which is what separates validation from transient.

**59 — A and C.** A high average can hide one document type or one field failing badly → analyse by
type and field. And sample the **high-confidence** group specifically, because that is the group
review would stop covering, so its true error rate is the only one that matters. B averages harder;
D trusts the confidence scores you are trying to validate.

**60 — B.** Sources were unavailable, so the report must say which findings are well supported and
which topics have gaps. A blocks the report on systems that may not return; C and D hide the gap
from the reader.

---

## What this set is testing

Mock 2 was written against one specific failure: answering on recognition rather than reasoning.
Three deliberate traps recur.

1. **The defensible late fix.** Q46, Q52, Q54, Q60 and others all offer an answer that repairs the
   symptom downstream — a post-processing layer, a validation rule, a reversal after submission, a
   retry. Ask instead which component was holding the information at the moment it was lost.
2. **The plausible feature that does not exist.** Q16, Q17, Q23, Q29, Q34 each offer one. Deleting
   these on sight costs no knowledge of the subject.
3. **The rule running backwards.** Q7 (directory CLAUDE.md, not glob rules), Q12 (fresh, not
   resume), Q20 (direct execution, not plan mode), Q46 and Q52 (required *and* nullable), Q44
   (do not escalate) and Q53 (chaining, not dynamic) all invert the version most practice sets
   show. If you learned the shape rather than the rule, these are where it shows.
