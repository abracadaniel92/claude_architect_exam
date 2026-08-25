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
| **Result** | **PASSED — 787 / 1000. Tuesday 25 August 2026.** Claude Certified Architect – Foundations. Fifteen days of prep, nine repo mocks plus Purcell’s set, from 11/20 cold on 8 Aug to a pass on the first attempt. |
| **How the real paper differed** | **Reported straight after the exam, and it is the most important line in this file for anyone reusing it.** The real items were **much longer, deliberately vaguer, and dense with traps** — nothing like this repo's papers, which are short, clean and single-trap by construction. The closest analogue of the three sources examined is **`claudecertificationguide.com/learn`**; Purcell's set and both GitHub repos are further away, and this repo's own mocks are the furthest. **Nine mocks at 95–98% did not predict the item style at all** — they predicted the *content*, which is why the pass was comfortable. Read weak point 47 as understated: the papers were not merely non-independent, they were **the wrong shape**. See also re-cinq's account (found 25 Aug): *the biggest gap between mock and real was the wording, not the difficulty — longer sentences with key qualifiers hidden inside them.* That warning was on file before the exam and was under-weighted |
| **Next session** | None required — the exam is done. Optional tidy-up only: Mocks 8 and 9 are still untracked and the 23 Aug edits to `LOG.md` and the cheat sheet are uncommitted; **Mock 9 has no score recorded** if it was taken; and decide whether the public repo now stands as a finished study guide for the next candidate. |
| **The one thing to change** | **Eye fatigue is skipping items. Break mid-paper, then check the count before submitting.** Three consecutive papers have lost an item this way — Mock 7's Q51–53, Purcell's 4.3, Mock 8's Q24 — and the candidate identified the cause on 23 Aug: the answers were known, the questions were not seen. The skips cluster on **two-paper days** (both 23 Aug papers, and Mock 5 on 20 Aug). **This is not pacing** — a 60-question paper takes 19–23 minutes of the 120, and the densest stems are read correctly every time; what degrades is visual coverage late in a scan. So: **take a two-minute break mid-paper** (there are ~100 unused minutes), **open the review screen before submitting and confirm nothing is blank**, and **do not take a practice paper on Tuesday morning.** See weak point 60 |
| **Outstanding** | ~~Regenerate the revision card~~ — **done 17 Aug, verified 18 Aug.** Both the interview pattern and the CI/CLAUDE.md line are in `tools/make-revision-card.py` and in the regenerated PDF; the log had simply not been updated. Next open item: the **D2 set** named under *Next session*, since neither Mock 4 miss is covered by Purcell's 60 |
| **What is still untested** | **Thirteen facts that appear in Purcell's set and in none of this repo's papers** — `tool_choice` values, **escalation in either direction**, `/compact` as an answer rather than a distractor, severity consistency, plain-text-JSON → tool use, batch resubmission by `custom_id`, re-review duplicate findings, goal-oriented vs rigid subagent prompts, personal command placement, `allowed-tools` as a guarantee, `--resume` in the positive direction, multi-issue single messages, escalation package contents — **ten of the thirteen came out clean on Mock 5**; the three that did not are plain-text-JSON → tool use (now on the cheat sheet), the handoff package and multi-issue handling — **all three were re-tested on Mock 6 the same day and all three came out clean** (Q1, Q59, Q60), so the untested-facts list is now closed · **the two facts that are still live are not on it**: coverage annotations (3 misses, 3 different distractors) and partial-results-vs-false-success. See weak points 47, 55, 56 |
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
| **16 Aug** | **Mock 1 — repo set, 60 questions** | **50/60 (83%)** | D1 13/15 · D2 10/11 · D3 9/12 · D4 9/12 · D5 9/10. All ten misses are on the cheat sheet; six are in warning boxes written on 14 Aug. See weak points 22–24 |
| 16 Aug | **Mock 2 — repo set, 60 questions, reverse-direction** | **46/60 (77%)** | D1 14/16 · D2 **11/11** · D3 **6/12** ⚠ · D4 11/12 · D5 **4/9** ⚠. Below the 80% target, two domains under the floor. Three select-twos answered with one letter. See weak points 30–33 |
| 16 Aug | `/cert-exam 60` — still unused as an independent 60 | | Purcell's set stays sealed for 23 Aug |
| 17 Aug | `/cert-exam 15` — D4 | | |
| **17 Aug** | **Mock 3 — repo set, 60 questions, gap-targeted** | **49/60 (82%)** | D1 13/16 · D2 10/11 · D3 **8/12** (at the floor) · D4 11/12 · D5 7/9. All five domains at or above the floor. **All four D3 misses were mechanism choice; the memorisation core went 8/8.** See weak points 35–39 |
| **18 Aug** | **Mock 4 — repo set, 60 questions, built from the repeat-miss list** | **58/60 (97%)** | D1 **16/16** · D2 **9/11** ⚠ · D3 **12/12** · D4 **12/12** · D5 **9/9**. Select-two 10/10. Both misses in D2: Q28 semantic search (**5th time**) and Q52 business-vs-permission (chose *transient*). First pass 30–40 min, as on every paper — see weak point 53. Every targeted repeat miss clean: format normalisation, manifests ×2, both noun traps, `stop_reason` ×2. See weak points 44–46 |
| 17 Aug | Post-Mock-3 ad-hoc set (20, D3/D5-skewed) | **16/20** | D3 grouping **4/6** · high-confidence sample **2/2** (closed). Missed Q2 and Q4 (the two swapped mechanisms), Q9 (manifests, 2nd time) and Q15 (post-processing layer, **4th time**). **Q6, which asks for the discriminator itself, was correct** — see weak point 40 |
| 18 Aug | Domain 1 drill — **retake** | | Compare with 10 Aug (10/15, pre-rebalance). First honest score on these questions |
| 19 Aug | Domain 4 drill (15) | | |
| 20 Aug | `/cert-exam 15` — D5 | | |
| **20 Aug** | **Mock 5 — repo set, 60 questions, built from the *untested*-facts list** | **48/60 (80%)** | D1 14/16 · D2 10/11 · **D3 6/12** ⚠ · D4 10/12 · D5 8/9. **Select-two 5/10** — worst in the repo after four clean sittings, and **five of the twelve misses are select-two questions**, including Q35 left blank. D3 is back to its Mock 2 number with `@import` and `.claude/rules/` swapped inside one scenario again. Of the thirteen ★ untested facts, **ten were clean** — the three that were not are plain-text-JSON → tool use, the handoff package (blank) and multi-issue handling (half). First pass 30–40 min, the same as Mocks 1, 3 and 4 — so pace is a constant, not a variable (weak point 53). See weak points 48–52 |
| **20 Aug** | **Mock 6 — repo set, 60 questions, reading-discipline paper (D3 block of ten, 10 select-two, 4 inverse-direction)** | **58/60 (97%)** | D1 **16/16** · D2 10/11 · D3 **12/12** · D4 **12/12** · D5 8/9. **Select-two 9/10** — the one loss was half-right, not single-lettered, and no blanks. **All four inverse-direction questions read in the right direction.** Both misses are content: Q14 coverage annotations (**3rd miss**, new distractor — "note the outage in the pipeline log") and Q48 partial-results-vs-empty-result. First pass **18 minutes**. See weak points 54–56 |
| 21 Aug | Domain 5 drill (15) | | |
| **22 Aug** | **Mock 7 — new 72-question paper, all six scenarios in one sitting** | **70/72 (97%)**, corrected — Q51–53 were mistranscribed when first reported and are all correct | D1 12/13 · D2 **11/11** · D3 **14/14** · D4 **18/18** · D5 15/16. **Select-two 9/9**, third clean paper running. **D3 and D4 both clean for the first time on a paper not built from their own repeat-miss lists** — all nine grouping questions correct, including the `@import`-vs-skill and `.claude/rules/`-vs-directory-CLAUDE.md traps, and every CI/extraction fact in D4 including the CLAUDE.md-as-CI-context fact that cost a mark on Mock 2. **Only two losses in 72 questions, both regressions:** `stop_reason: "refusal"` generalised as "not `end_turn`" (3rd occurrence of this exact trap), and a 3-week-stale session resumed instead of restarted (weak point 5, reopened after four clean sittings). Finished in **23 minutes**. See weak point 57 |
| 22 Aug | Domain 2 + 3 drills — **retake** | | |
| **23 Aug** | **Mock 8 — 60 questions, the first paper written without this log open** | **57/60 (95%)** | D1 **16/16** · D2 10/11 · D3 11/12 · D4 **12/12** · D5 8/9. Built from the blueprint objectives and domain notes only, with the **length tell deliberately inverted** (correct answer shortest on 28 of the 50 singles) and a letter-balanced non-rotating key. **Three losses, three different kinds.** Q24 **left blank** — the write-up runs 23, then 25 — which is the **third consecutive paper with a dropped item**. Q42 answered with one letter of two; the omitted letter was *"the subagent retries transient failures itself"*, **the identical omission as Mock 5 Q39**, same position. Q12 the only content miss: confidence calibration lost to a longer, rationale-carrying distractor, on the paper built to punish that heuristic. See weak point 60 |
| **23 Aug** | **Purcell's 60 — the rehearsal, cold and timed** | **59/60 (98%)** recorded; 60/60 reported | D1 **16/16** · D2 **10/11** · D3 **12/12** · D4 **12/12** · D5 **9/9**. **All 11 multiple-response questions correct**, both letters every time. Finished in **19 minutes** (3:45–4:04pm). The one gap is a write-up slip, not a content miss: the answer list skips from 4.2 to a line labelled 4.3 that carries 4.4's correct answer (A), then to 4.5 — one line dropped. **4.3 therefore has no recorded answer; the candidate reports having chosen B, which is correct.** Logged as 59/60 because, unlike Mock 7's Q51–53, there is no written answer to verify. **Treat as an upper bound, per weak point 47**, and see weak point 58 on the key's rotating answer pattern |
| **25 Aug** | **THE EXAM — Claude Certified Architect: Foundations** | **PASSED — 787/1000** | The real thing, first attempt. The number is a scaled score, not a percentage, so it does not sit on the same axis as the mock percentages below — but it lands under them, exactly as weak points 47 and 58 said practice scores would. The honest reading of this table afterwards: the independent papers (Mock 1 83%, Mock 7 97%, Mock 8 95%) were the informative ones, and the papers written from this log measured retrieval of a known list. No domain breakdown recorded. |

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

