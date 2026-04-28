# Pass: Diagnostic Audit

## Purpose

Identify specifically what is wrong with the text relative to the persona before rewriting it.

Rewriting without diagnosis produces different text that may have the same problems. The audit makes the problems visible so the rewrite can address them directly.

This audit is **persona-fit only**. It does not enumerate generic AI patterns. The reason — and the evidence behind it — is in `docs/voice-guide.md`. Asking the model to think about anti-AI patterns triggers defensive compression that pushes the prose away from the persona's natural rhythm. The audit stays positive: *does this match the persona, and where does it drift?*

## What to check

### Persona drift

Compare the existing text against the persona's positive fields:

- **Identity drift** — does the implied author still match? Has the draft drifted toward a generic helpful-assistant register?
- **Attention drift** — is the text attending to what the persona attends to (mechanism, problem, evidence, reader experience), or has it shifted focus?
- **Compression drift** — is the persona's compression model preserved? Over-explanation in a persona that assumes competence, or under-explanation in a persona that builds shared context, are both drift signals.
- **Stance drift** — does the text hold certainty the way the persona's stance model describes?
- **Rhythm drift** — does sentence length, variation, and energy match the persona's rhythm model and stylometric signature?

### Argument and structure

- Is the key point landed where the persona would land it?
- Is the argument shape consistent with the persona's reasoning preference (mechanism-first, example-first, tradeoff-first, narrative, problem-solution)?
- Are sections earning their place, or is there padding?

### Filler and over-explanation

These are character-judged, not pattern-judged:
- Is there content that takes space without doing work *for this persona's reader*? (A `clear-teacher` reader needs more setup than a `sharp-technical` reader. The same paragraph can be filler in one and load-bearing in the other.)
- Does the text define terms the persona's audience already knows?
- Does the text walk through reasoning the persona's audience can supply?

### Taboo patterns (persona-specific)

Each persona has a **Taboo patterns** section in its file. Check for those specific patterns. They are part of the persona's character, not a global checklist.

## Output

A short, specific list of what is wrong, framed as drift from the persona. Examples:

Bad: "The writing uses filler."
Good: "Para 3 explains what an SLO is — sharp-technical persona assumes the reader knows. Cut the definition. Para 5 ends with a one-sentence summary that restates the paragraph — pragmatic-builder doesn't padding-summarize. Cut."

Bad: "The tone is wrong."
Good: "The opening sentence reads as warm/agreement-seeking — sharp-technical's identity is calm-assured, not warm. Restart the paragraph with a mechanism statement."

This list is the input for the rewrite pass.

## What this audit deliberately does not do

- It does not consult `dictionaries/ai-patterns.md`, `banned-phrases.md`, `manager-speak.md`, or `docs/anti-ai-guidelines.md` as inputs to the audit. Those are reference material for contributors who want to understand background patterns; they are not a checklist applied during the audit.
- It does not look for "balanced-at-all-costs," "summary sentence accumulation," "structural parallelism" as global anti-patterns. Those are problems only when they cause the draft to drift from the persona's positive shape — and in that case, the persona-drift checks above catch them, framed positively.

If you find yourself enumerating generic AI patterns to remove, you are off-track. Re-anchor on the persona's positive fields.
