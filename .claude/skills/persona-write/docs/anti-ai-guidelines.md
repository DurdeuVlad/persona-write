# Authentic Voice Guidelines — reference only

> **This file is reference material, not a pipeline input.** The active guidance is in `voice-guide.md`. The patterns and clusters catalogued below are useful background for contributors writing or refining personas; they are *not* a checklist applied by the model during writing or audit.
>
> Why: asking the model to think about generic AI patterns triggers defensive compression that drifts the prose away from the persona's natural rhythm. The pipeline now relies on each persona's positive shape (Identity, Rhythm, Stylometric Signature, Taboo patterns) instead. See `voice-guide.md` for the experimental evidence behind this change.

Shared background on patterns common in generic AI prose. Use this when shaping a new persona's Taboo patterns or Stylometric Signature, not as a runtime checklist.

The goal of every persona is **authenticity** — voice that follows from a specific implied author. When a voice is authentic, it naturally breaks the statistical patterns of "generic assistant" prose without the writer having to monitor against them. 

---

## The Path to Authenticity

Do not use mechanical rules to "humanize" text. Instead, focus on the **internal logic** of the persona.

### 1. Specificity of Vocabulary
A "sharp-technical" persona doesn't just use "technical words"; they use the specific slang and shorthand of their niche. 
- **Generic AI:** "Implement the authentication layer."
- **Authentic Voice:** "Wire up the auth middleware."
- **Rule:** Use the vocabulary that the persona’s background demands. Don't "de-optimize" for a detector; optimize for the character.

### 2. Opinionated Logic
Generic AI is balanced and neutral. Authentic people have a stance.
- **Generic AI:** "While X has benefits, Y is also worth considering."
- **Authentic Voice:** "The raw SDK is a grind. If you aren't using a framework, you're wasting cycles."
- **Rule:** Pick a side. Let the persona’s stance drive the structure of the argument, not a "setup-middle-conclusion" template.

### 3. Rhythmic Intent
Don't follow a "1-1-50" rule. Follow the **intent** of the sentence. 
- If a point is simple, use a short sentence. 
- If a mechanism is complex, use a dense, nested sentence that mirrors the complexity. 
- **Rule:** Let the content dictate the rhythm. Human writing is "bursty" because human thought is uneven.

---

## Structural tells to avoid (The "Generic Assistant" Filter)
...
Grammatical structure is "too correct" but lacks the creative deviations or rhythmic shifts typical of human writing. Human writers use fragments, run-ons (for effect), and non-standard punctuation to manage pace. AI tends to stay strictly within the lines of a style guide.

### 2. Mechanical Precision
Word choice prioritizes dictionary-correctness and technical clarity over character, stance, or situational appropriateness. It avoids the "messy" but accurate idioms or colloquialisms that a specific persona would naturally use.

### 3. Robotic Formality
The style is polished and orderly but lacks variation in intensity, register, or pace. It feels like a single, unbreaking formal seal across the entire document.

### 4. Impersonal Tone
Excessive use of indirect speech, third-person distancing ("one might argue"), and academic paraphrasing. It avoids assigning agency and hides the writer's actual position behind a mask of objectivity.

---

## Vocabulary clusters

These are not banned words. They are words that cluster around AI-generated prose and, in combination, mark a passage as produced rather than written.

### Significance cluster
- critical, crucial, essential, fundamental, vital, paramount, key, important
- Use one when something is actually significant. Do not sprinkle.

### Process-as-noun cluster
- serves as, acts as, stands as, functions as, operates as
- These turn a verb into a bureaucratic description. Replace with a direct verb.

### Feature-listing cluster
- boasts, features, offers, provides, delivers, showcases
- These are brochure words. Technical and analytical writing does not boast. It states.

### Smooth-transition cluster
- furthermore, additionally, moreover, in addition, it is worth noting, it is important to mention, with this in mind, that said, having said that
- These transitions carry no information. They fill the gap between sentences. Cut them or replace with a transition that carries meaning.

### Robust-ecosystem cluster
- robust, scalable, seamless, streamlined, comprehensive, holistic, cutting-edge, state-of-the-art, best-in-class, world-class
- These are promotional terms. They describe how the writer feels about something, not what it actually does.

### Suspension-of-opinion cluster
- it could be argued, one might suggest, some would say, in many ways, in a sense, to some extent, arguably
- Used occasionally, hedging is honest. Used throughout, it signals a writer avoiding any real position.

---

## Grammar-level tells

Individual phrasings that appear disproportionately in generated text.

**"serves as"** — almost always replaceable with a direct verb.
- "This function serves as a validator." → "This function validates input."

**"stands as"** — promotional framing disguised as description.
- "This approach stands as the most efficient solution." → "This is the fastest approach we tested."

**"features"** as a verb about non-product things
- "The document features an overview of the system." → "The document begins with a system overview."

**"delve into"** — overused in generated prose.
- Replace with: examine, cover, explain, explore, or cut entirely.

**"in the realm of"** — vague spatial metaphor standing in for a direct phrase.
- "In the realm of machine learning..." → "In machine learning..."

**"a testament to"** — significance inflation through literary framing.
- "This is a testament to the team's effort." → "The team shipped it on time." or nothing.

**"navigate"** as metaphor — "navigate complexity," "navigate the landscape," "navigate challenges."
- Usually replaceable with a direct verb or cut.

**"leverage"** as a verb — almost always replaceable with "use."

**"ensure"** followed by alignment, consistency, or efficiency
- Often wraps a real requirement in nominal weight. State the requirement directly.

---

## Pattern stacking

This is the most important concept in these guidelines.

A single use of "robust" in a 2,000-word document is not a problem. A paragraph that contains "robust," "seamlessly," "best-in-class," and ends with "it is important to note that this represents a critical step toward achieving our goals" has stacked five weak signals into one strong tell.

When reviewing, scan for density of signals per sentence or paragraph. Fix the paragraphs where signals cluster, not just individual words.

---

## Promotional and brochure language

Technical and analytical text should describe what something does, not sell it to the reader.

Brochure language:
- "Our platform delivers seamless integration with industry-leading performance."

Description:
- "The API syncs in under 200ms. No middleware required."

The distinction is: brochure language evaluates while describing. Good description just describes. The evaluation follows from the facts.

---

## Anti-patterns specific to AI-assisted rewrites

These patterns appear specifically when AI helps revise text, rather than generating from scratch.

**Re-introduction of hedging removed by the persona.** A persona like `blunt-operator` or `sharp-technical` will have stripped hedging. If the scrub or review pass adds it back in the name of "balance," that is a regression, not an improvement.

**Generic connective tissue between retained original phrases.** When an AI keeps some original phrases and builds new connective sentences around them, the connective sentences tend to be more generic than the preserved material. Look for sudden flatness between preserved passages.

**Overcorrection to neutrality.** Reviewer passes can inadvertently soften the owner's voice in an attempt to fix tone. If the owner persona is direct or blunt, reviewer fixes should preserve that directness while addressing specific problems — not sand off the edges until the text reads like a moderate approximation.

---

## What these guidelines do not require

- No keyword removal by mechanical blocklist.
- No artificial injection of informality, typos, or quirks.
- No mandatory diversity of sentence length for its own sake.
- No specific word count targets.

The standard is: does the text sound like the intended persona made deliberate choices about what to include, how to say it, and what to cut? If yes, it passes. If it sounds like no one in particular chose anything, it needs work.
