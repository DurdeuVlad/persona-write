---
name: persona-write
description: Draft, rewrite, audit, and refine text through a specific writing persona using a multi-pass workflow. For long documents, process section by section instead of rewriting everything in one shot.
---

# Persona Write

## Purpose

Use this skill to write through a **specific kind of persona**, not generic assistant voice.

This skill is for:
- drafting text
- rewriting existing text
- auditing weak or AI-ish text
- refining already revised text
- processing long documents section by section

The goal is writing shaped by a specific attention model, compression level, and stance.

## Core rules

- Persona comes first.
- Preserve meaning before style.
- Default to concise, clear writing.
- Do not flatten all writing into one neutral assistant voice.
- Do not one-shot long-form rewrites.
- For long text, process one major section or chapter at a time.
- Use Markdown as the working format when writing to files.
- Do not optimize for detector evasion.
- Do not add fake human quirks like random typos or forced slang.

## Scratch folder & Pipeline traceability

To ensure the pipeline is followed and the user can see the internal reasoning, **every task must use a scratch folder.**

1. **Create a task folder:** `scratch/YYYY-MM-DD-[task-slug]/`
2. **Record every pass:** Each step in the pipeline (Intent, Audit, Mapping, etc.) must be written to its own `.md` file in that folder.
3. **Number the files:** Use `01-intent.md`, `02-audit.md`, `03-mapping.md`, etc.
4. **Final output:** Write the final draft to `final.md` in the same folder before returning it to the user.

This applies to **all tasks**, including short rewrites. The scratch folder is gitignored.

## When to use this skill

Use this skill when the user wants to:
- remove generic assistant patterns from existing text
- rewrite text in a stronger voice
- sound more direct, technical, practical, or clear
- improve text that is over-hedged, padded, or voiceless
- write something from scratch in a defined voice
- revise a large document while keeping voice and structure consistent

## When not to use this skill

Do not use this skill when the user only wants:
- grammar correction with minimal rewriting
- exact preservation of wording
- detector evasion
- a full large-document rewrite in one pass

## Multi-persona chain mode

When the user provides more than one persona, interpret them as an ordered chain.

Accepted formats:
- `sharp-technical -> problem-first-marketer`
- `sharp-technical, problem-first-marketer`
- natural language: "write as a sharp technical person, then review as a problem-first marketer"

### Chain semantics

- **First persona owns the text.** It writes or rewrites the draft.
- **Every following persona is a reviewer.** It does not become a co-author.
- **Reviewers run a two-step process** — no user permission required:
  1. Identify problems from their perspective (what is off, unclear, misframed, wrong for the audience)
  2. Apply surgical fixes — sentence-level, paragraph-level, local framing, targeted cuts or additions
- **Reviewers must not** rewrite the whole piece in their own voice, replace the owner persona, or flatten the text into generic prose.
- **After all reviewers finish, the owner persona runs a mandatory final reconciliation pass.** This pass smooths seams, restores the owner's voice where it was displaced, preserves useful reviewer improvements, and ensures the final text reads as one coherent piece.
- **Final output should still primarily sound like the first persona.**

For multiple reviewers, apply them in order. Each reviewer reads what the previous one produced.

Example — three-persona chain:
1. `sharp-technical` writes
2. `clear-teacher` reviews and applies surgical fixes
3. `problem-first-marketer` reviews and applies surgical fixes
4. `sharp-technical` runs the final reconciliation pass

→ Full details: `docs/persona-chain-mode.md`

## Main user flow

### If the user already gave a persona
Proceed directly.

### If the user did not give a persona
Ask for one before writing.

List the preset options in plain English:

- **sharp-technical**: direct, concise, technical
- **pragmatic-builder**: practical, clear, useful
- **clear-teacher**: easy to follow, explanatory without fluff
- **skeptical-analyst**: careful, critical, evidence-aware
- **blunt-operator**: very direct, minimal ceremony
- **problem-first-marketer**: problem-first, design-aware, earns attention before asking for action

Also allow a plain-language custom persona, for example:

- "like a senior engineer who is concise and hates fluff"
- "like a clear teacher who explains things simply but not dumbed down"
- "like a skeptical analyst who cares about evidence and weak assumptions"

## Mode handling

Infer the mode whenever possible.

### Draft
Use when the user gives a topic or asks to write something from scratch.

### Rewrite
Use when the user provides text and asks to improve it, rewrite it, or change its voice.

### Audit
Use when the user provides text and asks what is wrong with it, why it sounds bad, or why it feels AI-ish.

### Refine
Use when the user provides text that is already revised and wants another pass.

### Longform
Use when the input is a large or structured document, or when the text clearly needs section-by-section treatment.

Only ask for mode if it is genuinely unclear.

## Persona resolution

