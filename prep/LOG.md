# Progress Log

**Purpose:** so any future session — with me or with a different assistant — can see where you
are in about 30 seconds, without you having to explain again.

**How to use it:** after each study session, add a line to *Session history*. Update *Where I am
now* and *Scores*. Keep it short. One or two sentences is enough.

---

## Where I am now

| | |
|---|---|
| **Exam** | Claude Certified Architect – Foundations (CCAR-F) |
| **Exam date** | Tuesday 25 August 2026 |
| **Booked?** | ☑ **booked 11 Aug**, for Tue 25 August |
| **Study period** | Monday 10 August – Monday 24 August (15 days) |
| **Current day** | Day 2 of 15 — Tue 11 Aug. Domains 1 and 2 both drilled, ahead of schedule |
| **Next session** | Domain 3 — the memorisation domain. Also: work through `AUDIT.md` |
| **Study time** | About 2 hours per day |

---

## Scores

| Date | Test | Score | Notes |
|---|---|---|---|
| 8 Aug | Set 1 (20, cold) | **11/20** | D1 2/3 · D2 2/2 · D3 4/6 · D4 **1/5** · D5 2/4 |
| 10 Aug | Domain 1 drill (15) | **10/15** | Missed Q7, Q9, Q13, Q14, Q15. Taken before the rebalance — see note below |
| 10 Aug | D1 ad-hoc set (15) | ~~10/15~~ | **Void.** 14 of 15 answers were B. Discarded |
| 10 Aug | D1 ad-hoc set, balanced (10) | **10/10** | Cleared both traps missed earlier: unknown-scope decomposition, and resume-vs-fresh |
| 11 Aug | Domain 2 drill (15) | **14/15** | Missed Q15 (Grep/Glob/semantic). Taken before the rebalance — 12 of 13 singles were B, so treat as ~12 |
| 11 Aug | D2 ad-hoc set, balanced (15) | **13/15** | Missed Q1 (error category), Q10 (tool granularity) |
| 11 Aug | D2 ad-hoc set, balanced (10) | **7/10** | Rushed — read the questions too fast. Missed Q2, Q4 (half), Q10 |
| 11 Aug | D2 ad-hoc set, balanced (10) | **9/10** | Missed Q7 (`tool_choice` values). Error categories and search triad all clean |
| 12 Aug | `/cert-exam 15` — D2 | | |
| 14 Aug | `/cert-exam 15` — D3 | | |
| 15 Aug | Domain 3 drill (15) | | |
| **16 Aug** | **Mock 1 — `/cert-exam 60`, timed** | | Record the score for every domain |
| 17 Aug | `/cert-exam 15` — D4 | | |
| 18 Aug | Domain 1 drill — **retake** | | Compare with 11 Aug |
| 19 Aug | Domain 4 drill (15) | | |
| 20 Aug | `/cert-exam 15` — D5 | | |
| 21 Aug | Domain 5 drill (15) | | |
| 22 Aug | Domain 2 + 3 drills — **retake** | | |
| **23 Aug** | **Mock 2 — Purcell's 60, timed** | | The rehearsal. Take it cold |

**Target before the exam:** 80%+ on practice sets, and no domain below 60%.

**On the retakes:** the score matters less than *which* questions you miss twice. A question
missed twice is a fact you have not learned. Put it on the cheat sheet.

---

## What I know about my own weak points

Updated as evidence appears. Right now, from Set 1 only:

1. **Domain 4 is the big gap — 1 out of 5, on 20% of the exam.**
   Three of the four misses were flat facts: `tool_choice` values (`auto` allows text),
   required schema fields causing invented values, and which errors a retry can fix.
   → Fixed by `daily-facts-domain-4.md`, 5 minutes every day.
   The fourth (Q17, voting across passes) was applying a rule too widely — see point 2. So the
   Domain 4 gap is not pure recall.

2. **Applying a rule too widely.** Chose plan mode for a single-file fix (Q12). Chose voting
   across review passes (Q17), which is on the "never correct" list.
   → Re-read `01-answer-patterns.md`.

3. **Mechanism confusion.** Mixed up `fork_session` with parallel Task calls (Q8). Blamed the
   wrong component when the question named it (Q5).

