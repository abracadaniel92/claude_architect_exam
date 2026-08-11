# Domain 3 — Claude Code Configuration & Workflows (20%)

About 12 of the 60 questions come from here. There are 6 task statements.

This domain is mostly **memorisation**: file paths, frontmatter keys, and command-line flags.
That makes it the easiest domain to improve quickly. If you learn the tables in this file, you
will get these questions right.

---

## 3.1 The CLAUDE.md hierarchy

**CLAUDE.md** is a file with instructions that Claude Code loads automatically.

There are three levels:

| Level | Path | Shared with your team? |
|---|---|---|
| **User** | `~/.claude/CLAUDE.md` | ❌ **No.** Only for you |
| **Project** | `.claude/CLAUDE.md` or `CLAUDE.md` in the repository root | ✅ Yes |
| **Directory** | `CLAUDE.md` inside a subfolder | ✅ Yes, but only for that folder |

### The standard exam question

A new team member does not get the team's instructions. Everyone else does.

**Cause:** the instructions are in a **user-level** file (`~/.claude/CLAUDE.md`). This file is not
shared through version control.

**Fix:** move them to the project level.

### `@import`

`@import` lets one CLAUDE.md file reference another file. This keeps files small and avoids
copying the same text into several places.

Example: each package has its own CLAUDE.md, and imports only the standards documents that apply
to it. The package maintainer chooses which ones.

### `.claude/rules/`

This folder holds separate rule files by topic, instead of one very large CLAUDE.md.

Example files: `testing.md`, `api-conventions.md`, `deployment.md`.

### `/memory`

This command shows which memory files are currently loaded.

Use it when Claude Code behaves differently in different sessions.

> **Product note.** The guide says exactly this ("verify which memory files are loaded"), so it
> is the exam answer. In the shipping product `/memory` lists memory file *locations* and
> `/context` shows what actually loaded. Likewise `@import` is the guide's name for the import
> syntax; the shipping product uses a bare `@path/to/file.md`. Answer the guide's way.

---

## 3.2 Slash commands and skills

| Type | Project scope (shared) | User scope (personal) |
|---|---|---|
| **Slash commands** | `.claude/commands/` | `~/.claude/commands/` |
| **Skills** | `.claude/skills/` | `~/.claude/skills/` |

### Sample Q4 in the guide

You want a `/review` command that every developer gets when they clone the repository.

**Answer:** `.claude/commands/` inside the repository.

The wrong answers:
- `~/.claude/commands/` — personal, not shared
- CLAUDE.md — holds context, not command definitions
- `.claude/config.json` with a `commands` list — **this does not exist**

### SKILL.md frontmatter

A skill is a folder containing a `SKILL.md` file. The top of that file has settings called
**frontmatter**.

Three keys are tested:

| Key | What it does | Use it when |
|---|---|---|
| `context: fork` | Runs the skill in a **separate context**, away from the main conversation | The skill produces a lot of output (codebase analysis) or exploratory output (brainstorming) that would fill up the main conversation |
| `allowed-tools` | Limits which tools the skill may use | You want to prevent destructive actions. Example: allow only file writing |
| `argument-hint` | Asks the developer for a missing parameter | The skill needs a parameter and was called without one |

**Important:** `paths:` is **not** a SKILL.md key. It belongs to `.claude/rules/`. Mixing these
two sets of keys is the most common mistake in this domain.

