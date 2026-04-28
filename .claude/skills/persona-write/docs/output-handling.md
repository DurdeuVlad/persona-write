# Output Handling

How Persona Write returns results.

## Scratch folder — conditional

Scratch is **durable memory**, not virtuous traceability. Use it when memory is needed; skip it when the model already holds the context.

- **Default for short text:** in-memory. Return the result inline.
- **Long-form (multi-section, > ~2000 words):** scratch is required. Chapter memory and revision tickets do durable work that exceeds a single working window.
- **`/persona-copy` analysis the user wants saved:** scratch is required.
- **Short-text tasks where the user asks for the analysis to be saved:** scratch on request.

When scratch is in use, the folder is `scratch/YYYY-MM-DD-[task-slug]/`. See `voice-guide.md` for the reasoning.

## Default behavior

### Short tasks
Return the result inline with a brief note on what changed. The pipeline ran in-context; there is no scratch folder by default. If the user wants the analysis saved, they can ask.

The note should be short — one or two sentences naming the main adjustments. Return a full diagnostic only if the user explicitly asked for one.

### Audit requests
Return a concise diagnosis. If a rewrite would be useful and obvious, include it. Otherwise, ask first.

### Long-form tasks
Return a short note that the document was processed section by section, and that all artifacts and the final document are in the task-specific scratch folder.

## When to use files

When scratch is active, write each pipeline pass to a numbered Markdown file. Items most often serialised:

- intent extraction
- diagnostic audits
- persona mapping
- drafts
- voice coherence
- refinement notes
- fidelity checks
- global briefs (long-form)
- document maps (long-form)
- chapter memory logs (long-form)
- revision tickets (long-form)
- final assembled output

Markdown is the canonical working format.

## File naming in scratch folder

- `01-intent.md`
- `02-audit.md`
- `03-mapping.md`
- `04-draft.md`
- `05-coherence.md`
- `06-refine.md`
- `07-fidelity.md`
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
