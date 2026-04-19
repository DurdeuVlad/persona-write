# Example: Audit

Showing the audit mode — diagnosing what is wrong without rewriting.

## Request

```
/persona-write skeptical-analyst audit:
Our new product has been incredibly well-received by users. Early feedback shows that customers are highly satisfied with the experience, and the metrics we have gathered suggest that engagement is trending in a positive direction. We believe this momentum will continue as we roll out additional features in the coming months.
```

## Expected output

### Diagnosis

**Overclaiming without evidence:**
- "Incredibly well-received" — how? What data?
- "Highly satisfied" — what satisfaction metric? What score? What sample?
- "Metrics suggest engagement is trending in a positive direction" — which metrics, what trend, over what period?

**Hedged certainty performing as confidence:**
"Suggest that engagement is trending" is soft language used to make a vague claim sound careful. The softness is not doing epistemic work here — it is covering for the absence of numbers.

**Forward claim without basis:**
"We believe this momentum will continue" — belief is not a reason. If there is evidence that retention or engagement predicts future growth, say what it is. If there is not, do not make the claim.

**What is actually being claimed:**
Stripped of the framing: "some users gave positive feedback, some engagement metrics went up, we expect growth."

That may be true and reasonable. The problem is that the text presents it as stronger evidence than it is.

### Recommendation

If you have real numbers, use them. If you do not, say what you observed and leave out the conclusions that require more data than you have.

*Want a rewrite?*

---

## Notes

The skeptical-analyst audit does not rewrite by default. It names the specific epistemic problems and lets the user decide what to do.

The diagnosis is not hostile. It treats the writer as someone who can handle direct feedback on their claims.
