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
| **Current day** | Day 5 of 15 — Fri 14 Aug. **All five domains covered and above target**, seven days ahead of the plan |
| **Next session** | Sat 15 Aug — `/cert-exam 15` on D4 and D5. Independent questions, not written from these notes. Then Mock 1 on 16 Aug, timed and cold |
| **What is still untested** | Retention across a gap · 60 questions in 120 minutes · questions not derived from these notes. See weak point 21 |
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
| 12 Aug | Mixed D1+D2 set (15, balanced) | **12/15** | D1 8/9 · D2 4/6. Missed Q4 (tool granularity), Q11 (decomposition threshold), Q13 (semantic search). **All three are repeat misses** — see weak point 10 |
| 12 Aug | `/cert-exam 15` — D2 | | |
| 12 Aug | **Domain 3 drill (15)** — pulled forward from 15 Aug | **13/15** | Missed Q2 (`@import` — 2nd time) and Q12 (gave one answer where two were asked). Memorisation core clean: all paths, frontmatter keys and flags correct |
| 14 Aug | `/cert-exam 15` — D3 | | |
| 14 Aug | D5 ad-hoc set, balanced (15) | **14/15** | Missed Q4 only (subagent metadata — chose *both* wrong options). Both escalation directions clean in one sitting |
| 14 Aug | D4 ad-hoc set, balanced (15) | **13/15** | Missed Q6 (required-vs-nullable, reverse direction) and Q11 (format normalisation in the prompt). Both are Block A schema facts. All three select-twos clean |
| 14 Aug | Mixed D1+D2+D3 set (20, balanced) | **17/20** | D1 6/8 · D2 **6/6** · D3 5/6. Missed Q1 (stopping the loop on "text and no tool_use"), Q5 (one answer where two were asked — **5th time**), Q15 (`@import` — **3rd time, same wrong answer as 12 Aug**) |
| ~~15 Aug~~ | ~~Domain 3 drill (15)~~ — **taken 12 Aug** | | Retake on 22 Aug as planned |
| **16 Aug** | **Mock 1 — `/cert-exam 60`, timed** | | Record the score for every domain |
| 17 Aug | `/cert-exam 15` — D4 | | |
| 18 Aug | Domain 1 drill — **retake** | | Compare with 10 Aug (10/15, pre-rebalance). First honest score on these questions |
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

1. ~~**Domain 4 is the big gap — 1 out of 5, on 20% of the exam.**~~ **Largely closed 14 Aug
   (13/15).** Kept here because the diagnosis below still explains what to keep doing — see
   weak points 16 and 17 for what remains.
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

### Added 12 Aug, from the mixed D1+D2 set (12/15)

10. **Three facts are now missed twice or more. These are the cheat-sheet items.**

    | Fact | Missed | Now on the cheat sheet as |
    |---|---|---|
    | Chaining vs dynamic decomposition | **3×** (10 Aug, and Q11 here) | "Do I know the shape before I start?" — with the note that *audit / large / comprehensive do not decide it* |
    | Grep / Glob / **semantic** | **4×** | "If the question says you do not know what it is called → semantic" |
    | Tool granularity (`mode` enum → split) | **2×** | "Merging the modes into fewer modes is the wrong answer" |

    On Q11 the material was partly at fault: the cheat sheet had **no** chaining-vs-dynamic entry
    at all, and its one line on the subject ("large review → one pass per file") sat in the
    Domain 4 section with no qualifier, priming exactly the wrong answer. Fixed 12 Aug in both
    the cheat sheet and the revision card.

    **Evidence the rule itself is known:** Q12 (same rule, known 22-file list) was correct in the
    same sitting. What fails is the discriminator, not the rule.

**What is working:** all three select-two questions clean. Weak point 5's resume half is closed
too (Q10 correct, the exact trap that cost a mark on 10 Aug). `fork_session` vs parallel Task
calls clean (Q6), so weak point 3 is closing.

### Added 12 Aug, from the Domain 3 drill (13/15)

11. **Weak point 6 is improved but NOT closed — this is now its 4th occurrence.**
    Domain 3 Q12 asked for two answers and got one. Three of the four multi-answer questions in
    that drill were right, and all three were right in the mixed set earlier the same day, so the
    habit is mostly there. But the failure mode has not changed shape once.
    → **Exam-day rule: before answering any question, look at whether it says "select two".**
    If it does, count the symptoms in the scenario, then check you have one answer per symptom.
    Do this as a mechanical step, not as a judgement.

