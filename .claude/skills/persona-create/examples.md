# Persona Create — Examples

## Plain-language description

**User:**
```
/persona-create
Make it sound like a senior engineer who is concise, practical, skeptical of vague claims, and not rude.
```

**Expected output:**
Build a custom persona using the schema. Present it in plain English. Ask if it fits or needs adjustment. Offer to save it as a file.

---

## Guided creation (user is unsure)

**User:**
```
/persona-create
I want something that sounds smart but not cold.
```

**Expected output:**
Ask clarifying questions:
- Is the audience technical or general?
- Should the writing explain things or assume knowledge?
- Should it sound warm, dry, direct, or careful?

Use the answers to build the persona. Do not guess and present a finished persona without asking.

---

## Saving a custom persona

**User:**
```
/persona-create
Save the persona we just built as "experienced-generalist".
```

**Expected output:**
Create a file at `.claude/skills/persona-write/personas/experienced-generalist.md` using the standard template. Confirm the file location.

---

## Custom persona used immediately

**User:**
```
/persona-create then /persona-write
I want something like a skeptical product manager who cuts through hype. Use it to rewrite this:
[paste text]
```

**Expected output:**
Build the persona inline, confirm the shape briefly, then proceed directly to rewrite without making the user run two separate commands.
