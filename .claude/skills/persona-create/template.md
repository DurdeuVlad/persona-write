# Persona Template

Use this template when creating a new persona file.

Save completed personas to `.claude/skills/persona-write/personas/your-persona-name.md`.

---

```markdown
---
name: your-persona-name
description: One-line summary of what this persona sounds like.
---

# [Persona Name]

## Identity

Who this person is. What they care about. What their relationship to the reader is.

Keep this to two or three sentences. Not a biography.

## Attention model

What this persona notices first.

What they prioritize in any piece of writing:
- what they foreground
- what they cut
- what they push back on

## Compression model

How much they say versus how much they leave implied.

- Do they assume reader competence?
- Do they over-explain or under-explain by default?
- How do they handle background context?

## Stance model

How they hold certainty.

- When are they direct?
- When are they careful?
- Do they hedge? Do they push? Do they stay neutral?

## Reasoning preference

How they structure their thinking on the page.

Options: mechanism-first, example-first, tradeoff-first, structured-argument, narrative.

Describe which they prefer and when they shift.

## Rhythm model

Sentence length, energy, pacing.

- Short and punchy, or longer and layered?
- High energy or low energy?
- How much white space and visual breathing room?

## Linguistic Fingerprint

The granular, sub-conscious markers that define this persona's unique idiolect. (Burrows-Delta / LIWC tradition; see `../persona-write/docs/persona-theory.md`.)

- **Rhythmic Pulse:** (e.g., 80% Staccato / 20% Conversational).
- **Lexical Shunts:** Specific word-level swaps. (e.g., Use "wiring up" instead of "implementing").
- **Function Word Profile:** Preferences for connectors and "invisible" words. (e.g., Avoids "which"; prefers semicolons).
- **Cognitive Bias:** The psychological anchor for their reasoning. (e.g., Bias toward First Principles).
- **Social Deictics:** Frequency of "I" vs. "We" vs. "You." (e.g., High use of "I" to signal expertise).

## Cognitive & Psychological Profile

Where the implied author sits on the linguistic-marker correlates of the Big Five (Pennebaker & King 1999; Boyd & Pennebaker 2017).

- **Openness:** [low / mid / high — what shows it]
- **Conscientiousness:** [low / mid / high — what shows it]
- **Extraversion:** [low / mid / high — what shows it]
- **Agreeableness:** [low / mid / high — what shows it]
- **Neuroticism:** [low / mid / high — what shows it]
- **Cognitive style:** [need-for-cognition signal; mechanism vs example bias; field-independent vs field-dependent]

## Stylometric Signature

Concrete or banded numeric targets a writer or reproduction must hit. (Biber dimensions / Halliday lexical density / Burrows function-word profile.)

- **Mean sentence length:** [e.g., 14 ± 7 words]
- **Lexical density:** [low (<0.4) / mid (0.4–0.55) / high (>0.55)]
- **Type-token ratio (per 500 tokens):** [e.g., ≈ 0.6]
- **Punctuation profile per 1000 words:** [em-dashes: N, semicolons: N, colons: N, parentheses: N]
- **Biber dimension placement:** [Involved/Informational, Narrative/Non-narrative, Explicit/Situational, Persuasion, Abstract/Non-abstract, On-line elaboration — each on -- / - / 0 / + / ++]
- **Top sentence openers:** [list of 3–5 dominant opening constructions]

## Literary & Rhetorical Lineage

Three to five named exemplars or traditions this persona resembles. Used as anchors for the implied author, not templates to copy. Examples: "Williams' classic style," "Lanham's clarity school," "Klinkenborg short-sentence approach," "the *New Yorker* long-form register," named individual writers in the same tradition.

## Taboo patterns

Things this persona would never write.

Be specific. Examples are better than categories.

## Failure modes

How this persona goes wrong when taken too far or applied carelessly.

Every strong persona has a failure mode. Name it honestly.
```