### Added 16 Aug, from Mock 1 (50/60)

> **Read weak point 29 first. It reframes the other six.** The mock was finished in **under 30
> minutes** of the 120 available — about 30 seconds per question. The misses below are best read as
> what recognition-speed answering produces, not as gaps in knowledge.

22. **Every one of the ten misses was already on the cheat sheet, six of them inside a warning
    box.** This is the most useful thing the mock produced. The material is complete; what fails is
    recall under time. Two consequences:
    → **Stop writing material.** Nothing found here needs a new note, a new table, or a new
    warning. Adding more would dilute the file that already contains the answers.
    → **Change the drill.** Reading the cheat sheet is what has been happening, and the facts are
    not surviving into a question. Cover the right-hand column and say it out loud, and do it on
    the sections that produced misses: §2 (mechanism table), §10 and §14 (step 6), §11 (SLA
    arithmetic), §5 and §6 (loop and subagent mechanics).

23. **Weak point 19 is NOT closed. Both rows of the step-6 table were missed again, with the same
    distractor chosen both times.**

    | | 14 Aug chose | 16 Aug chose | Correct |
    |---|---|---|---|
    | Q47 — field the source always contains | nullable + reject null | **nullable + reject null** | **required** |
    | Q53 — inconsistent dates and currency | post-processing layer | **post-processing layer** | **normalisation rules in the prompt** |

    Identical answers two days apart, both after the warning boxes were written. The rule is
    understood in the abstract — the same idea was applied correctly on Q28 (subagents record dates
    upstream) in the same sitting. What fails is recognising the *shape* of a late fix while
    reading four plausible options.
    → On exam day, before choosing any answer that repairs, validates, post-processes or
    re-fetches: **name the component that was holding the information when it was lost.** If the
    answer you like is not that component, it is the distractor.

24. **`@import` has changed shape, and the Domain 3 mechanism table is now the problem instead.**
    Q32 was the fourth `@import` miss — but the first one where **skills were not chosen**. That
    trap is closed. The wrong answer this time was `.claude/rules/` with `paths` globs. And in the
    very next question, Q33, `.claude/rules/` with globs was the correct answer and the root
    CLAUDE.md was chosen instead.
    → The two mechanisms were **swapped inside one scenario**, so neither fact is missing. They are
    being matched by feel. The discriminator, in one line: **`@import` selects whole documents by
    package · `.claude/rules/` selects by file type across folders.** If the grouping is "which
    package", it is `@import`. If the grouping is "which kind of file", it is a glob rule.

25. **Reaching past the cheap fix — weak point 2, twice, in the strength-ladder direction.**
    Q26 forced `tool_choice` on every turn where the answer was *improve the tool description*
    (level 4 for a level 1 problem). Q41 built a skill where the answer was *two or three concrete
    input/output examples*. Note that Q41 is skills being attractive again, one question after
    correctly rejecting them on Q32.
    → The question said "first" in neither case, so the guard has to be the ladder itself: **choose
    the weakest fix that still meets the requirement, and only climb when money, identity, a policy
    limit, or the words guaranteed / must / never appear.** None of them appeared in Q26 or Q41.

26. **Two flat mechanics slipped, and one of them was removable without any knowledge.**
    Q2 (`tool_result` protocol — one block per `tool_use`, same `tool_use_id`, all in one user
    message) was answered with "a text summary of all three results". Q17 chose a `parallel: true`
    field in the AgentDefinition, **which does not exist** — step 2 of the 30-second method deletes
    that option on sight. Invented-feature answers have not been a failure mode before; watch
    whether it recurs.

27. **Weak point 6 is clean for the third sitting running.** All ten select-two questions were
    answered with two letters. The two that were wrong (Q33, Q58) were content errors with correct
    counting, which is the same split seen on 14 Aug. Treat the counting habit as learned, and keep
    the mechanical check anyway — it costs nothing.

28. **Q58 and Q59 were answered in opposite directions in the same sitting.** Q58 routed review by
    the model's self-reported low-confidence flag; Q59, two lines later, correctly required
    confidence **calibrated against labelled data**. The rule is known and did not fire when the
    wrong version was dressed as a sampling strategy.
    → **Uncalibrated confidence is never an answer, in any disguise** — not for escalation, not for
    filtering findings, and not for deciding what stops being reviewed.

29. **THE ONE TO CARRY TO THE EXAM: the mock was finished in under 30 minutes of 120. Pacing is not
    a risk. Over-speed is the whole problem.**
    Thirty seconds per question, including reading four scenario stems, is first-instinct
    answering. A candidate who passed used 90 of the 120 minutes. Three pieces of evidence that the
    misses are speed, not knowledge:

    | Correct in the same sitting | Missed | The rule involved |
    |---|---|---|
    | Q59 — confidence must be calibrated with labelled data | Q58, two questions earlier | uncalibrated confidence |
    | Q28 — subagents record dates upstream | Q47 and Q53 | step 6, upstream vs downstream |
    | — | Q17 — chose a `parallel: true` field | step 2 deletes non-existent features on sight |

    Nobody forgets a rule and re-learns it ninety seconds later. The six-step method is not being
    run; the questions are being pattern-matched. That yields 83%, which passes, and the residue is
    exactly what the exam is designed to catch: the defensible-engineering distractor, the
    plausible flag, the adjacent-feeling mechanism.

    Also note **Q56 was self-flagged with a "?", answered anyway, and wrong** — with 90 minutes
    unused and the answer written verbatim in cheat sheet §11. The uncertainty signal is accurate;
    it is just not being acted on.

    → **Exam-day plan** *(superseded 20 Aug by weak point 53 — this pace was never once achieved
    in four attempts, and the replacement is a second-pass sweep instead of a slower first pass).*
    **Budget 75 minutes for the first pass (75 seconds per question), finishing
    with 45 minutes spare, then a second pass over flagged questions only.** Two mechanical
    triggers:
    1. **Flag and return.** Anything that earns a "?" gets marked and revisited. Never committed on
       the first pass.
    2. **Stop on repair verbs.** If an option contains *post-process, validation layer, re-fetch,
       reject, reconcile, downstream* — halt and name the component that held the information at
       the moment it was lost. This one trigger covers Q47 and Q53, the two hardest repeat misses.

    Q17, Q56, Q58 and Q2 all look recoverable by slowing down alone — 54/60 without learning a new
    fact.

### Added 16 Aug, from Mock 2 (46/60) — the reverse-direction paper

30. **Weak point 22 was wrong as general advice, and Mock 2 disproved it. Four marks came from
    three facts that were not on the cheat sheet.**
    Mock 1's misses were all documented, so "stop writing material" looked right. It was right
    about *those* misses only. Today:

    | Fact | Cost | Where it was |
    |---|---|---|
    | **Coverage annotations** — declare which findings are supported and which topics have gaps | **2 marks** (Q15, Q60) | on the revision card, **not** in the cheat sheet |
    | **The interview pattern** — unfamiliar domain, let Claude ask questions first | 1 mark (Q21) | in neither file |
    | **CLAUDE.md as the CI project context** (testing standards, fixture conventions) | 1 mark (Q18) | in neither file |

    → **The cheat sheet and the revision card have now drifted apart three times** (12 Aug, 14 Aug,
    16 Aug). Stop assuming they match. All four facts added to the cheat sheet; the card needs
    regenerating for the interview pattern and the CI/CLAUDE.md line.

