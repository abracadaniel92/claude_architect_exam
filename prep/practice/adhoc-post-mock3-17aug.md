# Ad-hoc set — 17 August (20 questions), built on Mock 3's misses

Written straight after Mock 3 (49/60). **Not blueprint-weighted on purpose.** The spread is
deliberately skewed to where the misses were:

| Domain | Questions | Why |
|---|---|---|
| D3 — mechanism choice | 8 (Q1–Q8) | All four D3 misses were grouping questions, answered with each other's mechanisms |
| D5 — sampling and escalation | 5 (Q10, Q16, Q17, Q19, Q20) | The high-confidence sample is missed three times; the explicit-request rule slipped again |
| D4 — schema direction | 3 (Q13–Q15) | Nullable lost to a post-processing check |
| D1 — loop and subagent mechanics | 3 (Q9, Q11, Q12) | The `!= end_turn` row, and the omitted "through the coordinator" letter |
| D2 — MCP scoping | 1 (Q18) | An invented "disabled by default" server was chosen over a documented path |

Q1–Q5 are the same decision asked five times, with five different correct answers. Q6 asks for the
discriminator itself. Q7–Q10 are four mechanisms that all sound like "keep the context clean" and
are not interchangeable.

Three questions ask for **two answers**: Q12, Q15, Q17.

**The questions use exam-level English.** The explanations are in simple English.

Time: 30 minutes. Answers below — cover them while you work.

---

**Q1.** A secrets-handling standard must govern all work in every package of a monorepo, with no
action required from any package maintainer and no dependence on which files are being edited.

A. A `.claude/rules/` file with `paths: ["**/*"]`
B. The root CLAUDE.md
C. `@import` of the standard in every package's CLAUDE.md
D. A skill that engineers invoke when touching secrets

---

**Q2.** Storybook story files matching `**/*.stories.tsx` exist in nine of the repository's
packages. The team's conventions for writing them apply to those files and to nothing else.

A. A CLAUDE.md in each of the nine packages
B. `@import` of a shared stories document in each of the nine packages' CLAUDE.md files
C. A "Storybook" section in the root CLAUDE.md
D. A `.claude/rules/` file with `paths: ["**/*.stories.tsx"]`

---

**Q3.** The `infra/terraform/` directory has its own naming, tagging and state-file conventions.
They apply to everything inside that directory and to nothing outside it.

A. A CLAUDE.md inside `infra/terraform/`
B. A `.claude/rules/` file with `paths: ["**/*.tf"]`
C. An "Infrastructure" section in the root CLAUDE.md
D. A skill that engineers invoke before editing infrastructure

---

**Q4.** There are four shared engineering documents. Each service's team lead decides which of the
four apply to their service. Once chosen, the selected documents must govern all work in that
service. No text may be duplicated.

A. Four `.claude/rules/` files, each with `paths` globs naming the services it covers
B. Four skills, invoked by engineers when they become relevant
C. `@import` of the chosen documents in each service's CLAUDE.md
D. Copy the chosen documents into each service's CLAUDE.md

---

**Q5.** A twelve-step dependency-upgrade procedure is carried out four times a year by whoever is
on rotation. It is irrelevant the rest of the time.

A. The root CLAUDE.md
B. A `.claude/rules/` file with `paths: ["package.json"]`
C. A CLAUDE.md in the repository's `tooling/` directory
D. A skill in `.claude/skills/`

---

**Q6.** Two mechanisms are routinely confused: `@import` inside a package's CLAUDE.md, and a
`.claude/rules/` file with a `paths:` glob. Which single question distinguishes them?

A. Whether the content must load automatically, or only when someone asks for it
B. Whether the content is grouped by package, or by file type wherever that file lives
C. Whether the content is shared with the team, or personal to one engineer
D. Whether the content is a standard, or a workflow

---

**Q7.** An engineer must establish which of 200 services still call a deprecated endpoint. The
search will produce a large volume of output that has no value once the list of services exists.

