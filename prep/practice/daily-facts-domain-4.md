# Domain 4 — Daily Fact Drill (5 minutes)

**Why this file exists:** your day-1 diagnostic scored 1/5 in Domain 4, on 20% of the exam.
Three of the four misses (Q13, Q14, Q15) were flat recall failures — for those, the treatment is
spaced repetition, not more study time. The fourth (Q17) was applying a rule too widely; this
drill does not cover it, so re-read `01-answer-patterns.md` as well.

**How to use it:** once a day, every day, from day 2 to day 19. Cover the right column, recite
aloud, uncover. Under 5 minutes. Mark anything you miss twice in a row with a ✗ and drill only
those the next day.

Do **not** skip days. Eighteen 5-minute reps beat one 90-minute session; that's the entire point.

---

## Block A — Schema design (Q13's block)

| Prompt | Answer |
|---|---|
| Model fabricates plausible values for missing data. Cause? | The field is marked **required** in the schema |
| Fix? | Make it **optional / nullable** |
| Why does required cause fabrication? | The model must produce *something* to satisfy the schema |
| Extensible category that may not fit the enum? | Enum value `"other"` **+ a detail string field** |
| Ambiguous case, can't determine the value? | Enum value `"unclear"` |
| Source formatting is inconsistent (dates, currency)? | **Format normalization rules in the prompt**, alongside the strict output schema |
| Strict schemas eliminate which errors? | **Syntax** errors only |
| Which errors do they NOT prevent? | **Semantic** — line items that don't sum, values in the wrong fields |
| Detect a total mismatch? | Extract **`calculated_total` alongside `stated_total`** |
| Flag inconsistent source data? | A **`conflict_detected`** boolean |
| Analyze which code constructs trigger dismissed findings? | A **`detected_pattern`** field on each finding |

---

## Block B — `tool_choice` (Q14's block)

| Value | Behavior | Use it when |
|---|---|---|
| `{"type": "auto"}` | Model decides; **may return text instead of calling a tool** | Default. Never the fix for "it returned text instead of extracting" |
| `{"type": "any"}` | **Must** call a tool, chooses which | Multiple schemas, document type unknown; guarantee structured output |
| `{"type": "tool", "name": "..."}` | Must call **that** tool | Force `extract_metadata` before enrichment, then continue in follow-up turns |
| `{"type": "none"}` | Cannot use tools | Exists in the API; not tested by the guide |

One-line version: **auto may talk · any must act · forced picks the actor.**

---

## Block C — Retry limits (Q15's block)

| Prompt | Answer |
|---|---|
| Retry **works** for which failures? | **Format mismatches** and **structural output errors** |
| Retry is **useless** for which? | The information is **absent from the source document** (e.g. exists only in a document not supplied) |
| What goes in the retry request? | Original document **+** the failed extraction **+** the **specific** validation errors |
| Which error class does tool use already eliminate? | Schema **syntax** errors |
| Which class survives and needs validation? | **Semantic** errors |

---

## Block D — Message Batches API

| Prompt | Answer |
|---|---|
| Cost | **50%** savings |
| Processing window | up to **24 hours** |
| Latency SLA | **None guaranteed** |
| Request/response correlation | **`custom_id`** |
| Multi-turn tool calling in one request? | **Not supported** |
| Appropriate for? | Non-blocking, latency-tolerant: overnight reports, weekly audits, nightly test generation |
| Inappropriate for? | Blocking workflows — pre-merge checks, pre-commit hooks |
| A batch fails on some documents. Resubmit what? | **Only the failed ones**, identified by `custom_id`, with modifications (chunk oversized docs) |
| Guarantee a 30-hour SLA with a 24-hour window? | Submit every **4 hours** |
| Before batching 10,000 documents? | **Refine the prompt on a sample set** to maximize first-pass success |

---

## Block E — Criteria and few-shot

| Prompt | Answer |
|---|---|
| "Be conservative" / "only high-confidence findings" — effect on precision? | **None.** Vague instructions don't improve precision |
| What does work? | **Specific categorical criteria**: which issue classes to report (bugs, security) vs skip (minor style) |
| Example of vague vs explicit | "Check comments are accurate" → "Flag comments only when claimed behavior **contradicts** actual code behavior" |
| One category has 40% false positives, another 5%. Effect? | The bad category **undermines trust in the accurate one** |
| Remedy? | **Temporarily disable** the high-FP category while improving its prompt |
| Consistent severity classification? | Explicit severity criteria **with concrete code examples per level** |
| How many few-shot examples? | **2–4**, targeted |
| Target them at which cases? | The **ambiguous** ones, not the obvious ones |
| What should each example show? | The **reasoning for choosing one action over plausible alternatives** |
| Key benefit beyond format? | **Generalization to novel patterns**, not just matching pre-specified cases |
| When does few-shot lose? | When the root cause is a **tool description** problem, or when **deterministic compliance** is required |

---

## Block F — Multi-pass review

| Prompt | Answer |
|---|---|
| Why is self-review weak? | The model **retains reasoning context from generation** and won't question its own decisions |
| Better than self-review instructions or extended thinking? | An **independent review instance** with no prior reasoning context |
| 14-file PR, inconsistent depth and contradictory findings. Cause? | **Attention dilution** |
| Fix? | **Per-file local passes + a separate cross-file integration pass** |
| Does a bigger context window fix it? | **No** — larger windows don't solve attention quality |
| Does 3-runs-flag-if-2-agree fix it? | **No** — suppresses real bugs caught intermittently |
| Is self-reported confidence ever acceptable? | Yes — **alongside each finding**, to route reviewer attention. Never as an autonomy/escalation trigger |

---

## Weekly self-test

Every 7th day, write these out from a blank page instead of reading:

1. The four `tool_choice` values and one exam use for each.
2. Why required schema fields cause fabrication, and the fix.
3. The two retryable error classes and the one non-retryable one.
4. Five facts about the Message Batches API.
5. Why "be conservative" fails and what replaces it.
6. Two things that do **not** fix attention dilution.

If you can do all six cold by day 14, Domain 4 is no longer your weak domain.