12. **`@import` is a positive rule that has not anchored — missed twice.**
    Set 1 Q9 and Domain 3 Q2 are the same decision. The improvement: the old wrong answer
    (path globs) was correctly rejected this time; a new wrong answer (skills) replaced it.
    → **`@import` = the maintainer selects which shared documents apply, with no duplication.**
    Skills must be **invoked**, so they can never hold standards that must always apply.
    Path globs are for conventions that follow **file type across many folders**.

### Added 14 Aug, from the mixed D1+D2+D3 set (17/20)

13. **`@import` is now missed three times, twice with the same wrong answer (skills).**
    This is the most reliable predictor of a lost mark in the whole repo. The pattern of the miss
    has stabilised: the wrong answer is always *skills*, chosen because the question describes a
    person **choosing** which documents apply, and "choosing" feels like "invoking".
    → **The discriminator is WHO chooses and WHEN.** `@import`: the *maintainer* chooses once,
    when writing the file, and the content then loads **always**. A skill: the *model or
    developer* chooses at run time, every time, and the content loads **only when invoked**.
    If the question says the standards must apply to all work in that package, a skill cannot
    do it — no matter who selected it.

14. **A new shape of weak point 5: substituting an inference for the actual signal.**
    Q1 chose "exit when the response has a text block and no `tool_use` blocks". That condition
    is *usually true* at the end of a turn, which is exactly why it is attractive — same failure
    shape as the three misses in weak point 5. But the guide names "checking whether the response
    contains text" as one of the four wrong ways to stop.
    → **The loop reads `stop_reason` and nothing else.** Inspecting block types is a proxy, and
    the exam offers proxies as wrong answers on purpose. Note the second half of the trap: the
    replacement in the question was *also* wrong (`task_complete`), so the question was testing
    whether you would swap one wrong mechanism for another.

15. **Weak point 6 is at its 5th occurrence — but the failure has moved.**
    Q5 was answered with one letter; Q10, Q14 and Q20 were all answered with two, correctly.
    So the counting habit works when the two symptoms are *the same kind of thing*. Q5's two
    symptoms were different kinds — a policy breach and a data-format problem — and the second
    one was found while the first was dropped.
    → **Extend the exam-day rule:** after finding one answer, do not ask "is this right?" but
    "which symptom did this answer solve, and what solves the other one?"

### Added 14 Aug, from the D4 ad-hoc set (13/15)

16. **Domain 4 is no longer the weakest domain — 1/5 cold on 8 Aug, 13/15 now.**
    Everything the daily fact drill targets came out clean: `tool_choice`, the batch table
    (including no multi-turn tool calling), what a retry request contains, few-shot count and
    targeting, and both confidence traps in the same sitting — confidence **next to** a finding
    for triage is correct, confidence as a **filter** on what gets reported is not.
    → Keep the daily drill running; do not declare this closed until the 16 Aug mock agrees.

17. **Both misses were Block A schema design, and both were the same error: taking a rule in one
    direction only.**
    - *Required vs nullable.* The learned rule is "required makes the model invent values → use
      nullable". The scenario was the reverse case — a machine-generated document that **always**
      contains the field, where the failure was the field being **omitted**. The answer is
      **required**. The chosen answer, "nullable plus a validation rule rejecting null", gets the
      failure mode of required with none of the guarantee.
      → **Discriminator: does the source always contain this value?** Yes → required. Might not →
      nullable. Both are correct answers on this exam. Added to the cheat sheet and revision card.
    - *Format normalisation.* Chose a post-processing layer over normalisation rules in the
      prompt. Defensible engineering, wrong exam answer. → **The schema fixes the type, the prompt
      fixes the format.** The cheat sheet was missing this line entirely — the revision card had
      it, the cheat sheet did not. Fixed. Same class of material gap as the one Q11 exposed on
      12 Aug, so re-check the two files against each other rather than assuming they match.

    Note what this is **not**: Q3 (`"unclear"`) and Q9 (`conflict_detected` plus extracting both
    readings) came from the same block and were right. It is two specific rows, not the block.

18. **Weak point 6 is clean twice running.** All three select-two questions correct here, after
    3 of 4 on 14 Aug's mixed set. The mechanical "count the symptoms" step is working, including
    on Q14, where the two symptoms were **different kinds** — the shape that failed on 14 Aug.

### Added 14 Aug, from the D5 ad-hoc set (14/15) — and this is the one to carry to the exam

