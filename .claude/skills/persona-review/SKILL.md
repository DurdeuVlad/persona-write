---
name: persona-review
description: Review a text through a chosen reviewer persona. Identifies issues from that persona's perspective and applies targeted surgical fixes. Preserves the owner persona as primary author unless explicitly told otherwise.
---

# Persona Review

## Purpose

Use this skill when you want a specific reviewer perspective applied to existing text — without handing ownership of the text to the reviewer.

This skill is for:
- getting a second-persona read on text already written or rewritten
- applying targeted improvements from a specific editorial stance
- reviewing text before publication through a sharper or differently-calibrated lens
- running a standalone review pass that `/persona-write` chain mode would run internally

## Core rules

- The reviewer persona is not the author. The text has an owner — that is the voice the output should primarily reflect.
- Reviewers identify problems, then apply surgical fixes. They do not ask permission before making changes.
- Reviewers do not rewrite the whole piece in their own voice.
- Reviewers do not replace the owner persona.
- Fixes should be targeted: sentence-level, paragraph-level, or local framing. Not full rewrites.
- Preserve meaning before anything else.
- The reviewer's job is to make the text better, not to make it sound like them.

## When to use this skill

Use this skill when you want to:
- run a review pass through a specific lens without fully rewriting the text
- apply one reviewer persona without building a full chain
- get targeted editorial feedback from a defined perspective
- improve framing, clarity, compression, or audience fit without displacing the voice

## When not to use this skill

Do not use this skill when you want:
- a full rewrite in the reviewer's voice — use `/persona-write` with that persona instead
- grammar correction only — the reviewer edits with purpose, not just for correctness
- detector evasion

## Main user flow

### If the user gave a reviewer persona
Proceed directly.

### If the user did not give a reviewer persona
Ask which perspective to review from.

List the preset options:
- **sharp-technical**: direct, concise, technical — cuts excess, tightens reasoning
- **pragmatic-builder**: practical, useful — improves clarity of action and implementation
- **clear-teacher**: explanatory — opens up dense reasoning, improves accessibility
- **skeptical-analyst**: careful, evidence-aware — identifies assumptions, weak claims, overreach
- **blunt-operator**: maximum compression — cuts ceremony, softness, and length aggressively
- **problem-first-marketer**: audience-first — improves framing, problem articulation, entry points

Also accept plain-language descriptions.

### If the user has an owner persona in mind
Accept it and keep it in context. The review should preserve that owner's voice.

If no owner persona is stated, infer from the text's existing voice or proceed without one — still apply surgical fixes, not full replacement.

## Review workflow

### Step 1: Understand the text's owner voice
Before reviewing, identify:
- what persona or voice the text is currently written in
- what the text is trying to do
- who it is for
- what must be preserved

### Step 2: Apply the reviewer perspective
From the reviewer persona's stance, identify:
- what feels off, unclear, or misframed
- where tone is wrong for the intended audience
- where the owner persona overdid or underdid something
- what is too dense, too soft, too vague, too cold, too polished, or too weak
- where the argument, framing, or emphasis can improve
- where AI patterns or structural tells reduce credibility

Reference `docs/review-principles.md` and the shared anti-AI guidelines in the persona-write skill (`../persona-write/docs/anti-ai-guidelines.md`).

### Step 3: Apply surgical fixes
Make targeted changes directly. Do not ask permission first.

Apply:
- sentence-level rewording
- paragraph-level restructuring where needed
- local framing improvements
- cuts where content is redundant or misplaced
- additions where context is missing for the audience

Do not:
- rewrite the whole piece in the reviewer's voice
- shift the text's center of gravity unless clearly necessary
- flatten the text into generic prose in an attempt to improve neutrality

### Step 4: Report what changed
After the review pass, provide a short note explaining:
- what the reviewer identified as the main problems
- what was changed and why
- what was deliberately left alone

Keep this brief. The text is the output. The explanation is supporting context.

## Output format

Return:
- a short reviewer summary (what the main issues were)
- the revised text with changes applied

For substantial revisions, note which sections changed and what drove the changes.

## Reviewer pairings

For useful combinations, see `docs/reviewer-pairings.md`.

## Anti-AI guidelines

The reviewer should also catch structural and vocabulary patterns that make text feel generated.

Reference: `docs/review-principles.md` and `../persona-write/docs/anti-ai-guidelines.md`.
