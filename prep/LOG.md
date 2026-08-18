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
| **Current day** | Day 9 of 15 — Mon 18 Aug. **Mock 4: 58/60 (97%)**, D1 16/16 · D3 12/12 · D4 12/12 · D5 9/9, and **both misses in D2 — the domain twice declared closed.** Every fact the paper was built to trap came out clean, including format normalisation after four consecutive misses |
| **Next session** | Tue 19 Aug — Domain 4 drill as planned, but first a short **D2 set**: Grep/Glob/**semantic** and business-vs-permission. Those are the two Mock 4 misses and **neither is tested by Purcell's set** (checked 18 Aug), so 23 Aug will not catch them |
| **The one thing to change** | **The repair-verb halt and the grouping question both fired on 18 Aug — keep them.** What did not fire is the third member of a triad. Q28 offered Glob, Grep and semantic, and a Grep answer was taken because the word "export" was in the question. **When a question lists two of a three-member set, name the third before answering** (weak point 44) |
| **Outstanding** | ~~Regenerate the revision card~~ — **done 17 Aug, verified 18 Aug.** Both the interview pattern and the CI/CLAUDE.md line are in `tools/make-revision-card.py` and in the regenerated PDF; the log had simply not been updated. Next open item: the **D2 set** named under *Next session*, since neither Mock 4 miss is covered by Purcell's 60 |
| **What is still untested** | **Thirteen facts that appear in Purcell's set and in none of this repo's papers** — `tool_choice` values, **escalation in either direction**, `/compact` as an answer rather than a distractor, severity consistency, plain-text-JSON → tool use, batch resubmission by `custom_id`, re-review duplicate findings, goal-oriented vs rigid subagent prompts, personal command placement, `allowed-tools` as a guarantee, `--resume` in the positive direction, multi-issue single messages, escalation package contents · **whether a deliberate 75-minute pass converts the speed misses** — still unmeasured, no first-pass time was recorded for Mock 4. See weak points 21, 29, 45 |
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
| **18 Aug** | **Mock 4 — repo set, 60 questions, built from the repeat-miss list** | **58/60 (97%)** | D1 **16/16** · D2 **9/11** ⚠ · D3 **12/12** · D4 **12/12** · D5 **9/9**. Select-two 10/10. Both misses in D2: Q28 semantic search (**5th time**) and Q52 business-vs-permission (chose *transient*). **No first-pass time recorded** — see weak point 45. Every targeted repeat miss clean: format normalisation, manifests ×2, both noun traps, `stop_reason` ×2. See weak points 44–46 |
| 17 Aug | Post-Mock-3 ad-hoc set (20, D3/D5-skewed) | **16/20** | D3 grouping **4/6** · high-confidence sample **2/2** (closed). Missed Q2 and Q4 (the two swapped mechanisms), Q9 (manifests, 2nd time) and Q15 (post-processing layer, **4th time**). **Q6, which asks for the discriminator itself, was correct** — see weak point 40 |
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

    → **Exam-day plan. Budget 75 minutes for the first pass (75 seconds per question), finishing
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

45. **The first-pass time was not recorded, which is the one measurement still missing after four
    mocks.**
    Weak point 29 named a 75-minute first pass as the single exam-day fix, and it has now gone
    unmeasured on Mocks 3 and 4. A 58 says nothing about pacing: it is consistent with a
    deliberate pass and with a fast one. **On 23 Aug write the start and end time of the first pass
    before opening the key.** That number, not the score, is what the remaining week is for.

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

---

## Session history

| Date | What happened |
|---|---|
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
| `1784098676646.pdf` | Matthew Purcell's 60-question set. Blueprint-weighted 16/11/12/12/9, 11 multiple-response, answer key with rationales. **Structure corrected 18 Aug: 6 scenarios × 10 questions, not 4 × 15** — a lighter reading load than the real exam or the repo mocks. **Cross-checked 11 Aug: zero contradictions with the repo material. Overlap quantified 18 Aug: ~45 of the 60 have a counterpart in Mock 4 alone, 15 of them closely framed** (weak point 47), so treat the score as an upper bound. Its real value is the thirteen facts it tests that no repo paper does — listed under *What is still untested* | **23 Aug** — take it cold, and record the first-pass time |
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