31. **Two of the three single-letter select-twos were not counting lapses — they were content gaps
    hiding behind the counting habit.**
    Q27, Q34 and Q59 were answered with one letter, and in every case the letter given was correct
    (49/60 if counted). But the *omitted* letters were:
    - **Q34 → B, "parallel = several Task calls in one response"** — also missed in Mock 1 Q17, by
      choosing a `parallel: true` field that does not exist. **Twice.**
    - **Q59 → C, "stratified random sample of the high-confidence group"** — also missed in Mock 1
      Q58. **Twice.**

    → The habit of stopping at one answer is masking which facts are absent. When a select-two is
    answered with one letter, **the missing letter is the diagnostic**, not the counting error.
    Both facts now carry warning boxes.

32. **Domain 3 collapsed to 6/12, entirely on mechanism selection, and `.claude/rules/` has become
    the reflex answer.**
    Three questions, three different correct mechanisms, each answered with another row of the
    same table: Q7 a **directory CLAUDE.md** was right → chose `.claude/rules/`; Q8 **`@import`**
    was right → chose **skills** (fifth `@import` miss, and the skills answer is back after Mock 1
    finally rejected it); Q9 **`argument-hint`** was right → chose **`paths`**, the key correctly
    identified as *not* a SKILL.md key in Mock 1 Q36.
    → New rule on the cheat sheet: **choose by what the content is grouped by** — package →
    `@import`; file pattern → `.claude/rules/`; one folder → directory CLAUDE.md; always →
    root CLAUDE.md; on request → skill. `.claude/rules/` is correct **only** for a file pattern.

33. **Two never-list answers were chosen in Domain 5, both correct in Mock 1 nine hours earlier.**
    Q44 escalated on **sentiment**. Q30 returned an **empty result marked successful**. Both are on
    the "never the right answer" list, both were clean on Mock 1.
    → This is the strongest evidence yet for weak point 29. Facts that are genuinely known are not
    surviving contact with a plausible distractor at speed. The never-list is not a knowledge
    problem; it is a **stop-and-check** problem.

34. **What is confirmed closed — do not spend more time here.**
    - **Domain 2: 11/11**, including every Grep / Glob / semantic question. That was a four-time
      repeat miss (weak point 8). Closed.
    - **Required vs nullable, both directions in one paper** (Q46 required, Q52 nullable). That was
      missed twice with the identical wrong answer. Weak point 23's first row is closed.
    - **Resume→fresh (Q12), chaining with a known list (Q53), direct execution (Q20)** — all three
      are the opposite direction from Mock 1, all three correct. Those rules are genuinely learned,
      not shape-matched.

### Added 17 Aug, from Mock 3 (49/60) — the paper built from this list

35. **Domain 3 is a selection problem, not a memory problem, and this is now proved.**
    The memorisation core went **8 for 8** — every file path (Q16, Q17), every frontmatter key
    (Q21, Q22, Q23), the real flag (Q24, Q31), plan mode (Q25). All four misses were **grouping**
    questions, and they were **rotated**:

    | Q | The grouping was | Correct | Chose |
    |---|---|---|---|
    | 18 | file type across folders | `.claude/rules/` + `paths:` | **`@import`** |
    | 19 | one folder, nothing outside | a directory CLAUDE.md | **a skill** |
    | 20 | always + maintainer picks | root CLAUDE.md + `@import` | **`.claude/rules/` globs** |

    Three correct mechanisms, each handed to the wrong question. Nothing is missing from the table;
    the rows are being matched by feel, which is weak point 32 unchanged.
    → **Mechanical step: finish the sentence "this content is grouped by ___" out loud before
    reading the options.** Q26 belongs here too — `fork_session` chosen where an Explore subagent
    keeps noisy discovery out of the context.

