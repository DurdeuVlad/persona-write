# Extracted Persona Template

Use this template when `persona-copy` produces a `persona.md` from sample texts. It mirrors `../persona-create/template.md` and adds a **Source Evidence** section so the extraction is auditable.

If the user wants the extracted persona saved as a reusable preset, copy the resulting file (with the Source Evidence section trimmed if desired) to `../persona-write/personas/[chosen-name].md`.

---

```markdown
---
name: extracted-from-[source-slug]
description: One-line summary of what this persona sounds like, in plain English.
---

# [Persona Name]

## Identity

Who the implied author is. What they care about. Their relationship to the reader.

Two or three sentences. Not a biography. Grounded in source evidence (see below).

## Attention model

What this persona notices first. What they prioritise. What they cut.

## Compression model

How much they say versus how much they leave implied. Reader-competence assumptions.

## Stance model

How they hold certainty. When direct, when careful. Hedge / booster habits.

## Reasoning preference

Mechanism-first / example-first / tradeoff-first / structured-argument / narrative / problem-solution. Primary and secondary.

## Rhythm model

Sentence-length range, energy level, paragraph shape, white-space habits.

## Linguistic Fingerprint

- **Rhythmic Pulse:** [e.g., 60% Staccato / 40% Periodic]
- **Lexical Shunts:** specific word-level swaps used by the source.
- **Function Word Profile:** preferred connectors and "invisible" words.
- **Cognitive Bias:** the psychological anchor for their reasoning.
- **Social Deictics:** I / We / You frequency profile.

## Cognitive & Psychological Profile

Where the implied author sits on the linguistic-marker correlates of the Big Five (per Pennebaker & King 1999; Boyd & Pennebaker 2017). Be specific:

- **Openness:** [low / mid / high — evidence]
- **Conscientiousness:** [low / mid / high — evidence]
- **Extraversion:** [low / mid / high — evidence]
- **Agreeableness:** [low / mid / high — evidence]
- **Neuroticism:** [low / mid / high — evidence]
- **Cognitive style:** [need-for-cognition signal; mechanism vs. example bias]

## Stylometric Signature

Concrete numeric or banded targets a reproduction must hit:

- **Mean sentence length:** [e.g., 14 ± 7]
- **Lexical density:** [e.g., 0.52 — mid band]
- **Type-token ratio (per 500 tokens):** [e.g., 0.62]
- **Punctuation profile per 1000 words:** [em-dashes: N, semicolons: N, colons: N, parentheses: N]
- **Biber dimensions:** [Involved/Informational: -- to ++; Narrative/Non-narrative: ...; etc.]
- **Top sentence openers:** [list of 5]

## Literary & Rhetorical Lineage

Three to five named exemplars or traditions the implied author resembles. Examples: "Lanham's clarity school," "Klinkenborg short-sentence approach," "Williams' classic style," "Didion's rhythmic compression," "the New Yorker long-form register." Used as anchors for the implied author, not as templates to copy.

## Taboo patterns

Things this persona would never write. Be specific. Examples beat categories.

## Failure modes

How this persona goes wrong when pushed too far.

---

## Source Evidence

*(Trim or remove this section before saving as a public preset.)*

### Samples used
- [filename or one-line description] — [word count]
- ...

### Key extractions
- Voice quote: "..."
- Stance quote: "..."
- Rhythm example (short→long contrast): "..."
- Taboo confirmation (a phrase the source carefully avoided where most writers would not): "..."

### Rubric target profile (from `06-quality-target.md`)
[paste the dimension-by-dimension table]
```
