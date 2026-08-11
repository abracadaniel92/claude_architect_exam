# Domain 3 Drill — Claude Code Configuration & Workflows (15 questions)

**20% of the exam**, about 12 of 60 questions.

You scored 4 out of 6 in Set 1. You missed Q9 (`@import` vs path rules) and Q12 (using plan mode
when it was not needed). Both of those appear again here.

This is the easiest domain to improve. It is mostly memorisation: file paths, frontmatter keys,
and command-line flags. Every mistake here is a fact you can learn in one day.

**The questions use exam-level English.** The explanations are in simple English.

Time: 30 minutes. Answers below — cover them while you work.

---

**Q1.** A new engineer joins and reports that Claude Code ignores the team's error-handling
conventions, while everyone else's sessions apply them correctly. The conventions are documented
and were working before she joined. Where should you look first?

A. The conventions are in a user-level `~/.claude/CLAUDE.md`, which is not shared via version control.
B. The project CLAUDE.md exceeds the size at which later sections stop being loaded.
C. Her local `.claude/settings.json` may be overriding the project configuration.
D. Her Claude Code version predates `.claude/rules/` support.

---

**Q2.** Your monorepo has four packages. Each has a maintainer who should decide which of eight
shared standards documents apply to their package. You want no duplication of those documents.
What is the right mechanism?

A. A root CLAUDE.md containing all eight documents under per-package headers.
B. Eight skills in `.claude/skills/`, one per standards document, invoked as needed.
C. `.claude/rules/` files with `paths:` globs, one per package directory.
D. A CLAUDE.md in each package directory that uses `@import` to reference the applicable standards files.

---

**Q3.** Your Terraform configuration lives under `terraform/` and has conventions that apply only
when editing those files. You want them loaded automatically, and only then. What do you create?

A. A section in the root CLAUDE.md headed "Terraform conventions."
B. `terraform/CLAUDE.md` with the conventions.
C. A `.claude/rules/` file with YAML frontmatter `paths: ["terraform/**/*"]`.
D. A skill in `.claude/skills/terraform/SKILL.md` with `argument-hint`.

---

**Q4.** Your test files sit beside the code they test — `Button.test.tsx` next to `Button.tsx`,
`auth.test.ts` next to `auth.ts` — across roughly 60 directories. All tests must follow one set
of conventions. Which approach works, and why do the others fail? Select the correct approach.

A. A `.claude/rules/` file with `paths: ["**/*.test.*"]`.
B. A skill containing the testing conventions, invoked before writing tests.
C. A `CLAUDE.md` in each of the 60 directories.
D. A root CLAUDE.md section titled "Testing conventions."

---

**Q5.** Claude Code behaves inconsistently across sessions in the same repo — sometimes applying
your commit conventions, sometimes not. What is the first diagnostic step?

A. `claude --resume`
B. `/compact`
C. Delete and recreate `.claude/`
D. `/memory`

---

**Q6.** You've written a `/security-review` command your whole team should get automatically on
`git pull`. Where does the file go?

A. A `commands` array in `.claude/config.json`
B. `~/.claude/commands/security-review.md`
C. `.claude/commands/security-review.md`
D. `.claude/skills/security-review/SKILL.md`

---

**Q7.** Your team has a shared `/deploy-check` skill. You want a personal variant that also runs
your own extra linters, without changing your teammates' behavior. What do you do?

A. Create `~/.claude/skills/deploy-check/SKILL.md`, overriding the project skill by name.
B. Create a variant in `~/.claude/skills/` **with a different name**.
C. Add your linters to `~/.claude/CLAUDE.md`.
D. Edit `.claude/skills/deploy-check/SKILL.md` and add your linters behind a conditional.

---

**Q8.** Match each SKILL.md frontmatter option to the problem it solves. **(Select three correct
pairings.)**

A. Skill produces thousands of lines of analysis that displace the main task → `context: fork`
B. Skill should load automatically when editing matching files → `paths:`
C. Skill could delete files if it misinterprets an instruction → `allowed-tools`
D. Developers invoke the skill without the parameter it needs → `argument-hint`

---

**Q9.** You need to decide between a skill and CLAUDE.md for two pieces of content: (i) your
team's universal naming and error-handling standards, and (ii) a multi-step database migration
procedure used a few times a quarter. Which goes where?

A. (i) a skill — so it can restrict tools; (ii) CLAUDE.md — so it's always available when needed.
B. Both in CLAUDE.md; skills are for tool restrictions only.
C. Both as skills, invoked by a rule in `.claude/rules/`.
D. (i) CLAUDE.md — always-loaded universal standards; (ii) a skill — on-demand, task-specific workflow.

