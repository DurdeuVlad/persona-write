# Output Handling

How Persona Write returns results.

## Scratch folder mandate

**All tasks must use a task-specific scratch folder:** `scratch/YYYY-MM-DD-[task-slug]/`.

This folder is used to record every step of the pipeline, providing transparency and a record of the AI's internal reasoning.

## Default behavior

### Short tasks
Return the result inline with a brief note on what changed. Mention that the full pipeline trace is available in the scratch folder.

The note should be short — one or two sentences naming the main adjustments. Return a full diagnostic only if the user explicitly asked for one.

### Audit requests
Return a concise diagnosis. If a rewrite would be useful and obvious, include it. Otherwise, ask first.

### Long-form tasks
Return a short note that the document was processed section by section, and that all artifacts and the final document are in the task-specific scratch folder.

## When to use files

Use Markdown files in the scratch folder for **everything**:
- intent extraction
- diagnostic audits
- persona mapping
- drafts and refined versions
- fidelity checks
- global briefs
- document maps
- chapter memory logs
- revision ticket lists
- final assembled output

Markdown is the canonical working format.

## File naming in scratch folder

- `01-intent.md`
- `02-audit.md`
- `03-mapping.md`
- `04-draft.md`
- `05-scrub.md`
- `06-unbiased-critic.md`
- `07-refine.md`
- `08-fidelity.md`
- `final.md`

For long-form, use section prefixes as described in `pipeline.md`.

## Format

Markdown is the canonical working format.
...
Do not use `.docx` as a working format. If the user needs a `.docx` for final delivery, that is a separate export step handled outside this skill.

Do not use HTML. Do not use PDF as an intermediate format.

## What to annotate

For rewrites, keep annotations short:

**Yes:** "Cut the motivating preamble. Restructured to lead with the constraint."

**No:** A full before/after comparison of every paragraph, a list of all changes made, a summary of the diagnostic findings and how each was addressed.

If the user wants a detailed change log, they will ask for one.

## What not to include in output

- A summary of what the skill just did
- A reminder of what persona was used
- An explanation of the pipeline
- Caveats about AI writing
- An offer to make further adjustments (the user will ask if they want them)
