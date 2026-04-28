# Pass: Voice Coherence

## Purpose

Check whether the draft reads as the persona it was written through. **Positive frame only.** This pass does not enumerate AI patterns to remove. It checks fit against the persona's own positive shape.

The reasoning behind this framing is in `docs/voice-guide.md`. The short version: making the model think about generic AI patterns triggers defensive compression that pushes the prose *away* from the persona's natural rhythm. Keeping the frame positive — "is this the persona's voice?" — produces output that lands closer to the persona's actual stylometric signature.

## What to check

Read the draft once, then check it against the persona file's positive fields.

### 1. Identity match
Does the implied author of the draft match the persona's Identity section? If the persona is "calm-assured technical peer," does the draft read calm and assured, or tense and over-edited?

### 2. Rhythm match
Compare against the persona's **Rhythm model** and **Stylometric Signature**:
- Mean sentence length within the persona's band?
- Sentence-length variation appropriate (not metronomic, not jagged)?
- Opener inventory matches (bare-noun, clause-first, fragment, etc. as the persona prefers)?
- Punctuation profile in band (em-dashes, semicolons, colons as the persona uses them)?

If sentences are uniformly clipped when the persona has 13±7 mean SL — restore breath. If em-dashes are missing when the persona uses them — restore them. The fix is **toward the target**, not away from a banned pattern.

### 3. Stance match
Does the draft hold certainty the way the persona's **Stance model** describes? Reflexive hedging when the persona is direct, or unearned boosters when the persona is careful, are both drift signals.

### 4. Taboo patterns (persona-specific only)
Each persona's **Taboo patterns** section names things *that persona* would not write. Cross-check. These are character expressions, not a global checklist.

### 5. Lexical fit
Are the persona's **Lexical Shunts** present? If the persona prefers "wiring up" over "implementing," is the prose using the persona's vocabulary or a generic substitute?

## What this pass deliberately does not do

- It does not consult `dictionaries/ai-patterns.md`, `banned-phrases.md`, `manager-speak.md`, or `docs/anti-ai-guidelines.md` during the check. Those are reference material for contributors, not pipeline inputs.
- It does not scan for "balanced-at-all-costs," "summary sentence accumulation," or any other AI-pattern category. The persona file's positive fields already constrain those.
- It does not rewrite paragraphs to break parallelism for its own sake. Parallelism is fine when it carries the argument; it is a problem only when it overrides the persona's natural rhythm.

## Output

If the draft matches the persona on Identity, Rhythm, Stance, Taboo patterns, and Lexical fit: confirm and pass through.

If the draft drifts on a specific dimension: name the drift in one or two sentences, apply a targeted fix, and pass through. Drifts are sentence-level or paragraph-level, not document-level rewrites.

Examples of drift notes:
- "Mean sentence length sitting at 8 in para 3 — under the 13 target. Restored two longer mechanism sentences."
- "Two em-dashes from draft cut during refine. Restored one — the asides earned their place."
- "Para 5 hedges with `it could be argued` — not in persona. Replaced with direct claim."

## Calibration

Use the persona's **Stylometric Signature** as the calibration target, not the rubric's general guidance. A `blunt-operator` draft at mean SL 9 is on target; a `skeptical-analyst` draft at mean SL 9 is off target. Same number, different verdict.