A. Run the search in the main session and `/compact` afterwards
B. `fork_session` before the search, then abandon the branch
C. Dispatch an Explore subagent
D. Write the search output to scratchpad files as it arrives

---

**Q8.** Three hours into a session the context is nearly full of exploration output. The engineer
wants to carry on working in the same session, with the findings established so far still available.

A. `/compact`
B. `/memory`
C. `--resume`
D. `fork_session`

---

**Q9.** A four-agent migration job crashes at hour four and the completed work is lost. What should
be added before the job is run again?

A. `/compact` at fixed intervals during the run
B. A scratchpad file per agent, holding that agent's notes
C. A longer timeout on each agent
D. Each agent writes its state to a known location, and the coordinator loads the manifest when work
   resumes

---

**Q10.** Two hours into a single long session, the agent begins describing "typical patterns" for
the validation library instead of the specific validators it read earlier in the session. Nothing
has crashed and no tool has failed.

A. A manifest written by the coordinator at each step
B. Scratchpad files holding the key findings as they are established
C. A model with a larger context window
D. `/memory`, to confirm which files are loaded

---

**Q11.** An implementation continues the agentic loop whenever `stop_reason` is anything other than
`"end_turn"`. A response arrives with `stop_reason: "max_tokens"`, a partial text block and no
`tool_use` block. What happens, and what is correct?

A. It stops, which is correct: `max_tokens` is terminal, so the condition is equivalent in practice
B. It loops indefinitely; the fix is a maximum iteration count as the primary termination mechanism
C. It loops again with no tools to execute and a truncated turn in the history; the loop must
   continue **only** while `stop_reason` is `"tool_use"`
D. It stops, because the response contains a text block and no `tool_use` block

---

**Q12.** Two problems in a multi-agent system. Findings that one subagent hands to another do not
appear in the final report. And a subagent instructed to "carry on from the earlier analysis"
returns work unrelated to anything established so far. **(Select two.)**

A. Route every message through the coordinator, which is the only component that sees all results
B. Enable a shared-memory flag across the AgentDefinitions
C. Give the subagents a model with a larger context window
D. Write everything the subagent needs into its prompt, because subagents inherit no history

---

**Q13.** Payment remittance files are produced by the bank and always carry a payment reference. In
4% of extractions the `payment_reference` field is absent from the output, and those records are
rejected.

A. Keep the field nullable and reject nulls in a validation step
B. Make the field required in the schema
C. Add a few-shot example showing the payment reference being extracted
D. Fill the missing value from the bank statement afterwards

---

**Q14.** Purchase orders sometimes name a delivery contact and sometimes do not. When no contact is
named, the extraction returns a plausible-looking name.

A. Make the field required, so it is never omitted
B. Add a post-processing check against the customer database
C. Constrain the field to an enum of known contacts
D. Make the field optional and nullable

---

**Q15.** Two requirements for an extraction pipeline. Source documents state dates and currency
amounts in several different formats, and handling varies between runs. And records above €10,000
must never be submitted to the ERP automatically. **(Select two.)**

A. A post-processing layer that normalises dates and currency after extraction
B. Format normalisation rules in the prompt, alongside the strict schema
C. A programmatic gate that blocks automatic submission above €10,000
D. A prominent instruction in the system prompt stating the €10,000 limit

---

**Q16.** A team intends to stop reviewing the extractions their model scores as high confidence.
Which measurement tells them whether that is safe?

A. A stratified random sample of the high-confidence group, reviewed by hand
B. The model's average confidence score on that group
C. A uniform random sample drawn across all extractions
D. The historical error rate of the low-confidence group

---

**Q17.** Extraction accuracy averages 97% and the team proposes reducing human review.
**(Select two.)**

A. Increase the review sample uniformly across all extractions
B. Analyse accuracy separately by document type and by field
C. Review the extractions the model scores lowest, since those are the likeliest errors
D. Take a stratified random sample of the high-confidence extractions

