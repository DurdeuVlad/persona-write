# Example: Long-form Processing

Showing how the skill handles a multi-section document.

## Request

```
/persona-write pragmatic-builder:
Rewrite this technical guide section by section.

[A 2,000-word guide with sections: Introduction, Installation, Configuration, Common Problems, Advanced Usage]
```

## What the skill does

### Stage 0: Global brief

```
Persona: pragmatic-builder
Audience: engineers setting up the tool for the first time
Purpose: instructional — get the reader to a working setup
Format: technical guide
Core thesis: here is how to set this up and use it correctly
Must-keep: all version numbers, config key names, command syntax
Locked terminology: [tool name], configuration keys as written in the docs
Tone: direct, assumes technical competence, low ceremony
```

### Stage 1: Document map

```
Section 1: Introduction
  Function: context and scope
  Length: short
  Drift risk: likely over-explains why the tool exists; reader wants to set it up

Section 2: Installation
  Function: instructional steps
  Length: medium
  Dependencies: establishes file paths referenced in Configuration
  Drift risk: passive voice in instructions ("it can be installed by...")

Section 3: Configuration
  Function: instructional, reference
  Length: medium-long
  Dependencies: depends on Installation section paths
  Drift risk: config keys described in prose rather than shown

Section 4: Common Problems
  Function: troubleshooting
  Length: medium
  Dependencies: references steps in Installation and Configuration
  Drift risk: vague problem descriptions, no resolution steps

Section 5: Advanced Usage
  Function: extension
  Length: medium
  Dependencies: assumes completed Configuration
  Drift risk: over-documents edge cases the primary reader does not need
```

### Stage 2: Section processing loop

For each section, the skill:
1. Loads the global brief and chapter memory from previous sections
2. Runs intent extraction, diagnostic audit, persona mapping
3. Rewrites the section
4. Updates chapter memory

After Section 2 (Installation), chapter memory records:
- file paths established: `/etc/tool/config.yaml`, `~/.tool/credentials`
- commands established: `tool install`, `tool init`
- Section 3 depends on these paths

After Section 4 (Common Problems), a revision ticket is created:
- "Section 4 Problem 3 references `tool init --reset` but Section 2 did not mention `--reset` flag. Section 2 should note it or Section 4 should not assume it."

### Stage 3: Consistency pass

- Voice check across all five sections — consistent pragmatic tone throughout
- Terminology check — config keys used consistently
- Revision ticket resolved: added `--reset` note to Section 2

### Stage 4: Final assembly

Final document assembled from revised sections. Output as `tool-guide-final.md`.

---

## Notes

The long-form example shows the mechanism, not the output. The actual rewritten guide would be specific to the input document.

Key behaviors to observe:
- The global brief is derived from the document, not assumed
- Chapter memory prevents drift in config key names and file paths
- The revision ticket catches a forward-reference that would have confused the reader
- The consistency pass runs after all sections are complete, not during
