# Example: a style sheet

Task: a short formal Romanian motivation text for a university teaching-qualification committee. The sheet below is what `00-style-sheet.md` holds after the first passes.

| Area | Decision | Decided by | Why |
|---|---|---|---|
| Reader and register | University selection committee; formal, modest, first person singular | user | Form prompt and brief |
| Wish phrasing | "Doresc să urmez cariera didactică", stated plainly | writer | "Îmi doresc" reads as colloquial in this genre |
| Terms | "dezvoltator" kept as the job title | user | Dictionary lists only another sense; a user-supplied title is kept and flagged |
| Terms | "ateliere" for the workshops | source | Dictionary does not list the workshop sense; real use found on institutional and news pages and cited |
| Terms | "Inteligență Artificială și Viziune" in Romanian | user | The user's own draft uses this form |
| Numbers | At most two numbers in the text | user | Respect the committee's time |
| Numbers | The level in "nivelul I" always stays | writer | A qualifier the reader needs to read the fact correctly |
| Spelling and typography | Full diacritics; program name in quotation marks „…" | source | Romanian orthography guides for formal texts |
| Open questions | Is "primă persoană de contact" the right rendering of the role? | open | Not found in any source |

How the passes use it: `sentence-build` reads the term and number rows before it writes a sentence; `persona-wordcheck` checks flagged words against the Terms rows first; `native-fluency` takes quotation marks and diacritics from the Spelling row; `fidelity-check` reads the Terms, Names, and Numbers rows as part of what the text must still show; `proofread` takes the number limit and the spelling rules from the Numbers and Spelling rows.
