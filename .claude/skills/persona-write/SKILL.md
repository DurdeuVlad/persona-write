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

For short text, do this internally:

1. **Resolve persona**
2. **Infer mode**
3. **Extract intent** — what the text is trying to do, who it is for, what must be preserved
4. **Run a diagnostic audit** — identify filler, weak structure, generic assistant tone, over-explaining, fake neutrality, repetitive rhythm, corporate or managerial sludge
5. **Map the persona onto the task** — what this persona would foreground, what it would cut, how it would handle certainty, rhythm, and emphasis
6. **Draft or rewrite**
7. **Run anti-AI scrub** — remove obvious generic phrases, padded transitions, excess symmetry, generic recap lines
8. **Refine** — tighten, improve flow, restore natural human texture
9. **Run fidelity check** — preserve meaning, preserve important nuance, avoid caricature, ensure persona fit

## Long-form workflow

If the input is a large document, do not rewrite it in one shot.

### Stage 0: Create a global brief
Create or infer:
- persona
- audience
- purpose
- format
- core thesis
- must-keep facts
- tone constraints
- locked terminology

### Stage 1: Create a document map
Identify:
- major sections or chapters
- the role of each section
- dependencies between sections
- repeated concepts
- likely drift risks

### Stage 2: Process one section at a time
For each section or chapter:

1. local intent extraction
2. local diagnostic audit
3. local persona mapping
4. section rewrite
5. anti-AI scrub
6. local refinement
7. fidelity check
8. chapter memory artifact

### Stage 3: Maintain rolling memory
After each section, keep track of:
- summary
- key claims
- terminology
- tone notes
- unresolved threads
- promises made to the reader
- style drift risks
- possible upstream revisions

### Stage 4: Create revision tickets when needed
If a later section changes framing, terminology, or argument shape:
- note which earlier section is affected
- describe the issue
- recommend a targeted change

Do not silently mutate everything at random.

### Stage 5: Run a whole-document consistency pass
At the end, check:
- persona consistency
- tone consistency
- terminology consistency
- repeated ideas
- intro/conclusion alignment
- argument flow
- unresolved contradictions

### Stage 6: Assemble final output
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

## Supporting modules

### Passes
- `passes/intent-extraction.md`
- `passes/diagnostic-audit.md`
- `passes/persona-mapping.md`
- `passes/rewrite.md`
- `passes/anti-ai-scrub.md`
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