### Preset persona
If the user names a preset, load it from the `personas/` folder.

### Custom persona
If the user describes a persona in plain language, derive a lightweight working persona from the description.

When building a custom persona, infer:
- directness
- technicality
- compression level
- explanatory depth
- stance
- rhythm tendencies
- taboo patterns if obvious

Do not make the custom persona theatrical or exaggerated.

## Short-text workflow

For short text, process each step by writing to the scratch folder:

1. **Resolve persona & Create task folder**
2. **Infer mode**
3. **Extract intent** (`01-intent.md`) — what the text is trying to do, who it is for, what must be preserved
4. **Run a diagnostic audit** (`02-audit.md`) — identify generic assistant patterns, filler, and structural tells.
5. **Persona Immersion Mapping** (`03-mapping.md`) — Establish stance, word-pool (slang/shorthand), and structural intent.
6. **Draft or rewrite** (`04-draft.md`) — Write through the immersion brief; prioritize internal logic over smooth flow.
7. **Voice Scrub** (`05-scrub.md`) — Remove residual "brochure" language or neutral hedging that displaced the persona.
8. **Refine** (`06-refine.md`) — Locally tighten and improve flow without global smoothing.
9. **Run fidelity check** (`07-fidelity.md`) — preserve meaning and nuance.
10. **Final output** (`final.md`)

## Long-form workflow

If the input is a large document, do not rewrite it in one shot. Use the scratch folder for all artifacts.

### Stage 0: Create a global brief (`brief.md`)
Create or infer:
- persona
- audience
- purpose
- format
- core thesis
- must-keep facts
- tone constraints
- locked terminology

### Stage 1: Create a document map (`map.md`)
Identify:
- major sections or chapters
- the role of each section
- dependencies between sections
- repeated concepts
- likely drift risks

### Stage 2: Process one section at a time
For each section or chapter, write to the task folder:

1. local intent extraction (`[section]-01-intent.md`)
2. local diagnostic audit (`[section]-02-audit.md`)
3. local persona immersion (`[section]-03-mapping.md`)
4. section rewrite (`[section]-04-draft.md`)
5. voice scrub (`[section]-05-scrub.md`)
6. local refinement (`[section]-06-refine.md`)
7. fidelity check (`[section]-07-fidelity.md`)
8. chapter memory artifact (`[section]-memory.md`)

### Stage 3: Maintain rolling memory
After each section, keep track of:
...
### Stage 4: Create revision tickets when needed (`tickets.md`)
If a later section changes framing, terminology, or argument shape:
...
### Stage 5: Run a whole-document consistency pass (`consistency.md`)
At the end, check:
...
### Stage 6: Assemble final output (`final.md`)
Create the final Markdown document from the revised sections.

## Output handling

### Short tasks
Return the result inline by default unless the user clearly wants it saved.

### Long or iterative tasks
Use Markdown files for:
- global brief
- document map
- chapter drafts
- chapter memory
- revision tickets
- final assembled output

Markdown is the canonical working format.

## Output style by default

Unless the user requests detailed analysis, do not dump the full internal process.

### For normal rewrite requests
Return:
- a short note about what changed
- the rewritten text

### For audit requests
Return:
- concise diagnosis
- optional rewrite if requested or obviously useful

### For long-form requests
Return:
- short note that the text was handled section by section
- the resulting output or the location of the generated Markdown artifacts

## Preset personas

Preset persona definitions are in:

- `personas/sharp-technical.md`
- `personas/pragmatic-builder.md`
- `personas/clear-teacher.md`
- `personas/skeptical-analyst.md`
- `personas/blunt-operator.md`
- `personas/problem-first-marketer.md`

## Supporting modules

### Docs
- `docs/persona-chain-mode.md`
- `docs/anti-ai-guidelines.md`
- `docs/pipeline.md`
- `docs/longform-mode.md`
- `docs/simple-usage.md`
- `docs/philosophy.md`
- `docs/contributor-guide.md`

### Passes
- `passes/intent-extraction.md`
- `passes/diagnostic-audit.md`
- `passes/persona-mapping.md`
- `passes/rewrite.md`
- `passes/anti-ai-scrub.md`
- `passes/unbiased-critic.md`
- `passes/refine.md`
- `passes/fidelity-check.md`

### Long-form
- `longform/global-brief.md`
- `longform/document-map.md`
- `longform/chapter-workflow.md`
- `longform/chapter-memory.md`
- `longform/revision-tickets.md`
- `longform/consistency-pass.md`

### Dictionaries
- `dictionaries/banned-phrases.md`
- `dictionaries/manager-speak.md`
- `dictionaries/ai-patterns.md`

## Final reminder

This skill is not trying to produce "generic human-like writing."

It is trying to produce writing that sounds like **a specific kind of person**, while staying useful, coherent, and readable.
