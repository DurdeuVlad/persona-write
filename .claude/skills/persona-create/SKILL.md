---
name: persona-create
description: Help the user describe and shape a custom writing persona in plain language so it can be used with Persona Write.
---

# Persona Create

Use this skill when the user wants a custom writing persona instead of one of the presets.

## Goal

Help the user describe the kind of person they want the writing to sound like.

The output should be:
- understandable to the user
- practical
- reusable by `persona-write`

## How to guide the user

Ask for the kind of traits that matter most in writing:

- how direct they are
- how technical they are
- whether they explain a lot or keep it tight
- whether they sound calm, sharp, skeptical, warm, blunt, or analytical
- whether they prefer mechanism, examples, or tradeoffs
- what they should never sound like

Use plain language. Avoid schema jargon unless the user clearly wants it.

## Build a custom persona with these sections

- **identity**: who this person is, in one or two sentences
- **attention model**: what they notice, what they prioritize
- **compression model**: how much they say versus how much they leave out
- **stance model**: how they hold certainty, how they handle disagreement
- **reasoning preference**: mechanism-first, example-first, tradeoff-first, or structured-argument
- **rhythm model**: sentence length, pacing, energy level
- **taboo patterns**: what they would never write
- **failure modes**: how they go wrong when pushed too far

Keep the output readable. Do not overformalize it.

## Example user request

"Make it sound like a senior engineer who is concise, practical, skeptical of vague claims, and not rude."

## Example output shape

```
Identity: Senior engineer. Practical, clear, concise. Does not lecture.

Attention model: Notices vague claims, missing tradeoffs, hidden assumptions. Cares about whether something works.

Compression model: Assumes reader competence. Does not over-explain. Skips setup when the point is obvious.

Stance model: Direct when clear. Careful when uncertain. Does not overclaim.

Reasoning preference: Mechanism first, then tradeoffs.

Rhythm model: Short-to-medium sentences. Low ceremony. Varied enough to avoid monotone.

Taboo patterns: Corporate filler, motivational language, fake neutrality, throat-clearing intros.

Failure modes: Can sound cold or clipped when the material needs more warmth or context.
```

## Final behavior

When the persona is ready:
- present it clearly
- phrase it so it can be pasted into `/persona-write`
- keep it stable and reusable

If the user wants to save it, suggest they create a file in `.claude/skills/persona-write/personas/` following the template in `template.md`.
