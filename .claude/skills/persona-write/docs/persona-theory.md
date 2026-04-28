# Persona Theory

The research foundation behind every persona file in this skill set.

A persona is not a "tone setting." It is a **bundle of measurable choices** — what the writer attends to, how much they compress, how they hold certainty, the rhythm of their sentences, the words they reach for, and the words they refuse. The four research traditions below justify why this skill describes personas the way it does.

This doc is referenced by `persona-create`, `persona-copy`, `persona-write`, and every individual persona file. Read it once. The persona schema downstream is just an applied version of what is here.

---

## 1. Stylometry & computational linguistics

Stylometry is the quantitative study of writing style. Its core finding, repeated since Mendenhall (1887) and Mosteller & Wallace (1964), is that **style is measurable in features the writer is not consciously choosing**. Two features matter most:

### Function-word frequency (Burrows' Delta)
John Burrows (2002) showed that the relative frequency of the most common function words — `the`, `of`, `and`, `to`, `a`, `in`, `that`, `is`, `was`, `it`, etc. — is a stable author fingerprint. The method was refined by Eder, Rybicki, Kestemont, and others (Evert et al., 2017, *Digital Scholarship in the Humanities*). Authors differ reliably on which connectors they reach for and at what rate. This is the basis for the **Function Word Profile** field in our persona files.

### Multi-Dimensional register analysis (Biber)
Douglas Biber's 1988 *Variation across Speech and Writing* identified six dimensions on which English texts vary:

1. **Involved vs. Informational production** — first/second person, hedges, contractions vs. nouns, attributive adjectives, longer words.
2. **Narrative vs. Non-narrative concerns** — past-tense verbs, third-person pronouns, perfect aspect.
3. **Explicit vs. Situation-dependent reference** — `wh-` relatives and pied-piping vs. time/place adverbs.
4. **Overt expression of persuasion** — modals (`should`, `must`, `would`), suasive verbs (`demand`, `recommend`).
5. **Abstract vs. Non-abstract information** — passives, conjuncts, agentless constructions.
6. **On-line informational elaboration** — `that`-clauses as complements, demonstratives.

Every preset persona in this skill sits at a definable point on these dimensions. `sharp-technical` sits high on Informational, low on Involved. `clear-teacher` sits mid-Informational with deliberate Narrative flashes. `problem-first-marketer` sits high on Involved and on Persuasion. Naming this explicitly is what the **Stylometric Signature** field does.

### Vocabulary richness
Type-token ratio (TTR), Yule's K, Herdan's C, and lexical density (Ure 1971; Halliday 1985) all measure how varied and content-loaded the prose is. Lexical density = content words / total words. Conversational speech sits around 0.4; academic prose around 0.6–0.7. Persona files name a target range so generated prose lands where it should.

### Sentence-length distribution
Not just the mean — the **standard deviation**. Hemingway-style writing has a low mean and a low SD. Faulkner has a high mean and a very high SD (long sentences interrupted by short ones). Williams (*Style*, 1981) and Tufte (*Artful Sentences*, 2006) both treat sentence-length variation as a primary expressive resource.

---

## 2. Writing-quality rubrics (education research)

A persona is not just a fingerprint; it has to write **well** in its own register. The skill grounds quality on two converging frameworks:

### 6+1 Trait® Writing Model (Education Northwest)
Developed by what is now Education Northwest from analytical scoring research in the 1980s, refined through 2018. The seven traits are:

1. **Ideas** — content, focus, supporting detail.
2. **Organization** — internal structure, sequencing, transitions.
3. **Voice** — the writer's presence on the page; tone matched to audience and purpose.
4. **Word Choice** — precise, fresh, register-appropriate vocabulary.
5. **Sentence Fluency** — rhythm, variation, and readability of sentences.
6. **Conventions** — grammar, mechanics, usage.
7. **Presentation** (the +1) — visual layout and formatting.

Every persona must produce text that scores well on Voice, Word Choice, Sentence Fluency, and Conventions *in that persona's register*. `writing-quality-rubric.md` adapts these to a 5-point analytic rubric.

### Cognitive process model of writing (Hayes & Flower, 1981; Hayes 1996, 2012)
Flower and Hayes' 1981 *College Composition and Communication* paper established that skilled writing is recursive — Planning, Translating, and Reviewing are not stages but interleaved sub-processes monitored against goals. Hayes (1996) added working-memory and motivation; Hayes (2012) added a transcribing/proposer split. This is why our pipeline is **multi-pass with explicit reviewing passes**, not a single generation.

