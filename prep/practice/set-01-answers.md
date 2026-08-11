# Practice Set 1 — Answers and Explanations

**Your result: 11 out of 20.**

| Domain | Weight | Your score |
|---|---|---|
| D2 — Tool Design & MCP | 18% | 2/2 |
| D1 — Agentic Architecture | 27% | 2/3 |
| D3 — Claude Code Configuration | 20% | 4/6 |
| D5 — Context & Reliability | 15% | 2/4 |
| **D4 — Prompt & Structured Output** | **20%** | **1/5** ← weakest |

You missed: Q3, Q5, Q8, Q9, Q12, Q13, Q14, Q15, Q17.

Read the explanations for the questions you got **right** as well. Getting an answer right for
the wrong reason will cost you on the real exam.

---

**Q1 — A** · Domain 2

A generic error stops the agent from deciding what to do next. With
`errorCategory: "transient"` and `isRetryable: true`, the agent retries instead of telling the
customer the order does not exist.

- **B** — this **hides the error**, which is worse. It treats an access failure as an empty
  result.
- **C** — a longer timeout only delays the problem. The error message is still useless.
- **D** — the agent is not disobeying. It genuinely cannot tell "service is down" apart from "no
  such order."

---

**Q2 — B** · Domain 1

Money plus a hard requirement ("must never") means programmatic enforcement. Prompts and context
flags both fail sometimes.

- **A** — this is about which tools are **available**, not about the verification **requirement**.
  It also adds a classifier, which is too big a solution.
- **C** — few-shot examples are probabilistic. Level 2 for a level 4 problem.
- **D** — still depends on the agent choosing to check the flag. Same weakness, more code.

---

**Q3 — C** ❌ *(you answered B)* · Domain 5

**This is the most valuable question in the set.**

The customer said "just give me a human." That is an explicit request. Escalate **immediately**,
without investigating first. Also include a structured handoff summary, because the human cannot
see the conversation.

- **A** — sentiment is never an escalation signal on this exam.
- **B** — your answer. It is correct behaviour for a **frustrated** customer whose problem the
  agent can solve. It becomes wrong the moment the customer clearly asks for a human.

The guide draws this exact line, so expect it on the real exam. The test is: **did the customer
explicitly ask?**

- **D** — ignores a clear request.

---

**Q4 — B and D** ✅ · Domain 5

Two different layers. **B** stops the problem at the source, by trimming the output before it
enters the context. **D** protects the facts that summarising would destroy.

- **A** — the tokens are already used by the time the agent "ignores" them.
- **C** — a bigger context window does not fix degradation. This is never the right answer.

Notice the shape of a two-answer question: the two correct answers are **different layers**, not
two ways of saying the same thing.

---

**Q5 — D** ❌ *(you answered A)* · Domain 5

Source information is lost during **summarisation**, when findings are compressed without keeping
the link between each claim and its source. The subagent must output structured mappings: claim,
evidence excerpt, source name, publication date.

- **A** — your answer. It blames the coordinator. But the question says the subagent returns
  **prose summaries**. The coordinator cannot pass on source links that it never received.
- **B** and **C** — both blame agents further down the chain. Same mistake.

**The pattern:** the question told you what the subagent produces. Read that clause carefully.

---

**Q6 — A** ✅ · Domain 1

The Task tool starts subagents, and `allowedTools` must include `"Task"`. Without it there is no
mechanism, no matter what the prompt says.

- **B** — `.mcp.json` configures MCP servers, not subagents.
- **D** — stronger wording cannot create a missing capability.

---

**Q7 — C** ✅ · Domain 5

Record both numbers with their sources, and include the **methodology**. The two figures differ
by year *and* by region, so they may not actually disagree.

- **A** — a third source cannot settle a difference in definitions.
- **B** — an average is a number no source supports, and it hides the real difference.
- **D** — still picks one value. The guide says never choose one at random.

---

**Q8 — D** ❌ *(you answered A)* · Domain 1

Parallel means **several Task calls in one single response**.

- **A** — your answer. `fork_session` creates branches from **one shared analysis**, to compare
  different approaches. It is a real feature, used for the wrong purpose here.
- **B** — `allowedTools` is a permission list, not a concurrency setting.
- **C** — no such flag exists.

**Learn the difference:** parallel subtasks = several Task calls. Comparing approaches from one
starting point = `fork_session`.

---

**Q9 — B** ❌ *(you answered C)* · Domain 3

`@import` lets each package include the shared standards that apply to it, chosen by its
maintainer, without copying anything.

- **A** — skills must be called; standards must always apply.
- **C** — your answer, and a reasonable one. Path globs are correct when conventions apply to
  files **by type across many folders**. Here the boundaries are clean folders, and the
  requirement is choosing between shared documents.