36. **The stratified high-confidence sample has now been missed three times, in three papers.**
    Mock 1 Q58, Mock 2 Q59, Mock 3 Q45. Every time the **first** letter was right ("analyse by
    category and by segment") and the second came from the wrong family — this time *increase the
    sample uniformly*. The counting habit is not the problem; the fact is.
    → **Why that group:** it is the group review would **stop covering**, so its true error rate is
    the only number that matters. Uniform sampling and sampling what the model already flagged both
    tell you nothing about it.

37. **Five of the eleven misses are one shape: a documented answer displaced by an adjacent
    mechanism.** None of them is a gap in understanding; each is a mechanism that exists being
    swapped for another that also exists, or for one that does not.

    | Q | Correct | Chose | The displacement |
    |---|---|---|---|
    | 14 | manifests | `/compact` at intervals | crash recovery ← context hygiene |
    | 37 | optional and nullable | a post-processing check | schema ← **repair verb** |
    | 45 | stratified high-confidence sample | uniform sampling | see 36 |
    | 49 | `~/.claude.json` | committed `.mcp.json`, "disabled by default" | a real path ← an **invented feature** |
    | 57 | escalate immediately | finish the investigation first | the explicit-request rule |

    → Two triggers already written down would have caught two of these on sight: step 2 (delete
    features that do not exist) kills Q49, and weak point 29's repair-verb halt kills Q37.

38. **Weak point 5's original row came back on question 1.** "Continue whenever `stop_reason` is
    anything other than `end_turn`" was chosen over "continue only on `tool_use`". That row was
    identified on 10 Aug, and a variant of it (text-and-no-`tool_use`) cost a mark on 14 Aug.
    → The loop reads **one value** and continues on **one value**: `tool_use`. Everything else stops
    it, including `max_tokens` and `refusal`, which is exactly why "not `end_turn`" is wrong rather
    than merely imprecise.

39. **What Mock 3 confirms closed — and it was built to test these specifically.**
    - **Parallel = several Task calls in one response: 2 for 2** (Q3 as a single answer, Q60 as the
      half of a select-two that was omitted twice before). No `parallel: true` chosen anywhere.
    - **Coverage annotations: 2 for 2** (Q8, Q42), after two misses in one paper on 16 Aug.
    - **Error categories: 3 for 3** (Q43 permission, Q44 transient, Q52 business — including the
      business-vs-permission trap where a policy limit is not an access problem).
    - **`required`** (Q38) clean, and **SLA arithmetic** (Q36) clean.
    - **Select-two counting: 9 of 10.** The one lapse (Q5) gave a correct letter and omitted
      *"all messages go through the coordinator"*, which is the diagnostic, per weak point 31.

### Added 17 Aug, from the post-Mock-3 set (16/20)

40. **The Domain 3 rule is known and is not being applied. Q6 asked for the discriminator in the
    abstract and was answered correctly, in the same sitting as two wrong applications of it.**
    This closes the question of what kind of gap this is. It is **not** recitation — the table and
    the discriminator are both retrievable. What fails is reading the grouping off the **question's
    nouns** instead of off the content's own scope.

    | Q | The question said | What was picked up | The content actually governs |
    |---|---|---|---|
    | 2 | "…exist in **nine packages**" | package → `@import` | files matching `**/*.stories.tsx` |
    | 4 | "each team lead **decides**" | decides → a skill | everything in that service |

    → **The test, in its final form: *what set of files does this content govern?*** A pattern →
    `.claude/rules/`. One service or package → `@import`. One folder → a directory CLAUDE.md.
    Everything → the root CLAUDE.md. Only on request → a skill. Never decide it from which nouns the
    sentence contains, and never from the word "chooses".

    Note that Q4 is the **skills** trap from weak point 13, which was declared closed after Mock 1
    and has now returned twice (Mock 3 Q19, and here).

41. **Crash recovery = manifests is genuinely absent, and the changing distractor proves it.**
    Mock 3 Q14 chose `/compact` at intervals. This set's Q9 chose scratchpad files. Two attempts,
    two *different* wrong answers — which per weak point 31 is the signal for a fact that is not
    there at all, as opposed to one being out-competed by a specific distractor.
    → The four mechanisms, and the one problem each solves: **Explore subagent** keeps noise out ·
    **`/compact`** shrinks a live session · **manifest** survives a crash · **scratchpad** stops
    findings decaying. Q7, Q8 and Q10 were all correct in this set, so only the crash row is missing.

42. **Format normalisation has overtaken everything else: the post-processing distractor has now
    been chosen four times.**
    14 Aug (D4 ad-hoc Q11) · 16 Aug (Mock 1 Q53) · 17 Aug (Mock 3 Q37, as the nullable question's
    distractor) · 17 Aug (this set, Q15). Always the same family, and in Q15 the select-two counting
    worked and still produced the repair verb as the second letter.
    → **The schema fixes the type; the prompt fixes the format.** Read this against Q13 and Q14 in
    the same set, both correct: `required` vs nullable is **learned**. This one row is not.
    → This displaces the high-confidence sample as the leading repeat miss, and it is the fact that
    weak point 29's repair-verb trigger was written for. The trigger has not fired in four attempts.

43. **What this set closes.**
    - **Stratified high-confidence sample: 2 for 2** (Q16 standing alone, Q17 as the second letter of
      a select-two — the exact position it was lost in three times). Weak point 36 closed.
    - **Both escalation directions in one sitting** (Q19 explicit request, Q20 frustrated but
      solvable). Third time clean.
    - **The loop's exit condition** (Q11), one day after weak point 38.
    - **Coordinator routing and "subagents inherit nothing"** both selected on Q12 — the letter
      omitted on Mock 3 Q5.

### Added 18 Aug, from Mock 4 (58/60) — the paper built from this whole list

44. **Domain 2 is not closed, and it has now been declared closed twice while wrong.**
    16 Aug: "D2 11/11 — closed" (weak point 34). 17 Aug: error categories 3 for 3 (weak point 39).
    Today D2 was the **only** domain to lose a mark, and it lost both:

    | Q | Correct | Chose | Status of that fact |
    |---|---|---|---|
    | 28 | semantic search | `Grep` for "export", then read every match | **5th miss.** Declared closed 16 Aug |
    | 52 | business, not retriable | **transient, retriable** | Error categories were 3/3 on 17 Aug |

    Neither is a new fact and neither is missing from the material. What both share is a **triad
    collapsing to the wrong member under a familiar word.** Q28 printed the word "export", and
    Grep is what you reach for when a word is on the page — but the question also said no agreed
    name exists and that grepping the candidates returns nothing, which is the definition of having
    no string. Q52 named a rule about approvals with a valid token and a healthy API, which is
    business by every step of the test; transient additionally implies a retry, the exact behaviour
    Q51 had just been answered correctly to prevent.
    → **The rule: when a question offers two members of a three-member set, name the third out
    loud before choosing.** Glob / Grep / **semantic**. Transient / validation / business /
    permission — and run the test in order rather than matching the domain of the sentence.

45. ~~**The first-pass time was not recorded, which is the one measurement still missing after four
    mocks.**~~ **Corrected 20 Aug: the time is known and has been stable the whole time — every
    mock ran 30 to 40 minutes.** It was never written into the table, which is why three log
    entries called it missing. It is not missing; it is **consistent**. See weak point 53, which
    replaces this one.

46. **What Mock 4 confirms closed — and it was built to test exactly these.**
    - **Format normalisation: clean**, after four consecutive misses (weak point 42), and the
      `PostToolUse` counterpart (Q15) was also clean in the same paper. Getting both directions in
      one sitting is the first evidence the *discriminator* is held, not the row: the schema fixes
      the type, the prompt fixes the format, and a hook fixes a tool result.
    - **Crash recovery = manifests: 2 for 2** (Q41, Q58), with the scratchpad near-miss adjacent
      both times. Weak point 41 closed.
    - **Both Domain 3 noun traps: clean.** "Twelve packages" did not pull to `@import` (Q16) and
      "the lead decides" did not pull to a skill (Q18). D3 went 12/12 after 6/12 and 8/12. Weak
      points 32, 35 and 40 all closed.
    - **`stop_reason`: 2 for 2**, including `max_tokens` mid-run with "not `end_turn`" offered as a
      distractor. Weak point 38 closed.
    - **Select-two: 10 for 10**, fourth sitting running.
    - **Required and nullable in both directions, stratified high-confidence sample, parallel Task
      calls, coverage annotations, never-list at speed** — all clean.

### Added 18 Aug, from reading Purcell's set against the repo papers

47. **Purcell's set is not the independent measure weak point 21 claims. About 45 of his 60
    questions have a counterpart in Mock 4 alone.**
    Checked directly on 18 Aug, with the set opened for structural comparison only. At the fact
    level the two papers are near-duplicates — same guide v1.0, same six scenarios, and the set of
    testable rows is finite. Fifteen are close enough in framing that answering Mock 4 supplied the
    answer to his: the stale-resume and `fork_session` pair, coordinator-missing-`Task`, subagents
    inherit nothing, sequential-to-parallel, the 97% accuracy scenario and the 70%-false-positive
    category (**he uses the same two figures**), the `mode`-parameter split, error-as-success,
    fabrication under `required`, retry contents, syntactic-vs-semantic, `argument-hint`, CI
    non-interactive plus parseable output, CI test quality, and the `Edit` fallback.
    → **What survives is framing-resilience, which is the thing actually failing** — his dressing,
    numbers and distractors are his own. So keep 23 Aug, and read the score as an **upper bound**
    rather than a measure. Two corrections while here: his set is **6 scenarios × 10 questions**,
    not 4 × 15, so it is a lighter reading load than the real exam and than the repo mocks; and
    **neither of today's D2 misses is tested by it** — his Glob/Grep question covers exactly those
    two tools and never semantic search, and his business-vs-permission framing is policy
    rejection, not the healthy-API-plus-valid-token discrimination that Q52 failed on. The real
    value in his set is the thirteen facts listed under *What is still untested*, not the 60.

### Added 20 Aug, from Mock 5 (48/60) — the untested-facts paper

48. **Weak point 6 is reopened, and it is now the single largest cost in the repo: 5 marks in one
    paper.** It had been clean for four sittings running (10/10, 10/10, 9/10, 10/10) and was treated
    as learned. Select-two went **5 of 10**:

    | Q | Correct | Given | The failure |
    |---|---|---|---|
    | 1 | A, C | **A only** | one letter — the omitted letter was `--output-format json` |
    | 34 | A, D | **B, C** | answered the **inverse** question — gave the two valid reasons where it asked for the two that are never valid |
    | 35 | B, C | **nothing** | left blank |
    | 36 | A, B | B, D | one right letter, second from the wrong family |
    | 39 | C, D | **C only** | one letter — the omitted letter was "the subagent retries transient failures itself" |

    Note what this is **not**: every omitted letter is a fact that was answered correctly elsewhere
    in the same paper. Q39's missing half is the subagent-error rule; Q1's is a flag recited
    correctly on Q2. So this is not weak point 31 (counting concealing a content gap) — it is the
    counting itself, plus one blank.
    → **Exam-day rule, unchanged but clearly not automatic: after reading the last sentence, say
    how many letters you owe before reading the options. If a question is skipped, mark it and
    return — a blank is a guaranteed lost mark and a guess is not.**

49. **Q34 is a new failure shape: the question was read in the correct direction and answered in the
    opposite one.** Both lists were known — the three valid reasons and the two forbidden signals
    are separately correct elsewhere in the paper (Q31, Q32, Q33 all clean). The stem said *never*.
    → This is the same family as the reverse-direction misses on Q23 (which failure a retry fixes)
    and Q4. **Three of the twelve misses were direction, not content.** On a question containing
    *never*, *not*, *except* or *instead*, underline the word before looking at the options.

50. **Domain 3 is not learned. It is now 9/12 · 6/12 · 8/12 · 12/12 · 6/12 across five papers, and
    the 12/12 was on the paper written from its own miss list.**
    Six of the twelve went, and the two grouping questions were **swapped inside one scenario**
    for the third time (Mock 1 Q32/Q33, Mock 3 Q18/Q20, now Q10/Q11):

    | Q | The content governs | Correct | Chose |
    |---|---|---|---|
    | 3 | the project, in CI | CLAUDE.md as CI context | `.claude/rules/` + `paths: "**/*.ts"` |
    | 4 | duplicate tests | supply the existing test files | pass the coverage percentage |
    | 9 | a noisy skill's output | `context: fork` | `/compact` after each run |
    | 10 | `**/*.stories.tsx` | `.claude/rules/` + `paths:` | **`@import`** |
    | 11 | one service, maintainer picks documents | **`@import`** | `.claude/rules/` + globs |

    Q10 and Q11 are each other's answers, and Q3 is `.claude/rules/` as the reflex a third time
    (weak point 32). Q3 is also the **second** miss of "CLAUDE.md is the CI project context", first
    lost on Mock 2 Q18 — one of the three facts that were missing from the cheat sheet on 16 Aug and
    were added that day. So it has now been missed *after* being written down.
    → The 12/12 on Mock 4 measured a paper built from these exact misses, not the domain. **Treat
    D3 as the weakest domain again**, and drill it as recitation of the grouping sentence, out loud,
    before options are read.

51. **The material is nearly complete: ten of the thirteen never-tested facts were clean on first
    contact.** `tool_choice` in three directions, both escalation directions, `/compact` as a
    correct answer, severity by concrete examples, `custom_id` resubmission, goal-oriented subagent
    prompts, `--resume` positive, personal command placement, `allowed-tools`, re-review duplicates
    — all first-time correct. Only three of the thirteen went, and only **one is a genuine material
    gap**: plain-text JSON → tool use (Q16, answered with few-shot examples). The cheat sheet said
    what tool use *does not* fix (semantic errors) and never said it is **the** way to get
    structured output. Added to §10.
    The other two are weak point 48, not knowledge.

52. **What Mock 5 confirms closed.**
    - **Semantic search: clean on its 6th appearance** (Q54), with the two Grep variants and Glob
      all offered. Missed 5 times before. Weak point 44's first row is closed — but the paper it
      closed on named the triad in its own preamble, so re-test it cold on 23 Aug.
    - **Business vs permission: 2 for 2 in adjacent questions** (Q26 business with a healthy API and
      an authorised caller, Q27 permission on token scope). Weak point 44's second row is closed.
    - **`required` and nullable both directions, format normalisation, `calculated_total`,
      manifests, Explore vs `fork_session`, `stop_reason` on `max_tokens`, the `tool_result`
      protocol, coverage annotations, the stratified high-confidence sample** — all clean.
    - **D1 14/16 and D5 8/9**, with both misses being weak point 48 rather than content.

53. **THE ONE TO CARRY TO THE EXAM, and it replaces weak points 29 and 45. Every mock has run
    30–40 minutes of the 120. That is now four data points, and it is not a variable — it is how
    you answer.**

    | Paper | First pass | Score |
    |---|---|---|
    | Mock 1 | under 30 min | 50/60 (83%) |
    | Mock 3 | 30–40 min | 49/60 (82%) |
    | Mock 4 | 30–40 min | 58/60 (97%) — paper written from this log, discount it |
    | Mock 5 | 30–40 min | 48/60 (80%) |

    Two things follow, and the second is the important one.

    **First: 30–40 minutes reliably produces 80–83%.** That passes. The floor is not in danger at
    this speed; the residue is. So "go slower" is not a rescue plan, it is a marginal-marks plan.

    **Second: the 75-minute first pass has been the named exam-day fix since 16 August and has
    never once happened, across four attempts.** An instruction that fails four times is not going
    to start working on 25 August. Stop instructing pace and instruct an **action** instead —
    something with a start and a finish, which pace does not have:

    > **You will finish the first pass with roughly 80 minutes left. Do not leave. Do two sweeps
    > before you stop: (1) every question that says *select two* — count your letters; (2) every
    > question whose last sentence contains *never*, *not*, *except* or *instead* — re-read the
    > stem, not the options.**

    On Mock 5 those two sweeps alone target **Q1, Q34, Q35, Q36, Q39** — five of the twelve misses,
    and 53/60 without learning a single new fact. Neither sweep requires slowing the first pass
    down, which is the reason to prefer them: they are checks, not habits.

    **And 30–40 minutes is not rushing, for this reader.** Stated 20 Aug: a question is read and
    processed in **6–7 seconds**, so most of the 30–40 minutes is spent on the options and the
    choice, not on comprehension. The paper agrees: the longest, densest stems on Mock 5 — the two
    grouping questions, the 97%-accuracy question, the provenance question — were read correctly,
    and the ones that went wrong went wrong *after* the reading. **Weak point 29's "over-speed"
    label was inferred from one data point (Mock 1) and is not supported.** What the five
    multiple-response misses share is not comprehension but **completeness of the answer given**:
    one letter supplied where two were owed, one question passed over entirely. That is an output
    check, and it is why the fix is a sweep at the end rather than a slower pass at the start.

    **What the split also proves: the rest is not speed.** Q3, Q4, Q9, Q10, Q11 (D3 mechanisms) and
    Q16 (a material gap, now fixed) are not recoverable by re-reading. **Six marks of D3 and D4
    content, five marks of reading discipline, one direction error.** Weak point 29 claimed
    over-speed was "the whole problem"; on this paper it is under half of it, and the half that is
    left is Domain 3.

### Added 20 Aug, from Mock 6 (58/60) — the reading-discipline paper

54. **Weak point 48 is closed for the mechanics, and the mechanics were the whole of it.**
    Ten select-two questions, **9/10, no blanks, no single-letter answers**, and the one loss (Q48)
    was two letters with one wrong — a content error, not a counting error. Four questions ran in
    the **inverse** direction (Q25 which two do not exist, Q37 which two are never valid, Q48 which
    two a tool must never do, Q57 which two must never trigger escalation) and **all four were read
    in the right direction**, including Q57, where the two *valid* grounds sat in the option list as
    A and B. That is the exact trap that cost Mock 5 Q34.
    → The remaining risk on multiple-response is not counting. It is whether the two candidates you
    keep are both actually on the "never" list.

55. **Coverage annotations is now missed three times, and the distractor is different every time.**
    16 Aug: "retry until the sources respond" and "summarise more aggressively". 20 Aug (Q14):
    **"publish the totals and note the outage in the pipeline log"** — the most reasonable-looking
    version yet, and the first that does not try to remove the gap at all.
    → Three misses with three different wrong answers means the fact is **absent**, not out-competed
    (the same signature as manifests, weak point 41). The rule has one shape and it is about
    **where the gap is declared**: it goes **in the output the reader sees**, next to the findings.
    A log, a ticket, a monitoring alert and a footnote to the pipeline team are all the same miss.
    Ask: *would the person reading this report know that two carriers answered where three were
    expected?* If the answer lives anywhere other than the report, it is wrong.

56. **The error contract is known from the "must return" side and not from the "must never" side.**
    Q48 offered four behaviours and asked which two a tool must never do. Both letters given were
    plausible-bad; one was actually **good practice** — *"return the partial results it did obtain,
    marked as partial"* — which is the subagent report rule (partial results are one of its four
    required parts). The letter missed was *"return success with an empty result set when the lookup
    failed"*, which is **hiding the error as success**, the second item on the never list.
    → Two adjacent facts, one confusable pair: **partial results, labelled as partial, are always
    correct. A success with no results, when the lookup failed, is always wrong.** The tell is not
    how much data comes back, it is whether the **status is honest**. Same discriminator as weak
    point 55 one question apart: an incomplete answer that says so is fine; an incomplete answer
    that reads as complete is the failure.

    **What Mock 6 confirms — with the same caveat as Mock 4.** D3 **12/12**, all ten grouping
    questions in one block, with `@import`, `.claude/rules/`, a directory CLAUDE.md, the root
    CLAUDE.md and a skill live in the same scenario, plus both noun traps from weak point 40
    ("they exist in all nine packages", "each maintainer decides") answered correctly. D1 **16/16**,
    D4 **12/12**. The handoff package and multi-issue handling — the two Mock 5 blanks — both clean.
    **But this paper, like Mock 4, was written from this log**, so it measures retrieval of facts
    already listed here, not independence. The independent number is still 23 Aug.