### Argument and narrative rubrics (CCSS, IELTS, TOEFL)
Common Core writing standards split into argument, informative/explanatory, and narrative — each with its own rubric. IELTS/TOEFL analytic scales score Task Achievement, Coherence & Cohesion, Lexical Resource, and Grammatical Range & Accuracy. The scoring rubric in `writing-quality-rubric.md` borrows the analytic-band format (4 dimensions × 5 levels) from these scales because it is robust across genres.

---

## 3. Rhetoric & literary style

Stylometry says *what* a style is. Rhetoric says *why* it works on a reader.

### Implied author and voice (Booth, 1961)
Wayne Booth's *The Rhetoric of Fiction* introduced the **implied author** — the version of the writer the reader reconstructs from the text, distinct from the biographical author and from any narrator. Persona files encode an implied author. The Identity section is exactly that: who the reader believes is talking.

### Heteroglossia and stance (Bakhtin, 1981)
Bakhtin's *The Dialogic Imagination* shows that any utterance carries traces of other voices — what we now call stance and intertextuality. The **Stance model** field captures how a persona positions itself relative to the claim, the reader, and other voices in the discourse.

### Clarity, cohesion, emphasis (Williams, *Style*, 1981 and later)
Joseph Williams' principles, taught for decades at the University of Chicago, give us:

- Characters as subjects, actions as verbs.
- Old information first, new information last (the **given/new contract**).
- End emphasis — put the punchline at the end of the sentence.
- Cohesion via topic strings.
- Concision: delete metadiscourse, redundant pairs, and obvious throat-clearing.

These show up directly in the **Taboo patterns** lists and in the anti-AI guidelines (`anti-ai-guidelines.md`).

### Sentence-level craft (Tufte, *Artful Sentences*, 2006; Klinkenborg, *Several Short Sentences*, 2012; Pinker, *Sense of Style*, 2014)
Tufte catalogues syntactic moves (cumulative sentences, suspended sentences, parallelism, anaphora). Klinkenborg argues for sentence-as-unit-of-thought. Pinker formalises Thomas & Turner's "classic style" — the writer and reader as equals looking at the same world. The **Rhythm model** field is calibrated on these.

### The paramedic method (Lanham, *Revising Prose*, 1979)
Richard Lanham's procedural cleanup — circle the prepositions, find the action, find the doer, kick out the slow wind-up — is the operational core of the rewrite pass.

---

## 4. Personality & cognitive psychology of voice

How does a *kind of person* show up in word counts?

### LIWC and the Big Five (Pennebaker, Mehl, King, Boyd)
Pennebaker and King (1999, *Journal of Personality and Social Psychology*) first showed that linguistic dimensions correlate with stable personality traits. The Linguistic Inquiry and Word Count (LIWC) program operationalises this. Replicated findings (summarised in Boyd & Pennebaker, 2017; Mairesse et al., 2007, *JAIR*):

| Trait | Linguistic markers (high) | Markers (low) |
|---|---|---|
| **Openness** | Longer words, articles, prepositions, fewer first-person singulars, more abstract nouns | Concrete nouns, present-tense, social words |
| **Conscientiousness** | Longer words, fewer negations, fewer discrepancy words (`should`, `would`) | Swear words, negations, present-focus |
| **Extraversion** | First-person plural, social words, positive emotion, fewer hedges | Tentative words, articles |
| **Agreeableness** | Positive emotion, social words, fewer swear/anger words | Anger words, second-person |
| **Neuroticism** | First-person singular, negative emotion, anxiety words | Positive emotion, articles |

This research underpins the **Cognitive & Psychological Profile** field. We are not personality-testing the writer; we are saying *the implied author this persona constructs sits in this region of trait-marker space*.

### Cognitive style
Need-for-cognition (Cacioppo & Petty, 1982), thinking dispositions (Stanovich), and field-dependence/independence all correlate with discourse-level patterns: degree of qualification, use of mechanism vs. example, willingness to commit. The **Reasoning preference** field encodes this.

### Stance and engagement (Hyland, 2005)
Ken Hyland's stance/engagement framework breaks academic and professional voice into:

- **Stance**: hedges (`might`, `possibly`), boosters (`clearly`, `definitely`), attitude markers, self-mention.
- **Engagement**: reader pronouns (`you`, `we`), directives (`consider`, `note`), questions, asides.

