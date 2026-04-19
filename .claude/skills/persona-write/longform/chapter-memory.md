# Long-form: Chapter Memory

## Purpose

The chapter memory is a rolling record of what each section established.

It is the mechanism that prevents voice drift, argument drift, and terminology drift in long documents. Without it, each section is processed in isolation and the document loses coherence.

## When to write it

After each section is completed and passes the fidelity check.

## What to record

### Section identifier
The heading or working title of the section.

### Summary
One to three sentences. What this section said. Not what it was about — what it actually argued, explained, or established.

### Key claims
The main claims made in this section. Write them as statements, not as descriptions.

Description instead of claim: "The section discusses the tradeoffs of approach A versus approach B."
Claim with evidence: "Approach A outperforms approach B under high load, but requires more memory."

### Terminology established
Any terms defined or given specific meaning in this section that will be used elsewhere.

Format: `term: definition or usage note`

### Tone notes
If this section's tone was adjusted from the default persona application, note how and why.

This helps identify when a section was written differently from the rest, and prevents treating that adjustment as the new norm.

### Unresolved threads
Arguments or ideas introduced in this section that are not yet resolved.

A claim made in section 2 that section 5 is supposed to support. An open question acknowledged in section 3 that a later section should close.

If these are not tracked, they get lost.

### Promises made to the reader
Anything the section committed to that a later section must deliver.

"We will explain how this works in the next section." If section 5 makes that promise, it must be in the chapter memory so section 6 knows to fulfill it.

### Style drift risks
Any tendency this section showed that could become a drift risk if repeated.

Examples: "This section used a more formal register than the persona mapping intended." "Three rhetorical questions in this section — watch for accumulation."

### Possible upstream revisions
If this section introduced something that may require a change to an earlier section, note it here. A revision ticket should be created separately.

## Format

Keep each entry concise. This is a reference document, not prose.

```markdown
## Section: [title]

**Summary:** [1–3 sentences]

**Key claims:**
- [claim]
- [claim]

**Terminology:**
- term: meaning

**Tone notes:** [if any]

**Unresolved threads:**
- [thread]

**Promises to reader:**
- [promise]

**Style drift risks:** [if any]

**Possible upstream revisions:** [if any]
```
