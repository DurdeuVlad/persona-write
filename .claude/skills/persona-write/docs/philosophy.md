# Philosophy

## Cornerstone

**Writing quality is a positive-shape problem, not a negative-shape one.**

Telling a model *who to be* produces a specific writer. Telling a model *what not to be* produces a defensive, compressed, generic anti-AI register where every persona collapses toward the same flat voice.

Everything in this project follows from that one claim:

- Personas are defined by **positive shape** — Identity, Attention, Stance, Rhythm, Stylometric Signature, Lexical Shunts, opener inventory, persona-specific Taboo patterns *as character traits*.
- The pipeline runs **persona-fit checks**, not anti-AI scrubs. There is no global ban-list applied to the prose. The persona file is the filter.
- The dictionaries (`dictionaries/ai-patterns.md`, `banned-phrases.md`, `manager-speak.md`, `docs/anti-ai-guidelines.md`) are reference-only artifacts for *teaching* why generic AI prose fails. They are not pipeline inputs.
- New skills, new passes, and new personas must be expressible as positive-shape additions. If a proposal is shaped as "the writer should avoid X," it has to be re-expressed as "the writer is the kind of person who Y" before it earns its place.

This principle was empirically validated in two cross-model pilots; see `voice-guide.md` for the evidence.

## The problem this is solving

Most AI writing fails for structural reasons, not surface ones.

The text is too smooth. Sentences are the same length. Paragraphs are the same shape. Arguments are hedged into balance even when the evidence isn't balanced. Points are softened. No stance. No compression. No voice.

Fixing this by swapping out words or running text through a "humanizer" does not work. The problem is in the shape of the thinking, not the choice of vocabulary.

This is also why "avoid AI writing patterns" does not produce good writing on its own. Removing generic phrases produces non-generic text that is still shapeless. The goal is not to subtract bad patterns. The goal is to add something real.

## The core insight

Writing sounds like someone when it makes choices a specific kind of person would make.

Not typos. Not slang. Not informal contractions. Those are surface quirks that any writer can imitate and any reader can see through.

The real choices:
- what to foreground
- what to cut
- how much to explain
- what to assert directly versus what to hedge
- what rhythm to use
- what to care about

These choices are not random. They follow from who the writer is and what they pay attention to.

A technical writer who assumes reader competence does not explain things the reader knows. That is not a stylistic quirk — it is a compression decision that follows from their model of the reader.

A skeptical analyst who cares about evidence does not let weak claims pass. That is not a tone choice — it is an attention model that shapes what they notice.

## Why persona first

Persona is the organizing principle because it is what makes writing choices coherent.

Without a persona, writing rules pull in different directions. "Be concise" without a reader model produces terse text that drops necessary context. "Vary sentence length" without a sense of emphasis produces variation that lands nowhere.

A persona gives the rules direction. Concision becomes: cut what this specific reader does not need. Sentence variation becomes: short where this persona lands a point, longer where they build one.

## Why multi-pass

One-shot rewriting produces better text that has the same structural problems as the original, because the same instincts are applied throughout.

Multi-pass work separates concerns:
- first, understand what the text is doing
- then, diagnose what it is doing wrong
- then, apply the persona
- then, clean up what the persona application missed
- then, verify nothing was broken

Each pass does one job. The result is more reliable and easier to correct when something goes wrong.

## Why not detector evasion

This system does not try to produce text that fools AI detectors.

Detection is an arms race. The framing is wrong. Optimizing for detector evasion produces text that is calibrated against a classifier, not against a human reader's sense of quality.

More fundamentally: the goal is not to make text that does not look like it was generated. The goal is to make text that is actually good.

Good writing passes detectors as a side effect of being good. Evasion-optimized writing is often poor writing that happens to score well on a metric.

## Why not fake quirks

Random typos, affected informality, forced imprecision — these are also a form of performance.

Real human texture is not the presence of errors. It is the presence of mind. A writer who sees a problem clearly, states it without apology, and does not pad the conclusion has human texture. The mechanism of that is their attention model and their compression model, not a spelling mistake.

## What this is trying to produce

Writing that sounds like a specific kind of person made choices about what to say and how.

Not writing that sounds like nobody. Not writing that sounds like everyone. Writing that sounds like someone.

## How this principle is enforced

When evaluating any change to this project — new pass, new dictionary, new doc, new persona — apply this test:

1. **Is the change expressed as a positive shape** ("the writer is the kind of person who…") rather than a negative one ("the writer should avoid…")?
2. **Does the change live inside a persona file**, where it can be calibrated to a specific writer, rather than as a global rule applied to all prose?
3. **Does the change preserve the model's attention budget for the persona's positive shape**, instead of consuming it with monitoring against a generic list?

If the answer to any of these is *no*, the change has to be re-shaped before it ships. The dictionaries failed all three tests in v2.1.0 — that is why they were demoted in v2.2.0.
