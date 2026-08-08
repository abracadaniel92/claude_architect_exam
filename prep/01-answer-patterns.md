# How the Exam Builds Its Questions

Read this first. Re-read it on day 19.

This file is not about facts. It is about **how the questions are written**. If you understand
the pattern, you can remove wrong answers even when you are unsure of the right one.

All 12 sample questions in the official guide follow the same pattern.

---

## Part 1 — The main rule

For every question, ask two things, in this order.

### Question 1: What is the real cause of the problem?

The question text almost always tells you. Look for it.

Example from the guide (Sample Q7): "the coordinator's logs show it split the topic into three
subtasks." The text names the coordinator. So every answer that blames a different agent is
wrong.

### Question 2: What is the **smallest** change that fixes that cause?

Not the biggest change. Not the most advanced one. The smallest change that solves the problem
the text describes.

If two answers both fix the real cause, choose the simpler one.

**One exception:** if the question says the fix must be guaranteed, choose the strong method
instead. See Part 2.

---

## Part 2 — The strength ladder

Some fixes are weak but cheap. Some are strong but expensive. The exam wants the **weakest fix
that still meets the requirement**.

Here is the ladder, from weakest to strongest:

| Level | Fix | Choose it when |
|---|---|---|
| 1 | Write better **tool descriptions** | The model picks the wrong tool, and the descriptions are short or too similar |
| 2 | Add **few-shot examples** (2–4 examples in the prompt) | Behaviour is inconsistent in unclear cases |
| 3 | Write **explicit criteria** in the prompt | Too many false alarms; the current instruction is vague |
| 4 | Use **programmatic enforcement** (hooks, prerequisite gates, forced `tool_choice`) | The rule must always work |
| 5 | Build a **separate classifier or ML system** | Almost never the right answer on this exam |

**"Programmatic enforcement"** means: code checks the rule, not the model. The model cannot skip
it.

**"Prerequisite gate"** means: block step B until step A has finished.

### When does level 4 win?

Level 4 beats levels 1–3 when the question mentions any of these:

- Money (refunds, payments, billing)
- Identity checks
- Policy limits or thresholds
- The words **deterministic**, **guaranteed**, **must**, or **never**

Reason from the guide: prompt instructions have a "non-zero failure rate." That means they fail
sometimes. Sometimes is not acceptable when money is involved.

**Examples:**
- Sample Q1 — the agent must verify the customer before a refund. Money. → Level 4.
- Sample Q2 — the agent picks the wrong tool; descriptions are short. No money. → Level 1.
- Sample Q3 — the agent escalates the wrong cases. No money. → Level 2 and 3.

---

## Part 3 — The five kinds of wrong answer

Every wrong answer in the guide's samples is one of these five kinds. Learn to see them.

### Kind 1 — Too big a solution

It builds new systems before trying simple fixes.

**Words that signal this:** "train a classifier", "deploy a separate model", "add a routing
layer", "build a service".

Examples from the guide:
- Q2-C: a routing layer that reads user input before every turn. The guide calls this
  "over-engineered."
- Q3-C: a classifier trained on old tickets. The guide says this "requires labeled data and ML
  infrastructure when prompt optimization hasn't been tried."

### Kind 2 — It blames a part that works

The question tells you which part is broken. Any answer pointing at a different part is wrong.

Example: Q7-A, Q7-C and Q7-D all blame agents that the guide says were "working correctly within
their assigned scope."

### Kind 3 — The feature does not exist

The answer sounds confident but describes a flag or file that is not real.

**Not real:**
- `--batch`
- `CLAUDE_HEADLESS=true`
- `.claude/config.json` with a `commands` list

**Real:**
`-p` / `--print` · `--output-format json` · `--json-schema` · `.claude/commands/` ·
`.claude/skills/` · `.claude/rules/` · `.mcp.json` · `~/.claude.json` · `--resume` ·
`fork_session` · `/memory` · `/compact`

If you memorise the real list, these questions become easy.

### Kind 4 — It solves a different problem

The answer is reasonable, but it fixes something the question did not ask about.

Examples:
- Q1-D: turns tools on and off. But the problem was tool **order**, not tool **availability**.
- Q3-D: uses sentiment analysis. But the problem was case **difficulty**, and the guide says
  "sentiment doesn't correlate with case complexity."

### Kind 5 — It moves the work to people, or makes things worse

Examples:
- Q12-B: ask developers to split large pull requests. The guide says this "shifts burden to
  developers without improving the system."
- Q12-D: run three reviews and report only issues found in two of them. The guide says this
  "would actually suppress detection of real bugs."

---

## Part 4 — Rules that are always true

### Never the right answer

- **Self-reported confidence** used to decide when to escalate. The model is already confident
  about the hard cases it gets wrong.
- **Sentiment analysis** used to measure how difficult a case is.
- **A bigger context window** used to fix inconsistent quality. Context size does not fix
  attention.
- **Voting across several runs** to filter results. This hides real bugs.
- **Reading the model's text** to decide when the loop should stop. Use `stop_reason` instead.
- **A fixed maximum number of loops** as the main way to stop. (As a safety limit it is fine.)
- **Hiding errors** by returning empty results and calling them a success.
- **Stopping the whole workflow** because one subagent failed.
- **Guessing** when a tool returns several matches. Ask for another identifier instead.

### Usually the right answer

- Error responses that include a category and a retry flag, instead of one generic message.
- Passing context to a subagent **in its prompt**. Subagents inherit nothing automatically.
- Splitting a large review into one pass per file, **plus** one extra pass across files.
- Using a second, separate Claude instance to review, instead of asking the same one to check
  itself.
- Making schema fields optional so the model does not invent values.
- Sending all subagent messages through the coordinator.
- Escalating at once when the customer asks for a human.

---

## Part 5 — Word signals in the question

When you see the words on the left, think of the answer on the right.

| Words in the question | What to choose |
|---|---|
| "most effective **first step**" | The cheap, simple fix (level 1–3), not the big one |
| "deterministic", "guaranteed", "must never" | Programmatic enforcement (level 4) |
| "the logs show the coordinator..." | The cause is named — fix that part |
| "minimal descriptions" | Improve the tool descriptions |
| "blocking", "developers wait" | Real-time API, not batch |
| "overnight", "next morning", "weekly" | Batch API is fine here |
| "inconsistent results", "contradictory feedback" | Split into smaller, focused passes |
| "false positives", "developer trust" | Write explicit criteria |
| "hangs", "waiting for input" | `-p` / `--print` |
| "every developer when they clone the repo" | Project scope: `.claude/...` in the repo |
| "spread throughout the codebase" | `.claude/rules/` with glob patterns |
| "dozens of files", "architectural decisions" | Plan mode |
| "single-file fix with a clear stack trace" | Direct execution |

---

## Part 6 — Questions with more than one answer

The exam tells you how many answers to select. Read that line.

Two useful patterns:

1. When it says "select two," the two answers are usually **two different layers** of a
   solution. They are not two versions of the same idea. Example: change the schema **and**
   change the prompt.
2. One answer is often obviously correct. The second correct answer is often the one that
   handles the **edge case** the first one misses.

---

## Part 7 — Your 30-second method for each question

1. Read the **last sentence** of the question first. That is what is actually being asked.
2. Look for the word signals in Part 5.
3. Remove any answer that describes a feature that does not exist.
4. Remove any answer that blames a part the question says is working.
5. From what is left, choose the answer that fixes the named cause using the **weakest method
   that still meets the requirement**.
