# Pass: Native Fluency

## Purpose

Make the finished text read as if a native writer of the target language wrote it for this reader.

Runs automatically after `refine` and before the word check (`persona-wordcheck`) and `fidelity-check`, whenever the text is in a language other than the one the persona files are written in (English), or the user names a target language. Skip it for English-only work.

## The writer this pass makes

Someone who writes the target language natively and knows how this genre is written there. They choose the construction a native writer would reach for first, keep sentences at the length the genre uses, and write the register the reader expects.

## What to do

1. **Name the target** — language, locale, genre, reader, register (formal or informal, address form). If the user gave none, infer and state it.
2. **Read as a native reader.** Mark every phrase that reads as translated: word order copied from English, a noun where the language prefers a verb, a literal idiom, a connector the genre does not use, an English sentence rhythm.
3. **Replace each marked phrase** with the construction a native writer would use. Change the form, keep the content.
4. **Set the conventions of the locale:** quotation marks, diacritics, date and number formats, honorifics, capitalisation, punctuation.
5. **Check the register end to end.** One address form and one level of formality from first line to last.
6. **Hand off to the word check.** Facts, numbers, names, and claims stay exactly as they were.

## Output

The adjusted text, plus a short list of the substantive changes (not every comma). With scratch in use, save as `06b-native.md`.
