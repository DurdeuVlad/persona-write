# Pass: Cold Reader

## Purpose

Learn how the text reads to someone who has only the text: what they understood, what impression they formed of the author, and where they stumbled.

Every earlier pass was done by someone who knows the sources, the brief, and the skeleton. This pass uses a reader who knows none of them, as ISO 24495-1 asks of plain-language work: evaluate the text with readers unfamiliar with its content.

Runs after `fidelity-check` as pipeline step 12, when the stakes are high or the user asks for it. Leave it out for a throwaway text.

## The writer this pass makes

A writer who tests their text on a stranger before it goes out, and who takes the stranger's report as data about the text. When the reader's impression differs from the intended one, they change the text, not the reader.

## What to do

1. **Pick the reader.** The role the text is written for (for example a member of a selection committee), and the question the reader's form asks.
2. **Give the reader the text and nothing else.** Pass a fresh subagent (no memory of this session) only: the text, the reader role, and the form's question. Withhold the brief, the skeleton, the style sheet, the sources, and every earlier draft. Without an agent tool, re-read the text yourself with only that in view and answer the same questions in writing; this is a weaker test, and the note says so.
3. **Ask the reader these questions, in this order:**
   1. In your own words, what is the author saying and asking for? (three sentences at most)
   2. What facts about the author did you take away? List them.
   3. What impression did you form of the author? Give three adjectives and the sentences that created it.
   4. As the reader, what would you do next?
   5. Where did you stumble: a sentence you re-read, a term you did not know, a claim you doubted, a question you would put to the author?
   6. Does the text answer the form's question? Answer yes, partly, or no, and say what is missing.
4. **Compare the report with the intent.** Put the reader's answers next to the brief: the facts the text meant to convey, the impression it meant to leave, the action it meant to prompt.
5. **Act on the differences.**
   - A fact the reader missed or got wrong: the sentence carrying it is unclear. Send it back to `sentence-build` or `persona-wordcheck`.
   - An impression other than the intended one: find the sentences the reader named and change their register or content.
   - A stumble: fix the word, term, or sentence.
   - A doubt about a claim: check the claim against its source and, if it stands, support it in the text.
6. **Run it once more** on a fresh reader after changes that touch more than a word or two. Two rounds are enough.

## What this pass tests

How the text reads: understanding, impression, and action. A cold reader has no sources, so it cannot confirm that a fact is true; `fidelity-check` and `/persona-research` own that.

## Output

A short reading note: the reader's answers, the intended against the reported impression, what changed, and whether a second round was run. With scratch in use, save as `07b-cold-reader.md`. The text then goes to the proofread.
