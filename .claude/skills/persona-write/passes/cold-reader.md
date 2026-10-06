# Pass: Cold Reader

## Purpose

Learn how the text reads to someone who has only the text: what they understood, what impression they formed, and where they stumbled.

Every earlier pass was done by someone who knows the sources, the brief, and the skeleton. This pass uses a reader who knows none of them, as ISO 24495-1 asks of plain-language work: evaluate the text with readers unfamiliar with its content.

Runs after `fidelity-check` as pipeline step 12 when the stakes are high, and whenever the user asks. Stakes are high when the reader decides something about the author or the text's purpose (an application, a bid, an appeal, a publication), or when field 6 of the reader brief says so. Leave it out for a throwaway text.

## The writer this pass makes

A writer who tests the text on a stranger before it goes out, and who takes the stranger's report as data about the text. When the reader's impression differs from the intended one, they look at the sentences that created it. They also know the writer's own intent is the reference: a trait the persona or the user chose on purpose is the text doing its job.

## What to do

1. **Fix the intent first.** Take the intended impression, the facts to convey, and the action to prompt from the reader brief (the Impression, Does not know, and Action fields) or from the intent extraction. When neither records an impression, take it from the persona's Identity and say so in the note.
2. **Pick the reader and the question.** The role the text is written for (for example a member of a selection committee) and the question the text answers: the form's question, or the brief's purpose.
3. **Give the reader the final text and nothing else.** Pass a fresh subagent (no memory of this session) the text pasted into the prompt, never a file path, so it cannot open the scratch folder. Withhold the brief, the skeleton, the style sheet, the sources, and every earlier draft. Use this prompt:

   > You are [reader role], reading this text for the first time. Do not read any files and do not use any tools; answer only from the text. The question the text answers: "[question]". TEXT: [the text]. Answer in order, honestly, including negative reactions: 1. In your own words, what is the text saying and asking for? (three sentences at most) 2. What facts did you take away? List them. 3. What impression did you form of the author or the text? Give three adjectives and quote the sentences that created it. 4. As the reader, what would you do next? 5. Where did you stumble: a sentence you re-read, a term you did not know, a claim you doubted, a question you would put to the author? 6. Does the text answer the question? Answer yes, partly, or no, and say what is missing.

   With no agent tool, ask the user to have another person read it. A self-read cannot hold back what the writer knows, so when it is the only option, run it and mark the result as the weaker test.
4. **Compare the report with the intent.** Put the reader's answers next to the facts, the impression, and the action from step 1.
5. **Decide each difference.**
   - A fact the reader missed or got wrong: the sentence carrying it is unclear.
   - An impression other than the intended one: find the sentences the reader named and see whether they carry the wrong register or content.
   - A trait the reader reported that matches the persona or the intended impression: this is a pass, so the sentence stays.
   - A stumble over a word or term: fix the word, or gloss the term once.
   - A doubt about a claim: check the claim against its source and, if it stands, support it in the text.
   - A sentence whose wording the user decided (a user row in the style sheet, or text the user supplied): the sentence stays, and the difference goes to the user.
6. **Send the changes back through the pipeline.** Make each change in `sentence-build` or `persona-wordcheck`. After any change beyond a word or two, re-run `voice-coherence` and `fidelity-check` on the changed sentences and update the style sheet before the next round.
7. **Run it once more** with a fresh reader after changes that go beyond a word or two. Two rounds are the limit. If the second round still shows a gap, report the remaining differences to the user.

## Long-form

A whole document can exceed one reader's attention. Sample the opening, one middle section, and the closing, and send findings that touch a section's earlier text back through `tickets.md`.

## What this pass tests

How the text reads: understanding, impression, and action. A cold reader has no sources, so it cannot confirm that a fact is true; `fidelity-check` and `/persona-research` own that. It reports taste as well as clarity, so each difference is weighed against the intent from step 1.

## Output

A short reading note: the reader's answers, the intended impression against the reported one (and where the intended impression came from), each difference and how it was decided, what changed, and whether a second round ran. With scratch in use, save as `07b-cold-reader.md`. The text then goes to the proofread.
