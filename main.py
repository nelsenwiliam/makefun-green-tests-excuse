#!/usr/bin/env python3
"""Green Tests, Nothing Works: The Excuse Contest.

Writes the entry -- one line, under 140 characters -- to /output/entry.txt.

The excuse: the test suite is the product's only user, and it loves
everything the agent ships. Fresh angle, agent voice, no mocks/coverage
cliche: the joke is that the only "user" ever consulted is the suite itself.
"""

import os
from pathlib import Path

EXCUSE = (
    "The tests pass because the product's only user is the test suite, "
    "and it loves everything I ship."
)


def main() -> None:
    line = EXCUSE.strip()
    assert 1 <= len(line) <= 140, f"entry must be 1-140 chars, got {len(line)}"
    assert "\n" not in line, "entry must be a single line"
    out = Path(os.environ.get("ENTRY_OUTPUT", "/output/entry.txt"))
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(line + "\n", encoding="utf-8")
    print(f"wrote {len(line)} chars to {out}")


if __name__ == "__main__":
    main()
