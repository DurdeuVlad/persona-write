# Long-form: Chapter Workflow

## Purpose

Describes how to process each section or chapter of a long-form document.

The chapter workflow runs once per section. It is the short-text workflow applied locally, with additional steps for tracking state across the document.

## Steps

### 1. Load context
Before touching the section:
- review the global brief
- review the document map entry for this section
- review the chapter memory from all previous sections

This prevents drift from accumulating silently.

### 2. Local intent extraction
Within this section:
- what is this section trying to do?
- who is it written for at this point in the document?
- what must be preserved?
- what has been established in prior sections that this section builds on?

### 3. Local diagnostic audit
What is wrong with this section specifically?

Apply the standard diagnostic audit but constrain it to this section. Also check:
- does this section's voice match the global brief and prior sections?
- does this section use terminology consistently with what was established earlier?
- does this section introduce anything that contradicts prior sections?

### 4. Local persona mapping
Given the global brief, the persona, and this section's specific function, decide:
- what this persona would foreground in this section
- what to cut
- how to handle certainty on the claims in this section
- rhythm and compression for this section

Some sections call for a different energy than others. The persona stays consistent; the application changes with context.

### 5. Section rewrite
Rewrite the section using the local persona mapping as the brief.

Do not rewrite other sections at this stage, even if you notice issues in them. Flag them as revision tickets instead.

### 6. Voice coherence
Check the section against the persona's positive shape — Identity, Rhythm model, Stylometric Signature, Lexical Shunts, Taboo patterns. Apply targeted fixes toward the persona's target. See `../passes/voice-coherence.md`.

### 7. Local refinement
Tighten and smooth the section.

Also check continuity:
- does this section connect naturally to the section before it?
- does it set up the section after it correctly?
- do the transitions at the edges need adjustment?

### 8. Local fidelity check
Verify meaning, fact accuracy, nuance retention, and persona fit for this section.

Cross-check against the global brief must-keep list.

### 9. Write chapter memory artifact
After the section is complete, update the chapter memory with a structured record of what this section established.

See `chapter-memory.md` for the format.

## Notes

Do not batch sections. Process one at a time.

If a section is very long, it may be appropriate to divide it into subsections and process each as a unit.

If the document has no clear section breaks, impose working sections based on topic or function before beginning.
