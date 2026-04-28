# Persona Copy — Pipeline detail

This is the long-form companion to `SKILL.md`. Read it when you need precise instructions for one of the passes.

The pipeline is grounded in `../persona-write/docs/persona-theory.md`. Familiarity with that doc is assumed.

---

## Pass 1 — Sample audit

Goal: know what you are working with before you measure it.

For each sample, write into `01-sample-audit.md`:

```
### Sample [N]
- words: [count]
- topic: [one line]
- audience: [one line]
- genre: [essay / blog post / email / spec / tweet thread / etc.]
- representativeness: [typical / atypical / unsure — reason]
- visible distinctive features: [first impressions, no analysis yet]
```

If total words across all samples is below 500, stop and tell the user the fingerprint will be unreliable. Ask whether they want to proceed anyway with that caveat.

If samples are stylistically inconsistent (mean sentence length differs by >50% between samples, or one is conversational and another is formal), name the inconsistency and ask whether the user wants:
1. one persona per cluster, or
2. a single persona averaged across.

---

## Pass 2 — Stylometric extraction

Compute by inspection (no need for an external tool — all of this is doable from reading the samples carefully and counting):

### Sentence-length statistics
- Sample N=20+ sentences if available.
- Compute mean and SD.
- Note distribution shape: uniform (low SD), bimodal (mix of clipped and long), normal-with-tail.

### Lexical density
- Pick a 200-word span from each sample.
- Count content words (nouns, lexical verbs, adjectives, most adverbs).
- Density = content / total.
- Average across samples.
- Place in a band: **low** (< 0.4, conversational), **mid** (0.4–0.55, accessible non-fiction), **high** (> 0.55, academic / dense technical).

### Type-token ratio
- For each 500-token window: TTR = unique tokens / 500.
- Average. Note whether the author is repetitive on key terms (low TTR → motif words) or varies aggressively (high TTR → vocabulary range).

### Function-word tilt
List notable over-/under-uses among the top-50 English function words. Examples to look for:
- Heavy `that` (formal, embedded clauses) vs heavy `which` (parenthetical) vs avoidance of both.
- `and` joining vs semicolon joining vs em-dash joining.
- High `but` / `however` rate (argumentative) vs low (declarative).
- Rate of `I` / `we` / `you` (Hyland engagement).
- Modals: `should`, `must`, `would`, `might` — distribution maps onto Hyland stance.

### Sentence-opener inventory
List the 5 most common opening constructions across all samples. Examples:
- bare noun phrase (`The system…`)
- `When` / `If` clause-first
- gerund (`Building a…`)
- fragment (`Two problems.`)
- discourse marker (`So,` / `But` / `Now`)
- pronoun-first (`I` / `We` / `You`)

A persona's opener inventory is one of the strongest reproducibility signals.

### Punctuation profile (per 1000 words)
- em-dashes
- semicolons
- colons
- parentheses
- ellipses
- exclamation marks (usually zero in non-fiction; flag if present)
- question marks (rhetorical questions are a stylistic choice)

### Biber dimension placement
For each of the six dimensions in `persona-theory.md`, place the source on a `--` / `-` / `0` / `+` / `++` scale and quote one piece of evidence.

### LIWC-style markers
- First-person singular rate (`I`, `me`, `my`)
- First-person plural rate (`we`, `us`, `our`)
- Second-person rate (`you`, `your`)
- Hedge density (`maybe`, `seems`, `tends to`, `roughly`, `often`, `usually`, `mostly`)
- Booster density (`clearly`, `obviously`, `certainly`, `always`, `never`, `definitely`)
- Negation density (`no`, `not`, `never`, `n't`)
- Concrete vs abstract noun bias (qualitative judgement: do nouns name physical things and named entities, or processes and abstractions?)

Write all of the above to `02-fingerprint.md` as a structured table.

---

## Pass 3 — Rhetorical & structural extraction

Read for **how the writer thinks on the page**, not just how they sound.

### Opening moves
For each sample, quote the opening sentence and label the move: cold claim / anecdote / question / fragment / personal-historical / problem-statement / scene-setting.

### Closing moves
Same for the closing sentence(s). Label: callback / verdict / question / quiet / call-to-action / aphorism.

### Argumentative scaffolding
Identify the dominant pattern across samples:
- **mechanism-first**: explain how something works, then implications
- **example-first**: open with a concrete case, generalise from it
- **tradeoff-first**: lay out competing considerations before resolving
- **narrative**: chronological development
- **problem-solution**: name a frustration, then resolve it
- **recursive / dialectical**: claim → counter → synthesis

Most authors mix two; name the primary and secondary.

### Paragraph shape
- average paragraph length in sentences
- whether one-sentence paragraphs are used as a deliberate move
- whether long paragraphs braid multiple ideas or develop one

### Layout features (genre-dependent)
- headings: present? hierarchy?
- lists: bullets? numbered?
- code blocks, quotes, blockquotes, callouts?

### Stance profile (Hyland 2005)
| Marker | Rate | Examples from samples |
|---|---|---|
| Hedges | low / mid / high | quote |
| Boosters | low / mid / high | quote |
| Attitude markers | low / mid / high | quote (`unfortunately`, `surprisingly`) |
| Self-mention | low / mid / high | quote |

### Engagement profile (Hyland 2005)
| Marker | Rate | Examples |
|---|---|---|
| Reader pronouns | | |
| Directives | | (`note`, `consider`, `imagine`) |
| Questions | | |
| Personal asides | | |

