# Contributor Guide

How the repo is structured and how to extend it.

## File structure

```
.claude/skills/persona-write/
  SKILL.md               — main skill definition
  docs/                  — documentation
  personas/              — preset persona definitions
  passes/                — internal pass definitions
  longform/              — long-form workflow modules
  dictionaries/          — phrase and pattern references
  examples/              — example files
```

## Adding a persona

Create a new file in `personas/` following the schema in `persona-create/template.md`.

Required sections:
- identity
- attention model
- compression model
- stance model
- reasoning preference
- rhythm model
- taboo patterns
- failure modes

Every section must be complete. A persona file without failure modes is incomplete.

**Do not add:**
- gimmick personas (personas defined by a single quirk)
- caricatures (personas that are just a stereotype turned up to maximum)
- personas defined entirely by what they sound like, with no attention or compression model
- personas designed for detection evasion

After adding a persona, add an entry in `persona-list/SKILL.md` and an example in `persona-list/examples.md`.

## Improving a pass

Pass files are in `passes/`. Each pass has a purpose, steps, and output format.

When improving a pass:
- keep the purpose statement accurate
- update the steps to reflect the actual intended behavior
- add examples where they make the step clearer
- do not add complexity for its own sake

## Updating the dictionaries

Dictionary files are in `dictionaries/`. They are reference documents, not blocklists.

When adding to a dictionary:
- add specific, real patterns, not abstract categories
- group by mechanism, not alphabetically
- include examples that show why the pattern is a problem
- do not add patterns that are only a problem in specific contexts

## Adding examples

Example files are in `examples/` for the main skill, and in sub-skill folders for `persona-list` and `persona-create`.

Good examples:
- show a realistic user request
- show what the expected output looks like or how the skill should behave
- cover a distinct case (not a variation on an existing example)

## Modifying the long-form workflow

Long-form workflow files are in `longform/`. The workflow is designed to be linear and checkpointed.

Before modifying the workflow:
- read `docs/philosophy.md` to understand why the workflow is designed as it is
- read `docs/longform-mode.md` to understand the user-facing behavior
- read the existing workflow files end-to-end

Do not add steps that do not have a clear reason to exist. Do not remove steps without understanding what problem they solve.

## What does not belong in this repo

- CLI code, Python, TypeScript, or any executable
- Scoring or grading mechanisms for text
- Detector-evasion framing or language
- Bloated pass files with long lists of rules and no explanation of why
- Personas without full schema
- Examples that are contrived or not realistic

When in doubt, read `docs/philosophy.md` first.
