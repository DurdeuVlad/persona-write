# Output Handling

How Persona Write returns results.

## Default behavior

### Short tasks
Return the result inline with a brief note on what changed.

The note should be short — one or two sentences naming the main adjustments. Return a full diagnostic only if the user explicitly asked for one.

### Audit requests
Return a concise diagnosis. If a rewrite would be useful and obvious, include it. Otherwise, ask first.

### Long-form tasks
Return a short note that the document was processed section by section, then either:
- the final assembled document inline if it is manageable in length
- the location of the generated Markdown files if the output is large

## When to use files

Use Markdown files for:
- global briefs
- document maps
- chapter memory logs
- revision ticket lists
- final assembled long-form documents
- multi-iteration work where the user will want to track changes

Do not use files for short rewrites or single-section audits. Inline output is faster and easier for the user.

## File naming

Use the document title or a short description as the base name:

- `deployment-guide-brief.md`
- `deployment-guide-map.md`
- `deployment-guide-memory.md`
- `deployment-guide-tickets.md`
- `deployment-guide-final.md`

If there is no natural document title, use the date and a brief description.

## Format

Markdown is the canonical working format.

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