**The deciding phrase:** "maintainers control which shared documents apply, without duplicating
them." That points to import.

- **D** — copies content and gives maintainers no control.

This was the hardest question in the set. It appears again as Q2 in the Domain 3 drill.

---

**Q10 — C** ✅ · Domain 3

`/memory` shows which memory files are loaded.

---

**Q11 — A** ✅ · Domain 3

`context: fork` runs the skill in a separate context, so its long output does not fill the main
conversation.

---

**Q12 — D** ❌ *(you answered A)* · Domain 3

One file, clear scope, and the stack trace already gives you the line. Direct execution.

- **A** — your answer. A shared utility does **not** make a null check architectural. Plan mode is
  triggered by unclear scope or unclear design, not by how many files import something.
- **B** — the Explore subagent is for noisy discovery in multi-phase work.
- **C** — expands the work beyond what was asked.

This appears again as Q11 in the Domain 3 drill, with the same bait. Watch for it.

---

**Q13 — B** ❌ *(you answered C)* · Domain 4

A **required** field forces the model to produce a value. If the document does not contain one,
the model invents it. Make the field optional and nullable.

- **A** — an instruction fighting against a structural pressure. The weakest option.
- **C** — your answer. A checksum check happens **after** the value is invented. A fabricated tax
  ID may even pass the checksum.
- **D** — examples might help, but the schema still demands a value. Fix the schema.

---

**Q14 — A** ❌ *(you answered C)* · Domain 4

`"any"` forces the model to call a tool, while letting it choose which one. That is exactly right
when the document type is unknown.

- **B** — `none` blocks tools completely.
- **C** — your answer. `auto` **allows the model to reply with text**. That is the bug described
  in the question.
- **D** — forcing one tool defeats the purpose when you do not know the type.

**Memorise:** auto may talk · any must act · forced picks the actor.

---

**Q15 — C** ❌ *(you answered A)* · Domain 4

Retries fix **format and structure** problems. Retries cannot find information that is **not in
the document**.

- **A** — your answer, which is the reverse. Format errors are the ones retries fix.
- **B** — assumes retries always work.
- **D** — says retries never work.

---

**Q16 — D** ✅ · Domain 4

Up to 24 hours and no speed guarantee, so batch is wrong for a blocking pre-commit hook and right
for an overnight job.

- **A** — a misunderstanding. `custom_id` matches results correctly.

---

**Q17 — A** ❌ *(you answered B)* · Domain 4

A category with many false alarms damages trust in the accurate categories too. Turn it off
temporarily, keep the security category running, and fix the prompt.

- **B** — your answer. Voting across passes **hides real bugs** that are only found sometimes.
  This is on the "never correct" list in `01-answer-patterns.md`.
- **C** — a confidence threshold. Not calibrated, and it does not fix the category.
- **D** — "only report what you are confident about" is exactly the vague instruction the guide
  says does not work.

---

**Q18 — C** ✅ · Domain 3

`-p` (`--print`) is the documented non-interactive mode.

Note that two of the four options (`CLAUDE_HEADLESS=true` and `--no-interactive`) describe things
that **do not exist**. `--json-schema` is a real flag, but it solves a different problem — forcing
output to follow a schema, not fixing a job that hangs waiting for input. Learning the real list
of flags makes these questions easy.

---

**Q19 — B** ✅ · Domain 3

Include the earlier findings and tell Claude to report only new or still-unfixed issues.

---

**Q20 — D** ✅ · Domain 2

"Searches code." is a very short description. The guide says to improve MCP tool descriptions so
the agent does not prefer built-in tools like Grep over better MCP tools.

- **A** — strong wording in the system prompt causes over-triggering, and the guide warns that
  prompt wording can create unwanted tool links.

---

## What your results mean

**You missed four Domain 4 questions, and three of them were facts, not reasoning.** Q13, Q14 and
Q15 each test one flat fact. Facts are quick to learn. Use `daily-facts-domain-4.md` every day.
The fourth Domain 4 miss, Q17, was **not** a fact — see the next paragraph. The Domain 4 gap is
not pure recall.

**Two mistakes were about applying a rule too widely.** Q12 (plan mode) and Q17 (voting across
passes) were both already answered in `01-answer-patterns.md`. Read that file slowly.

**Two mistakes were mechanism confusion.** Q8 (`fork_session` vs parallel Task calls) and Q5
(which component is at fault).

**One was the escalation trap.** Q3. Learn the difference between a customer who is frustrated and
a customer who explicitly asks for a human.

**What went well:** Q1, Q2, Q4, Q6, Q7, Q16 and Q20. You correctly handled structured errors,
programmatic enforcement, two-layer context management, conflicting sources, and batch versus
real-time. Your architecture reasoning is already working. The gap is recall.
