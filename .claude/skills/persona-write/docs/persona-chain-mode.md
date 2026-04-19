# Persona Chain Mode

How Persona Write handles multiple personas in sequence.

## What it is

When you give `/persona-write` more than one persona, the skill interprets them as an ordered chain.

- The first persona **owns the text**. It writes or rewrites the draft.
- Every subsequent persona is a **reviewer**. It does not become a co-author.
- After all reviewers finish, the owner runs a **final reconciliation pass** to smooth the seams and restore voice coherence.
- The final output should still read primarily as the first persona's work.

## How to invoke it

The skill accepts natural expressions. Any of these work:

```
/persona-write sharp-technical -> problem-first-marketer:
[paste text]
```

```
/persona-write sharp-technical, problem-first-marketer:
[paste text]
```

```
/persona-write: write this as a sharp technical person, then review it as a problem-first marketer
[paste text]
```

Do not use `owner:` or `reviewer:` syntax. The skill infers roles from position.

## What each reviewer does

Reviewers run a two-step process automatically. They do not ask permission before making changes.

### Step A: identify problems

From the reviewer persona's perspective, note:

- what feels off, unclear, or misframed
- where tone is wrong for the intended audience
- where the owner persona overdid or underdid something
- where the argument, framing, or emphasis can improve
- what is too dense, too soft, too vague, too technical, too cold, or too polished

### Step B: apply surgical fixes

The reviewer then makes targeted changes directly:

- sentence-level rewording
- paragraph-level restructuring
- local framing improvements
- cuts where content is redundant or misplaced
- additions where context is missing for the audience

Reviewers must not:
- rewrite the whole piece in their own voice
- replace the owner persona as the primary author
- flatten the text into blended, generic prose
- shift the text's center of gravity without clear cause

The reviewer makes the text better without stealing it.

## Final owner reconciliation pass

After all reviewers finish, the owner persona runs one more pass.

This pass:
- smooths seams left by reviewer edits
- restores the owner's dominant voice where it was displaced
- preserves reviewer improvements that work
- ensures the document reads as one coherent piece, not a patchwork
- keeps the owner's reasoning style, compression habits, stance, and rhythm

This pass is mandatory in chain mode. It is not optional.

## Multiple reviewers

Reviewers are applied in order. Each reviewer reads what the previous one produced.

Example with three personas:

```
/persona-write sharp-technical -> clear-teacher -> problem-first-marketer:
[paste text]
```

Execution order:
1. `sharp-technical` writes the draft
2. `clear-teacher` reviews and applies surgical fixes
3. `problem-first-marketer` reviews and applies surgical fixes
4. `sharp-technical` runs the final reconciliation pass

The final output should still feel like `sharp-technical` at the core.

## Long-form documents

For long documents, the same chain logic applies per chapter or major section.

Per chapter:
1. owner persona drafts or rewrites the chapter
2. each reviewer persona reviews that chapter in order
3. each reviewer applies surgical fixes
4. owner persona runs a final reconciliation pass on the chapter
5. chapter memory is updated with the outcome
6. revision tickets are created if the chapter affects earlier sections

At the whole-document level, after all chapters are complete:
- reviewers may contribute consistency or framing observations
- the owner persona runs the final whole-document reconciliation pass

## Examples of useful pairings

### Two-persona chains

**`sharp-technical -> problem-first-marketer`**
Use for: README files, public docs, tool landing pages.
What it does: `sharp-technical` writes the substance with precision and density. `problem-first-marketer` softens entry points, surfaces the reader's problem earlier, and improves framing for a broader audience without diluting the content.

**`sharp-technical -> clear-teacher`**
Use for: tutorials, onboarding docs, how-to explanations.
What it does: `sharp-technical` writes a dense accurate draft. `clear-teacher` opens up the reasoning, adds the missing explanatory steps, and removes assumptions the reader may not share.

**`pragmatic-builder -> skeptical-analyst`**
Use for: proposals, plans, architecture decision records.
What it does: `pragmatic-builder` drafts a clear, action-oriented proposal. `skeptical-analyst` identifies assumptions, gaps, and weak evidence, and sharpens the argument.

**`blunt-operator -> pragmatic-builder`**
Use for: aggressive cleanup of padded or bureaucratic text.
What it does: `blunt-operator` cuts to the bone. `pragmatic-builder` then adds back the usability — necessary context, clear next steps, reader orientation.

### Three-persona chain

**`sharp-technical -> clear-teacher -> problem-first-marketer`**
Use for: technical product documentation that also needs to be accessible and compelling.
What it does: `sharp-technical` writes for accuracy. `clear-teacher` opens up the explanation. `problem-first-marketer` improves entry and framing for a wider audience. Owner reconciliation restores the sharp-technical core.

## What chain mode is not

Chain mode is not co-authorship. The final text has one dominant voice — the owner's.

Chain mode does not blend personas. The goal is one persona improving another's work, not averaging them together.

Chain mode does not require the reviewers to be polite. They identify problems directly and apply fixes. The owner reconciliation pass is where the result gets smoothed back into a coherent voice.
