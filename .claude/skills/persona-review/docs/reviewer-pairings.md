# Reviewer Pairings

Practical combinations for specific writing goals. Each pairing has a primary purpose.

---

## Two-persona chains

### `sharp-technical -> problem-first-marketer`
**Use for:** README files, public documentation, developer tool landing pages, anything technical that needs to reach a broader audience.

What happens: `sharp-technical` writes with accuracy and density. `problem-first-marketer` surfaces the reader's problem before the mechanism, improves entry points, and softens sections where the reader needs orientation before being given detail. The final text still sounds like `sharp-technical` wrote it — it just no longer assumes the reader already cares.

---

### `sharp-technical -> clear-teacher`
**Use for:** Tutorials, how-to guides, onboarding documentation, technical explanations for a mixed-experience audience.

What happens: `sharp-technical` writes an accurate, dense draft. `clear-teacher` opens up reasoning steps that the author skipped, makes implicit assumptions explicit, and improves the learning path. Does not add unnecessary warmth — just the explanation the reader needs to follow the argument.

---

### `pragmatic-builder -> skeptical-analyst`
**Use for:** Proposals, architecture decision records, technical plans, anything that needs to hold up to scrutiny.

What happens: `pragmatic-builder` drafts a clear, action-oriented proposal with a defined implementation path. `skeptical-analyst` then identifies which claims are assumptions, which predictions need evidence, and where alternatives were dismissed too quickly. The final text is still practical and concrete — but its reasoning is tighter.

---

### `blunt-operator -> pragmatic-builder`
**Use for:** Aggressive editing passes on padded, bureaucratic, or over-hedged text, followed by usability correction.

What happens: `blunt-operator` cuts aggressively — padding, ceremony, recap sentences, overlong setup. `pragmatic-builder` then restores what was cut unnecessarily: context the reader needs, next steps that disappeared, transitions that carry meaning rather than just filling space. The result is shorter than the original but still usable.

---

### `clear-teacher -> sharp-technical`
**Use for:** Over-explained text that needs compression without losing accessibility.

What happens: `clear-teacher` ensures the explanation is correct and followable. `sharp-technical` then compresses it — cuts repetition, removes unnecessary scaffolding, tightens the argument. The result explains accurately without walking the reader through things they can supply themselves.

---

### `problem-first-marketer -> skeptical-analyst`
**Use for:** Marketing copy, product announcements, and public-facing content that tends to overclaim.

What happens: `problem-first-marketer` writes compelling, audience-oriented content with strong framing. `skeptical-analyst` then removes unsupported claims, tones down superlatives, and makes the argument more credible by identifying where the text oversells. The result is still persuasive but does not make claims the product cannot back up.

---

## Three-persona chains

### `sharp-technical -> clear-teacher -> problem-first-marketer`
**Use for:** Technical product documentation intended for both technical users and broader stakeholders.

What happens:
1. `sharp-technical` writes for accuracy
2. `clear-teacher` opens up the explanation for readers with less context
3. `problem-first-marketer` improves framing, entry, and audience orientation
4. `sharp-technical` runs the final reconciliation to restore core voice

The final output is technically accurate, followable, and oriented around the reader's situation — without sounding like three different people wrote it.

---

### `pragmatic-builder -> skeptical-analyst -> clear-teacher`
**Use for:** Internal proposals that need to be both rigorous and readable by non-expert stakeholders.

What happens:
1. `pragmatic-builder` drafts a concrete, action-oriented proposal
2. `skeptical-analyst` tightens the reasoning and identifies assumptions
3. `clear-teacher` makes the argument accessible to readers without deep domain context
4. `pragmatic-builder` runs the final reconciliation to restore action-orientation

---

## Choosing a reviewer

Ask: what is the most likely failure mode of the owner persona's output for this specific piece?

- `sharp-technical` writing for a mixed audience: add `problem-first-marketer` or `clear-teacher`
- `pragmatic-builder` writing something that needs to hold up to scrutiny: add `skeptical-analyst`
- `blunt-operator` writing something that cut too aggressively: add `pragmatic-builder`
- `problem-first-marketer` writing something that overclaims: add `skeptical-analyst`
- Any persona writing dense technical content for beginners: add `clear-teacher`
- Any persona writing internal content that needs to be concise: add `blunt-operator`

---

## What makes a pairing work

Good reviewer pairings have a clear reason to exist. The reviewer addresses a specific failure mode of the owner.

A reviewer that shares most of the owner persona's values does not add much. A reviewer that directly addresses the owner's blind spot adds the most.

Do not stack reviewers for the sake of coverage. Two reviewers with overlapping concerns will produce redundant passes and introduce more reconciliation work without proportional benefit.