> **Product note (checked against exam guide v1.0, July 2026 — answer the exam the guide's way).**
> The guide confirms all three rows above, and lists exactly these three SKILL.md keys. In the
> shipping product the behaviour has drifted: `allowed-tools` *pre-approves* tools rather than
> hard-restricting them, `argument-hint` is only an autocomplete display hint and never prompts,
> and current docs do list `paths` for SKILL.md. On the exam, use the table and the rule above.

### Personal versions of a shared skill

Create your version in `~/.claude/skills/` **with a different name**. This way your teammates are
not affected.

### Skill or CLAUDE.md?

- **Skill** = called when needed, for a specific task.
- **CLAUDE.md** = always loaded, for universal standards.

---

## 3.3 Path-specific rules

Files in `.claude/rules/` have YAML frontmatter with a **`paths`** field. It contains glob
patterns.

```yaml
---
paths: ["terraform/**/*"]
---
```

The rule loads **only** when you edit a matching file. This keeps unrelated instructions out of
the context and saves tokens.

### The key comparison (Sample Q6)

When conventions apply to files **spread across many folders**, use glob rules. Do **not** use
directory-level CLAUDE.md files.

**The standard example:** test files sitting next to their source code.
`Button.test.tsx` is next to `Button.tsx`, in 60 different folders.

`paths: ["**/*.test.tsx"]` applies the conventions by **file type**, wherever the file is.
A directory CLAUDE.md cannot do this, because it only covers one folder.

Why the other options in Q6 are wrong:
- All conventions in the root CLAUDE.md, under headings → the model must **guess** which section
  applies. Guessing is unreliable.
- A skill per code type → skills need to be **called**. The question asked for automatic.
- A CLAUDE.md in each subfolder → it only covers one folder, so it cannot handle files spread
  everywhere.

---

## 3.4 Plan mode or direct execution?

**Plan mode** means Claude explores and designs before making changes.
**Direct execution** means Claude changes the code immediately.

| Use plan mode | Use direct execution |
|---|---|
| Large changes | Small, clear changes |
| Several possible approaches | One obvious approach |
| Architectural decisions | A single-file bug fix with a clear stack trace |
| Changes across many files | Adding one validation check to one function |
| Prevents expensive rework | — |

### Examples from the guide

**Plan mode:** restructuring a monolith into microservices; a library migration affecting 45+
files; choosing between integration approaches that need different infrastructure.

**Direct execution:** a single-file bug fix with a clear stack trace; adding one date validation
check.

### Sample Q5 — why one answer is a trap

The trap answer says: "start with direct execution, and switch to plan mode if unexpected
complexity appears."

This is wrong because **the complexity is already described in the requirements**. It is not
something that might appear later.

### Combining both

Use plan mode to investigate. Then use direct execution to implement the plan.

### The Explore subagent

The **Explore subagent** handles noisy discovery work and returns only a summary. This keeps the
main conversation clean during multi-phase tasks.

---

## 3.5 Iterative refinement

| Technique | Use it when |
|---|---|
| **Concrete input/output examples (2–3)** | Written descriptions produce inconsistent results. The guide calls this the *most effective* way to show an expected transformation |
| **Test-driven iteration** | Write the tests first (normal behaviour, edge cases, performance). Then share the failures and improve step by step |
| **The interview pattern** | You are working in an unfamiliar area. Let Claude ask you questions first, so it raises things you did not think about — for example cache invalidation or failure modes |
| **Specific test cases with input and expected output** | Fixing an edge case, such as null values in a migration script |

### One message or several?

- Problems that **affect each other** → put them all in one detailed message.
- Problems that are **independent** → fix them one at a time.

---

## 3.6 Claude Code in CI/CD

### The command-line flags

Learn these exactly.

| Flag | What it does |
|---|---|
| `-p` / `--print` | Non-interactive mode. **This fixes a pipeline that hangs** (Sample Q10) |
| `--output-format json` | Output that a script can read |
| `--json-schema` | Forces the output to follow a schema |

**These do not exist.** The exam offers them as wrong answers:
- `--batch`
- `CLAUDE_HEADLESS=true`
- Redirecting stdin from `/dev/null` as the "correct approach"

Use `--output-format json` together with `--json-schema` to produce structured findings you can
post automatically as inline pull request comments.

### CLAUDE.md gives CI the project context

When Claude Code runs in CI, CLAUDE.md is how it learns your testing standards, fixture
conventions, and review criteria. Writing these down reduces low-value test suggestions.

### Session context isolation

The same session that **wrote** code is worse at reviewing that code. It remembers its own
reasoning and does not question it.

Use a **separate, independent instance** to review. (This also appears in section 4.6.)

### Re-running a review after new commits

Include the earlier findings in the context. Tell Claude to report only **new or still-unfixed**
issues. This stops duplicate comments.

### Generating tests

Give Claude the existing test files. Then it will not suggest tests for scenarios that are
already covered.

---

## Memory drill for Domain 3

Cover the right column. Say the answer out loud. Do this every day.

| Question | Answer |
|---|---|
| Shared team slash command | `.claude/commands/` |
| Personal slash command | `~/.claude/commands/` |
| Not shared through version control | `~/.claude/CLAUDE.md` |
| Keep CLAUDE.md modular | `@import` |
| Rule files by topic | `.claude/rules/` |
| Load a rule only for matching files | YAML frontmatter `paths:` with globs |
| Keep a noisy skill out of the main conversation | `context: fork` |
| Limit which tools a skill can use | `allowed-tools` |
| Ask for a missing parameter | `argument-hint` |
| Which memory files are loaded? | `/memory` |
| Reduce context in a long session | `/compact` |
| Non-interactive mode in CI | `-p` / `--print` |
| Structured output in CI | `--output-format json` + `--json-schema` |
| Noisy discovery without filling the context | Explore subagent |
| Test conventions across many folders | `.claude/rules/` glob, not a directory CLAUDE.md |