---

**Q10.** You must migrate a library used in 45+ files, and there are two viable migration
strategies with different infrastructure implications. Which approach?

A. Plan mode to explore the codebase and design the approach, then direct execution to implement the chosen plan.
B. Plan mode throughout, including implementation.
C. Direct execution with a detailed upfront specification of the target state.
D. Direct execution, switching to plan mode if unexpected complexity appears.

---

**Q11.** A stack trace identifies a missing null check on line 88 of `dateUtils.ts`. The fix is
one conditional. Which approach?

A. Spawn an Explore subagent to map usage, then direct execution.
B. Plan mode, then direct execution.
C. Direct execution.
D. Plan mode, because `dateUtils` is imported in many places.

---

**Q12.** During a multi-phase refactor, the discovery phase produces enormous output — file
listings, dependency traces, search results — and by phase three the main agent is giving
inconsistent answers about what it found in phase one. Which two mechanisms address this?
**(Select two.)**

A. Use the Explore subagent for the verbose discovery phases, returning summaries.
B. Restart the session between each phase with no carryover.
C. Maintain a scratchpad file of key findings and reference it in later phases.
D. Increase the session's context window setting.

---

**Q13.** Your CI job runs:
```
claude "Review this PR for security issues" --output-format json
```
The job hangs indefinitely; logs show it waiting for interactive input. Which single change
fixes it?

A. Set `CLAUDE_HEADLESS=true`.
B. Add `-p`.
C. Redirect stdin from `/dev/null`.
D. Add `--json-schema` so it terminates once valid output is produced.

---

**Q14.** Your CI review posts findings as inline PR comments via a script that parses Claude
Code's output. The parser breaks whenever the prose format shifts. Which two flags make the
output reliably machine-parseable? **(Select two.)**

A. `--print`
B. `--output-format json`
C. `--strict`
D. `--json-schema`

---

**Q15.** Your CI review runs again after each new commit. Developers complain that resolved and
unresolved issues alike are re-posted every run, burying new findings. Separately, your
test-generation job keeps proposing tests for scenarios already covered. What addresses both?
**(Select two.)**

A. Include prior review findings in context and instruct Claude to report only new or still-unaddressed issues.
B. Document testing standards and available fixtures in CLAUDE.md.
C. Run both jobs only once, at PR open time.
D. Provide the existing test files in context so generation avoids duplicate scenarios.

---
---

# Answers

**Q1 — A.** A user-level `~/.claude/CLAUDE.md` works only for that one person. It is **not shared
through version control**. Everyone else set it up on their own machine. The new engineer never
did. The guide names this exact diagnosis.
- **B** — this failure does not exist.
- **C** — possible in real life, but the question says it works for everyone else. That points to
  something they each have locally, not something extra that she has.
- **D** — this failure does not exist.

**Q2 — D.** `@import` references other files, so CLAUDE.md stays small. Each package includes only
the standards that apply to it, chosen by its maintainer, with no copying. The question gives two
requirements — the maintainer chooses, and nothing is duplicated. Both point here.
- **A** — copies content, and maintainers have no control.
- **B** — skills must be called. Standards must always apply.
- **C** — **the close answer, and the one you missed in Set 1.** Path globs are correct when
  conventions apply to files **by type across many folders**. Here the boundaries are clean
  folders, and the requirement is choosing between shared documents. Globs would force you to
  copy the eight documents into four rule files.

**Q3 — C.** `.claude/rules/` with `paths: ["terraform/**/*"]` — this is the guide's own example.
It loads only when you edit a matching file, which keeps unrelated context out and saves tokens.
- **A** — always loaded, so it fails the "only then" requirement.
- **B** — **this works, but it is the weaker choice.** A directory CLAUDE.md only covers one
  folder. A path rule is explicit and still works if the files move or the pattern grows.
- **D** — skills must be called. The requirement says automatic.

**Q4 — A.** Glob patterns apply conventions **by file type, in any folder**. This is exactly the
case the guide uses to explain the difference between path rules and directory CLAUDE.md files.
- **B** — needs to be called, or the model must choose to load it. The question says automatic.
- **C** — CLAUDE.md files only cover one folder. 60 copies is impossible to maintain, and they
  will slowly become different from each other.
- **D** — the model has to **guess** which section applies, instead of matching a pattern.

