# Changelog

All notable changes to this project will be documented here.

Format follows [Keep a Changelog](https://keepachangelog.com/en/1.0.0/).

## [2.2.0] - 2026-04-28

### Removed

- `passes/anti-ai-scrub.md` deleted. Empirical pilot showed that asking the model to enumerate generic AI patterns to avoid produces defensive compression (white-bear effect) — the prose drifts *away* from the persona's natural rhythm. Output came in 30-40% shorter and at half the persona's target mean sentence length. The pass made every persona read like a homogenised "anti-AI register."
- The phantom `passes/unbiased-critic.md` reference removed from `SKILL.md` and `docs/pipeline.md`. The "Unbiased Anti-AI Critic" pass was the same defensive pattern-matcher; its file did not exist.
- Mandatory scratch-folder requirement for all tasks dropped. Scratch is now conditional.

### Added

- `passes/voice-coherence.md` — replaces `anti-ai-scrub.md`. Positive-shape framing only: does the draft match the persona's Identity, Rhythm model, Stylometric Signature, Lexical Shunts, and Taboo patterns? Targeted fixes go *toward* the persona's target, not against a global ban list.
- `docs/voice-guide.md` — empirical companion to `persona-theory.md` and `writing-quality-rubric.md`. Documents the pilot results that drove the pipeline change.

### Changed

- `passes/diagnostic-audit.md` rewritten to be persona-fit only. No longer references `dictionaries/*` or the "Four Core AI Similarities."
- `dictionaries/banned-phrases.md`, `dictionaries/manager-speak.md`, `dictionaries/ai-patterns.md`, and `docs/anti-ai-guidelines.md` demoted to **reference-only** with a banner at the top of each. They remain in the repo as background reading for contributors writing new personas, but the pipeline does not consult them during writing or audit.
- `docs/writing-quality-rubric.md` Voice and Word Choice diagnostics updated to reference each persona's positive shape (Lexical Shunts, Stylometric Signature, Taboo patterns) instead of `dictionaries/ai-patterns.md`.
- `persona-copy/pipeline.md` Pass 9 changed from "anti-AI scrub" to "voice coherence against the extracted persona" — calibrated against the source author's positive shape.
- `persona-review/SKILL.md` and `docs/review-principles.md` updated to frame review through the owner persona's positive shape, not a global anti-AI checklist.
- Scratch folder usage made **conditional**:
  - **In-memory** is now the default for short text. The model holds intermediate state in working memory; serialising and re-reading attenuates persona commitment.
  - **Scratch required** for long-form (chapter memory does durable work) and `persona-copy` analysis the user wants saved.
  - **Scratch on request** for short text where the user wants the analysis saved.
- `passes/refine.md`, `longform/chapter-workflow.md`, `examples/rewrite.md`, `examples/quickstart.md`, `docs/pipeline.md`, `docs/output-handling.md` updated to reference the new pass names and conditional-scratch model.

### Personas

- All 6 persona files **unchanged**. Their `Taboo patterns` sections are character expressions, not defensive checklists, and remain part of the persona's positive shape.

## [2.1.0] - 2026-04-28

### Added

- `persona-copy` skill — extract a writer's style from sample texts and reproduce a new piece at matched quality. 11-pass pipeline with stylometric fingerprinting, Booth-style implied-author construction, and rubric-based verification.
- `docs/persona-theory.md` — research foundation for every persona file. Grounds the schema in stylometry (Burrows, Biber, Halliday), writing-quality rubrics (Education Northwest's 6+1 Trait, Hayes–Flower), rhetoric (Booth, Williams, Lanham, Pinker), and personality–linguistics (Pennebaker, Hyland).
- `docs/writing-quality-rubric.md` — research-backed 7-dimension analytic rubric (Ideas, Organization, Voice, Word Choice, Sentence Fluency, Stance Calibration, Reader Engagement) used by `persona-copy` for verification and by `persona-review` for scoring.
- Three new sections on every preset persona: **Cognitive & Psychological Profile** (Big Five linguistic-marker tendencies), **Stylometric Signature** (concrete numeric or banded targets — sentence length, lexical density, TTR, punctuation profile, Biber dimensions, opener inventory), and **Literary & Rhetorical Lineage** (named exemplars).

### Changed

- `persona-create` upgraded to use the research-backed schema and the full template (12 fields instead of 8). The customer-facing surface remains plain-language; the research grounding sits underneath in `persona-theory.md`.
- `persona-create/template.md` extended with the three new sections.

## [1.1.0] - 2026-04-19

### Added

- `problem-first-marketer` preset persona — problem-first, design-aware, leads with the reader's frustration before the product. Treats visual hierarchy as part of the message.

## [1.0.0] - 2026-04-19

### Added

- `persona-write` skill with full short-text and long-form workflows
- `persona-list` skill for browsing available personas
- `persona-create` skill for building custom personas
- Five preset personas: `sharp-technical`, `pragmatic-builder`, `clear-teacher`, `skeptical-analyst`, `blunt-operator`
- Seven internal pass definitions: intent extraction, diagnostic audit, persona mapping, rewrite, anti-AI scrub, refine, fidelity check
- Six long-form workflow modules: global brief, document map, chapter workflow, chapter memory, revision tickets, consistency pass
- Three dictionaries: banned phrases, manager speak, AI patterns
- Example files for quickstart, rewrite, audit, and longform use cases
- Philosophy, pipeline, simple usage, longform mode, output handling, and contributor guide documentation