### Added 22 Aug, from Mock 7 (70/72, corrected) — the all-six-scenarios paper

57. **Domain 3, Domain 4, and select-two are all genuinely learned, not paper-specific.** First
    reported as 67/72 with three D4 losses in Scenario E (Q51–53); those three were a transcription
    error when writing down answers, not exam misses — corrected the same day to 70/72 once the
    actual answers (51 C, 52 B, 53 C) were confirmed. Read the numbers below as the corrected ones.

    This is the first paper where **D3 (14/14)** and **D4 (18/18)** both went clean without being
    built from either domain's own miss list — Mock 4 and Mock 6 scored 12/12 on D3 papers written
    to test exactly those facts, which the log flagged each time as the less convincing kind of
    evidence. Here the scenarios, the packages, and the documents were all new, and `@import` vs a
    skill vs `.claude/rules/` vs a directory CLAUDE.md vs the root CLAUDE.md still sorted correctly
    every time; every CI and extraction fact in D4 held too, including the CLAUDE.md-as-CI-context
    fact that cost a mark on Mock 2. **Select-two went 9/9** — third clean sitting running, every
    pair exactly right, no blanks, no single letters. All three of the log's longest-running
    problems can now be called learned rather than paper-lucky.

    Only two losses survive in the whole 72, and both are regressions rather than new gaps:

    | Q | Correct | Chosen | What this is |
    |---|---|---|---|
    | 1 | Stop on `stop_reason: "refusal"` | "continue, not `end_turn`" | Weak point 5/38's trap, **3rd occurrence** — the loop reads one continue value, `"tool_use"`, and everything else stops it, `refusal` included |
    | 23 | Fresh session, written summary | `--resume`, list every change | Weak point 5's *other* half, reopened after four clean sittings (Mocks 2, 3, 4) |

    **Q23 is the sharper of the two.** Q4, in the same paper, tested the identical discriminator —
    a returning conversation with most of the earlier context stale — and was answered correctly,
    with `--resume` correctly rejected in favour of a fresh session. Q23 changed only the surface
    (three weeks instead of nine days, a renamed package and a changed build tool instead of expired
    promotions) and the same judgement failed. **The rule itself ("how much is stale") is
    retrievable; recognising *enough* staleness in an unfamiliar dressing is not yet automatic.**
    Ask directly, every time: *of what I'd carry forward by resuming, how much is still true?* Three
    changed facts against a three-week gap is a lot, not a little.

    **Q1 is the stop_reason trap in a costume it has not worn before.** Every earlier occurrence
    used `max_tokens` as the value that broke the "not `end_turn`" shortcut. This one used `refusal`,
    and the same shortcut failed the same way — confirming the fix has to be the full list, not a
    memorised pair. Say all seven values before answering any `stop_reason` question: `end_turn`,
    `tool_use`, `max_tokens`, `stop_sequence`, `pause_turn`, `refusal`,
    `model_context_window_exceeded`. Exactly one continues the loop.

    **What this closes:** D3 grouping and D4 (both 14/14 and 18/18, first time on fresh dressing),
    select-two mechanics (9/9, third clean paper), the handoff package, multi-issue handling, and
    duplicate-test handling (all clean again), all four `tool_choice` values, the SLA-arithmetic
    pattern on new numbers, and both directions of required-vs-nullable. **First pass 23 minutes for
    72 questions** — faster per-question than any prior mock and still 97%. The strongest evidence
    yet that speed is not the variable: the two remaining losses are both threshold judgements
    applied to unfamiliar dressing, not comprehension failures, and reading faster would not have
    touched either one.

    **A second lesson from this entry, independent of the exam material: verify a self-reported
    answer transcription before logging it as a miss.** The first pass treated Q51–53 as three lost
    marks and wrote a whole cluster analysis around them; all three were transcription slips. Score
    corrections happen — the fix is to update the log in place with the correction visible, not to
    leave the wrong analysis standing next to the right one.

