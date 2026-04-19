# Pipeline

The internal processing pipeline for Persona Write.

This document is for contributors and people who want to understand how the system works.

## Short-text pipeline

### 1. Resolve persona
Determine which persona to use.

- If a preset name was provided, load from `personas/`
- If a plain-language description was provided, derive a working persona
- If nothing was provided, ask the user

### 2. Infer mode
Determine what the user wants to do.

- provided text + improvement request = rewrite
- topic or blank-slate request = draft
- "what is wrong with this" = audit
- "another pass" or "tighten this" = refine
- large structured document = longform

Ask only if genuinely unclear.

### 3. Intent extraction (`passes/intent-extraction.md`)
Understand what the text is trying to do, who it is for, what must be preserved.

This is internal. It informs all subsequent passes.

### 4. Diagnostic audit (`passes/diagnostic-audit.md`)
Identify specifically what is wrong with the text.

Produce a short list of concrete problems to target. Not categories — examples.

### 5. Persona mapping (`passes/persona-mapping.md`)
Translate the persona definition into specific decisions for this text.

Produce a working brief: what to foreground, what to cut, how to handle certainty, rhythm and compression for this content.

### 6. Rewrite (`passes/rewrite.md`)
Produce the rewritten or drafted text using the persona mapping brief.

Address the diagnostic list. Preserve meaning.

### 7. Anti-AI scrub (`passes/anti-ai-scrub.md`)
Remove residual patterns that make text feel generated.

Check opener patterns, symmetry, hollow transitions, recap sentences, balanced-at-all-costs conclusions.

Do not add fake human quirks.

### 8. Refine (`passes/refine.md`)
Tighten sentences. Fix rhythm breaks. Repair awkward transitions.

Lighter than the rewrite pass. Works at sentence and paragraph level.

### 9. Fidelity check (`passes/fidelity-check.md`)
Verify that the rewritten text preserves the meaning of the original.

Check key claims, specific facts, nuance, and persona fit. Check for caricature.

Only output text that passes this check.

---

## Long-form pipeline

### Stage 0: Global brief (`longform/global-brief.md`)
Establish the anchor document: persona, audience, purpose, format, core thesis, must-keep facts, tone constraints, locked terminology.

### Stage 1: Document map (`longform/document-map.md`)
Map the structure: sections, their roles, dependencies, repeated content, drift risks.

### Stage 2: Chapter workflow loop (`longform/chapter-workflow.md`)
For each section, run:
1. Load context from global brief and chapter memory
2. Local intent extraction
3. Local diagnostic audit
4. Local persona mapping
5. Section rewrite
6. Anti-AI scrub
7. Local refinement
8. Local fidelity check
9. Write chapter memory artifact (`longform/chapter-memory.md`)
10. Create revision tickets if needed (`longform/revision-tickets.md`)

### Stage 3: Consistency pass (`longform/consistency-pass.md`)
Whole-document review: persona, tone, terminology, repetition, intro/conclusion alignment, argument flow, open revision tickets.

### Stage 4: Final assembly
Assemble the revised sections into the final Markdown document.

---

## Dictionary references

The passes reference the dictionaries when identifying patterns:

- `dictionaries/banned-phrases.md` — specific phrases to avoid
- `dictionaries/manager-speak.md` — corporate language patterns
- `dictionaries/ai-patterns.md` — structural AI patterns

The dictionaries are pattern guides, not blocklists. Apply judgment.
