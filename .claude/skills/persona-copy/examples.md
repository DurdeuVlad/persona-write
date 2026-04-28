# Persona Copy — Examples

## Example 1 — Continuing a series

**User:**
```
/persona-copy
Here are five essays I've written. Write a sixth one in the same style on the topic of "what good documentation actually does."

[paste 5 essays]
```

**Expected behaviour:**
1. Pass 1 — sample audit on the five essays.
2. Pass 2 — fingerprint extraction (mean sentence length, density, openers, punctuation profile, Biber placement).
3. Pass 3 — rhetorical structure (opening / closing moves, scaffolding, paragraph shape, stance/engagement).
4. Pass 4 — implied-author construction.
5. Pass 5 — write `persona.md` in the scratch folder.
6. Pass 6 — score the five essays on the rubric → target profile.
7. Pass 7 — reconcile brief.
8. Pass 8 — draft the sixth essay.
9. Pass 9 — voice coherence against the extracted persona.
10. Pass 10 — verify against rubric target and fingerprint; fix gaps.
11. Pass 11 — return the final essay plus a one-line note that the analysis is in the scratch folder.

Default surface to the user: the essay only. Offer to show the persona file or the verification table on request.

---

## Example 2 — Reproducing a public author

**User:**
```
/persona-copy
Here are three Paul Graham essays. Write one in his style about "why most analytics dashboards are useless."

[paste essays]
```

**Expected behaviour:**
Same pipeline. Be especially careful in pass 9: do not copy his characteristic phrases (`What I mean by`, `If you look at`) verbatim — extract the *moves* (low-warning openers, short paragraphs, mechanism-first scaffolding, rhetorical questions placed mid-paragraph) and rebuild from those.

In pass 4, identify what is reproducible (rhythm, scaffolding, stance) versus what is not without impersonation (specific anecdotes from his life). The reproduction must not invent biographical detail.

---

## Example 3 — Extracting a house style

**User:**
```
/persona-copy and save as company-blog
Here are the last 8 posts from our company blog, written by various people but edited to a consistent house style. Extract the persona and save it.

[paste posts]
```

**Expected behaviour:**
1. Run passes 1–6.
2. Notice this is a multi-author corpus filtered through editing — flag in pass 1 that the persona being extracted is the *editor's* implied author, not any individual writer.
3. Skip passes 7–11 (no new piece requested).
4. Save the resulting `persona.md` to `.claude/skills/persona-write/personas/company-blog.md`.
5. Confirm the save and show how to use it: `/persona-write company-blog draft: ...`.

---

## Example 4 — Insufficient samples

**User:**
```
/persona-copy
Here is one paragraph from a writer I like. Write a 2000-word essay in their style on machine learning ops.

[paste paragraph]
```

**Expected behaviour:**
Stop at pass 1. Tell the user the sample is too short for a reliable fingerprint (under 500 words). Offer two options:
1. Provide more samples.
2. Proceed with explicit caveats — the reproduction will be approximate, drawing more on the rhetorical impressions than measurable stylometry.

Wait for the user's choice before continuing.

---

## Example 5 — Genre mismatch

**User:**
```
/persona-copy
Here are three of my long-form blog essays. Write me a 280-character tweet in the same voice.

[paste essays]
```

**Expected behaviour:**
Run passes 1–6 normally. In pass 7, name the genre mismatch:
- carry over: stance profile, attention model, lexical shunts, taboo patterns
- adapt: sentence length cap, paragraph shape (irrelevant), opening moves (must commit faster)
- risks: a single tweet cannot exhibit the rhythm variation that the long-form fingerprint depends on; voice will be present but partial

Confirm the user accepts the mismatch, then draft.

---

## Anti-pattern — what not to do

**User:**
```
/persona-copy
Here are five essays. Write a sixth.

[paste essays]
```

**Wrong behaviour:**
- Skipping the rubric and stylometric verification.
- Drafting from "vibes" instead of from the extracted fingerprint.
- Including 5+ word verbatim spans from the samples.
- Inventing biography about the author.
- Returning the piece without the `persona.md` and `10-verification.md` artifacts in scratch.

If you find yourself short-cutting, stop and run the missing passes. The skill is the pipeline, not the final paragraph.
