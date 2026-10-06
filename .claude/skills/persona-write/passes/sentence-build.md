# Pass: Sentence Build

## Purpose

Build the text one sentence at a time instead of producing the whole thing in one shot. Each sentence is chosen, checked, and locked before the next one is written.

This pass is the drafting step (pipeline step 6). It replaces writing the full text in a single generation, for drafts and for rewrites, short and long.

## The writer this pass makes

A writer who builds a text the way a mason builds a wall. They know the plan of the whole, then lay one sentence, check it sits true against the one before, and only then lay the next. They do not run ahead of what the reader has been given.

## What to do

### 1. Skeleton (`04a-skeleton.md`)

Before any sentence, list the claims the text must make, in the order the reader needs them (use the reader brief if there is one). One line per planned sentence:

- **Claim** — the single thing this sentence says
- **Source** — where the fact comes from (a file, the user, the original text)
- **Job** — what the reader should understand or feel after it
- **Register** — the register it is written in

For a rewrite, extract the claims from the original and keep its facts. Merge or drop claims the reader does not need.

Show the skeleton to the user when the text is high-stakes or the claims are uncertain.

### 2. Build loop (`04b-sentences.md`)

For each line of the skeleton, in order:

1. **Write one sentence** that carries only that claim, in the persona's rhythm and voice.
2. **Choose the words on purpose.** For each content word and phrase, ask the two questions from `/persona-wordcheck`: is it appropriate for this context, and is it used correctly in the target language. Look up what is uncertain.
3. **Read it against the one sentence before it, and no further back.** Does it follow without a gap? Does it repeat a word or construction just used? Does the register stay the same? Only that one sentence is in view; earlier ones are not re-read or reopened while building.
4. **Fix it, then leave it.** Once it passes, the sentence stays exactly as written for the rest of the build. If a later sentence shows that an earlier one is wrong, write a note under a "Revisions" heading in `04b-sentences.md` and keep going. The note is handled in the revise stage, not now.
5. **Log it now.** Append the locked sentence to `04b-sentences.md` (and any word the check changed) before you write the next sentence. The log is written as you build, not after; its file time and order are how the build is verified. Append to the file (for example a shell `>>`), because file-write tools overwrite the whole file.

### 3. Assemble and revise (`04-draft.md`)

The build is finished. This is a separate stage, and it is the only place where earlier sentences are reopened. Handle the notes under "Revisions" first, then assemble.

Join the sentences into paragraphs. Paragraph breaks follow the skeleton's jobs, not the sentence count.

Then read each paragraph aloud as the reader would. Where short sentences stack into a list, join the ones that form one thought with the connective the reader needs (for example a cause, a contrast, or a sequence word). Do this only where the relation is true and already in the skeleton; do not add claims. Keep each joined sentence to one idea the reader can hold. Record each join in `04b-sentences.md` under the "Revisions" heading, since it reopens finished sentences deliberately. The same words go through the two wordcheck questions again.

## Rules

- One claim per sentence. If a sentence needs two, it is two sentences. Parallel parts of one claim ("some ... others ...") are one claim and may share a sentence.
- No sentence is written without a skeleton line behind it. If a good sentence has no claim, it does not go in.
- Do not look ahead and write later sentences early to see how they will sound.
- Do not look further back than the one sentence before. Reopening earlier sentences belongs to the revise stage.
- Facts, numbers, and names come only from the listed source.
- Titles, program names, and terms the user gave keep the user's own form and language. Do not replace one because a dictionary is silent or lists a different sense; flag it for the user instead.
- A limit on how many numbers or details to include never removes a qualifier the reader needs to read the fact correctly (a level, a date, a scope). If the limit and the qualifier clash, keep the qualifier and drop another detail.
- The skeleton states the writer's main wish or position explicitly (for example, that they want to do this) when the reader's question asks for it. If the input points lack it, ask for it or flag the gap.

## Output

The assembled draft, with `04a-skeleton.md` and `04b-sentences.md` saved when scratch is in use. The later passes (`voice-coherence`, `refine`, `native-fluency`, the full-text `wordcheck`, `fidelity-check`) then work on the whole text as before.
