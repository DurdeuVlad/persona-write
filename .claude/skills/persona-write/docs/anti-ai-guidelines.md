# Anti-AI Writing Guidelines

Shared guidance for the diagnostic audit, anti-AI scrub, and persona-review passes.

These guidelines describe patterns that make text feel generated rather than written. The goal is not to fool detectors. It is to produce writing that was shaped by a point of view, not assembled from averaged training signals.

---

## How to use these guidelines

Do not treat this as a banned-word list. Individual words rarely matter. Patterns matter. Clusters matter most.

When multiple weak signals appear in the same sentence or paragraph, treat that as one strong signal. A sentence with "serves as," "leverages," "robust," and a balanced hedged ending does not have four small problems. It has one large problem.

Apply judgment. Remove what makes the text feel empty or processed. Preserve what makes the text sound like the intended persona.

---

## Structural tells

These are patterns in how the text is organized, not just what words it uses.

### Formulaic section shape

Every section has the same structure: opening claim, three supporting points, summary sentence. This symmetry signals assembly, not thinking. Real argument does not always need three supporting points. Sometimes one concrete fact is enough. Sometimes the claim is the whole thing.

### Repeated takeaway endings

Every paragraph ends with a sentence that restates the paragraph's main point. This treats the reader as incapable of retaining what they just read. It also produces a grinding rhythm — every paragraph lands the same way.

### Identical list shapes

Lists where every item is the same length, same grammatical form, and covers equal conceptual weight. Real lists have uneven entries. Some items matter more. Some are simpler. Forced parallelism for its own sake signals generation.

### Significance inflation

Every point is "important," "critical," "key," "essential," or "fundamental." When everything is important, nothing is. Significance claims should be used sparingly and earned by the argument, not sprinkled as emphasis.

### Setup-middle-summary structure at every scale

Text that follows the same three-part shape at the paragraph level, section level, and document level simultaneously produces a fractal quality that feels processed. Real writing varies structure by scale and by what the content actually needs.

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
