<div align="center">

# Persona Write

**Writing should sound like someone. This helps.**

Give Claude Code a persona and it writes from that person's point of view — their attention, their compression, their stance — rather than smoothing everything into the same neutral assistant voice.

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Claude Code](https://img.shields.io/badge/Claude_Code-skill-blue)](https://claude.ai/code)
[![Version](https://img.shields.io/badge/version-2.2.0-green)]()

</div>

---

## Why this exists

If you've used AI to help with writing, you've probably noticed the result feels a bit off — even when the words are technically fine. It's balanced. It's smooth. It covers all the angles. But it doesn't sound like anyone in particular made a choice about what mattered.

Swapping out phrases doesn't fix it. Neither does asking Claude to "sound more human." The problem is structural: the writing doesn't have a point of view because it wasn't shaped by one.

Persona Write gives Claude Code a real working persona — not a style hint, but a defined attention model, compression level, and stance. The writing follows from that, not from word substitution after the fact.

---

## What you get

A Claude Code skill set with five commands:

- **`/persona-write`** — draft, rewrite, audit, or refine text in a target persona; supports multi-persona chains
- **`/persona-review`** — review text through a specific reviewer persona, applying targeted surgical fixes
- **`/persona-copy`** — extract a writer's style from sample texts and reproduce a new piece at matched quality, verified against a research-backed rubric
- **`/persona-list`** — browse the available personas with plain-English descriptions
- **`/persona-create`** — describe what you need in plain language and build a custom persona

Six personas ship with the repo. Each is grounded in stylometry, writing-quality rubrics, rhetoric, and personality–linguistics research — see [`persona-theory.md`](.claude/skills/persona-write/docs/persona-theory.md). You can add your own.

Short text goes through a 7-pass pipeline. Long documents are handled section by section with rolling state, so voice stays consistent from the first page to the last.

V2 adds **persona chain mode**: one persona writes, another reviews and applies targeted fixes, the owner reconciles. You get the substance of one voice sharpened by the perspective of another — without blending them into something generic.

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
cp -r persona-write/.claude/skills/persona-review /your-project/.claude/skills/
cp -r persona-write/.claude/skills/persona-copy /your-project/.claude/skills/
cp -r persona-write/.claude/skills/persona-list /your-project/.claude/skills/
cp -r persona-write/.claude/skills/persona-create /your-project/.claude/skills/
```

See [INSTALL_SKILL.md](INSTALL_SKILL.md) for the full guide including a quick verification step.

---

## Usage

No persona given — the skill asks you to pick one:

```
/persona-write
```

Rewrite existing text in a specific voice:

```
/persona-write sharp-technical rewrite:
[paste text]
```

Draft something new from a brief:

```
/persona-write pragmatic-builder draft:
Explain how our deployment pipeline works, for an engineer joining the team.
```

Use a plain-language custom persona:

```
/persona-write:
Make this sound like a skeptical analyst who cares about evidence and does not overclaim.
[paste text]
```

Chain two personas — first writes, second reviews, first reconciles:

```
/persona-write sharp-technical -> problem-first-marketer:
[paste text]
```

Output reads primarily as the first persona's work. The reviewer sharpens it, doesn't replace it.

Standalone review through one persona lens, without full rewrite:

```
/persona-review clear-teacher:
[paste text written by sharp-technical]
```

Reproduce another writer's style from sample texts:

```
/persona-copy
Here are five essays I've written. Write a sixth one in the same style on this topic: ...
[paste 5 essays]
```

Output is verified against a research-backed rubric (Education Northwest 6+1 Trait + Hyland stance/engagement) and a stylometric fingerprint match. The extracted persona can be saved as a reusable preset.

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

### Multi-persona chain — V2

Give more than one persona and the skill runs them as an ordered chain.

| Step | What happens |
|---|---|
| Owner writes | First persona runs the standard pipeline |
| Reviewer N applies fixes | Each reviewer identifies problems and applies surgical changes |
| Owner reconciles | First persona smooths seams, restores voice, keeps useful improvements |

Final output reads as the first persona's work. Reviewers improve it; they do not replace it.

→ [Chain mode docs](.claude/skills/persona-write/docs/persona-chain-mode.md)

### Short text — 7 passes

| Pass | What it does |
|---|---|
| Intent extraction | What is this text trying to do, and for whom |
| Diagnostic audit | Where the draft drifts from the persona's positive shape |
| Persona mapping | What this persona foregrounds, cuts, asserts |
| Rewrite | Apply the brief |
| Voice coherence | Check fit to the persona's Identity / Rhythm / Stylometric Signature |
| Refine | Tighten, fix rhythm |
| Fidelity check | Meaning and nuance survived |

The pipeline runs **in-memory by default** for short text. Scratch folders are used for long-form work, `persona-copy` analysis, and on request — see [`voice-guide.md`](.claude/skills/persona-write/docs/voice-guide.md) for why this matters.

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
    docs/           ← philosophy, pipeline, usage, chain mode, anti-AI guidelines
    examples/       ← quickstart, rewrite, audit, longform

  persona-review/   ← standalone review through a specific persona lens
    docs/           ← review principles, reviewer pairings
    examples.md

  persona-copy/     ← extract a writer's style from samples and reproduce at matched quality
    pipeline.md     ← 11-pass workflow: sample audit → fingerprint → implied author → draft → verify
    template.md     ← extracted-persona file template
    examples.md

  persona-list/     ← browse and explain personas
  persona-create/   ← build a custom persona, research-backed schema
```

The research foundation lives in [`.claude/skills/persona-write/docs/persona-theory.md`](.claude/skills/persona-write/docs/persona-theory.md) and the verification rubric in [`.claude/skills/persona-write/docs/writing-quality-rubric.md`](.claude/skills/persona-write/docs/writing-quality-rubric.md). Both are referenced by every persona file and by `persona-copy`.

---

## Design

- **Persona-first** — voice follows from who the writer is, not from surface word choices
- **Multi-pass** — diagnosis, rewrite, scrub, and verification happen separately
- **Meaning before style** — the argument survives the rewrite
- **Section-by-section for long docs** — voice stays consistent, state is tracked
- **Chain mode** — multiple personas collaborate; the first owns the output
- **No detector evasion** — the goal is writing that's genuinely good

→ [Full design rationale](.claude/skills/persona-write/docs/philosophy.md)

---

## Contributing

Contributions are welcome. Read [CONTRIBUTING.md](CONTRIBUTING.md) before opening a PR — it explains what fits the project and what does not.

Good places to start: improving an existing persona definition, adding a realistic example, or sharpening a pass description.

---

## License

MIT — see [LICENSE](LICENSE).
