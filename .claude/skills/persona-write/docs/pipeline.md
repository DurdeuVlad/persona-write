# Pipeline

The internal processing pipeline for Persona Write.

Every task must be executed through a task-specific scratch folder: `scratch/YYYY-MM-DD-[task-slug]/`. This ensures traceability and allows the user to inspect intermediate steps.

## Short-text pipeline

### 1. Resolve persona & Create task folder
Determine which persona to use and create the scratch task folder.

### 2. Infer mode
Determine what the user wants to do.

- provided text + improvement request = rewrite
- topic or blank-slate request = draft
- "what is wrong with this" = audit
- "another pass" or "tighten this" = refine
- large structured document = longform

Ask only if genuinely unclear.

### 3. Intent extraction (`01-intent.md`)
Understand what the text is trying to do, who it is for, what must be preserved.

This must be recorded in the task folder.

### 4. Diagnostic audit (`02-audit.md`)
Identify specifically what is wrong with the text.

Produce a short list of concrete problems to target. Not categories — examples.

### 5. Persona mapping (`03-mapping.md`)
Translate the persona definition into specific decisions for this text.

### 6. Rewrite (`04-draft.md`)
Produce the rewritten or drafted text using the persona mapping brief.

### 7. Anti-AI scrub (`05-scrub.md`)
Remove residual patterns that make text feel generated.

### 8. Surgical Tightening (`06-refine.md`)
Locally tighten sentences and improve specific transitions. Restore natural human texture at the sentence level without applying global "smoothing" that increases AI predictability.

### 9. Unbiased Anti-AI Critic (`07-unbiased-critic.md`)
Mandatory "Chaos & Entropy" pass. Act as a vicious critic to break predictability (perplexity) and symmetry (burstiness). Inject stochastic noise and sub-optimal word choices to restore human-like irregularity.

### 10. Fidelity check (`08-fidelity.md`)
Verify that the rewritten text preserves the meaning of the original.

Only output text that passes this check.

### 11. Final assembly (`final.md`)
The final version to be returned to the user.

---

## Multi-persona chain pipeline

When the user provides more than one persona, the pipeline extends. All reviewer passes and reconciliation must be recorded in the task folder.

### Chain execution order

1. **Owner persona drafts or rewrites** — runs the standard short-text pipeline
2. **Each reviewer persona runs in order** — for each reviewer:
   - Step A: identify problems (`[reviewer]-feedback.md`)
   - Step B: apply surgical fixes (`[reviewer]-revision.md`)
3. **Owner persona runs a final reconciliation pass** (`reconciliation.md`)

---

## Long-form pipeline

For long documents, the scratch folder contains the global artifacts and per-section records.

### Stage 0: Global brief (`brief.md`)
Establish the anchor document: persona, audience, purpose, format, core thesis, must-keep facts, tone constraints, locked terminology.

### Stage 1: Document map (`map.md`)
Map the structure: sections, their roles, dependencies, repeated content, drift risks.

### Stage 2: Chapter workflow loop
For each section, run the pipeline and record:
1. `[section]-01-intent.md`
2. `[section]-02-audit.md`
3. `[section]-03-mapping.md`
4. `[section]-04-draft.md`
5. `[section]-05-scrub.md`
6. `[section]-06-refine.md`
7. `[section]-07-unbiased-critic.md`
8. `[section]-08-fidelity.md`
9. `[section]-memory.md`

### Stage 3: Consistency pass (`consistency.md`)
Whole-document review: persona, tone, terminology, repetition, intro/conclusion alignment, argument flow, open revision tickets in `tickets.md`.

### Stage 4: Final assembly (`final.md`)
Assemble the revised sections into the final Markdown document.

---

## Dictionary references

The passes reference the dictionaries when identifying patterns:

- `dictionaries/banned-phrases.md` — specific phrases to avoid
- `dictionaries/manager-speak.md` — corporate language patterns
- `dictionaries/ai-patterns.md` — structural AI patterns

The dictionaries are pattern guides, not blocklists. Apply judgment.
