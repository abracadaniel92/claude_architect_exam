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
| **Booked?** | ☐ not yet — do this first |
| **Study period** | Monday 10 August – Monday 24 August (15 days) |
| **Current day** | Not started. First study day is Mon 10 Aug |
| **Next session** | Domain 1 notes, sections 1.1–1.4 |
| **Study time** | About 2 hours per day |

---

## Scores

| Date | Test | Score | Notes |
|---|---|---|---|
| 8 Aug | Set 1 (20, cold) | **11/20** | D1 2/3 · D2 2/2 · D3 4/6 · D4 **1/5** · D5 2/4 |
| 10 Aug | `/cert-exam 15` — D1 | | |
| 11 Aug | Domain 1 drill (15) | | |
| 12 Aug | `/cert-exam 15` — D2 | | |
| 13 Aug | Domain 2 drill (15) | | |
| 14 Aug | `/cert-exam 15` — D3 | | |
| 15 Aug | Domain 3 drill (15) | | |
| **16 Aug** | **Mock 1 — `/cert-exam 60`, timed** | | Record the score for every domain |
| 17 Aug | `/cert-exam 15` — D4 | | |
| 18 Aug | Domain 1 drill — **retake** | | Compare with 11 Aug |
| 19 Aug | Domain 4 drill (15) | | |
| 20 Aug | `/cert-exam 15` — D5 | | |
| 21 Aug | Domain 5 drill (15) | | |
| 22 Aug | Domain 2 + 3 drills — **retake** | | |
| **23 Aug** | **Mock 2 — 60, timed, multi-response** | | The rehearsal |

**Target before the exam:** 80%+ on practice sets, and no domain below 60%.

**On the retakes:** the score matters less than *which* questions you miss twice. A question
missed twice is a fact you have not learned. Put it on the cheat sheet.

---

## What I know about my own weak points

Updated as evidence appears. Right now, from Set 1 only:

1. **Domain 4 is the big gap — 1 out of 5, on 20% of the exam.**
   All three misses were flat facts, not reasoning: `tool_choice` values (`auto` allows text),
   required schema fields causing invented values, and which errors a retry can fix.
   → Fixed by `daily-facts-domain-4.md`, 5 minutes every day.

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

---

## Session history

| Date | What happened |
|---|---|
| 8 Aug | Identified two different exams (CCAR-F vs CCAR-P) and chose Foundations. Confirmed Foundations is accepted for Intertec partner tier. Built the full prep folder. Took Set 1 cold: 11/20. Converted everything to simple English. Found and installed the community 77-question practice exam as `/cert-exam`. Pushed everything to GitHub. |

---

## Still to be built

| Needed by | What |
|---|---|
| 19 Aug | Domain 4 drill (15 questions) |
| 21 Aug | Domain 5 drill (15 questions) |
| 23 Aug | Full mock — 60 questions, timed, **including multiple-response questions** (the community `/cert-exam` bank is single-answer only) |

---

## Decisions already made — do not revisit

- **Foundations (CCAR-F), not Professional (CCAR-P).** Confirmed as accepted for partner tier.
- **Skip the Bedrock and Google Cloud courses.** Cloud provider configuration appears exactly
  once in the 39-page guide, in the out-of-scope list.
- **Skip AI Fluency and Claude 101.** Level 100, below this exam's candidate profile.
- **Take:** Claude Code in Action (covers Claude Code *and* the Agent SDK), Intro to MCP, and
  only the tool use / prompt engineering / agents modules of Building with the Claude API.
- **The official exam guide PDF is not pushed to GitHub.** It is Anthropic partner material and
  the repository is public. It is in `.gitignore`.

---

## Useful context for a new session

- Write in plain English. English is not my first language. Keep exact exam terminology.
- Explanations in simple English; **practice questions stay at exam-level English on purpose**,
  because reading that style quickly is part of the test.
- Background: medical doctor, now in product and program management. Comfortable with
  architecture reasoning and trade-offs; less comfortable with backend implementation. This exam
  does not test backend implementation — Section 17 of the guide excludes it.
- Files are mirrored at **github.com/abracadaniel92/claude_architect_exam**.
