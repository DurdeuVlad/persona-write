# Writing Quality Rubric

A research-backed analytic rubric used by `persona-copy`, the diagnostic-audit pass in `persona-write`, and the review-feedback step in `persona-review`. Grounded in the 6+1 Trait Writing Model (Education Northwest, 2018), Hyland's stance/engagement (2005), Williams' *Style*, and analytic-band scoring conventions from IELTS / TOEFL writing.

The point of this rubric is **not to give text a single number**. It is to score on independent dimensions so that a persona can be reproduced at the right *kind* of quality, not flattened into "good" or "bad."

See `persona-theory.md` for the research foundations.

---

## How to use this rubric

Score each dimension on a 1–5 band. For each band you assign:

1. Quote 1–3 short pieces of evidence from the text.
2. State which descriptor in the band the evidence matches.
3. If the score is below the persona's target, name the specific fix (sentence-level if possible).

Do not average the scores. Persona fit is multidimensional — a text can be 5 on Voice and 2 on Sentence Fluency, and that gap is the actionable finding.

---

## Dimensions

The seven dimensions are grouped: **content** (Ideas, Organization), **expression** (Voice, Word Choice, Sentence Fluency), **register & stance** (Stance Calibration, Reader Engagement). 6+1's Conventions and Presentation are handled separately by `passes/refine.md` and the host environment, not scored here.

---

### 1. Ideas

*Adapted from 6+1 Trait: Ideas. Measures content quality and informational density.*

| Band | Descriptor |
|---|---|
| **5 — Strong** | Clear, focused thesis. Every paragraph earns its space. Supporting detail is specific, non-obvious, and load-bearing. The reader learns something they could not have inferred from the headline. |
| **4 — Effective** | Thesis is clear. Most detail supports it. One or two passages drift toward generality or restate the point without adding evidence. |
| **3 — Developing** | Topic is identifiable but the controlling idea is implicit or shifts mid-piece. Detail is present but mixed with filler or summary. |
| **2 — Emerging** | Reader can guess the topic but not the argument. Detail is generic, padded, or recycled. |
| **1 — Weak** | No discernible thesis. Strings of generalities. Could be about almost anything. |

Diagnostics: lexical density target ≥ 0.5 for non-fiction (Halliday 1985); count of unique concrete claims per 250 words; ratio of named entities and specific quantifiers to vague intensifiers.

---

### 2. Organization

*Adapted from 6+1 Trait: Organization. Measures internal structure, sequencing, transitions.*

| Band | Descriptor |
|---|---|
| **5 — Strong** | Structure is invisible because it works. Each move follows from the last. Transitions are earned, not announced. The opening commits, the close lands. |
| **4 — Effective** | Logical sequence; structure mostly invisible but with a few "as we discussed" or "in conclusion" tells. |
| **3 — Developing** | Order is defensible but transitions are weak or mechanical. The piece could be re-ordered without much loss. |
| **2 — Emerging** | Sequence feels arbitrary. Sections begin and end without dependency on each other. |
| **1 — Weak** | No structure. Reads as a list of paragraphs in arrival order. |

Diagnostics: Williams' given/new contract — does each sentence open with information already established? Topic-string coherence: the subjects of consecutive sentences should form a connected chain, not jump.

---

### 3. Voice

*Adapted from 6+1 Trait: Voice. Booth's implied author. The persona's most important dimension.*

| Band | Descriptor |
|---|---|
| **5 — Strong** | A specific kind of person is unmistakably present on the page. Stance, attention, and rhythm are all aligned with the persona. The reader could pick this writer's next paragraph out of a lineup. |
| **4 — Effective** | Persona is present and consistent. One or two passages slip into neutral assistant register. |
| **3 — Developing** | Persona shows in flashes but is overridden by generic prose for stretches. The voice is recognisable but unstable. |
| **2 — Emerging** | Hints of voice but mostly generic. The piece would be unattributable to its persona without context. |
| **1 — Weak** | No voice. Could have been written by anyone or anything. The piece is structurally smooth and informationally hollow — the dominant failure mode of generic AI prose. |

Diagnostics: anti-AI scrub patterns (`dictionaries/ai-patterns.md`); ratio of persona-tagged lexical shunts present; absence of throat-clearing openers (`In today's...`, `It's worth noting that...`).

---

### 4. Word Choice

*Adapted from 6+1 Trait: Word Choice. Lexical precision and register fit.*

| Band | Descriptor |
|---|---|
| **5 — Strong** | Words are precise, fresh, and load-bearing. Technical terms used exactly. No corporate filler. No cliché. Verbs do most of the work; modifiers are rationed. |
| **4 — Effective** | Mostly precise. A handful of soft verbs (`utilize`, `leverage`), generic intensifiers (`very`, `really`), or unearned abstractions slip in. |
| **3 — Developing** | Vocabulary is competent but unmemorable. Heavy reliance on weak verbs and abstract nouns where concrete ones would serve. |
| **2 — Emerging** | Frequent vague nouns, manager-speak, or undifferentiated synonyms. Reader has to translate. |
| **1 — Weak** | Pervasive cliché, jargon-without-content, or the AI-prose register of `delve`, `intricate`, `tapestry`, `ever-evolving landscape`. |

