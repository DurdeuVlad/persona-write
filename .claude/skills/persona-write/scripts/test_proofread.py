#!/usr/bin/env python3
"""Self-check for proofread.py. Run: python3 test_proofread.py (exits non-zero on failure)."""
import os
import subprocess
import sys
import tempfile

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from proofread import check  # noqa: E402

CED = "ş"      # s with cedilla
OPEN, CLOSE = "„", "”"


def msgs(text, **kw):
    return [(lvl, m) for lvl, _, m in check(text, **kw)]


def has(found, level, fragment):
    return any(lvl == level and fragment in m for lvl, m in found)


clean = "Predau din liceu. Am ținut cinci sesiuni pentru colegi."
assert not any(lvl == "FAIL" for lvl, _ in msgs(clean, lang="ro", plain=True, max_chars=4000, max_numbers=2))

# length: newline cost 2 (cautious) vs 1 (Word-like)
assert has(msgs("aaaa\nbbbb\ncccc", max_chars=12), "FAIL", "exceeds 12")
assert not has(msgs("aaaa\nbbbb\ncccc", max_chars=12, newline_cost=0), "FAIL", "exceeds")
assert has(msgs("aaaa\nbbbb\ncccc", max_chars=13, newline_cost=1), "FAIL", "exceeds")

# plain text: formatting markers fail, ordinary text does not
for bad in ("# Titlu", "**bold**", "[a](http://x)", "| a | b |", "<b>x</b>", "`cod`"):
    assert has(msgs(bad, plain=True), "FAIL", "formatting"), bad
for fine in ("Un text simplu, cu virgulă.", "Semnătura: ________", "a<b, atunci b>a", "- o linie cu liniuță"):
    assert not has(msgs(fine, plain=True), "FAIL", "formatting"), fine
assert has(msgs("- punct", plain=True), "WARN", "list bullet")

# spacing, with realistic non-errors left alone
f = msgs("Doua  spatii , si  lipsa,spatiu.")
assert has(f, "WARN", "double space") and has(f, "WARN", "space before punctuation") and has(f, "WARN", "missing space")
for fine in ("Valoarea 1,5 este corecta.", "Vezi https://exemplu.ro/x si fisierul a.md :)", "a) primul punct"):
    g = msgs(fine)
    assert not has(g, "WARN", "missing space") and not has(g, "WARN", "space before") and not has(g, "WARN", "parenthesis"), fine
assert has(msgs("o (paranteza"), "WARN", "unclosed parenthesis")

# repeated words and numbers
assert has(msgs("Am am ținut sesiuni."), "WARN", "repeated word")
assert has(msgs("Am 15 sesiuni și 5 stagiari și 3 ateliere.", max_numbers=2), "FAIL", "numbers")
assert not has(msgs("Suma 1.000.000 lei la 06.10.2026 ora 10:30.", max_numbers=3), "FAIL", "numbers")
assert has(msgs("agenții agenții agenții"), "WARN", "used 3 times")

# Romanian: cedilla fails, comma-below passes, quotes
assert has(msgs(f"Să predau a{CED}a.", lang="ro"), "FAIL", "cedilla")
assert not has(msgs("Să predau așa.", lang="ro"), "FAIL", "cedilla")
assert has(msgs('Programul "AI".', lang="ro"), "WARN", "straight quotes")
assert not has(msgs(f"Programul {OPEN}AI{CLOSE} și it's.", lang="ro"), "WARN", "quot")
assert has(msgs("Programul “AI”.", lang="ro"), "WARN", "non-Romanian quotation")
assert has(msgs("fara diacritice " * 25, lang="ro"), "WARN", "no Romanian diacritics")

# command line: exit codes, CRLF, BOM, unreadable file
script = os.path.join(HERE, "proofread.py")


def run(content, *args, raw=False):
    with tempfile.NamedTemporaryFile("wb", suffix=".md", delete=False) as fh:
        fh.write(content if raw else content.encode("utf-8"))
        path = fh.name
    try:
        return subprocess.run([sys.executable, script, path, *args], capture_output=True, text=True, encoding="utf-8")
    finally:
        os.unlink(path)


assert run(clean, "--lang", "ro-RO", "--plain").returncode == 0
assert run(f"a{CED}a", "--lang", "ro").returncode == 1
assert run("Linia unu.\r\nLinia doi.\r\n", "--plain").returncode == 0                       # CRLF
assert run(b"\xef\xbb\xbf# Titlu", "--plain", raw=True).returncode == 1                       # BOM must not hide the heading
assert run(b"\xff\xfe\x00bad", raw=True).returncode == 2                                      # not UTF-8
assert subprocess.run([sys.executable, script, "no-such-file.md"], capture_output=True).returncode == 2
assert run("").returncode == 0                                                                # empty file

print("proofread.py: all checks passed")