---

**Q18.** One engineer wants an MCP server available in their own sessions on their own machine,
with no effect on any teammate who clones the repository.

A. `.mcp.json`, committed, with the server disabled by default and enabled locally
B. `.claude/settings.json`, in a personal servers block
C. A `.mcp.json` added to `.gitignore`
D. `~/.claude.json`

---

**Q19.** Midway through diagnosing a billing problem, the customer states that they want to speak
to a person. The agent is two tool calls away from an answer.

A. Finish the diagnosis, then escalate with the findings attached
B. Escalate only if the customer asks a second time
C. Escalate immediately
D. Offer to resolve it now, since the case is nearly solved

---

**Q20.** A customer uses strong language about a duplicate charge. The charge is straightforward,
the agent can refund it immediately, and the customer has not asked for a person.

A. Acknowledge the frustration, offer to resolve it now, and escalate only if the customer asks for
   a person
B. Escalate, because the language is strongly negative
C. Escalate, because emotionally charged cases have lower resolution rates
D. Process the refund without acknowledging the frustration

---
---

## Answers

**Q1 — B.** Grouped by **nothing** — it always applies, with no maintainer action and no dependence
on file type. That is the root CLAUDE.md.

- **A** — `paths: ["**/*"]` is a rules file pretending to be a global. Rules files load when a
  matching file is edited; "all work" includes work that edits nothing.
- **C** — `@import` requires each maintainer to choose. The question removes that.
- **D** — a skill must be invoked, so it can never hold something that must always apply.

---

**Q2 — D.** Grouped by **file type, wherever the file lives**. This is the one case `.claude/rules/`
with `paths:` is for, and the nine packages are a distraction: the grouping is the file pattern, not
the packages.

---

**Q3 — A.** Grouped by **one directory, everything in it, nothing outside**. A directory CLAUDE.md
covers exactly that subtree.

- **B** is the trap, and it is a strong one: `.tf` files can exist outside `infra/terraform/`, so the
  glob applies the conventions where the question says they must not apply.

---

**Q4 — C.** Grouped by **package or service, with the maintainer choosing**, and no duplication.
That is `@import`. Note the wording the exam uses: the lead **chooses**, which feels like invoking,
but after the choice the documents apply to **all** work in the service. That is authoring-time
selection, not run-time invocation.

- **B** — skills load only when invoked, so they cannot govern all work.
- **D** — duplicates text, which the question forbids.

---

**Q5 — D.** Grouped by **the moment someone asks for it**: a procedure, run occasionally, irrelevant
the rest of the time. That is a skill.

---

**Q6 — B.** The discriminator is the **grouping**, and nothing else. Package → `@import`. File type
→ `.claude/rules/` with `paths:`.

- **A** describes the difference between `@import` and a **skill**, not between `@import` and rules
  files.

Q1–Q6 are one question asked six ways. If any of Q1–Q5 was wrong, the fix is not to re-read the
table — it is to say the sentence *"this content is grouped by ___"* before looking at the options.

---

**Q7 — C.** Noisy discovery whose output has no later value → an Explore subagent, which keeps it
out of the main context in the first place.

- **A** lets the damage happen and then repairs it.
- **B** `fork_session` branches an analysis to compare approaches; it is not a context-hygiene tool.
- **D** scratchpads preserve findings that would otherwise decay — a different problem.

---

**Q8 — A.** Reduce context inside a **running** session, keeping what has been established →
`/compact`. `/memory` only lists loaded memory files; `--resume` and `fork_session` both leave the
current session.

---

**Q9 — D.** Crash recovery is **manifests**, loaded by the coordinator when work resumes.

- **B** is the scratchpad answer, which addresses degradation, not crashes.

---

**Q10 — B.** "Typical patterns" instead of the specifics it read is the textbook signal of context
**degradation** → scratchpad files, written as findings are made.