19. **All five domains are covered, and one error shape now accounts for every recent miss:
    repairing a symptom downstream instead of requiring the right structure upstream.**
    Three misses across 30 questions, in three different domains, all the same:

    | Domain | The failure | Chose (late fix) | Correct (early fix) |
    |---|---|---|---|
    | D4 | A field the source always has goes missing | nullable + reject null | **required** |
    | D4 | Dates and currency arrive inconsistent | a post-processing layer | **normalisation rules in the prompt** |
    | D5 | Synthesis cannot judge a source's age or type | re-fetch at synthesis; weigh credibility | **subagents record dates, location, methodology** |

    Every late fix is **defensible engineering**, which is exactly why it is offered. The exam is
    testing whether you locate the component that held the information at the moment it was lost.
    → Now step 6 of the 30-second method, in the cheat sheet and on the revision card.

    **Note the failure mode on D5 Q4:** both selected answers were wrong, and both mapped cleanly
    onto the two symptoms in the scenario. So the select-two counting habit worked and produced
    two answers from the wrong family. Counting symptoms and judging content are separate steps;
    the first being right says nothing about the second.

20. **Domain 5 is covered: 14/15, with both escalation directions correct in one sitting.**
    No progress possible + calm customer → escalate (Q2). Explicit request for a human mid
    investigation → escalate **immediately**, do not finish the diagnosis first (Q13). Criteria
    plus few-shot rather than a classifier (Q8). The Set 1 escalation trap is closed. Q15 was an
    over-application trap — a vague answer in a *fresh* session, where nothing has degraded and
    the agent simply never read the file — and it was not taken, which is weak point 2 improving.

21. **Read the two 14 Aug scores with their caveat.** Both sets were written from these notes and
    taken in the same sitting as the review, so they measure recall at zero delay from material
    just read. The cold numbers are still Set 1 (11/20) and whatever Mock 1 returns. More
    generally: every question answered well so far traces back to one source — these notes, from
    guide v1.0, and questions written from these notes. **Purcell's set is the only independent
    measure, which is the strongest argument for keeping it sealed until 23 Aug.**

---

## Session history

| Date | What happened |
|---|---|
| 14 Aug | Domain 5 straight after Domain 4: 15 new questions, balanced key, all six task statements, avoiding `drill-domain-5.md` so it stays cold for 21 Aug. **14/15** — one miss. **All five domains are now covered, seven days ahead of the plan.** Reworked the calendar from 15 Aug onward: the four days reserved for domains already finished go to independent question sources and timed practice instead, because coverage is no longer the gap — independence of source and time pressure are. Added weak points 19–21; 19 is the one to carry to the exam and is now step 6 of the 30-second method. |
| 14 Aug | Started Domain 4, the weakest domain. Ad-hoc set of 15 new questions, balanced key, all six task statements, deliberately avoiding the framings in `drill-domain-4.md` so that drill stays cold for 19 Aug. **13/15** — up from 1/5 cold on 8 Aug, and above the drill's own "done with this domain" bar. Both misses were Block A schema design, both the same shape: applying a rule in one direction only (weak point 17). Fixed the cheat sheet, which stated "make it optional and nullable" with no qualifier and had no format-normalisation line at all; the revision card had the second but not the first. Both regenerated. |
| 14 Aug | Mixed set across all three completed domains: 20 new questions, blueprint-weighted, balanced key. **17/20** (D1 6/8, D2 6/6, D3 5/6) — clears the 80% target with every domain above the floor, and Domain 2 is now clean twice running. All three misses were traps aimed at the repeat-miss list: `@import` (3rd time, same wrong answer as 12 Aug), a select-two answered with one (5th time, but 3 of 4 select-twos were right), and a *new* variant of weak point 5 — stopping the loop on "text and no tool_use" instead of on `stop_reason`. Weak points 13–15 added. Notable: Grep-vs-semantic and tool granularity, both long-running repeat misses, were correct when asked from the reverse direction. |
| 12 Aug | Domain 3 drill, pulled forward from 15 Aug: **13/15**, clearing the drill's own "done with this domain" bar. The memorisation core — file paths, frontmatter keys, CLI flags — was fully clean, which is the bulk of this domain. Two misses, both recurrences: `@import` (2nd time) and a select-two answered with one answer (4th time). Added two things to the cheat sheet in response: a "which mechanism holds which content" table, and a mechanical select-two check. |
| 12 Aug | Confirmation set before starting Domain 3: 15 mixed D1+D2 questions, balanced key, all new. **12/15** (D1 8/9, D2 4/6) — clears the 80% target with both domains above the 60% floor. The three misses were all repeat misses, so they went onto the cheat sheet; one of them (decomposition) exposed a real gap in the cheat sheet itself, now fixed. Select-two habit confirmed closed. Cleared to start Domain 3. |
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
