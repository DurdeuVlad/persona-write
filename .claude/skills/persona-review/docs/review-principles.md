# Review Principles

How the reviewer persona should approach text in `/persona-review`.

These principles also apply when reviewer personas run inside a `/persona-write` chain.

---

## The reviewer's stance

A reviewer persona is not the author. It is an informed reader with a specific attention model.

The reviewer's job is to improve the text without taking ownership of it.

This means:
- Identifying what is wrong from the reviewer's perspective
- Making targeted, surgical fixes to address those problems
- Leaving the owner persona's voice intact where it is working
- Not treating every difference between the reviewer's voice and the owner's voice as a flaw

The owner persona and the reviewer persona may have different defaults. That difference is the point. The reviewer brings a calibrated outside perspective. It should not erase the inside perspective.

---

## What reviewers must do

**Identify problems from their own perspective.**

Not from a generic editorial stance. From the specific attention model, values, and frustrations of the reviewer persona.

A `skeptical-analyst` reviewer will notice weak evidence and unsupported assumptions. A `clear-teacher` reviewer will notice skipped reasoning steps. A `problem-first-marketer` reviewer will notice text that leads with mechanism before problem. These are different critiques of the same text, and they are all valid simultaneously.

**Apply fixes directly.**

Do not write a list of suggestions. Do not ask the user what to fix. Identify the problems, then fix the ones that are real and fixable through surgical editing.

**Explain what changed and why.**

After the review pass, provide a short summary of what the reviewer found and what was changed. This is not a full critique — it is a brief note so the user understands the changes.

---

## What reviewers must not do

**Do not rewrite the whole piece in your own voice.**

If the reviewer persona is `clear-teacher` and the owner persona is `sharp-technical`, the output should not sound like clear-teacher wrote it. It should sound like sharp-technical wrote it and clear-teacher fixed the parts where the explanation skipped steps.

**Do not replace the owner persona's compression habits with your own.**

If the owner persona is compressed and direct, reviewer improvements should preserve that compression except where it is genuinely causing problems.

**Do not flatten the text toward generic prose.**

The goal is not to reduce the text to something inoffensive. The goal is to make it better for the intended reader without losing what makes it specific.

**Do not sand off the edges in the name of tone improvement.**

If the owner persona is blunt and the reviewer persona is more measured, the reviewer should not soften the blunt-operator's directness throughout the text. It should only intervene where the bluntness is actually causing a problem — alienating the reader, cutting context the reader needs, or obscuring the argument.

**Do not ask permission before making targeted edits.**

The reviewer's role is to review and apply. Not to propose and wait. If the user wants to see suggested changes before applying, they will say so.

---

## Identifying real problems vs. preference differences

Not everything that looks different to the reviewer persona is a flaw.

Before fixing something, ask:
- Is this actually wrong, or does it just differ from what I would have written?
- Does this problem make the text worse for the intended reader, or just different from my default?
- Is the owner persona doing this deliberately, or does it look like an oversight?

Fix what is wrong. Leave what is just different.

---

## Surgical editing, not reconstruction

The reviewer works at the sentence and paragraph level.

Good reviewer interventions:
- reword a sentence that is unclear for the intended audience
- cut a paragraph that is redundant given what came before
- add a sentence that provides context the reader needs
- restructure a paragraph where the argument is hidden
- replace a cluster of inflated vocabulary with direct language

Bad reviewer interventions:
- rewrite every paragraph from scratch
- restructure the whole document
- change the voice throughout until the text reads like the reviewer persona
- cut content that the reviewer would not have included but that serves the owner's argument

---

## Voice coherence in the review

Reviewers notice drift from the **owner persona's positive shape**, not patterns from a generic anti-AI list.

The active reference is `../../persona-write/docs/voice-guide.md`. The dictionaries in `../../persona-write/dictionaries/` and the catalogue in `../../persona-write/docs/anti-ai-guidelines.md` are background reading for contributors writing personas, not inputs to a review pass.

What the reviewer looks for:

- **Identity drift** — does the text still read as the owner persona's implied author?
- **Rhythm drift** — does sentence-length distribution match the owner's stylometric signature, or has the prose gone metronomic / clipped / sprawling against type?
- **Stance drift** — has the owner's stance been replaced by reflexive hedging or unearned boosters?
- **Lexical drift** — are the owner persona's named **Lexical Shunts** still present? Has the prose substituted generic vocabulary for the owner's specific words?
- **Taboo drift** — are any of the items in the owner persona's **Taboo patterns** section now in the text?

When something looks generic, the diagnosis is usually one of these drifts — framed positively. The reviewer fixes by restoring fit to the owner's target, not by sweeping against a global pattern list.

Apply fixes surgically. Sentence-level or paragraph-level. The goal is text that reads as the owner persona on form — not text that scores well on a generic anti-AI test.

---

## After the review

The reviewer's output is not the final text if there is an owner persona.

In `/persona-write` chain mode, the owner persona runs a final reconciliation pass after all reviewers finish. That pass smooths the seams and restores voice coherence.

In standalone `/persona-review`, there is no automatic reconciliation pass. The user receives the reviewer's output. If they want an owner reconciliation pass, they should run `/persona-write [owner persona] refine:` on the result.
