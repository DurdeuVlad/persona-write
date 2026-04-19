# Pass: Persona Mapping

## Purpose

Translate the persona definition into specific decisions about this particular piece of text.

Persona definitions describe tendencies. Persona mapping applies those tendencies to the content at hand.

## What to decide

### What this persona foregrounds
Given the subject matter and intent, what would this persona lead with?

A sharp-technical persona writing about a database design decision would foreground the mechanism and constraints.
A pragmatic-builder persona writing the same piece would foreground the tradeoffs and the recommendation.
A clear-teacher persona would build from the unfamiliar concept toward the practical implication.

The same content, structured differently.

### What this persona cuts
What would this persona find unnecessary?

- background context the reader does not need
- motivational framing on a technical point
- softening hedges on a clear claim
- examples when the mechanism is obvious

Not every persona cuts the same things. Map it specifically.

### How this persona handles certainty
Is the text making strong claims, hedged claims, or uncertain ones?

- How does this persona handle a strong claim? Does it assert it directly or qualify it?
- How does this persona handle uncertainty? Does it name it explicitly or understate it?
- Where would this persona push back on claims that feel overclaimed?

### Compression level for this content
Given the audience and subject, how dense should this version be?

- What vocabulary is safe to use without definition?
- What can be implied versus stated?
- What must be made explicit even though it slows the pace?

### Rhythm decisions
Given the persona's rhythm model, how should this content be structured?

- Where are the short sentences?
- Where is there more room to breathe?
- What gets a paragraph break? What stays in the same paragraph?

## Output

A short working brief — not written prose, just decisions:

```
Persona: sharp-technical
Lead with: the constraint that makes the naive approach fail
Cut: the motivating paragraph about why this matters (reader knows)
Certainty: direct on the failure mode, hedged on the performance claim (data is thin)
Compression: high — expert audience, no definitions needed
Rhythm: short sentences for the main claim, medium for the mechanism explanation
```

This brief is the operating guide for the rewrite pass.
