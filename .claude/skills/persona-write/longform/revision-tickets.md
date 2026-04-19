# Long-form: Revision Tickets

## Purpose

Revision tickets record problems with earlier sections discovered while working on later ones.

In long-form work, it is common to rewrite section 3, then discover that section 5 changes the framing in a way that makes section 2 inconsistent. The solution is not to silently edit section 2 mid-process. The solution is to log a revision ticket and address it in the final consistency pass.

## When to create one

Create a revision ticket when:

- a later section introduces an argument or conclusion that contradicts an earlier section
- a later section uses terminology in a way that conflicts with how an earlier section defined it
- a later section makes a claim that requires an earlier section to set it up — but the earlier section does not
- a later section changes the implied audience, scope, or purpose in a way that affects earlier sections

Do not create a revision ticket for minor style inconsistencies. Those are handled in the consistency pass.

## Format

```markdown
## Revision Ticket

**Affects:** Section [number or title]
**Discovered in:** Section [number or title]
**Issue:** [Describe the specific problem in one to three sentences]
**Recommended change:** [Describe what should change in the affected section]
**Priority:** [High / Medium / Low]
**Status:** [Open / In progress / Resolved]
```

### Priority guidance

**High:** The inconsistency directly contradicts something the reader was told. If left unresolved, the document will confuse or mislead.

**Medium:** The inconsistency creates friction or a missed opportunity. The document still works but is weaker.

**Low:** A minor alignment issue. Worth fixing but will not break the document if it remains.

## When to resolve tickets

Revision tickets are resolved during the final consistency pass (see `consistency-pass.md`), not during section-by-section work.

The exception is a high-priority ticket that was discovered early and where resolving it now makes subsequent section work significantly easier.

## Keeping the list

As section work progresses, the revision ticket list may grow. Review it before the consistency pass to prioritize.

Mark tickets as resolved after the consistency pass addresses them. Do not delete resolved tickets — they are a record of what was found and fixed.