4. **The escalation trap (Q3).** A customer who explicitly asks for a human = escalate
   immediately. A customer who is frustrated but can be helped = offer help first.
   These two look similar and the exam uses that.

**What is already working:** structured error design, programmatic enforcement vs prompting,
two-layer context management, conflicting sources, batch vs real-time. The architecture reasoning
is sound. The gap is recall.

### Added 10–11 Aug, from the Domain 1 and 2 drills

5. **Rules stored where the guide has a threshold.** Three Domain 1 misses were all this shape:
   *stale → fresh session* (it is actually "how much is stale"), *audit → per-file passes* (it is
   actually "do I know the shape before I start"), and `!= end_turn` *→ continue* (it is actually
   "continue only on `tool_use`"). Each rule works most of the time, which is why it sticks.
   → Convert each into a question you ask the scenario. All three came out clean afterwards.

6. **Stopping at the first correct answer on select-two questions.** Happened three times.
   → Reliable tell: **if the scenario names two distinct symptoms, the two answers map onto
   them.** One answer cannot be complete.

7. **Error categories decided by feel rather than by test.** Two misses. The test, in order:
   did the system fail and might a retry succeed → *transient*; is the input malformed →
   *validation*; input and system both fine but a rule says no → *business*; caller lacks access
   → *permission*. Only transient is retriable.

8. **Grep / Glob / semantic search.** Missed three times before it stuck. **Glob = file paths.
   Grep = text you can spell exactly. Semantic = concepts with no literal to search for.**
   If the question prints the string you are looking for, it is Grep.

9. **`tool_choice` values.** `auto` = may call a tool *or answer directly*. `any` = must call
   some tool, model picks which. `{"type": "tool", "name": ...}` = must call that one.
   "any" reads like "anything permitted"; it means "one of them, mandatory."

**Confirmed strong in Domain 2:** programmatic enforcement, scope partitioning vs iterative
refinement, MCP resources vs tools, `.mcp.json` vs `~/.claude.json`, `${VAR}` expansion,
community vs custom servers, local recovery vs reporting upward.

---

## Session history

| Date | What happened |
|---|---|
| 11 Aug | **Booked the exam for Tue 25 August.** Built the Domain 5 drill (15 questions, all six task statements, balanced key) — every domain now has a drill. |
| 11 Aug | Cross-checked Purcell's 60-question set and the official exam guide (both PDFs were already in the folder). Purcell's answer key agrees with this repo's material on **all 60 questions** — zero contradictions, though topical overlap is heavy since both are written against guide v1.0. The guide adjudicated every remaining docs-drift item in `AUDIT.md` in the notes' favour; annotations added, `stop_reason` count corrected to seven, `AUDIT.md` is now fully closed. Bonus finding: the guide itself uses both `isRetryable` and `retriable` in the same task statement — the origin of the spelling inconsistency. |
| 11 Aug | A second review independently confirmed every verified `AUDIT.md` finding, then applied the fixes: the `--json-schema` contradiction, one spelling for the retriable field (`isRetryable`), the Set 1 blueprint header, the Domain 4 miss count (four, not three — in four files, including this one), the resume-vs-fresh "how much is stale" qualifier (now also on the cheat sheet and revision card), required-vs-nullable, Scenario 4's missing Domain 5, the fourth wrong-way-to-stop (`task_complete`), and the `PreToolUse` name. All three PDFs regenerated. Docs-only items 3a–3e/3g/3h left for a session with the exam guide open. |
| 11 Aug | Domain 2: took the repo drill (14/15) then three balanced ad-hoc sets (13/15, 7/10, 9/10). **Discovered a severe answer-key bias in all five practice files** — 56 of 66 single-answer questions were B and D was never correct, so "always answer B" scored 56/66. Rebalanced every file and verified no option text changed. Ran a full audit of the material for contradictions and factual drift → **`AUDIT.md`**, nothing fixed yet. |
| 10 Aug | Domain 1: took the repo drill cold (10/15), reviewed the whole domain by mental model rather than fact list, then 10/10 on a balanced ad-hoc set. Three weak spots identified and closed — see weak points 5–7 above. |
| 10 Aug | Reviewed Matthew Purcell's LinkedIn exam review and his 60-question practice set. Confirmed three earlier calls (Bedrock/Vertex out of scope, Claude 101 and AI Fluency too basic, exam is memorisation-heavy). Downgraded the scenarios from "study" to "skim once". Adjusted exam-day timing. His set replaces the mock I was going to write for 23 Aug. |
| 8 Aug | Identified two different exams (CCAR-F vs CCAR-P) and chose Foundations. Confirmed Foundations is accepted for Intertec partner tier. Built the full prep folder. Took Set 1 cold: 11/20. Converted everything to simple English. Found and installed the community 77-question practice exam as `/cert-exam`. Pushed everything to GitHub. |

