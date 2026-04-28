# Output Handling

How Persona Write returns results.

## Scratch folder — length-driven rule

Scratch is **durable memory**, not virtuous traceability. The mode is decided by the target output length.

| Target output | Mode |
|---|---|
| ≤ 600 words (≈ 1–2 pages) | In-memory — default |
| > 600 words | Scratch — required |
| Long-form (multi-section, > 2000 words) | Scratch with chapter workflow |
| `/persona-copy` analysis | Scratch — always |

Estimate the target from the user's brief. The user can override by explicitly asking for the analysis to be saved on a short task.

When scratch is in use, the folder is `scratch/YYYY-MM-DD-[task-slug]/`. See `voice-guide.md` for the empirical reasoning and `philosophy.md` for the cornerstone principle.

## Default behavior

### In-memory tasks (≤ 600 words)
Return the result inline with a brief note on what changed. The pipeline ran in-context; there is no scratch folder. If the user wants the analysis saved, they can ask.

The note should be short — one or two sentences naming the main adjustments. Return a full diagnostic only if the user explicitly asked for one.

### Audit requests
Return a concise diagnosis. If a rewrite would be useful and obvious, include it. Otherwise, ask first.

### Scratch tasks (> 600 words)
Write each pass to its numbered file in the task folder. Return a short note that the result is in `scratch/[task-folder]/final.md`, with the main adjustments named in one or two sentences.

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
