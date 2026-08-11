# Material Audit — 11 August 2026

Findings from a review of the study material.

**Status (updated later on 11 Aug):** **everything is closed.** All Verified items (0, 1, 2,
4a–4e) are fixed, and item 3 was adjudicated directly against `exam guide.pdf` (v1.0, July 2026),
which was in the folder — see item 3 below for the row-by-row verdicts. All three PDFs are
regenerated from the corrected sources. A second review confirmed every Verified finding and
found two extra instances of 4b the original audit missed (`LOG.md` and
`practice/daily-facts-domain-4.md`), both fixed. Purcell's 60-question set was also cross-checked:
zero contradictions with this repo's material.

**How to read the confidence column:**

- **Verified** — checked directly in these files. The contradiction is internal, so no outside
  source is needed. Fix these.
- **Docs-only** — the notes disagree with current public Claude Code / API documentation. The
  official exam guide is not in this repository, so *it could not be checked*. The guide, not the
  product, decides the exam answer. Recommendation for all of these is **annotate, do not
  overwrite**: keep the guide's answer, add a line saying what the product actually does.

---

## 0. Answer-key rebalance — DONE 11 Aug

The five practice files had a severe answer-position bias: **56 of 66 single-answer questions
were B, and D was never correct in any of them.** Every multi-answer question was A+B or A+C.
"Always answer B" scored 56/66.

Two consequences: past scores overstated knowledge, and the material was training a guessing
habit that would fail on the real exam, where D is correct about a quarter of the time.

Fixed by permuting the option order in every question and rewriting the keys and explanation
letters. Verified afterwards: the option-text multiset is byte-identical to the previous commit
in all five files, and for all 80 questions the option text at the new key letter is the same
text the old key pointed to.

New distribution across 66 single-answer questions: **A 17 · B 14 · C 17 · D 18.**

| File | A | B | C | D | Multi-answer pairs |
|---|---|---|---|---|---|
| drill-domain-1 | 3 | 3 | 3 | 3 | B+D, A+D, B+C |
| drill-domain-2 | 3 | 3 | 3 | 4 | A+D, B+D |
| drill-domain-3 | 3 | 2 | 3 | 3 | A+C+D, A+C, B+D, A+D |
| drill-domain-4 | 3 | 2 | 3 | 3 | B+D, A+D, B+C, A+C |
| set-01 | 5 | 4 | 5 | 5 | B+D |

### Consequence: the PDFs no longer match — RESOLVED 11 Aug

All three PDFs were regenerated from the corrected markdown, so the question booklet now matches
the rebalanced keys in `prep/practice/`.

---

## 1. `--json-schema` is taught as a fake flag in one place, real in four — **Verified — FIXED 11 Aug**

`practice/set-01-answers.md:235` — *"Note that three of the four options here describe things
that **do not exist**."*

Q18's four options (`set-01-questions.md:220-223`) are `CLAUDE_HEADLESS=true`, `--no-interactive`,
`-p`, and `--json-schema`. Only the first two are fake. The sentence necessarily labels
`--json-schema` as non-existent.

Contradicted by `03-cheat-sheet.md:84`, `01-answer-patterns.md:109` (an explicit "real flags"
list), `notes/domain-3-claude-code-config.md:200`, and `practice/drill-domain-3.md` Q14, where
`--json-schema` is part of the correct answer.

**Why it matters most:** "does this flag actually exist?" is one of the documented answer
patterns. Poisoning the real/fake list breaks the technique itself.

**Fix:** change to *"two of the four options describe things that do not exist; the fourth is a
real flag that solves a different problem."*

---

## 2. The retriable error field is spelled two ways — **Verified — FIXED 11 Aug** (standardised on `isRetryable`, with a note that the guide's prose sometimes writes "retriable")

| Spelling | Where |
|---|---|
| `isRetryable` | `03-cheat-sheet.md`, `exercises/README.md`, `notes/domain-2-tool-design-mcp.md` ×2, `practice/drill-domain-2.md`, `practice/set-01-answers.md`, `practice/set-01-questions.md` |
| `retriable` | `03-cheat-sheet.md`, `notes/domain-2-tool-design-mcp.md`, `practice/drill-domain-2.md` ×2 |

