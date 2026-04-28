# Changelog

All notable changes to this project will be documented here.

Format follows [Keep a Changelog](https://keepachangelog.com/en/1.0.0/).

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