Each persona has a defined stance/engagement profile.

---

## How this maps to the persona schema

When you read a persona file in `personas/`, every section is grounded in the research above:

| Persona section | Grounded in |
|---|---|
| **Identity** | Booth's implied author |
| **Attention model** | Cognitive style; what counts as relevant in this persona's frame |
| **Compression model** | Lexical density target; given/new contract; Pinker's classic style |
| **Stance model** | Hyland stance/engagement; Bakhtin |
| **Reasoning preference** | Hayes-Flower planning sub-process; argument vs. narrative rubric |
| **Rhythm model** | Tufte, Klinkenborg, Williams; sentence-length mean & SD |
| **Linguistic Fingerprint** | Burrows' Delta; LIWC; function-word profile |
| **Cognitive & Psychological Profile** | Pennebaker/Boyd; Big Five linguistic markers |
| **Stylometric Signature** | Biber dimensions; TTR; punctuation density; modals |
| **Literary & Rhetorical Lineage** | Named exemplars to anchor the implied author |
| **Taboo patterns** | Lanham; Williams' diagnostics; LIWC anti-markers |
| **Failure modes** | When the trait profile is pushed too far |

A persona without these is a vibe. A persona with these is reproducible.

---

## References

Bakhtin, M. M. (1981). *The Dialogic Imagination: Four Essays.* University of Texas Press.

Biber, D. (1988). *Variation across Speech and Writing.* Cambridge University Press.

Booth, W. C. (1961, 2nd ed. 1983). *The Rhetoric of Fiction.* University of Chicago Press.

Boyd, R. L., & Pennebaker, J. W. (2017). Language-based personality: A new approach to personality in a digital world. *Current Opinion in Behavioral Sciences*, 18, 63–68.

Burrows, J. (2002). 'Delta': A measure of stylistic difference and a guide to likely authorship. *Literary and Linguistic Computing*, 17(3), 267–287.

Cacioppo, J. T., & Petty, R. E. (1982). The need for cognition. *Journal of Personality and Social Psychology*, 42(1), 116–131.

Education Northwest. (2018). *6+1 Trait® Writing Rubrics, Grades 3–12.* https://educationnorthwest.org/traits

Evert, S., Proisl, T., Jannidis, F., Reger, I., Pielström, S., Schöch, C., & Vitt, T. (2017). Understanding and explaining Delta measures for authorship attribution. *Digital Scholarship in the Humanities*, 32(suppl_2), ii4–ii16.

Flower, L., & Hayes, J. R. (1981). A cognitive process theory of writing. *College Composition and Communication*, 32(4), 365–387.

Halliday, M. A. K. (1985). *Spoken and Written Language.* Deakin University Press.

Hayes, J. R. (1996). A new framework for understanding cognition and affect in writing. In C. M. Levy & S. Ransdell (Eds.), *The Science of Writing* (pp. 1–27). Erlbaum.

Hayes, J. R. (2012). Modeling and remodeling writing. *Written Communication*, 29(3), 369–388.

Hyland, K. (2005). Stance and engagement: A model of interaction in academic discourse. *Discourse Studies*, 7(2), 173–192.

Klinkenborg, V. (2012). *Several Short Sentences About Writing.* Knopf.

Lanham, R. A. (1979, rev. 2007). *Revising Prose.* Pearson Longman.

Mairesse, F., Walker, M. A., Mehl, M. R., & Moore, R. K. (2007). Using linguistic cues for the automatic recognition of personality in conversation and text. *Journal of Artificial Intelligence Research*, 30, 457–500.

Mendenhall, T. C. (1887). The characteristic curves of composition. *Science*, 9(214S), 237–246.

Mosteller, F., & Wallace, D. L. (1964). *Inference and Disputed Authorship: The Federalist.* Addison-Wesley.

Pennebaker, J. W., & King, L. A. (1999). Linguistic styles: Language use as an individual difference. *Journal of Personality and Social Psychology*, 77(6), 1296–1312.

Pinker, S. (2014). *The Sense of Style.* Viking.

Tufte, V. (2006). *Artful Sentences: Syntax as Style.* Graphics Press.

Ure, J. (1971). Lexical density and register differentiation. In G. E. Perren & J. L. M. Trim (Eds.), *Applications of Linguistics* (pp. 443–452). Cambridge University Press.

Williams, J. M. (1981, current ed. with Bizup). *Style: Lessons in Clarity and Grace.* Pearson.