Diagnostics: type-token ratio; banned-phrase hit count (`dictionaries/banned-phrases.md`, `dictionaries/manager-speak.md`); nominalisation density (Lanham — circle prepositions and `-tion`/`-ment` nouns).

---

### 5. Sentence Fluency

*Adapted from 6+1 Trait: Sentence Fluency. Rhythm, variation, readability.*

| Band | Descriptor |
|---|---|
| **5 — Strong** | Rhythm is varied and intentional. Sentence-length distribution matches the persona target. Short sentences land claims; longer ones develop them. No metronome, no jitter, no run-ons. Read aloud, the prose has a pulse. |
| **4 — Effective** | Mostly varied. One or two stretches of uniform sentence length or comma-spliced pile-ups. |
| **3 — Developing** | Adequate but predictable. Either too uniform or jaggedly inconsistent. |
| **2 — Emerging** | Choppy or run-on. Few transitions inside the sentence. |
| **1 — Weak** | Consistently broken: fragments without purpose, run-ons without architecture, or paragraphs of uniform 18-word sentences. |

Diagnostics: mean sentence length; standard deviation; opener variety (count of sentences beginning with the same construction); cumulative-vs-periodic balance.

---

### 6. Stance Calibration

*Adapted from Hyland (2005) stance markers. Domain-specific addition not in 6+1.*

| Band | Descriptor |
|---|---|
| **5 — Strong** | Confidence matches evidence at every move. Hedges and boosters are used precisely. The reader knows what is claimed strongly, what is suggested, what is uncertain. |
| **4 — Effective** | Mostly calibrated. Occasional unearned booster (`clearly`, `obviously`) or reflex hedge (`it could be argued that`). |
| **3 — Developing** | Stance is uniform — either everything is hedged or everything is asserted. The reader cannot tell which claims are weight-bearing. |
| **2 — Emerging** | Mismatched stance: weak claims overstated, strong claims softened. |
| **1 — Weak** | Certainty theater (confident on weak ground) or hedging-as-padding (rigorous-sounding but committing to nothing). |

Diagnostics: count of hedges (`might`, `seems`, `tends to`, `roughly`, `often`); count of boosters (`clearly`, `obviously`, `certainly`, `definitely`); modal verb distribution (`should` vs `must` vs `would`).

---

### 7. Reader Engagement

*Adapted from Hyland (2005) engagement markers. Critical for `clear-teacher`, `problem-first-marketer`; secondary for `sharp-technical`, `skeptical-analyst`.*

| Band | Descriptor |
|---|---|
| **5 — Strong** | Reader is positioned correctly: addressed at the right level, given the right amount of context, never patronised, never lost. The piece anticipates where the reader could disengage and earns attention there. |
| **4 — Effective** | Reader is mostly positioned well. One or two passages assume too much or explain too much. |
| **3 — Developing** | Audience model is roughly right but inconsistent — explains the easy parts and skips the hard ones, or vice versa. |
| **2 — Emerging** | Persistent miscalibration: lectures the expert, mystifies the novice. |
| **1 — Weak** | No audience model. Reads as if produced into a void. |

Diagnostics: reader pronouns (`you`, `we`); directive frequency (`note`, `consider`, `imagine`); questions to the reader; ratio of explanation to assumed knowledge.

---

## Persona target profiles

Each preset persona has a target band on each dimension. A `persona-copy` reproduction is judged against the source-extracted target, not these defaults.

| Dimension | sharp-technical | pragmatic-builder | clear-teacher | skeptical-analyst | blunt-operator | problem-first-marketer |
|---|---|---|---|---|---|---|
| Ideas | 5 | 5 | 4 | 5 | 5 | 5 |
| Organization | 5 | 5 | 5 | 5 | 5 | 5 |
| Voice | 5 | 5 | 5 | 5 | 5 | 5 |
| Word Choice | 5 | 4 | 4 | 5 | 5 | 5 |
| Sentence Fluency | 4 | 4 | 5 | 4 | 4 (deliberately clipped) | 5 |
| Stance Calibration | 5 | 5 | 4 | 5 | 4 | 4 |
| Reader Engagement | 3 | 4 | 5 | 4 | 3 | 5 |

A 3 in Reader Engagement for `sharp-technical` is **not a weakness**. It reflects the persona's deliberate stance: it does not perform engagement.

---

## Output format

When this rubric is applied, the output should be a Markdown table or list with:

- the dimension
- the score (1–5)
- one quoted piece of evidence
- one specific revision direction if the score is below the persona target

Example:

```
| Dimension | Score | Evidence | Revision |
|---|---|---|---|
| Voice | 3 | "It's worth noting that the system has many factors" | Cut throat-clearing; lead with the mechanism. |
| Sentence Fluency | 4 | Three consecutive 22-word sentences in para 2 | Break or compress one to a 6–8 word claim. |
```

This format is consumed directly by `persona-copy`'s reproduction and verification passes.

---

## References

See `persona-theory.md` for full citations. Primary sources for this rubric: Education Northwest (2018) for trait categories and band logic; Hyland (2005) for stance/engagement; Williams (*Style*) for cohesion diagnostics; IELTS Public Band Descriptors and TOEFL iBT analytic scoring rubric for the 5-band analytic format.