Write to `03-structure.md`.

---

## Pass 4 — Implied author construction

Synthesise. Write `04-implied-author.md` as four short paragraphs:

1. **Who is talking?** Build the implied author from evidence. Profession or temperament suggested by the texts; what they appear to value; how senior they sound.
2. **What do they pay attention to?** First-noticed thing, recurring fixations, what they ignore.
3. **Relationship to the reader.** Peer? Teacher? Skeptic? Salesperson? Confessor? Quote evidence.
4. **Refusals.** What this writer would never write. Quote a closely-related but stylistically wrong example for contrast (e.g. "would not write `In today's fast-paced world`").

Keep it grounded. No biography you cannot infer from the text.

---

## Pass 5 — Persona file

Use `template.md` (mirrors `../persona-create/template.md` plus a `Source Evidence` section). Fill every field. The Stylometric Signature, Linguistic Fingerprint, and Cognitive & Psychological Profile fields come straight from passes 2 and 4. Quote source evidence sparingly under each section so the persona is auditable later.

---

## Pass 6 — Quality target profile

Apply `../persona-write/docs/writing-quality-rubric.md` to the source samples. Score each dimension 1–5 with quoted evidence. The resulting profile is the target — not what *good writing* in the abstract looks like, but what *this writer's good writing* looks like. The reproduction will be measured against this, not against generic ideals.

---

## Pass 7 — Brief reconciliation

If the user's brief is in the same genre as the samples, write a one-paragraph summary of how the persona will execute it.

If there is genre mismatch (samples are essays, brief is for a tweet thread; samples are formal, brief is for a chat reply), explicitly name how the persona's stylometric signature will adapt:
- which features carry over (lexical signature, stance profile, attention model)
- which must shift (sentence length cap for tweets, register for chat)
- what risks the user should be aware of

If the mismatch is severe, ask the user before drafting.

---

## Pass 8 — Draft

Write through the persona brief and the rhetorical scaffolding. Hit the opener inventory — start the piece with one of the source author's typical opening moves. Hit the paragraph-shape target. Use the punctuation profile. Stay inside the lexical-density and sentence-length bands.

Do not look back at the source text while drafting. You are reproducing a *style*, not paraphrasing a piece. Looking at the source increases verbatim overlap risk.

---

## Pass 9 — Voice coherence against the extracted persona

Run `../persona-write/passes/voice-coherence.md` against the draft, calibrated against the **extracted** persona's Identity, Rhythm model, Stylometric Signature, and Taboo patterns from `persona.md` (pass 5).

The check is *fit to the source author's positive shape*, not removal of generic AI patterns. Why: see `../persona-write/docs/voice-guide.md`. Asking the model to enumerate generic AI patterns produces defensive compression that drifts the draft *away* from the source's natural rhythm.

What to check, in order:

- **Stylometric drift**: is mean sentence length within ±20% of the extracted target? Lexical density in band? Punctuation profile in band? Opener inventory matches the source's top openers?
- **Lexical fit**: are the source author's named **Lexical Shunts** present in the draft? Did the draft introduce vocabulary the source author would not use?
- **Stance fit**: hedge / booster / self-mention rates in line with the extracted profile?
- **Taboo patterns** from the extracted persona: cross-check.

If the draft drifts on a specific dimension, fix toward the target. The target is the source author, not a generic ideal.

---

## Pass 10 — Verification

Run two checks side by side. Write to `10-verification.md`.

### Check A — Quality match
Score the draft on the rubric. Compare each dimension against the pass-6 target. Record a table:

```
| Dimension | Target | Draft | Δ | Pass? |
|---|---|---|---|---|
| Ideas | 5 | 5 | 0 | ✓ |
| Organization | 4 | 4 | 0 | ✓ |
| Voice | 5 | 4 | -1 | ✓ (within ±1) |
| Word Choice | 5 | 5 | 0 | ✓ |
| Sentence Fluency | 4 | 4 | 0 | ✓ |
| Stance Calibration | 4 | 4 | 0 | ✓ |
| Reader Engagement | 3 | 3 | 0 | ✓ |
```

Pass criteria:
- every dimension within ±1 band of target
- Voice and Word Choice match exactly (these are the persona-bearing dimensions)
- if either fails, fix and re-score

### Check B — Stylometric match
```
| Feature | Source | Draft | ±20%? |
|---|---|---|---|
| Mean sentence length | 14.2 | 13.8 | ✓ |
| SD sentence length | 7.1 | 6.4 | ✓ |
| Lexical density | 0.52 | 0.54 | ✓ |
| em-dashes / 1000w | 8 | 9 | ✓ |
| ... | | | |
```

### Check C — Verbatim overlap
Scan the draft for any 5-word span that appears in any sample. If found, paraphrase. Five-word overlaps on idiomatic phrases (`at the end of the day`) are acceptable and rarely a real overlap; longer matches are not.

If any check fails, name the specific fix in the verification doc and apply it before producing the final.

---

## Pass 11 — Final

Write `final.md` with:

```
# [Title of new piece]

## Persona summary
[one paragraph from pass 4–5]

## Quality match
[rubric table from pass 10]

## Stylometric match
[fingerprint table from pass 10]

## Piece
[the actual final text]
```

Return to the user. By default, surface only the piece and a one-line note that the rubric and fingerprint tables are in `final.md`. Surface the full report only if the user asks.
