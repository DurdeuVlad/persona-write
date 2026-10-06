#!/usr/bin/env python3
"""Self-check for proofread.py. Run: python3 test_proofread.py (exits non-zero on failure)."""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from proofread import check  # noqa: E402


def msgs(text, **kw):
    return [(lvl, m) for lvl, _, m in check(text, **kw)]


def has(found, level, fragment):
    return any(lvl == level and fragment in m for lvl, m in found)


clean = "Predau din liceu. Am ținut cinci sesiuni pentru colegi."
assert not any(lvl == "FAIL" for lvl, _ in msgs(clean, lang="ro", plain=True, max_chars=4000, max_numbers=2))

# length: newlines counted as 2, so a 10-char text with 2 newlines can exceed a limit of 12
assert has(msgs("aaaa\nbbbb\ncccc", max_chars=12), "FAIL", "exceeds 12")
assert not has(msgs("aaaa\nbbbb", max_chars=12), "FAIL", "exceeds")

# plain text: formatting markers fail, ordinary punctuation does not
for bad in ("# Titlu", "**bold**", "- punct", "[a](http://x)", "| a | b |", "<b>x</b>", "`cod`"):
    assert has(msgs(bad, plain=True), "FAIL", "formatting"), bad
assert not has(msgs("Un text simplu, cu virgulă.", plain=True), "FAIL", "formatting")

# spacing
f = msgs("Doua  spatii , si  lipsa,spatiu.")
assert has(f, "WARN", "double space") and has(f, "WARN", "space before punctuation") and has(f, "WARN", "missing space")
assert not has(msgs("Valoarea 1,5 este corecta."), "WARN", "missing space")

# repeated words and numbers
assert has(msgs("Am am ținut sesiuni."), "WARN", "repeated word")
assert has(msgs("Am 15 sesiuni și 5 stagiari și 3 ateliere.", max_numbers=2), "FAIL", "numbers")
assert has(msgs("agenții agenții agenții"), "WARN", "used 3 times")

# Romanian: cedilla fails, comma-below passes, straight quotes warn
assert has(msgs("Să predau aşa.", lang="ro"), "FAIL", "cedilla")
assert not has(msgs("Să predau așa.", lang="ro"), "FAIL", "cedilla")
assert has(msgs('Programul "AI".', lang="ro"), "WARN", "straight quotes")
assert has(msgs("fara diacritice " * 25, lang="ro"), "WARN", "no Romanian diacritics")

print("proofread.py: all checks passed")
