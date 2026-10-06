# Pipeline

The internal processing pipeline for Persona Write.

Scratch use is **length-driven** — see `../SKILL.md` "Scratch folder & Pipeline traceability" and `voice-guide.md`. Target ≤ 600 words runs in-memory; target > 600 words runs in scratch. Long-form and `persona-copy` always use scratch. The cornerstone principle is in `philosophy.md`.

When scratch is in use, the file naming convention below applies. When in-memory, the same passes run, but no `.md` files are materialized — the result is returned inline.

## Short-text pipeline

### 1. Resolve persona
Load the persona file. Hold its Identity, Rhythm model, Stylometric Signature, Lexical Shunts, and Taboo patterns as the brief.

### 2. Infer mode
Determine what the user wants to do.

- provided text + improvement request = rewrite
- topic or blank-slate request = draft
- "what is wrong with this" = audit
- "another pass" or "tighten this" = refine
- large structured document = longform

Ask only if genuinely unclear.

### 3. Intent extraction and style sheet (`01-intent.md`, `00-style-sheet.md` if scratch is in use)
Understand what the text is trying to do, who it is for, what must be preserved. Open the style sheet with the decisions already made on terms, names, numbers, and register; the passes that edit and check text read it and add to it. See `../passes/style-sheet.md`.

Optional inputs before this step: `/persona-research` saves `00-research.md` (genre norms and a claim table) and `/persona-brief` saves the reader brief. Step 3 reads them when present.

### 4. Diagnostic audit (`02-audit.md`)
Identify specifically what is wrong with the text **relative to the persona**. The audit is persona-fit only — it does not enumerate generic AI patterns. See `../passes/diagnostic-audit.md` and `voice-guide.md`.

Produce a short list of concrete problems framed as drift from the persona's positive shape.

### 5. Persona mapping (`03-mapping.md`)
Translate the persona definition into specific decisions for this text — stance, word-pool, structural intent.

### 6. Build sentence by sentence (`04a-skeleton.md`, `04b-sentences.md`, `04-draft.md`)
Produce the drafted or rewritten text through the persona mapping brief, one sentence at a time: a skeleton of claims first, then each sentence written, checked, and fixed before the next. The text grows one sentence at a time from the skeleton. Each finished sentence is logged as it is built, and the assemble-and-revise stage joins stacked short sentences. See `../passes/sentence-build.md`.

### 7. Voice coherence (`05-coherence.md`)
Check fit to the persona's positive shape — Identity, Rhythm, Stylometric Signature, Lexical Shunts, Taboo patterns. Apply targeted fixes toward the persona's target. See `../passes/voice-coherence.md`.

This pass replaces the previous "anti-AI scrub" and the "Unbiased Anti-AI Critic" passes. The change is empirically motivated — see `voice-guide.md` for the experiment.

### 8. Surgical tightening (`06-refine.md`)
Locally tighten sentences and improve specific transitions. Sentence-level work only — no global smoothing.

### 9. Native fluency (`06b-native.md`)
When the text is in a language other than English, or the user names a target language, rewrite phrases that read as translated into the constructions a native writer would use. Skipped for English-only work. See `../passes/native-fluency.md`.

### 10. Word check (`06c-wordcheck.md`)
Ask of every sentence, and of every content word in it, whether it fits the context (genre, reader, register) and whether it is used correctly in the target language (meaning, collocation, grammar). Fix what fails; look up what is uncertain. Runs for every language, English included. See the `persona-wordcheck` skill.

### 11. Fidelity check (`07-fidelity.md`)
Verify that the rewritten text preserves the meaning of the original.

Only output text that passes this check.

### 12. Proofread (`08-proofread.md`)
Read the finished text as it will appear in the reader's form: length as the form counts it, plain text or formatting, spacing, doubled words, the language's characters. Mechanical fixes only. See `../passes/proofread.md` and `scripts/proofread.py`.

### 13. Final assembly (`final.md` if scratch is in use)
Return the final version to the user.

---

## Multi-persona chain pipeline

When the user provides more than one persona, the pipeline extends. Each reviewer reads what the previous one produced.

### Chain execution order

1. **Owner persona drafts or rewrites** — runs the standard short-text pipeline.
2. **Each reviewer persona runs in order** — for each reviewer:
   - Step A: identify drift from the owner persona's positive shape, through the reviewer's own attention model (`[reviewer]-feedback.md` if scratch is in use).
   - Step B: apply surgical fixes (`[reviewer]-revision.md`).
3. **Owner persona runs a final reconciliation pass** (`reconciliation.md`) — smooths seams, restores owner voice where displaced, keeps useful reviewer improvements.

---

## Long-form pipeline

For long documents, scratch is **required** — chapter memory and revision tickets do durable work that exceeds a single working window.

### Stage 0: Global brief (`brief.md`)
Establish the anchor: persona, audience, purpose, format, core thesis, must-keep facts, tone constraints, locked terminology.

### Stage 1: Document map (`map.md`)
Map the structure: sections, their roles, dependencies, repeated content, drift risks.

### Stage 2: Chapter workflow loop
For each section, run the pipeline and record:

1. `[section]-01-intent.md`
2. `[section]-02-audit.md`
3. `[section]-03-mapping.md`
4. `[section]-04a-skeleton.md`, `[section]-04b-sentences.md`, `[section]-04-draft.md`
5. `[section]-05-coherence.md`
6. `[section]-06-refine.md`, `[section]-06b-native.md`, `[section]-06c-wordcheck.md`
7. `[section]-07-fidelity.md`
8. `[section]-memory.md`

### Stage 3: Consistency pass (`consistency.md`)
Whole-document review: persona, tone, terminology, repetition, intro/conclusion alignment, argument flow, open revision tickets in `tickets.md`.

### Stage 4: Final assembly (`final.md`)
Assemble the revised sections into the final Markdown document. Then run the proofread pass (`../passes/proofread.md`) on it.

---

## On the dictionaries

`dictionaries/banned-phrases.md`, `dictionaries/manager-speak.md`, and `dictionaries/ai-patterns.md` are **reference material for contributors** writing or refining personas. They are *not* pipeline inputs. The passes do not consult them during writing or audit.

The reasoning is empirical: requiring the model to enumerate generic AI patterns to avoid produces defensive compression that drifts the prose away from the persona's natural rhythm. Each persona's positive shape (Identity, Rhythm, Stylometric Signature, Taboo patterns) does the work the dictionaries used to do — calibrated to that specific persona, not as a global sweep.

See `voice-guide.md` for the experimental evidence and the contributor-facing implications.
