# Pass: Proofread

## Purpose

Give the finished text one last read as it will appear in the reader's form: right length, right format, clean spacing, correct characters.

Runs after `fidelity-check` as pipeline step 12, on the final text, and changes nothing but mechanics.

## The writer this pass makes

A proofreader who reads the page as the reader will meet it. They hold the form's rules in hand (the character limit, plain text or formatting, the language's characters), count the way the reader's form counts, and fix a slip the moment they see it without touching a word of meaning.

## What to do

1. **Collect the form's rules.** From the user or the style sheet (`00-style-sheet.md`, Numbers and Spelling rows): the length limit and how it is counted, plain text or formatting allowed, language and its characters, any number limit.
2. **Run the script** when a shell is available:

   `python scripts/proofread.py final.md --max-chars 4000 --max-numbers 2 --lang ro --plain`

   Use the limits that apply (leave a flag off when the form has no such rule). It checks length (counting newlines cautiously), formatting marks in plain text, spacing, doubled and repeated words, number count, and for Romanian the cedilla forms, quotation marks, and missing diacritics. Without a shell, go through the same list by hand.
3. **Fix every FAIL.** Review every WARN and fix the real ones; leave a repeated word that is the right word, and say so.
4. **Read the text once more, line by line,** for what a script cannot see: a diacritic missing inside a word, a wrong word form, a doubled word split across a line break, a number that no longer matches the sheet.
5. **Count the way the reader's form counts** (for example Word's "characters with spaces") when the form says so, and report that count.
6. **Keep the fixes mechanical.** When a finding needs a different word or sentence, send it back to `sentence-build` or `persona-wordcheck` and re-run `fidelity-check` before proofreading again.

## Output

The text, plus a short note: the length as counted, the rules checked, what was fixed, and any WARN left on purpose. With scratch in use, save as `08-proofread.md`.
