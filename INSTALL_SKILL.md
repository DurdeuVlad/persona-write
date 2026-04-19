---
name: persona-write
description: Install this skill set to draft, rewrite, audit, and refine text through a specific writing persona using a multi-pass workflow. Handles both short text and long-form documents.
install: copy .claude/skills/ folders into your repo
version: 1.0.0
skills:
  - persona-write
  - persona-list
  - persona-create
---

# Installing Persona Write

## Requirements

- [Claude Code](https://claude.ai/code)

## Install

Clone this repo, then copy the skill folders into your project:

```bash
git clone https://github.com/your-org/persona-write.git
```

**Fresh `.claude/` setup:**
```bash
cp -r persona-write/.claude /your-project/.claude
```

**Existing `.claude/skills/` folder:**
```bash
cp -r persona-write/.claude/skills/persona-write /your-project/.claude/skills/
cp -r persona-write/.claude/skills/persona-list /your-project/.claude/skills/
cp -r persona-write/.claude/skills/persona-create /your-project/.claude/skills/
```

No configuration files. No environment variables. No package installs.

## What you get

| Skill | Command | Purpose |
|---|---|---|
| persona-write | `/persona-write` | Draft, rewrite, audit, or refine text in a target persona |
| persona-list | `/persona-list` | Browse and explain the available preset personas |
| persona-create | `/persona-create` | Build a custom persona in plain language |

**Preset personas:** `sharp-technical`, `pragmatic-builder`, `clear-teacher`, `skeptical-analyst`, `blunt-operator`

## Verify install

Open Claude Code in your project and run:

```
/persona-list
```

The five preset personas are listed with descriptions. If the command is not found, check that the skill folders are in `.claude/skills/` at your project root.

## Usage

```
/persona-write sharp-technical rewrite:
[paste text]
```

```
/persona-write pragmatic-builder draft:
Write an explanation of how our CI pipeline works, for a new engineer joining the team.
```

```
/persona-write:
Make this sound like a skeptical analyst who cares about evidence and does not overclaim.
[paste text]
```

No persona given? The skill asks you to pick one.

## How it works

**Short text:** 8-pass pipeline — intent extraction → diagnostic audit → persona mapping → rewrite → anti-AI scrub → refine → fidelity check.

**Long-form documents:** section-by-section workflow with global brief, chapter memory, revision tickets, and a final consistency pass. No one-shot full-document rewrites.

## Updating

Pull the latest and re-copy the skill folders. No migration between minor versions.

```bash
cd persona-write && git pull
cp -r .claude/skills/persona-write /your-project/.claude/skills/
cp -r .claude/skills/persona-list /your-project/.claude/skills/
cp -r .claude/skills/persona-create /your-project/.claude/skills/
```

## Design constraints

This skill does not optimize for AI detector scores. The goal is writing that sounds like a specific kind of person — not writing that games a classifier.

Full design rationale: `.claude/skills/persona-write/docs/philosophy.md`
