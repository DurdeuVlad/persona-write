# Long-form Mode

How Persona Write handles large documents.

## Why long-form needs different handling

Long documents fail when rewritten in one pass because:

- voice drifts across sections
- terminology shifts without intention
- earlier sections become inconsistent with later ones after revision
- the whole-document structure is not visible while working on individual passages
- argument threads get dropped or repeated accidentally

A one-shot rewrite of a long document produces cleaner sentences and accumulated drift — voice shifts, terminology inconsistencies, argument threads dropped mid-document.

## When long-form mode activates

The skill switches to long-form mode when:

- the input is a large structured document (multiple sections or chapters)
- the user explicitly requests section-by-section processing
- the text is long enough that one-pass rewriting would produce drift

There is no fixed word count threshold. Use judgment. A 1,500-word document with clear sections may benefit from long-form processing. A 3,000-word continuous essay may not.

## What happens

### Before touching any text

1. **Global brief** — establish what the document is, who it is for, what must stay consistent
2. **Document map** — identify sections, their roles, dependencies, and drift risks

Both documents are created before any section is touched.

### Section-by-section processing

Each section is processed as a unit:

1. Load context from the global brief and all previous chapter memory
2. Run the full short-text pipeline on this section alone
3. Write a chapter memory artifact

The chapter memory is the mechanism that prevents drift. It tracks what each section established so subsequent sections can stay consistent.

### Revision tickets

If a later section introduces something that requires a change to an earlier section, a revision ticket is created instead of silently changing the earlier section mid-process.

Revision tickets are resolved in the final consistency pass.

### Consistency pass

After all sections are complete:

- check persona and tone consistency throughout
- check terminology consistency
- identify and remove unintended repetition
- verify intro/conclusion alignment
- resolve open revision tickets

### Final assembly

Assemble the revised sections into the final Markdown document.

## Output

For long-form work, output is Markdown files:

- `[document-name]-brief.md` — global brief
- `[document-name]-map.md` — document map
- `[document-name]-memory.md` — chapter memory (running log)
- `[document-name]-tickets.md` — revision tickets (if any)
- `[document-name]-final.md` — final assembled document

The working files let the user see what decisions were made and intervene at any point.

## Multi-persona chains in long-form mode

When a persona chain is active, the same chain logic applies at the chapter level and at the whole-document level.

### Per chapter

For each chapter, after the owner persona completes its section rewrite:

1. Each reviewer persona reviews the chapter in order
2. Each reviewer identifies problems from their perspective and applies surgical fixes
3. The owner persona runs a final reconciliation pass on that chapter
4. Chapter memory is written with the outcome of all passes
5. Revision tickets are created if needed

The chapter memory should reflect the state after reconciliation — the owner's voice, not the reviewers'.

### Whole-document level

After all chapters are complete:

1. Reviewers may contribute consistency or framing observations for the whole document
2. The owner persona runs the whole-document reconciliation pass, which includes resolving consistency issues across reviewer passes
3. The consistency pass (`longform/consistency-pass.md`) applies as usual, with the owner's voice as the reference

### What does not change

The global brief, document map, chapter memory structure, and revision ticket system remain the same. The chain behavior is layered on top of the existing section-by-section workflow, not a replacement for it.

## Intervening mid-process

The user can intervene between sections or after the consistency pass.

If the user changes the persona or scope mid-document, the chapter memory and global brief should be updated before continuing. Sections already processed may need a targeted revision ticket rather than a full re-pass.