---

## Still to be built

| Needed by | What |
|---|---|
| ~~19 Aug~~ | ~~Domain 4 drill~~ — **built 10 Aug** |
| ~~21 Aug~~ | ~~Domain 5 drill (15 questions)~~ — **built 11 Aug.** Balanced key, covers all six task statements, deliberately avoids Purcell's D5 framings so the 23 Aug mock stays cold |
| ~~Before revision day~~ | ~~Work through `AUDIT.md`~~ — **fully closed 11 Aug.** Verified items fixed, docs-drift items adjudicated against the exam guide (the notes matched the guide on every row), annotations added, PDFs regenerated |

~~23 Aug: full mock~~ — **no longer needed.** Matthew Purcell's 60-question practice set
(`1784098676646.pdf`, kept locally, not in the public repo) replaces it. Written by someone who
passed CCAR-F, blueprint-weighted, and it includes 11 multiple-response questions.

---

## External resources

| Resource | What it is | When |
|---|---|---|
| `/cert-exam` | 77 community questions by Olivier Legris, installed as a Claude Code skill. Single-answer only | Daily, 15 at a time |
| `1784098676646.pdf` | Matthew Purcell's 60-question set. Blueprint-weighted, 11 multiple-response, answer key with rationales. **Cross-checked 11 Aug: zero contradictions with the repo material.** Caveat: heavy topical overlap with the repo drills (same guide, same scenarios), so a high mock score partly reflects repetition — weight the domains you haven't drilled recently | **23 Aug only** — take it cold |
| Matthew Purcell's LinkedIn review | He passed all four exams. Confirms: Bedrock/Vertex not tested, Claude 101 and AI Fluency too basic, CCAR-F is the hardest of the four, scenarios are "dressing", finished in 90 of 120 min | Read once |
| Paul Larionov's GitHub repo | A study guide Purcell recommends. **Not yet evaluated** | Optional |

**To check:** Purcell reports a 100% exam discount for Global Premier partners until 31 Aug 2026.
The exam is 25 Aug, inside that window. Ask Intertec whether it is free.

---

## Decisions already made — do not revisit

- **Foundations (CCAR-F), not Professional (CCAR-P).** Confirmed as accepted for partner tier.
- **Skip the Bedrock and Google Cloud courses.** Cloud provider configuration appears exactly
  once in the 39-page guide, in the out-of-scope list.
- **Skip AI Fluency and Claude 101.** Level 100, below this exam's candidate profile.
- **Take:** Claude Code in Action (covers Claude Code *and* the Agent SDK), Intro to MCP, and
  only the tool use / prompt engineering / agents modules of Building with the Claude API.
- **The official exam guide PDF is not pushed to GitHub.** It is Anthropic partner material and
  the repository is public. It is in `.gitignore`. The same applies to Purcell's practice set —
  it is his copyrighted work.
- **The scenarios are context, not content to memorise.** A candidate who passed calls them
  "more dressing than anything substantive". Skim them once; do not study them.

---

## Useful context for a new session

- Write in plain English. English is not my first language. Keep exact exam terminology.
- Explanations in simple English; **practice questions stay at exam-level English on purpose**,
  because reading that style quickly is part of the test.
- Background: medical doctor, now in product and program management. Comfortable with
  architecture reasoning and trade-offs; less comfortable with backend implementation. This exam
  does not test backend implementation — Section 17 of the guide excludes it.
- Files are mirrored at **github.com/abracadaniel92/claude_architect_exam**.
