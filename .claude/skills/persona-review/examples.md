# Persona Review Examples

Every review task is processed through a task-specific scratch folder (e.g., `scratch/2026-04-20-auth-review/`). The trace includes:
- `01-owner-voice.md` — Analysis of the original voice and intent.
- `02-review-feedback.md` — Targeted feedback from the reviewer persona.
- `03-revision-draft.md` — The draft incorporating surgical fixes.
- `final.md` — The final version returned to the user.

## Example 1: Single reviewer pass on technical text

**Input:**
```
/persona-review clear-teacher:
[technical text written in sharp-technical voice]
```

**What happens:**
- Reviewer reads as someone focused on explanation and accessibility
- Identifies where dense reasoning skips steps the reader needs
- Applies targeted additions and sentence-level rewording to open up the explanation
- Does not dilute the technical accuracy or replace the sharp-technical voice

**Output includes:**
- Short note on what the clear-teacher reviewer found
- Revised text with improvements applied
- The sharp-technical core is still audible

---

## Example 2: Audience framing improvement

**Input:**
```
/persona-review problem-first-marketer:
[draft README for a developer tool, written by a pragmatic-builder]
```

**What the reviewer targets:**
- Opening that leads with what the tool does, not why anyone would want it
- Feature list without problem context
- No moment where the reader thinks "yes, that is my situation"

**What the reviewer fixes:**
- Rewrites the opening paragraph to surface the problem first
- Adds one or two sentences of problem context before the feature descriptions
- Trims promotional filler that appeared in the original

**What the reviewer does not do:**
- Replace the pragmatic-builder's implementation clarity
- Add excessive warmth or marketing language
- Restructure the whole document

---

## Example 3: Assumption audit

**Input:**
```
/persona-review skeptical-analyst:
[architecture proposal written in pragmatic-builder voice]
```

**What the reviewer targets:**
- Claims presented as settled that are actually assumptions
- Missing evidence for performance predictions
- Sections where alternatives are dismissed without reasoning

**What the reviewer fixes:**
- Adds hedge where an assumption is presented as a fact
- Cuts an unsubstantiated performance claim and replaces with "to be verified"
- Rewrites the alternatives section to show the actual tradeoffs

**What stays unchanged:**
- The proposal's structure and action orientation
- The pragmatic-builder's clarity about implementation path

---

## Example 4: Compression pass

**Input:**
```
/persona-review blunt-operator:
[onboarding guide with substantial padding]
```

**What the reviewer targets:**
- Introductory paragraphs that restate section headings
- Explanations of things the target reader already knows
- Sentences that exist to transition rather than communicate

**What the reviewer does:**
- Cuts 30% of the word count through local deletions
- Removes recap sentences at the end of each section
- Compresses two slow paragraphs into one

**What stays:**
- The guide's friendly, explanatory register in the surviving text
- All actual instructional content

---

## Example 5: Voice-coherence pass against an owner persona

**Input:**
```
/persona-review sharp-technical [owner: sharp-technical]:
[text drafted by sharp-technical but drifting into generic register]
```

**What the reviewer targets (through `sharp-technical`'s own positive shape):**
- The opening sentence reads warm/agreement-seeking — sharp-technical's identity is calm-assured, not warm.
- Mean sentence length sitting at 8 words across the middle section — under the persona's 13 ± 7 target. Several mechanism descriptions have been clipped where they needed breath.
- "robust" and "ensures alignment" appear in para 4 — neither is in sharp-technical's named Lexical Shunts; both are in the persona's Taboo patterns.
- Para 6 ends with a one-sentence summary of itself — sharp-technical does not summary-recap.

**What the reviewer applies:**
- Restarts the opening with a mechanism statement.
- Restores two longer mechanism sentences in the middle section.
- Replaces "robust" / "ensures alignment" with direct description.
- Cuts the recap.

The fixes are framed as restoration toward the persona's positive target, not as removal of generic AI tells.

---

## Example 6: Reviewer with explicit owner persona context

**Input:**
```
/persona-review clear-teacher [owner: blunt-operator]:
[text written in very compressed, direct style that loses beginners]
```

**What happens:**
- Reviewer knows the owner persona is blunt-operator
- Applies improvements calibrated to that knowledge
- Does not add elaborate explanation — just enough for the audience to follow
- Does not undermine the blunt-operator's compression habit

**Output:**
- Targeted additions where the logic skips steps beginners need
- No change to the blunt-operator's sentence rhythm or directness elsewhere
