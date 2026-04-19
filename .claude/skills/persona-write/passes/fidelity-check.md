# Pass: Fidelity Check

## Purpose

Verify that the rewritten text still means what the original meant.

Voice work can drift meaning. Compression can drop necessary nuance. Persona caricature can change the argument without changing the words. The fidelity check catches this before output.

## What to check

### Meaning preservation
Does the rewrite convey the same information and argument as the original?

Go through the key claims in the original one by one:
- Is each claim still present?
- Has any claim been weakened, strengthened, or changed in meaning?
- Have any important qualifications been dropped?

A claim that was hedged in the original ("this approach often works in low-latency environments") should not become a strong assertion in the rewrite ("this approach works in low-latency environments"). The hedge was there for a reason.

### Factual accuracy
Are all specific facts correct in the rewrite?

- Numbers, dates, names, version numbers
- Technical specifications
- Named systems, products, or tools
- Anything the writer is accountable for getting right

Do not change these. If something looks wrong in the original, flag it — but do not silently correct it.

### Nuance retention
Is important nuance still present?

Compression and persona work can strip nuance that the original carried. Check:
- Caveats the original included
- Distinctions the original made
- Acknowledgements of uncertainty or complexity

If a nuance was important, it should survive the rewrite. If it was not important, it may have been right to cut it — but that is a judgment call, not an accident.

### Persona fit check
Does the rewritten text actually sound like the persona, or has it drifted to a generic voice?

A rewrite that is tighter but sounds like nobody in particular has not done its job. The persona should be identifiable in the finished text.

### Caricature check
Has the persona been overdone?

Each persona has a failure mode. Check whether the rewrite has gone there:
- sharp-technical: does it sound arrogant or dismissive?
- pragmatic-builder: does it oversimplify real complexity?
- clear-teacher: does it condescend or over-explain?
- skeptical-analyst: does it refuse to commit to anything?
- blunt-operator: does it cut content the reader actually needed?

## Output

If the fidelity check passes, return the text for output.

If problems are found, flag them specifically:
- what was changed in meaning
- what was dropped
- what drifted in persona

Then fix the specific issues and run the check again.

Do not return text that fails the fidelity check without flagging the failure.
