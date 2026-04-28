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

### 3. Intent extraction (`01-intent.md` if scratch is in use)
Understand what the text is trying to do, who it is for, what must be preserved.

### 4. Diagnostic audit (`02-audit.md`)
Identify specifically what is wrong with the text **relative to the persona**. The audit is persona-fit only — it does not enumerate generic AI patterns. See `../passes/diagnostic-audit.md` and `voice-guide.md`.

Produce a short list of concrete problems framed as drift from the persona's positive shape.

### 5. Persona mapping (`03-mapping.md`)
Translate the persona definition into specific decisions for this text — stance, word-pool, structural intent.

### 6. Rewrite (`04-draft.md`)
Produce the rewritten or drafted text through the persona mapping brief.

### 7. Voice coherence (`05-coherence.md`)
Check fit to the persona's positive shape — Identity, Rhythm, Stylometric Signature, Lexical Shunts, Taboo patterns. Apply targeted fixes toward the persona's target. See `../passes/voice-coherence.md`.

This pass replaces the previous "anti-AI scrub" and the "Unbiased Anti-AI Critic" passes. The change is empirically motivated — see `voice-guide.md` for the experiment.

### 8. Surgical tightening (`06-refine.md`)
Locally tighten sentences and improve specific transitions. Sentence-level work only — no global smoothing.

### 9. Fidelity check (`07-fidelity.md`)
Verify that the rewritten text preserves the meaning of the original.

Only output text that passes this check.

### 10. Final assembly (`final.md` if scratch is in use)
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
4. `[section]-04-draft.md`
5. `[section]-05-coherence.md`
6. `[section]-06-refine.md`
7. `[section]-07-fidelity.md`
8. `[section]-memory.md`

### Stage 3: Consistency pass (`consistency.md`)
Whole-document review: persona, tone, terminology, repetition, intro/conclusion alignment, argument flow, open revision tickets in `tickets.md`.

### Stage 4: Final assembly (`final.md`)
Assemble the revised sections into the final Markdown document.

---

## On the dictionaries

`dictionaries/banned-phrases.md`, `dictionaries/manager-speak.md`, and `dictionaries/ai-patterns.md` are **reference material for contributors** writing or refining personas. They are *not* pipeline inputs. The passes do not consult them during writing or audit.

The reasoning is empirical: requiring the model to enumerate generic AI patterns to avoid produces defensive compression that drifts the prose away from the persona's natural rhythm. Each persona's positive shape (Identity, Rhythm, Stylometric Signature, Taboo patterns) does the work the dictionaries used to do — calibrated to that specific persona, not as a global sweep.

See `voice-guide.md` for the experimental evidence and the contributor-facing implications.
