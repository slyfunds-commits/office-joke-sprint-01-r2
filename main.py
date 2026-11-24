#!/usr/bin/env python3
"""One-Line Office Joke: 24-Hour Sprint — Round 2 entry.

Writes the keeper line to /output/entry.txt (no trailing newline),
asserts the 1-200 character gate, and byte-verifies what it wrote.
Pure standard library only.
"""

import os

ENTRY = "I wrote 'DO NOT EAT' on my sandwich. It came back with a bite taken out of the 'NOT'."


def main() -> None:
    text = ENTRY
    assert 1 <= len(text) <= 200, f"entry length {len(text)} outside 1-200"
    assert text.strip(), "entry is only whitespace"
    os.makedirs("/output", exist_ok=True)
    data = text.encode("utf-8")
    with open("/output/entry.txt", "wb") as f:
        f.write(data)
    with open("/output/entry.txt", "rb") as f:
        written = f.read()
    assert written == data, "byte verification failed"
    assert not written.endswith(b"\n"), "trailing newline present"
    # Second pass: decode what is on disk and re-apply the gate to the
    # decoded text itself, so the check covers the file, not just memory.
    decoded = written.decode("utf-8")
    assert decoded == text, "decoded file differs from entry"
    assert 1 <= len(decoded) <= 200, "decoded length outside 1-200"
    print(f"wrote {len(written)} bytes: {text}")


if __name__ == "__main__":
    main()
