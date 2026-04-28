# Example: Rewrite

Showing the rewrite mode in more detail, with before/after and annotation.

## Request

```
/persona-write pragmatic-builder rewrite:
Authentication is a critical component of any modern application. It ensures that users are who they say they are and that unauthorized access is prevented. There are many approaches to authentication, each with their own strengths and weaknesses. In this section, we will explore some of the key considerations when implementing authentication in your system.
```

## Diagnostic audit

- "Authentication is a critical component of any modern application" — generic opener that delays the content
- "It ensures that users are who they say they are" — restates the definition of authentication for an audience that already knows it
- "There are many approaches... each with their own strengths and weaknesses" — filler that describes the paragraph but does not do it
- "In this section, we will explore some of the key considerations" — announces the content instead of delivering it

## Persona mapping (pragmatic-builder)

- Cut the definition and the "importance" framing
- Lead with the decision the reader actually needs to make
- Name the real tradeoffs instead of gesturing at them
- Compression: assume the reader knows what authentication is

## Scratch Folder Trace

The following files were created in `scratch/2026-04-20-auth-rewrite/`:

- `01-intent.md` — Identified primary intent (inform/guide) and audience (developers).
- `02-audit.md` — Noted generic opener, redundant definitions, and announcement filler.
- `03-mapping.md` — Decided to lead with implementation choices and tradeoffs.
- `04-draft.md` — Initial draft in pragmatic-builder voice.
- `05-coherence.md` — Voice coherence check against `pragmatic-builder`: confirmed mean sentence length in band, persona Lexical Shunts present, no items from Taboo patterns. One small fix: shortened a 28-word mechanism sentence to two clauses.
- `06-refine.md` — Tightened the revocation explanation.
- `07-fidelity.md` — Confirmed session/token tradeoffs are accurately represented.
- `final.md` — Final version as shown below.

## Output

**What changed:** Removed definition and generic importance framing. Restructured to lead with the decision. Named the actual tradeoff instead of describing it.

---

Authentication has two main implementation choices with meaningfully different tradeoffs: session-based and token-based.

Session-based auth stores state server-side. Simpler to revoke access. Requires sticky sessions or shared session storage in a distributed setup.

Token-based auth (JWT is the common choice) is stateless. Scales without shared storage. Revocation requires extra machinery — a token blocklist or short expiry with refresh tokens.

For most web apps without strict revocation requirements, token-based auth is easier to operate at scale. For apps where immediate revocation matters (admin tools, financial systems), factor in the revocation cost before defaulting to tokens.

---

## Notes

The pragmatic-builder persona requires the text to be actionable. Announcing that "there are many approaches with strengths and weaknesses" is not actionable. Naming the two main approaches and the real tradeoff is.
