# Simple Usage

How to use Persona Write without reading anything else first.

## The basic pattern

```
/persona-write [persona] [mode]:
[your text or request]
```

If you leave out the persona, the skill will ask you to choose one.
If you leave out the mode, it will infer it from your text.

## Multi-persona chains (V2)

You can give more than one persona. The first one owns the text. The rest are reviewers.

```
/persona-write sharp-technical -> problem-first-marketer:
[paste text]
```

The skill will:
1. rewrite as `sharp-technical`
2. have `problem-first-marketer` review and apply targeted improvements
3. have `sharp-technical` run a final reconciliation pass
4. return output that still reads primarily as `sharp-technical`

You can also use commas or plain language:

```
/persona-write sharp-technical, clear-teacher:
[paste text]
```

```
/persona-write: write this as a sharp technical writer, then have a clear teacher review it
[paste text]
```

Three personas work the same way — first writes, second reviews, third reviews, first reconciles.

→ See `docs/persona-chain-mode.md` for full details and pairing recommendations.

## The preset personas

- **sharp-technical** — direct, concise, technical
- **pragmatic-builder** — practical, implementation-minded
- **clear-teacher** — explanatory without fluff
- **skeptical-analyst** — careful, evidence-aware
- **blunt-operator** — very direct, minimal ceremony
- **problem-first-marketer** — problem-first, audience-oriented, earns attention before asking for action

Not sure which to pick? Run `/persona-list` and it will explain them.

## Examples

### Rewrite a piece of text

```
/persona-write sharp-technical rewrite:
[paste your text]
```

### Draft something new

```
/persona-write pragmatic-builder draft:
Write an explanation of how our deployment pipeline works, for an engineer joining the team.
```

### Let the skill decide the mode

```
/persona-write clear-teacher:
[paste your text]
```

The skill will infer whether you want a rewrite, an audit, or something else from context.

### Use a plain-language custom persona

```
/persona-write:
Make this sound like a senior engineer who is concise and hates fluff.
[paste your text]
```

### Process a long document

```
/persona-write pragmatic-builder:
Rewrite this doc section by section.
[paste document]
```

For long documents, the skill will work through the text one section at a time instead of rewriting everything in one shot.

## Choosing a mode

You do not have to specify the mode. The skill will infer it.

But if you want to be explicit:

| Mode | When to use |
|---|---|
| `draft` | Writing something new from a topic or brief |
| `rewrite` | Improving existing text |
| `audit` | Finding what is wrong without rewriting |
| `refine` | A lighter pass on already-revised text |
| `longform` | Large documents, section-by-section |

## Output

For short tasks, you get inline output with a brief note on what changed.

For long tasks, the skill will produce Markdown files if the output is too large for inline display.

## If something is off

If the output does not fit the persona or changed something it should not have, say what went wrong specifically. The skill will adjust.

If the persona is not working as expected, try `/persona-list` to see the full descriptions, or `/persona-create` to build a custom one.