Read Q7, Q8, Q9 and Q10 together. Four mechanisms, four different problems: keep noise out
(Explore) · shrink a live session (`/compact`) · survive a crash (manifest) · stop findings decaying
(scratchpad). They are never interchangeable, and **C in Q10 is the permanent wrong answer about
context windows.**

---

**Q11 — C.** The loop continues on **one** value: `"tool_use"`. `max_tokens` is not `end_turn`, so
the faulty condition loops with nothing to execute. Note why "not `end_turn`" is genuinely wrong
rather than merely imprecise: `max_tokens`, `refusal`, `pause_turn` and
`model_context_window_exceeded` all fail it too.

- **B** promotes a safety limit to the termination mechanism — one of the four named wrong ways to
  stop.
- **D** inspects block types, which is another of the four.

---

**Q12 — A and D.** Two symptoms, two rules. Findings lost between subagents → all messages go
**through the coordinator**; subagents never communicate directly. A subagent with no idea what came
before → put it in the **prompt**, because subagents inherit nothing.

- **B** is an invented flag. **C** is the context-window answer again.

---

**Q13 — B.** The source **always** contains the value and the failure is **omission** → `required`
guarantees the field cannot be left out.

- **A** is the long-running trap: it keeps the fabrication risk *and* adds rejections.
- **D** repairs downstream what the schema should have required.

---

**Q14 — D.** The source **may not** contain the value and the model is **inventing** one → optional
and nullable. Read with Q13: same rule, opposite directions, decided by the **source** and never by
which failure you saw most recently.

- **B** is the defensible late fix that cost a mark on Mock 3.

---

**Q15 — B and C.** Two requirements, two layers. Inconsistent formats in the source → normalisation
rules in the **prompt**: the schema fixes the *type*, the prompt fixes the *format*. "Must never"
plus a monetary threshold → a **programmatic gate**.

- **A** is a post-processing layer, which needs a branch per variant and breaks on the first layout
  nobody anticipated.
- **D** puts a hard limit in a prompt, which has a non-zero failure rate.

---

**Q16 — A.** The group you are about to **stop reviewing** is the only group whose true error rate
matters, so sample **it**, at random and stratified, and check by hand.

- **B** asks the scores to validate themselves.
- **C** spreads effort over a population that includes the group you will keep reviewing anyway.
- **D** measures the group that stays under review.

---

**Q17 — B and D.** A high average hides a bad segment → analyse by document type and by field. And
review is about to stop for the high-confidence group → sample that group, stratified.

- **C** is the same error in its most persuasive form: reviewing what the model already doubts tells
  you nothing about what it is confident and wrong about.

Q16 and Q17 are the same fact twice, once alone and once as the second letter of a select-two, which
is where it has been lost three times.

---

**Q18 — D.** Personal MCP servers live in `~/.claude.json`. Anything under `~/` is personal and does
not travel through version control.

- **A** invents a "disabled by default" mechanism and still ships the server to everyone.
- **B** invents a personal servers block.
- **C** solves it by omission where a documented location already exists.

---

**Q19 — C.** The customer **explicitly asked** for a person → escalate immediately. Being close to
an answer does not change it, and A is the answer that reads as most professional, which is why it is
offered.

---

**Q20 — A.** The customer has **not** asked for a person and the problem is solvable now →
acknowledge, resolve, escalate only on request.

- **B** and **C** escalate on **sentiment**, which is never a valid signal: anger does not measure
  case difficulty.

Q19 and Q20 are the pair the exam builds to look identical. The discriminator is one thing only:
**did they ask for a human?**

---

## Score

Record it here, with the count of D3 grouping questions right out of six (Q1–Q6), and whether Q16
and Q17 both came out clean.

Target: **20/20 on Q1–Q6, Q16 and Q17.** Those eight are the ones the log says are unlearned. The
rest of the set is there so the eight are not obvious.
