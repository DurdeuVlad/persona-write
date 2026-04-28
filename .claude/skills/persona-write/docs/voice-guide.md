# Voice Guide — what makes a persona sound like a person

Empirical companion to `persona-theory.md` and `writing-quality-rubric.md`. The framing in this guide is the active framing for `persona-write`, `persona-review`, and `persona-copy`.

## Origin

This guide was written after a controlled pilot that compared four pipeline configurations on the same prompt and persona (`sharp-technical`, technical topic):

- **A** — scratch step files + anti-AI scrub (the previous default)
- **B** — scratch step files, no anti-AI scrub
- **C** — in-memory, anti-AI scrub
- **D** — in-memory, no anti-AI scrub

Quantitative result (target mean sentence length for `sharp-technical` is 13 ± 7):

| Condition | Words | Mean SL | Voice (target 5) | Human-likeness (1-5) |
|---|---|---|---|---|
| A — scratch + scrub (previous default) | 450 | 7.6 | 3 | 2 |
| C — in-memory + scrub | 490 | 7.3 | 3 | 3 |
| B — scratch, no scrub | 572 | 9.7 | 4 | 4 |
| **D — in-memory, no scrub** | **722** | **11.5** | **5** | **5** |

The scrub-active conditions came in 30-40% shorter and at mean sentence length **half** of the persona's target. The previous default scored worst on the human-likeness judgement. The simplest configuration — in-memory, no scrub — scored cleanest on every dimension.

The full experiment, condition outputs, blind-then-unblind scoring, and findings doc lived in `scratch/2026-04-28-pipeline-test/` (gitignored). The findings drove the pipeline changes shipped alongside this doc.

## The principle

A persona's voice is built from **positive shape** (Identity, Attention, Stance, Rhythm, Stylometric Signature, Lineage). Negatives — Taboo patterns — only work when they live inside that positive shape, framed as character expressions of the same writer.

A global "anti-AI" sweep does the opposite. It strips the prose of anything that *resembles* a generic-AI tell, including features the persona genuinely uses. The result is a homogenized defensive register that does not match any of the personas.

If you want a persona to sound like a person, **do not ask the model to think about AI patterns**. Ask it to be the persona.

## What this means in practice

### When drafting through a persona

- Read the persona file once. Hold its Identity, Rhythm, and Stylometric Signature as the brief.
- Write through them. Do not pause to scan for banned phrases.
- After the draft, do one coherence check: *does this match the persona's Rhythm and Stylometric Signature?* If sentences are uniformly clipped when the persona has 13±7 mean SL, restore breath. If em-dashes are missing when the persona uses them, restore them. The check is **fit to positive target**, not enumerate-and-remove.

### When reviewing

- Reviewers identify problems through their own persona's lens.
- Reviewers do not enforce a global anti-AI checklist on the owner persona's text.
- The Taboo patterns inside each persona file are still useful — but only as part of the reviewer's character ("from a `sharp-technical` reviewer's perspective, the over-explanation in para 3 is the problem"). They are not a master list to apply globally.

### When extracting a persona from samples (`persona-copy`)

- The extracted persona's Stylometric Signature is the target. The reproduction should match the *source author's* signature, not avoid generic AI tells in the abstract.
- If the source author *does* use phrases that appear in `dictionaries/ai-patterns.md`, that is fine. Patterns become tells only out of fit; in fit they are voice.

## Why the negative framing fails

Three reasons, supported by the pilots:

1. **The white-bear effect.** Telling the model "do not write `delve`" puts `delve` in the working context.
2. **Defensive compression.** The model removes anything resembling a flagged pattern even when the pattern is doing legitimate work. Em-dashes get cut. Section labels lose their natural language. Paragraph rhythm flattens.
3. **Persona drift toward a homogenized anti-AI register.** Every persona ends up reading the same — short, clipped, fragment-heavy. The persona's actual signature is overwritten.