### Added 23 Aug, from Purcell's 60 (59/60 recorded) — the rehearsal

58. **The rehearsal landed exactly where weak point 47 said it would, which is the least surprising
    and therefore least informative result in the repo.** 59/60 in 19 minutes, with D1, D3, D4 and
    D5 all clean and **all 11 multiple-response questions correct**. On 18 Aug this set was
    downgraded from "the only independent measure" to "an upper bound," on the grounds that ~45 of
    its 60 have a counterpart in Mock 4 alone. The score is consistent with that and adds no new
    evidence about readiness. **Do not treat it as a fifth confirmation.** The genuinely independent
    signals remain Mock 1 (50/60, 83%) and Mock 7 (70/72, 97% on six unfamiliar scenarios).

    **Two further reasons to discount it, both defects in construction rather than content.**

    *One: the answer key rotates.* Every scenario's single-answer keys run a strict four-cycle,
    phase-shifted per scenario — S1 `B D A C B D A C`, S4 `D B A C D B A C`, S6 `C A D B C A D B`.
    Same defect this repo found in its own files on 11 Aug (56 of 66 singles keyed B).

    *Two, and larger: the correct answer is nearly always the longest option, and it embeds its own
    rationale.* "…does not include `Task` — the Task tool is the mechanism for spawning subagents,
    so without it no delegation can occur." "…scope each subagent's tool set to its role — since
    large tool inventories degrade selection reliability." The right answer explains why it is
    right; the distractors are left bare, and several are not serious ("the prompt needs the word
    *please*", "skip retries on Mondays"). **A candidate with no Claude knowledge could pick the
    longest self-justifying option and clear a comfortable pass.** Together the two leaks mean the
    paper cannot distinguish content knowledge from rhythm and option length. Nothing suggests
    either was used here — the answers track the reasoning — but a paper that *could not have
    detected it* certifies nothing.

    **What this does not license, and the distinction matters for Tuesday.** His difficulty
    calibration and his item-writing craft are separate, and only the craft is weak: he sat the
    exam, he claims the set is pitched at what he experienced, and the 18 Aug comparison found ~45
    of his 60 have a Mock 4 counterpart — so he is testing the **right facts** and building **poor
    items** around them. Meanwhile this repo's papers are harder in a direction the real exam
    probably is not: Mock 6 ran 10 select-two and 4 inverse-direction items in 60, Mock 7 ran nine
    consecutive D3 grouping questions. Live certification items are psychometrically reviewed, which
    tends to produce **better distractors than his and less adversarial clustering than ours**. Read
    the live exam as sitting between the two, and keep Mock 1 (50/60, cold, pre-tuning) as the
    honest floor.

    **The one gap is a write-up slip, and it is worth recording precisely because of what it is
    not.** The answer list runs 4.2, then a line labelled 4.3 carrying **A** — which is 4.4's
    correct answer — then 4.5. One line was dropped in transcription, so 4.4 was answered correctly
    and 4.3 has **no recorded answer at all**. The candidate reports having chosen B, which is
    correct; logged as 59/60 rather than 60/60 because, unlike Mock 7's Q51–53, there is no written
    answer to check the claim against. Either way **nothing on this paper was a content miss**, and
    4.3's question (incremental exploration — Grep for entry points, then Read selectively) is one
    the repo has never lost.

59. **THE ONE TO CARRY INTO TUESDAY, and it is not a fact.** Two consecutive papers have produced a
    **transcription** error and zero new content gaps: Mock 7's Q51–53 (three recorded misses, all
    three verifiably correct) and Purcell 4.3/4.4 (one line dropped, shifting an answer onto the
    wrong number). Across both sittings that is up to four marks attributable to bookkeeping and
    none to knowledge. The live exam removes most of this — answers are selected in the system, not
    written onto a list — so the residual risk is small. But the corresponding on-screen habit costs
    nothing: **confirm the answer you selected belongs to the question you just read, then move on.**
    That, plus the two second-pass sweeps from weak point 53 (count letters on every *select two*;
    re-read every stem containing *never / not / except / instead*), is the whole exam-day protocol.
    No pacing instruction — 19 to 23 minutes for a full paper has produced 97–98% twice running.

    **What the last three papers say about readiness, stated plainly.** Mock 7 (six unfamiliar
    scenarios, not built from this log) 70/72 with two threshold regressions. Purcell's 60 (an upper
    bound by construction) 59/60 with no content miss. Mock 6 58/60. Every domain has scored at or
    above 90% on a paper that did not rehearse it. The remaining named risks are three: the
    `stop_reason` continue-value shortcut, the resume-vs-fresh staleness threshold, and answer
    bookkeeping. **Nothing on the list requires new material, and none of it is a domain.**

### Added 23 Aug, from Mock 8 (57/60) — the blueprint-built paper

60. **THE ONE TO FIX BEFORE TUESDAY, and weak point 59 understated it. Three consecutive papers have
    lost an item to a dropped or misaligned line.**

    | Paper | What happened | Cost |
    |---|---|---|
    | Mock 7 (22 Aug) | Q51–53 answers written against the wrong numbers | 0 (recovered) |
    | Purcell (23 Aug) | 4.3 never written; 4.4's answer sat under a 4.3 label | 1 mark as recorded |
    | Mock 8 (23 Aug) | Q24 never answered — list runs 23, then 25 | **1 mark** |

    On 23 Aug weak point 59 called the residual risk "small" because the live exam takes answers into
    a system rather than onto a list. **That reasoning was wrong in one specific way: the live exam
    still lets you leave an item unanswered, and this candidate demonstrably skips items without
    noticing.** Three for three is a behaviour, not an accident.

    **The cause is now known, stated by the candidate on 23 Aug: eye fatigue.** Q24's answer
    (`argument-hint`) was known; the item was simply not seen. That is consistent with when the skips
    happen — they cluster on **high-volume days**. Both papers on 23 Aug dropped an item (Purcell 4.3,
    Mock 8 Q24); Mock 5 left Q35 blank on 20 Aug, also a two-paper day. Mock 6, taken second on
    20 Aug, is the only counter-example.

    **This is not a pacing problem and must not be treated as one.** A 60-question paper is finished
    in 19–23 minutes of the 120 available, and comprehension is demonstrably fine — the densest stems
    in every paper are answered correctly. What degrades is *visual coverage* late in a scanning
    session. The prescription is therefore recovery and a count check, not slower reading:
    → **Take a deliberate two-minute break mid-paper, eyes off the screen.** There are roughly 100
    unused minutes; nothing about the schedule makes this expensive.
    → **Before submitting, open the review screen and confirm every question shows as answered.**
    Not a re-read, not a second content pass — a completeness check on the count. If the interface
    offers no such screen, page back and count. A blank is a guaranteed lost mark; a guess is not.
    → **Do not take a practice paper on the morning of the exam.** Three papers across two days is
    the condition that produced this.

61. **Q42 is not a counting lapse — it is the same fact omitted in the same slot, twice.**
    Mock 5 Q39 was answered "C only" where C, D were owed; the omitted letter was *the subagent
    retries transient failures itself and reports upward only what it cannot fix*. Mock 8 Q42 was
    answered "C only" where C, D were owed; **the omitted letter is the same rule.** In both cases
    the letter that *was* given (transient / `isRetryable: true`) is correct, so the error is not
    reading and not counting.
    → Per weak point 31, the missing letter is the diagnostic. **The four-part subagent error rule is
    held from the categorisation side and not from the recovery side.** Say the pair together:
    *classify it as transient — and the subagent retries it itself, escalating only what it cannot
    resolve.* Both halves, one sentence. Note that select-two otherwise went 9/10 here, so the
    mechanics are still sound; this is content.

