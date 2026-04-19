# Pass: Anti-AI Scrub

## Purpose

Remove the residue that makes text feel generated rather than written.

This pass runs after the rewrite. Its job is to catch the patterns that survive even a good rewrite because they are so deeply habitual.

This is not about fooling detectors. It is about removing patterns that make text feel empty, over-symmetric, or frictionless — processed rather than written.

## What to look for

### Opener patterns
Does every paragraph begin the same way?

- "It is worth noting that..."
- "One important consideration is..."
- "When we think about..."
- "This is a key point because..."

These are filler openers. They exist to start a sentence, not to communicate.

### Symmetrical structure
Does the text have unnaturally even parallel structure throughout?

- Every point followed by exactly one elaborating sentence
- Every section with exactly one example
- Every argument followed by a counterargument followed by a resolution

Real writing is not this even. Symmetry used throughout signals processing, not thinking.

### Generic transitions
Do paragraphs connect with transitions that could fit anywhere?

- "Furthermore..."
- "Additionally, it is important to..."
- "With this in mind..."
- "That said..."

These transitions do not carry information. They fill the gap between one thing and the next.

### Recap sentences
Does the text summarize what it just said at the end of each section?

A summary sentence signals that the writer was not confident the point landed. In well-written text, the point either lands or it does not — adding a recap rarely helps.

### Balanced-at-all-costs conclusions
Does the conclusion acknowledge every possible concern in a way that says nothing?

"While X has challenges, it also has benefits. With careful consideration, it can be effective in many contexts."

This is a non-conclusion. Real writers have a view. They state it.

### Forced warmth
Does the text add warmth signals that were not in the original?

- "This is an exciting development..."
- "It is fascinating to consider..."
- "What a great question this raises..."

These are enthusiasm performances. If the original was not warm, do not add warmth.

## What not to do

Do not introduce fake human signals:

- deliberate typos
- affected informality ("y'know", "tbh", "lemme")
- forced imprecision
- contrived self-correction ("well, actually...")

These are not human texture. They are a different kind of performance.

## Extended pattern reference

For vocabulary clusters, grammar-level tells, pattern stacking, and the concept of treating clusters as single strong signals, see:

`docs/anti-ai-guidelines.md`

That document is the shared reference for all passes and for `persona-review`. Use it alongside the patterns above, not instead of them.

## Output

Return the scrubbed version with the changed passages noted if the changes are substantial.

If few patterns were found, say so briefly and confirm the text passes the scrub.
