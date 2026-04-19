# Contributing to Persona Write

Read this before opening a PR.

## Philosophy first

Persona Write has a specific design. Contributions that drift from it will not be accepted. Read [`.claude/skills/persona-write/docs/philosophy.md`](.claude/skills/persona-write/docs/philosophy.md) before contributing anything substantive.

**In scope:**
- persona-first voice shaping
- multi-pass workflows
- meaning preserved before style changes
- long-form text handled section by section
- avoiding generic assistant voice

**Out of scope:**
- detector evasion
- shallow word-swapping
- fake human quirks
- one-shot large-document rewrites
- scoring or grading text

## What to contribute

**Good:**
- improve a preset persona definition — clearer identity, tighter taboo list, more honest failure modes
- improve a pass definition — clearer steps, better examples
- improve long-form workflow docs
- add realistic examples to `examples/` folders
- fix incorrect or unclear wording
- add real patterns to the dictionary files

**Not accepted:**
- new personas that are gimmicks or caricatures
- personas without the full 8-section schema
- new passes without clear rationale
- detector-evasion framing anywhere in the repo
- scoring mechanisms
- banned-phrase lists with no reasoning
- file bloat without behavior improvement

## Process

1. Fork the repo and create a branch: `git checkout -b your-feature-name`
2. Read the existing file in the relevant folder to understand the schema before adding or changing anything
3. Make your changes
4. Open a PR with a clear description of what changed and why

No special tooling required. The entire repo is Markdown.

## File locations

| Contribution type | Folder |
|---|---|
| New or improved persona | `.claude/skills/persona-write/personas/` |
| New or improved pass | `.claude/skills/persona-write/passes/` |
| Long-form workflow changes | `.claude/skills/persona-write/longform/` |
| Dictionary additions | `.claude/skills/persona-write/dictionaries/` |
| Examples | `examples/` inside the relevant skill folder |
| Docs | `.claude/skills/persona-write/docs/` |

## PR checklist

- [ ] Read `.claude/skills/persona-write/docs/philosophy.md`
- [ ] Contribution fits the project goals
- [ ] New files follow the existing schema
- [ ] No detector-evasion framing
- [ ] No gimmick personas
- [ ] Examples are realistic and specific
- [ ] Wording is clear and not bloated

## Writing style

This repo is written plainly. Not corporate. Not academic. Just clear.

If you are adding documentation, write it the same way. Direct statements, no throat-clearing.
