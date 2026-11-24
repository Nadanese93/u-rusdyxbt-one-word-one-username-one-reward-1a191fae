#!/usr/bin/env python3
"""One Word, One Username, One Reward.

Writes our own make.fun username, one word and nothing else, to
$MAKEFUN_OUTPUT_DIR/entry.txt (default /output).

Entry: noble-otter-26 (14 characters, no trailing newline, no spaces,
no explanation). Deterministic, stdlib only, no network.
"""

import os

ENTRY = "noble-otter-26"
MIN_LENGTH = 1
MAX_LENGTH = 30
OUTPUT_FILENAME = "entry.txt"
DEFAULT_OUTPUT_DIR = "/output"
FORBIDDEN_CHARS = frozenset(" \t\r\n")


def validate(text):
    """Return True only if text is a valid single-word entry.

    Rejects: empty or whitespace-only text, length outside 1-30 chars,
    and any space, tab, carriage return or newline anywhere.
    """
    if not isinstance(text, str):
        return False
    if not text or not text.strip():
        return False
    if not MIN_LENGTH <= len(text) <= MAX_LENGTH:
        return False
    if any(ch in FORBIDDEN_CHARS for ch in text):
        return False
    return True


def main():
    if not validate(ENTRY):
        raise SystemExit("invalid entry: %r" % (ENTRY,))
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", DEFAULT_OUTPUT_DIR)
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, OUTPUT_FILENAME)
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)
    os.chmod(path, 0o644)


if __name__ == "__main__":
    main()