62. **The length tell may have been quietly helping, and this is the first paper that could detect
    it.** Mock 8 was built with the correct answer as the **shortest** option on 28 of 50 singles,
    after the 23 Aug audit found Purcell's set keys the longest, self-justifying option almost every
    time. The single content miss (Q12, confidence calibration) fell exactly there: the correct
    answer was short, unadorned and last; the chosen distractor was longer and carried its own
    reasoning. **Confidence calibration had been clean on every previous paper**, all of which keyed
    the long explanatory option.
    → One data point, so state it no more strongly than that: it is **suggestive, not established**,
    that some earlier clean marks had help from option length. What follows for Tuesday is small and
    cheap — **a short, flat option is not less likely to be right.** Real exam items are usually
    padded to even length precisely to kill this heuristic, so it should not fire at all.

    **What Mock 8 confirms, and it is the most independent evidence in the repo after Mock 1.**
    Written from the blueprint without the miss list open, on four scenarios with fresh dressing:
    **D1 16/16 and D4 12/12**, all nine Domain 3 grouping questions correct, both hook directions in
    adjacent questions (`PreToolUse` to block a call, `PostToolUse` to normalise a result), the
    semantic-vs-Grep pair clean, and select-two 9/10. Nothing in the paper's content was
    unrecoverable — the three losses are one blank, one half-answer, and one heuristic.

---

## Session history