Both appear in the **same cheat-sheet table**. Worse: in drill 2 the *wrong* option uses
`isRetryable` and the *correct* option uses `retriable`, so it is possible to learn a spelling
cue that has nothing to do with the concept.

Neither is an MCP specification field — `isError` is the only real one — so this is pure recall
of a guide convention, and the name has to be consistent.

**Fix:** pick one spelling, use it everywhere, add a one-line note that the guide's prose
sometimes writes it the other way.

---

## 3. Product drift — **ADJUDICATED 11 Aug against exam guide v1.0 (July 2026)**

The guide PDF was in the repo folder all along (`exam guide.pdf`, gitignored). Checked directly.
**Verdict: on every row the notes already matched the guide** — the "notes say" column *is* the
exam answer. Product-drift annotations were added in the notes files (domain-3 ×2, domain-4
batches, exercises README) so the wrong mental model does not carry into real work. Row-by-row:

- **3a, 3b, 3c** — the guide states the notes' version verbatim ("restrict tool access",
  "prompt developers for required parameters", and `paths` listed only under `.claude/rules/`,
  never in the SKILL.md frontmatter set). Annotated, not changed.
- **3d** — "`@import` syntax" is the guide's own wording. Annotated.
- **3e** — "verify which memory files are loaded" is the guide's own wording for `/memory`. Annotated.
- **3f** — the guide never names `PreToolUse`; it writes "tool call interception" throughout, and
  its appendix lists "hooks (PostToolUse, tool call interception)". The asymmetry in the notes
  faithfully mirrored the guide. The real name stays as an annotation (already added).
- **3g** — the guide names only `tool_use`/`end_turn` and never counts API values, so the "six"
  claim was this repo's own added fact. **Corrected to seven** (`model_context_window_exceeded`)
  in the notes, cheat sheet, and revision card.
- **3h** — "no multi-turn tool calling support" appears word-for-word in the guide's appendix.
  Annotated with the docs' contrary position.

Independent corroboration: Matthew Purcell's 60-question set (also written against guide v1.0)
agrees with the guide on every one of these points, including using both `isRetryable` **and**
`retriable` — the guide itself uses both spellings in the same task statement, which is where
item 2's inconsistency originally came from.

| # | Location | Notes say | Docs say |
|---|---|---|---|
| 3a | `notes/domain-3-claude-code-config.md:82`, `03-cheat-sheet.md:64` | `allowed-tools` **limits** which tools a skill may use; use it to prevent destructive actions | It **pre-approves** tools for the skill's turn — i.e. grants, not restricts. `disallowed-tools` is the restricting field |
| 3b | `notes/domain-3-claude-code-config.md:83, 248`, `03-cheat-sheet.md:65`, `exercises/README.md:91` | `argument-hint` **asks the developer** for a missing parameter | It is an autocomplete display hint only. It never prompts, blocks, or collects a value — the exercise that promises a prompt will not reproduce |
| 3c | `notes/domain-3-claude-code-config.md:85`, `03-cheat-sheet.md:70`, `drill-domain-3.md` Q8 | `paths:` is **not** a SKILL.md key — "the most common mistake in this domain" | Docs list `paths` in the SKILL.md frontmatter reference, with the same glob semantics as path rules |
| 3d | `notes/domain-3-claude-code-config.md:32-38`, `03-cheat-sheet.md:47` | `@import` as a literal directive | Real syntax is a bare `@path/to/file.md`. An option showing `@docs/standards.md` should be recognisable |
| 3e | `notes/domain-3-claude-code-config.md:46`, `03-cheat-sheet.md:78` | `/memory` shows which memory files are **loaded** | `/memory` lists memory file *locations*; `/context` shows what actually loaded this session |
| 3f | `notes/domain-1-agentic-architecture.md:174, 229`, `03-cheat-sheet.md:130` | "tool call interception hook" — no event name given | The real event is **`PreToolUse`**. `PostToolUse` is named precisely everywhere, so the pair is asymmetric and there is zero name recognition if `PreToolUse` appears as an option |
| 3g | `notes/domain-1-agentic-architecture.md:30`, `03-cheat-sheet.md:98` | `stop_reason` has **six** values | Seven — `model_context_window_exceeded` is missing. The exam still tests only `tool_use` / `end_turn` |
| 3h | `notes/domain-4-prompt-structured-output.md:249`, `03-cheat-sheet.md:218`, `daily-facts-domain-4.md:66`, `02-course-map.md:156` | Batches API: multi-turn tool calling **not supported** | Batch docs list tool use and multi-turn conversations as supported. The defensible point is that a batch request is one *stateless* call, so a client-side agentic loop cannot run inside it |

