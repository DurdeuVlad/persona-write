<div align="center">

# Persona Write

**Writing should sound like someone. This helps.**

Give Claude Code a persona and it writes from that person's point of view — their attention, their compression, their stance — rather than smoothing everything into the same neutral assistant voice.

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Claude Code](https://img.shields.io/badge/Claude_Code-skill-blue)](https://claude.ai/code)
[![Version](https://img.shields.io/badge/version-1.0.0-green)]()

</div>

---

## Why this exists

If you've used AI to help with writing, you've probably noticed the result feels a bit off — even when the words are technically fine. It's balanced. It's smooth. It covers all the angles. But it doesn't sound like anyone in particular made a choice about what mattered.

Swapping out phrases doesn't fix it. Neither does asking Claude to "sound more human." The problem is structural: the writing doesn't have a point of view because it wasn't shaped by one.

Persona Write gives Claude Code a real working persona — not a style hint, but a defined attention model, compression level, and stance. The voice follows from that.

---

## What you get

A Claude Code skill set with three commands:

- **`/persona-write`** — draft, rewrite, audit, or refine text in a target persona
- **`/persona-list`** — browse the available personas with plain-English descriptions
- **`/persona-create`** — describe what you need in plain language and build a custom persona

Six personas ship with the repo. You can add your own.

Short text goes through an 8-pass pipeline. Long documents are handled section by section with rolling state, so voice stays consistent from the first page to the last.

---

## Requirements

- [Claude Code](https://claude.ai/code) — CLI, desktop app, or IDE extension
- Nothing else

---

## Install

```bash
git clone https://github.com/your-org/persona-write.git
cp -r persona-write/.claude /your-project/.claude
```

Already have `.claude/skills/`?

```bash
cp -r persona-write/.claude/skills/persona-write /your-project/.claude/skills/
cp -r persona-write/.claude/skills/persona-list /your-project/.claude/skills/
cp -r persona-write/.claude/skills/persona-create /your-project/.claude/skills/
```

See [INSTALL_SKILL.md](INSTALL_SKILL.md) for the full guide including a quick verification step.

---

## Usage

```
/persona-write
```

No persona given — the skill asks you to pick one before it starts.

```
/persona-write sharp-technical rewrite:
[paste text]
```

```
/persona-write pragmatic-builder draft:
Explain how our deployment pipeline works, for an engineer joining the team.
```

```
/persona-write:
Make this sound like a skeptical analyst who cares about evidence and does not overclaim.
[paste text]
```

---

## Personas

| Persona | Sounds like |
|---|---|
| `sharp-technical` | Direct, mechanism-first, assumes reader competence |
| `pragmatic-builder` | Practical, focused on what to do and why |
| `clear-teacher` | Explanatory without bloat, earns understanding |
| `skeptical-analyst` | Careful, evidence-aware, notices weak assumptions |
| `blunt-operator` | Maximum compression, no ceremony |
| `problem-first-marketer` | Warm, problem-first, design-aware — earns attention before asking for action |

```
/persona-list          # see all personas with full descriptions
/persona-create        # build one from a plain-language description
```

---

## How it works

### Short text — 8 passes

| Pass | What it does |
|---|---|
| Intent extraction | What is this text trying to do, and for whom |
| Diagnostic audit | What needs attention and why |
| Persona mapping | What this persona foregrounds, cuts, asserts |
| Rewrite | Apply the brief |
| Anti-AI scrub | Remove residual generic patterns |
| Refine | Tighten, fix rhythm |
| Fidelity check | Meaning and nuance survived |

### Long-form — section by section

1. build a global brief — persona, audience, purpose, locked terminology
2. map the document structure and dependencies
3. process one section at a time, writing chapter memory after each
4. log revision tickets when later sections affect earlier ones
5. whole-document consistency pass
6. assemble final output

→ [Full pipeline docs](.claude/skills/persona-write/docs/pipeline.md)

---

## Repository structure

```
.claude/skills/
  persona-write/
    personas/       ← 6 preset persona definitions (add your own here)
    passes/         ← 7 internal pass definitions
    longform/       ← 6 long-form workflow modules
    dictionaries/   ← banned phrases, manager speak, AI patterns
    docs/           ← philosophy, pipeline, usage, contributor guide
    examples/       ← quickstart, rewrite, audit, longform

  persona-list/     ← browse and explain personas
  persona-create/   ← build a custom persona
```

---

## Design

- **Persona-first** — voice follows from who the writer is, not from surface word choices
- **Multi-pass** — diagnosis, rewrite, scrub, and verification happen separately
- **Meaning before style** — the argument survives the rewrite
- **Section-by-section for long docs** — voice stays consistent, state is tracked
- **No detector evasion** — the goal is writing that's genuinely good

→ [Full design rationale](.claude/skills/persona-write/docs/philosophy.md)

---

## Contributing

Contributions are welcome. Read [CONTRIBUTING.md](CONTRIBUTING.md) before opening a PR — it explains what fits the project and what does not.

Good places to start: improving an existing persona definition, adding a realistic example, or sharpening a pass description.

---

## License

MIT — see [LICENSE](LICENSE).
