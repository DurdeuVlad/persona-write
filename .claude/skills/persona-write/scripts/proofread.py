#!/usr/bin/env python3
"""Mechanical proofread of a finished text against the reader's form rules.

usage: proofread.py FILE [--max-chars N] [--max-numbers N] [--lang ro] [--plain]

Exit 0 = no FAIL findings, 1 = at least one FAIL. WARN findings never change the exit code.
Stdlib only. Checks what a script can see; meaning and word choice stay with the writer.
"""
import argparse
import re
import sys
from collections import Counter

CEDILLA = {"ş": "ș", "Ş": "Ș", "ţ": "ț", "Ţ": "Ț"}  # ş Ş ţ Ţ
MARKDOWN = [
    (r"^\s{0,3}#{1,6}\s", "heading marker"),
    (r"\*\*|__", "bold marker"),
    (r"(?<![\w*])\*[^\s*][^*\n]*\*(?![\w*])", "italic marker"),
    (r"`", "backtick"),
    (r"\[[^\]\n]+\]\([^)\n]+\)", "markdown link"),
    (r"^\s*[-*+]\s+\S", "list bullet"),
    (r"^\s*\|.*\|\s*$", "table row"),
    (r"</?[a-zA-Z][^>\n]*>", "html tag"),
]


def check(text, max_chars=None, max_numbers=None, lang=None, plain=False):
    """Return a list of (level, line_number_or_0, message)."""
    out = []
    lines = text.split("\n")
    body = text.strip("\n")

    # length: report both counts; the limit is tested against the cautious one (newline = 2)
    no_nl = len(body.replace("\n", ""))
    cautious = no_nl + 2 * body.count("\n")
    if max_chars is not None and cautious > max_chars:
        out.append(("FAIL", 0, f"length {cautious} (newlines as 2) exceeds {max_chars}; {no_nl} without newlines"))
    out.append(("INFO", 0, f"{no_nl} characters with spaces (without newlines), {cautious} counting newlines as 2, {len(body.split())} words"))

    blank_run = 0
    for i, line in enumerate(lines, 1):
        blank_run = blank_run + 1 if not line.strip() else 0
        if blank_run == 3:
            out.append(("WARN", i, "more than two blank lines in a row"))
        if plain:
            for pat, name in MARKDOWN:
                if re.search(pat, line):
                    out.append(("FAIL", i, f"formatting in plain text: {name}"))
        if re.search(r"[ \t]+$", line):
            out.append(("WARN", i, "trailing whitespace"))
        if "\t" in line:
            out.append(("WARN", i, "tab character"))
        if " " in line:
            out.append(("WARN", i, "non-breaking space"))
        if re.search(r"(?<=\S)  +(?=\S)", line):
            out.append(("WARN", i, "double space"))
        if re.search(r"\s[,;:!?.](?!\.)", line):
            out.append(("WARN", i, "space before punctuation"))
        if re.search(r"[,;:](?=[^\s\d\"'”»)\]])", line):
            out.append(("WARN", i, "missing space after punctuation"))
        for m in re.finditer(r"\b(\w+)\s+\1\b", line, re.IGNORECASE):
            if not m.group(1).isdigit():
                out.append(("WARN", i, f"repeated word: {m.group(0)!r}"))
        if line.count("(") != line.count(")"):
            out.append(("WARN", i, "unbalanced parentheses"))

    # same longer word three or more times
    words = [w.lower() for w in re.findall(r"[^\W\d_]{7,}", body)]
    for w, n in Counter(words).items():
        if n >= 3:
            out.append(("WARN", 0, f"word used {n} times: {w!r}"))

    if max_numbers is not None:
        count = len(re.findall(r"\d+(?:[.,]\d+)?", body))
        if count > max_numbers:
            out.append(("FAIL", 0, f"{count} numbers, limit {max_numbers}"))

    if lang == "ro":
        for i, line in enumerate(lines, 1):
            for bad, good in CEDILLA.items():
                if bad in line:
                    out.append(("FAIL", i, f"cedilla form {bad!r}; use comma-below {good!r}"))
            if re.search(r"[\"']", line):
                out.append(("WARN", i, "straight quotes; Romanian text uses „…”"))
        if len(body.split()) > 40 and not re.search(r"[ăâîșțĂÂÎȘȚ]", body):
            out.append(("WARN", 0, "no Romanian diacritics found in a long text"))

    return out


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("file")
    ap.add_argument("--max-chars", type=int)
    ap.add_argument("--max-numbers", type=int)
    ap.add_argument("--lang")
    ap.add_argument("--plain", action="store_true")
    a = ap.parse_args(argv)
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8")
    text = open(a.file, encoding="utf-8").read().replace("\r\n", "\n")
    found = check(text, a.max_chars, a.max_numbers, a.lang, a.plain)
    for level, line, msg in found:
        print(f"{level:4} {('line ' + str(line)) if line else 'text':8} {msg}")
    return 1 if any(level == "FAIL" for level, _, _ in found) else 0


if __name__ == "__main__":
    sys.exit(main())