| Date | What happened |
|---|---|
| 25 Aug | **Post-exam debrief, reported the same day.** The real questions were **a lot longer, somewhat vaguer, and carried many more traps** than anything in this repo — and of the outside sources checked, the closest to the real thing was **`claudecertificationguide.com/learn`**, not Purcell's set and not either GitHub repo. **What this settles:** the prep was right about *content* and wrong about *form*. Every fact needed was on the cheat sheet, which is why 787 with 67 points of margin; but nine mocks of short, single-trap, one-sentence-stem questions gave no rehearsal for long multi-clause stems with buried qualifiers, and the 95–98% scores measured recall of a fact list, not performance on the real item type. Weak point 47 ("built from this log, so it measures retrieval") named the wrong defect — the deeper one is **shape**, and it is invisible from inside a repo whose author also writes the questions. **For any future paper (CCAR-P, or a set built for someone else): write stems of three or four clauses, put the discriminating qualifier in the middle rather than the last sentence, give every distractor a plausible mechanism, and stop capping at one trap per item.** Two independent signals had said as much before the exam — re-cinq's *"the gap was the wording, not the difficulty"* and Weidner's *"dense enough that two minutes goes fast"* — against a candidate who finishes 60 in 19–23 minutes. Both were logged and neither changed how the papers were built. |
| 25 Aug | **Exam day. Passed, 787/1000, first attempt.** Fifteen days end to end: 11/20 cold on 8 Aug, a rebalance of every practice file on 11 Aug after the answer-key bias was found, nine repo mocks, Purcell’s 60 as the rehearsal, and a cheat sheet rebuilt from repeat misses rather than from the syllabus. What the prep got right, in order of value: **treating a fact missed twice as a fact not learned** (the repeat-miss list drove Mocks 3, 4 and 7), **writing the last two papers without this log open** so the score meant something, and **separating counting and coverage failures from knowledge failures** — the select-two habit and the dropped-item habit each cost more marks across the mocks than any single fact did. Left open: **Mock 9 was built for 24 Aug and no result was ever logged**, and the 23 Aug files (Mocks 8 and 9, the cheat-sheet additions, weak points 60–62) are still uncommitted. |
| 23 Aug | **Mock 8, second paper of the day and the first built to the two construction rules agreed earlier: written without `LOG.md` open (blueprint objectives and domain notes only) and with the length tell inverted — correct answer shortest on 28 of the 50 singles, embedded rationale placed in wrong answers at least as often as right ones, letter-balanced non-rotating key. 57/60 (95%).** After Mock 1, the most independent number in the repo. **D1 16/16, D4 12/12**, all nine D3 grouping questions correct, both hook directions right in adjacent items, select-two 9/10. **The three losses are three different kinds and none is a knowledge gap in the ordinary sense.** Q24 was left blank — the **third consecutive paper with a dropped item**, which retires the "small residual risk" reading in weak point 59 and makes the pre-submit completeness check the single thing to carry into Tuesday. Q42 was answered with one letter of two, and the omitted letter is **identical to Mock 5 Q39's** — the subagent-retries-transient rule, held from the categorisation side but not the recovery side, so it is content rather than counting. Q12 was the only pure content miss and fell exactly where the paper inverted the length heuristic, which is the first (single, suggestive) evidence that earlier clean marks may have had help from option length. Weak points 60–62 added. |
| 23 Aug | **The rehearsal, on schedule: Purcell's 60-question set, cold and timed. 59/60 (98%) in 19 minutes** — D1 16/16, D2 10/11, D3 12/12, D4 12/12, D5 9/9, and **all 11 multiple-response questions correct**. The one gap is a dropped line in the write-up (4.4's answer landed under a 4.3 label, 4.3 never recorded), not a content miss — the second transcription slip in two papers, after Mock 7's Q51–53. **Two reasons the number means less than it looks**, both now in weak point 58: the set was downgraded to an upper bound on 18 Aug (~45 of its 60 have a Mock 4 counterpart), and **its answer key rotates in a strict four-cycle**, phase-shifted per scenario — the same defect this repo found in its own files on 11 Aug — so the paper cannot distinguish content knowledge from rhythm. The independent numbers remain Mock 1 (83%) and Mock 7 (97% on six unfamiliar scenarios). Weak points 58 and 59 added. **Exam-day protocol is now fixed and short:** two second-pass sweeps (count letters on every *select two*; re-read every *never / not / except / instead* stem) plus one on-screen check that the selected answer belongs to the question just read. No pacing instruction. Tomorrow is revision only — read the cheat sheet twice, write nothing new. |
| 22 Aug | **Mock 7, requested as a paper covering all six exam scenarios in one sitting rather than the usual 4-of-6: 72 new questions, six fresh scenarios not used in any earlier mock.** First scored as **67/72 (93%)** with three D4 losses in a row (Q51–53); those turned out to be a transcription slip when the answers were written down, not exam misses — **corrected same-day to 70/72 (97%)** once the real answers (51 C, 52 B, 53 C) came back. Finished in 23 minutes. **D3 14/14 and D4 18/18** — the first clean scores for either domain on a paper not built from its own repeat-miss list — and **select-two 9/9**, a third clean sitting running. Only two losses survive, both regressions: `stop_reason: "refusal"` generalised as "not `end_turn`" (the weak-point-38 trap, now in its third costume), and a three-week-stale session `--resume`d instead of restarted fresh (weak point 5, reopened after four clean sittings, on the *identical* discriminator tested correctly earlier in the same paper at Q4). Weak point 57 added, including a note on verifying a self-reported transcription before logging it as a content gap. This closes D3, D4, and select-two as paper-specific results and narrows the live gap to two threshold judgements that decay under unfamiliar dressing. |
| 20 Aug | **Mock 6, taken the same day as Mock 5: 60 new questions built as a reading-discipline paper — Domain 3 as one unbroken block of ten grouping questions, 10 select-two, and four questions running in the inverse direction. 58/60 (97%).** The paper was designed to reproduce the two Mock 5 failures on purpose, and neither reproduced: **select-two 9/10 with no blanks and no single-letter answers**, and **all four inverse-direction questions answered in the right direction** — including Q57, where the two *valid* escalation grounds were sitting in the option list. **D3 12/12** with `@import`, `.claude/rules/`, a directory CLAUDE.md, the root CLAUDE.md and a skill all live in one scenario, and both weak-point-40 noun traps ("they exist in all nine packages", "each maintainer decides") answered correctly; D1 16/16; D4 12/12. The three facts that failed on Mock 5 — plain-text-JSON → tool use, the handoff package, multi-issue messages — were all clean, which closes the untested-facts list. **Both misses are single absent facts, not habits:** coverage annotations for the third time, with a third different distractor ("note the outage in the pipeline log" — the first version that does not try to remove the gap), and Q48, where the two letters given included *"return partial results, marked as partial"*, which is correct behaviour, instead of *"return success with an empty result set"*, which is hiding the error as success. Weak points 54–56 added; both misses share one discriminator, now the single line to carry to the exam. **Caveat, same as Mock 4: this paper was written from this log**, so it measures retrieval of listed facts, not independence. 23 Aug is still the only independent number. |
| 20 Aug | **Mock 5: 60 new questions, built from the *untested*-facts list instead of the repeat-miss list** — all thirteen facts that appear in Purcell's set and in no repo paper, each marked ★ in the key, plus both live D2 misses and four invented features. Four scenarios in a pairing not used before; balanced key (A 13 · B 12 · C 13 · D 12 across the singles, each letter 5× across the select-twos). **48/60 (80%)** — on target, every domain above the floor except D3. **The material is close to complete: ten of the thirteen never-tested facts were clean on first contact**, and only one miss is a real gap (plain-text JSON → tool use, added to cheat sheet §10). **The result is not about knowledge.** Five of the twelve misses are select-two questions — one blank, two answered with a single letter, one answered with the *inverse* of what was asked — after four sittings at 10/10. Three more were direction rather than content. And **D3 fell back to 6/12**, with `@import` and `.claude/rules/` swapped inside one scenario for the third time in the repo, so Mock 4's 12/12 measured the paper and not the domain. Weak points 48–52 added; D3 is the weakest domain again and select-two is reopened as the largest single cost. **First pass 30–40 minutes, the same as every previous mock** — which retires weak point 45 (the time was never missing, only never written down) and replaces weak point 29's 75-minute plan with two second-pass sweeps that have a finish line. See weak point 53. |
| 17 Aug | **Post-Mock-3 set, taken the same day: 20 questions, deliberately not blueprint-weighted** — eight aimed at the two unlearned facts (Q1–Q6 the grouping decision with five different correct answers, Q16 and Q17 the high-confidence sample) and twelve to hide them in. **16/20.** The result settles what kind of gap Domain 3 is: **Q6, which asks for the discriminator itself, was correct**, and two applications of it in the same sitting were not — so the fix is not more recitation. The two misses show the mechanism: the grouping is being read off the question's nouns ("nine packages" → `@import`) and off the word "decides" (→ a skill, the weak-point-13 trap returning for the second time today). Two other facts confirmed absent rather than out-competed: **manifests** (second miss, and with a *different* wrong answer each time) and **format normalisation → the prompt** (fourth miss, same post-processing family every time, and now the leading repeat miss in the repo). Against that, the **high-confidence sample is closed 2 for 2**, including in the select-two position where it was lost three times, and both escalation directions came out clean again. Weak points 40–43 added. No new facts written to the cheat sheet — all four misses were already in it; one retrieval cue added to §2. |
| 17 Aug | **Mock 3: 60 new questions, written from the repeat-miss list rather than the blueprint alone** — each fact missed twice or more appearing twice, in different disguises, with two fresh scenarios (Multi-Agent Research, Code Generation) so the dressing was unfamiliar. Balanced key (A 12 · B 13 · C 12 · D 13 across the singles, each letter 5× across the select-twos). **49/60 (82%)** — above the 80% target with **every domain at or above the floor** for the first time since Mock 1, and D5 back from 4/9 to 7/9. The gap-targeting worked on four of the five facts: parallel Task calls 2/2, coverage annotations 2/2, `required` clean, error categories 3/3. It did **not** work on the fifth: the stratified high-confidence sample is now missed three times in three papers, always as the second letter. **D3 is the one live problem, and the diagnosis is now precise** — the memorisation core scored 8/8 while all four misses were grouping questions, answered with each other's mechanisms in rotation. Five further misses share one shape: a documented answer displaced by an adjacent mechanism (`/compact` for manifests, post-processing for nullable, an invented "disabled by default" server for `~/.claude.json`, finish-then-escalate for an explicit request). Weak points 35–39 added. **No new material written** — every miss is already in the cheat sheet; the remaining work is the grouping recitation and the two mechanical triggers. |
| 18 Aug | **Mock 4: 60 new questions, four scenarios not paired before, 10 select-two, balanced key (A 13 · B 12 · C 13 · D 12 across the singles). 58/60 (97%)** — the highest score in the repo, and the least independent number in it: the paper was written *from this log*, targeting the exact facts already missed. Read it that way. **Every trap it was built for came out clean** — format normalisation after four consecutive misses, and its `PostToolUse` counterpart in the same paper; manifests twice; both D3 noun traps, taking D3 from 8/12 to 12/12; `stop_reason` twice including `max_tokens`; select-two 10/10. **Both misses were D2** — semantic search for the fifth time, and business-vs-permission answered *transient*. Weak points 44–46 added; **D2 is downgraded from "confirmed closed" back to active, having now been declared closed twice while wrong.** Then, with approval, opened Purcell's set for a structural comparison: ~45 of his 60 have a counterpart in Mock 4, fifteen closely enough framed to be pre-seen, so 23 Aug is now an upper bound rather than a measure — weak point 47, and the thirteen genuinely untested facts it surfaced are in *What is still untested*. |
| 16 Aug | **Mock 2, same day, deliberately built against the Mock 1 failure mode** — every question offering a defensible late fix, a plausible non-existent feature, or a known rule running in the opposite direction. **46/60 (77%)**, below target, with **D3 at 6/12 and D5 at 4/9**, both under the floor. Three findings. First, **weak point 22 was wrong**: four marks came from three facts absent from the cheat sheet (coverage annotations, twice; the interview pattern; CLAUDE.md as CI context) — the cheat sheet and revision card have drifted apart for the third time, and all four are now added. Second, the three single-letter select-twos were **not** counting lapses: two of the omitted letters (parallel Task calls, stratified high-confidence sampling) are Mock 1 repeat misses, so the counting habit was concealing content gaps. Third, D3 mechanism selection has degraded into a reflex for `.claude/rules/`. Against that, D2 scored **11/11** and required-vs-nullable came out clean in both directions, so weak point 8 and the first row of 23 are closed. Weak points 30–34 added. |
| 16 Aug | **Mock 1: 60 new questions, four scenarios, 10 select-two, blueprint-weighted, balanced key (A 13 · B 12 · C 13 · D 12 across the singles). 50/60 (83%) in under 30 minutes of the 120.** The time is the headline, not the score — 30 seconds a question is first-instinct answering, and the misses read as speed rather than gaps: the same rule was applied correctly and incorrectly two questions apart, three separate times. Weak point 29 has the exam-day fix: a 75-minute first pass, flag-and-return, and a hard stop on repair verbs. — clears the 80% target with every domain above the 60% floor, and the first 60-question sitting. Marked against the cheat sheet afterwards: **all ten misses were already in it**, six inside warning boxes written two days earlier. Both rows of the step-6 table were missed again with the *same* distractors as 14 Aug, so weak point 19 is reopened, not closed. `@import` changed shape — fourth miss but the first without choosing skills; the confusion has moved to `@import` vs `.claude/rules/`, which were swapped inside one scenario. Select-two counting clean 10 for 10. Weak points 22–28 added. **Decision: write no new material before the exam. The gap is retrieval, so the remaining sessions are cover-and-recite on the cheat sheet plus timed questions from independent sources.** |
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
| `1784098676646.pdf` | Matthew Purcell's 60-question set. Blueprint-weighted 16/11/12/12/9, 11 multiple-response, answer key with rationales. **Structure corrected 18 Aug: 6 scenarios × 10 questions, not 4 × 15** — a lighter reading load than the real exam or the repo mocks. **Cross-checked 11 Aug: zero contradictions with the repo material. Overlap quantified 18 Aug: ~45 of the 60 have a counterpart in Mock 4 alone, 15 of them closely framed** (weak point 47), so treat the score as an upper bound. Its real value is the thirteen facts it tests that no repo paper does — listed under *What is still untested* | **23 Aug** — take it cold, then do both second-pass sweeps before stopping (weak point 53) |
| Matthew Purcell's LinkedIn review | He passed all four exams. Confirms: Bedrock/Vertex not tested, Claude 101 and AI Fluency too basic, CCAR-F is the hardest of the four, scenarios are "dressing", finished in 90 of 120 min | Read once |
| Paul Larionov's GitHub repo | A study guide Purcell recommends. **Evaluated 24 Aug:** guides in 14 languages plus a 60-question HTML practical test (4 scenarios × 15, **zero multiple-response**, key A 19 · B 15 · C 12 · D 14, correct answer longest 47% of the time, one duplicate pair). **Zero contradictions with this repo's material** on every mechanism checked. Item style short and clean — same wrong shape as our own mocks | Superseded |
| `hamzafarooq/claude-certified-architect` | 55 questions in `practice-exam.html` (README claims 64) + 10 in `quick-quiz.html`. Content is good and contradicts nothing here, and it carries **8 items marked as the official sample questions**. But the key is broken: **A never appears as an answer in 55 questions** (C 29 · B 23 · D 3), D3 runs `CBCBCBBCBCBC`, four duplicate pairs, and the paper is not blueprint-weighted despite its own README chart. Useful for the 8 starred items and nothing else | Superseded |
| `claudecertificationguide.com/learn` | Free lesson site with a 230+ question bank, drill mode, diagnostic and a 60-question mock. **Named by the candidate on 25 Aug as the closest of all sources to the real exam's item style.** Aligned to guide v1.0 facts, and it fixed its own length bias on 13 July (correct answer had been longest 87% of the time). **One systematic caution:** it "corrects" the guide toward current Claude Code behaviour, and on four points the guide keys the opposite — `Edit` non-unique match (guide: Read + Write), `allowed-tools` (guide: restricts), coordinator tool field (guide: `allowedTools`), `@import` (guide uses that name). Its `SubagentStart`/`SubagentStop` and `structured_output` material is not in the guide at all | **The one to reuse** |

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
