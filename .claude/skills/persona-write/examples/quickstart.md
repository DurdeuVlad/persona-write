# Example: Quickstart

A minimal example showing the basic pattern.

## Request

```
/persona-write sharp-technical:
We have developed a new deployment system that allows teams to push code to production with greater speed and reliability. The system uses a number of advanced techniques to ensure that deployments are both fast and safe. Teams have found it to be a significant improvement over previous approaches.
```

## What the skill does

1. Loads `sharp-technical` persona
2. Infers mode: rewrite
3. Intent extraction: announcing a system; audience is technical
4. Diagnostic audit: vague claims ("greater speed and reliability", "advanced techniques", "significant improvement"), no mechanism described, hollow opener
5. Persona mapping: lead with what it does; cut "we have developed"; name the actual mechanism or be honest that it is not named here; direct assertion on the outcome
6. Rewrite, voice coherence, refine, fidelity check

## Expected output shape

**What changed:** Removed vague improvement framing. Cut "a number of advanced techniques." Made the claim specific where possible or removed it where not.

---

The new deployment system cuts push-to-production time and reduces rollback frequency. It handles rollback automatically on health check failure and gates staging promotion on passing test suites. Teams that have migrated are shipping more frequently with fewer incidents.

---

## Notes

The example output names real mechanisms (automatic rollback, health checks, staged promotion) because sharp-technical would not accept "advanced techniques." If the original text has no mechanism to describe, the rewrite should say less rather than more.