**Q5 — D.** `/memory` shows which memory files are loaded. The guide names it as the tool for
diagnosing inconsistent behaviour between sessions.
- **A** — continues a session. It does not diagnose configuration.
- **B** — reduces context size. It does not show which files are loaded.
- **C** — destroys the evidence before you have looked at it.

**Q6 — C.** Project commands live in `.claude/commands/`. They are version-controlled, so everyone
gets them automatically when they clone or pull.
- **A** — `.claude/config.json` with a `commands` list **does not exist**.
- **B** — personal only, not shared.
- **D** — a skill is a different thing. The question describes a slash command.

**Q7 — B.** The guide says: create personal versions in `~/.claude/skills/` **with a different
name**, so teammates are not affected.
- **A** — **the trap.** The same name in user scope makes it unclear which version runs. The guide
  says to use a different name for exactly this reason.
- **C** — CLAUDE.md holds always-loaded standards, not a workflow you call.
- **D** — changes the shared skill, which is what you were told not to do.

**Q8 — A, C and D.** These are the three real SKILL.md frontmatter keys, each matched to its
purpose. `context: fork` keeps long or exploratory output out of the main conversation.
`allowed-tools` limits which tools the skill may use — the guide's example is allowing only file
writing, to prevent destructive actions. `argument-hint` asks the developer for a missing
parameter.
- **B** — `paths:` belongs to **`.claude/rules/`, not SKILL.md**. Mixing these two sets of keys is
  the most common mistake in Domain 3.

**Q9 — D.** The guide's rule: skills are **called when needed, for specific tasks**. CLAUDE.md is
**always loaded, for universal standards**.
- **A** — wrong on both counts.
- **B** — `allowed-tools` is one feature of skills, not their purpose.
- **C** — standards that always apply should not need to be called.

**Q10 — A.** Plan mode is for large changes, several possible approaches, architectural decisions,
and changes across many files. The guide names "library migrations affecting 45+ files" and
"choosing between integration approaches with different infrastructure requirements" as examples.
It also lists combining plan mode for investigation with direct execution for the work.
- **B** — goes too far. Plan mode is for the design phase.
- **C** — assumes you already know the right structure, without exploring.
- **D** — the complexity is **already in the requirements**. It is not something that might appear
  later.

**Q11 — C.** One file, clear scope, and the exact line is known. Direct execution.
- **A** — the Explore subagent is for noisy discovery in multi-phase work.
- **B** — plan mode adds a step with nothing to decide.
- **D** — **this is the one you missed in Set 1.** A shared utility does not make a null check
  architectural. Plan mode is triggered by unclear scope or unclear design, not by how many files
  import something.

**Q12 — A and C.** Two different techniques that work together. **A** stops the long output
entering the main conversation at all. **C** saves the key findings to a file, which is the
guide's named fix for context degradation — the symptom is inconsistent answers about earlier
discoveries.
- **B** — throws away the coordination that the main agent exists to provide.
- **D** — no such setting exists, and a bigger context does not fix degradation anyway.

**Q13 — B.** `-p` (`--print`) is the documented non-interactive mode. It reads the prompt, prints
the result, and exits.
- **A** — this environment variable does not exist.
- **C** — a Unix workaround that does not address Claude Code's command syntax. The guide rejects
  it by name.
- **D** — controls the output structure. It has nothing to do with waiting for input.

**Q14 — B and D.** `--output-format json` together with `--json-schema` produces structured output
that a script can read and post as inline pull request comments.
- **A** — `--print` fixes the hanging problem, not the output structure. You need it in CI, but it
  is not what this question asks.
- **C** — this flag does not exist.

**Q15 — A and D.** Two separate skills for the two separate problems in the question. Include the
earlier findings and tell Claude to report only new or still-unfixed issues. Give it the existing
test files so it does not repeat scenarios.
- **B** — a real and useful practice. Documenting standards and fixtures in CLAUDE.md improves
  test quality. But it fixes test **quality**, not the **duplication** the question describes.
  Right technique, wrong problem.
- **C** — reduces coverage instead of improving the system.

---

## Score

___ / 15 · Q8, Q12, Q14 and Q15 need more than one answer. Q8 needs three.

**Below 11 is a problem here.** Domain 3 is 20% of the exam and is almost entirely memorisation.
That means mistakes in this domain are the easiest points on the whole test to win back.

Put every mistake onto the memory table at the bottom of
`notes/domain-3-claude-code-config.md`. Recite it each day, together with the Domain 4 facts.

**13 or more** — you are finished with this domain until day 17.