**3f is the one worth adding unconditionally** — knowing the real event name costs nothing and
protects against it appearing as an option. **DONE 11 Aug:** `PreToolUse` is now named alongside
"interception hook" in the domain-1 notes, the cheat sheet, and the revision card. The rest of
item 3 is untouched, pending the guide. Treat 3a and 3c with extra care: the documented behaviour
of `allowed-tools` and `paths:` in SKILL.md is less settled than this table implies.

---

## 4. Smaller internal problems — **Verified — ALL FIXED 11 Aug**

(4b also existed in two more locations the original audit missed — `LOG.md` weak point 1, which
said "1 out of 5" and "all three misses" in the same paragraph, and
`practice/daily-facts-domain-4.md:4`. Both fixed with the others.)

**4a. Set 1's stated blueprint contradicts its own answer key.**
`practice/set-01-questions.md:3` claims D1×5 · D2×4 · D3×4 · D4×4 · D5×3. Tallying the
per-question domain labels in the answers file gives D1×3 · D2×2 · D3×6 · D4×5 · D5×4, which
matches the score table in that same file. The header line is the wrong one.

**4b. The Domain 4 miss count is wrong, and it changes a conclusion.**
Set 1 Domain 4 was 1/5 — four misses (Q13, Q14, Q15, Q17). Three files say "three misses":
`set-01-answers.md:258`, `notes/domain-4-prompt-structured-output.md:5`, `drill-domain-4.md:5`.
Q17 keeps being dropped, and it is the one miss that was **not** a flat fact — it was applying a
rule too widely. The whole Domain 4 plan rests on "my D4 gap is pure recall," and Q17 is
evidence against that.

**4c. Resume-vs-fresh is stated as a rule in one place and a threshold in another.**
`notes/domain-1-agentic-architecture.md:231` (quick review, item 9): *"Stale tool results = new
session with a summary, not `--resume`."* But `drill-domain-1.md` Q9's answer is to **resume** and
name the changed files, because only three files of a wider analysis were stale. The real rule is
about **how much** is stale, and the quick-review line drops that qualifier.
This cost a mark in practice on 10 Aug. **Also: `03-cheat-sheet.md` does not cover
resume-vs-fresh at all**, so the exam-day file has no version of it.

**4d. Required schema fields are a trap in one drill question and a virtue in another.**
`drill-domain-4.md` Q1 — required fields force the model to invent values, make them nullable.
Q12 option C — a required field is good because it cannot be omitted. Both are true; the
distinction is not stated anywhere in `notes/domain-4-prompt-structured-output.md`.
**Fix:** add one line — *required when the value is always derivable from the source; nullable
when the source may not contain it.*

**4e. Two coverage gaps.**
`notes/scenarios.md:97` omits Domain 5 from Scenario 4's domain list, although the lines below it
list scratchpads, `/compact` and manifests — all Domain 5.
`notes/domain-1-agentic-architecture.md:40-47` lists exactly three wrong ways to stop the agentic
loop, but `drill-domain-1.md` Q1 uses a fourth distractor (an explicit `task_complete` tool) that
no notes file mentions.

---

## Suggested order of work

1. ~~Item 1 — `--json-schema`. Breaks an answer technique.~~ **Done.**
2. ~~Item 2 — one spelling for the retriable field.~~ **Done — `isRetryable`.**
3. ~~Item 4c — add the "how much is stale" qualifier, and put the rule on the cheat sheet.~~ **Done — also on the revision card.**
4. ~~Item 3f — add the name `PreToolUse`.~~ **Done.**
5. ~~Items 4a, 4b, 4d, 4e — small corrections.~~ **Done, plus the LOG.md instance of 4b.**
6. ~~Item 3 (the rest) — only with the exam guide open. Annotate, do not overwrite.~~ **Done — adjudicated against the guide 11 Aug; notes matched the guide on every row, annotations added.**
7. ~~Decide about the PDFs.~~ **Done — all three regenerated.**