## How scrub fails depends on the persona

A second pilot — Gemini × `clear-teacher` — confirmed the headline result (no-scrub wins on every condition) but revealed that the *shape* of the failure depends on which positive-shape feature is most diagnostic for the persona.

| Persona type | Scrub failure mode |
|---|---|
| **Terse / compressed** (sharp-technical, blunt-operator) | Sentence-length collapse. Mean SL drops to half the persona's target. Persona becomes a parody — clipped where it should have breath. |
| **Explanatory / engagement-rich** (clear-teacher, problem-first-marketer) | Lexical Shunt absence + opener-inventory miss + Taboo leakage. The persona's named openers (`Imagine…`, `Suppose…`, `Here's the idea:`) go missing. Generic explainer prose fills the gap. The persona's specific Taboo entries (`simply`, `just`) leak through *more* than they would without the scrub, because the scrub's exhaustive generic ban-list consumes the model's monitoring budget and the persona's targeted Taboo list gets drowned in noise. |

Same root cause — attention stolen from the persona's positive shape — expressed differently because different personas live in different parts of the stylometric space.

The diagnostic is the same in both cases: the persona's positive shape (Identity, Rhythm, Stylometric Signature, named Lexical Shunts, opener inventory, persona-specific Taboo patterns) is what does the actual filtering. The dictionaries cannot replace the persona file because they cannot be calibrated to the specific writer.

## Why positive framing works

When the model is asked to *be* a specific writer, it produces sentences as that writer would — including the long ones, the parenthetical asides, the parallel paragraphs that genuinely belong. The model does not have to spend attention monitoring against a list. The persona file's positive shape is the filter.

The Taboo patterns inside the persona file work the same way because they are read as character: "a `sharp-technical` writer would never open with `In today's fast-paced world`." That is not a banned-phrase rule. It is a fact about who this writer is.

## Heuristic

If you find yourself listing AI patterns to avoid, you are off-track. Re-anchor on the persona's positive shape.

If the output reads like every persona's output (short, clipped, defensively compressed, fragment-heavy), the scrub is on. Turn it off.

If the output drifts away from the persona's voice (mean sentence length wrong, lexical density wrong, opener inventory wrong), the persona file is what you re-check. Not a banned-phrase list.

## On scratch step files

A separate finding from the same pilot: scratch step files help when context cannot hold the task and hurt slightly when it can.

The rule, as shipped:

- **≤ 600 words (≈ 1–2 pages):** in-memory. The passes are fast and the model holds them naturally.
- **> 600 words:** scratch. The state exceeds one working window; materializing each pass keeps the persona stable across the longer arc.
- **Long-form (multi-section, > 2000 words):** scratch with chapter workflow. Chapter memory and revision tickets do durable work.
- **`persona-copy` analysis:** scratch always. Extracted persona files and verification reports are saved artifacts by definition.

The 600-word threshold is calibrated to the model's working window for a single short-task pipeline (intent → audit → mapping → draft → coherence → refine → fidelity). Beyond that, the early passes start to fade by the time the late passes run, and the persona drifts. Scratch puts each pass in front of the model again at read time and the persona stays committed.

The principle: **scratch files are durable memory, not virtuous traceability.** Use them when memory is needed. Skip them when it is not.

## What to keep, what to cut

| Keep | Cut |
|---|---|
| Persona Identity, Attention, Stance, Rhythm, Stylometric Signature, Lineage | A "scrub against AI patterns" pass step |
| Persona Taboo patterns (character-driven) | A diagnostic-audit step that enumerates AI clusters |
| `dictionaries/*` as reference material a contributor can consult | Pipeline directives that point the model at the dictionaries during writing |
| `docs/anti-ai-guidelines.md` as background reading | Treating it as a scrub-step input |
| Voice-coherence checks against the persona's positive target | Voice-coherence checks framed as anti-AI scrub |
