# Pass: Diagnostic Audit

## Purpose

Identify specifically what is wrong with the text before rewriting it.

Rewriting without diagnosis produces different text that may have the same problems. The audit makes the problems visible so the rewrite can address them directly.

## What to check

### Generic assistant tone
Does the text sound like it was produced by an AI trying to sound helpful?

Signs:
- balanced, symmetrical sentence structure throughout
- every claim softened to avoid seeming too direct
- transitions that do the work of enthusiasm rather than logic
- summary sentences at the end of every paragraph
- filler at the beginning of every paragraph

### Filler and padding
Is there content that takes up space without doing work?

Patterns:
- introductory clauses that restate what was just said
- sentences that exist to transition rather than to communicate
- closing sentences that summarize without adding
- explanations of things the reader does not need explained

### Over-explanation
Does the text explain what the reader already knows?

Signs:
- definitions of common terms in a technical document
- background context the audience has
- explaining the purpose of something the reader is already using
- walking through reasoning the reader can supply

### Weak structure
Is the argument or explanation organized clearly?

Problems:
- key point buried in the middle or end
- setup and conclusion mismatched
- repetition of the same point in different words
- sections that do not earn their place

### Corporate or managerial sludge
Does the text use language that sounds official but communicates nothing?

Signs:
- leverage, synergy, alignment, bandwidth, visibility
- "ensure alignment with stakeholder expectations"
- any noun phrase where a verb would be clearer
- passive voice used to avoid assigning responsibility

### Voice flatness
Does every sentence read at the same register and energy level?

Signs:
- consistent mid-length sentences throughout
- no variation in sentence length or rhythm
- no moments of emphasis or compression
- uniformly hedged or uniformly assertive throughout

### Fake neutrality
Does the text present a clear position as if it were balanced, or balance as if it were wisdom?

Signs:
- "on the one hand... on the other hand" when one side is clearly stronger
- hedged conclusions that do not commit to what the evidence supports
- refusing to name a recommendation when one exists

## Extended pattern reference

For vocabulary clusters, pattern stacking, grammar-level tells, promotional language patterns, and the principle of treating clusters as single strong signals, see:

`docs/anti-ai-guidelines.md`

Apply those patterns as part of this audit pass. The audit is not only about structural or tonal problems — dense AI vocabulary in a single paragraph is also a concrete problem to name.

## Output

Produce a short, specific list of what is wrong. Not categories — examples.

Bad: "The writing uses filler."
Good: "The opening sentence restates the paragraph heading. The fourth paragraph ends with a summary that adds nothing. Three uses of 'it is important to note that'."

This list is the target for the rewrite pass.
