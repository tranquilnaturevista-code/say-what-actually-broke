#!/usr/bin/env python3
"""Say What Actually Broke.

Writes one line of honest software error copy -- the brutal truth
about what went wrong, funny on a single read -- to /output/entry.txt.

Python 3.13, standard library only, deterministic, no network.
The output directory is /output, or MAKEFUN_OUTPUT_DIR when set.
"""

import os
import sys

ENTRY = (
    "Nothing crashed. The server is fine and the database is fine "
    "\u2014 the config file someone edited at 2 a.m. was never "
    "committed, and now it is gone."
)


def main() -> int:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(ENTRY)
    # Self-check: read the file back and verify it holds exactly the
    # entry, and that the gate's limits hold (1-200 Unicode code
    # points, not only whitespace). Reading back catches a partial
    # write or an encoding surprise instead of trusting the write.
    with open(path, "r", encoding="utf-8", newline="\n") as f:
        written = f.read()
    if written != ENTRY:
        print("error: entry.txt does not match the entry", file=sys.stderr)
        return 1
    if not (1 <= len(written) <= 200):
        print(
            f"error: entry is {len(written)} characters, must be 1-200",
            file=sys.stderr,
        )
        return 1
    if not written.strip():
        print("error: entry is only whitespace", file=sys.stderr)
        return 1
    if "\n" in written:
        print("error: entry must be a single line", file=sys.stderr)
        return 1
    print(f"wrote {path} ({len(written)} characters)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
