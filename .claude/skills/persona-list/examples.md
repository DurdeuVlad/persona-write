# Persona List — Examples

## Basic list request

**User:**
```
/persona-list
```

**Expected output:**
List all six presets with one-sentence descriptions. Offer to explain any of them in more detail.

---

## User is unsure

**User:**
```
/persona-list
I want to rewrite a technical blog post but I'm not sure which persona fits.
```

**Expected output:**
Ask whether the post is aimed at experts or beginners. If experts: suggest `sharp-technical`. If beginners: suggest `clear-teacher`. If the audience is mixed: suggest `pragmatic-builder`.

---

## User wants details on one persona

**User:**
```
/persona-list
Tell me more about skeptical-analyst.
```

**Expected output:**
Explain the skeptical-analyst identity, what kind of writing it produces, what it naturally cuts, and what it is bad at. Then offer to run `/persona-write` with that persona.
