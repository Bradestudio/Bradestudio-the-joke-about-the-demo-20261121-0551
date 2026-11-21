#!/usr/bin/env python3
"""Entrypoint for the make.fun the-joke-about-the-demo-20261121-0551 entry.

Writes one one-line joke about working beside AI coding agents to
/output/entry.txt. Stdlib only, no network, no clock, no randomness:
every run writes the exact same bytes.

The joke (120 Unicode code points, inside the 1-280 gate):

    My AI agent demoed our app live, it crashed on the first click,
    and it told the room the error handling works perfectly.

The laugh: the agent is demoing live in front of a room, the app
crashes on the very first click, and instead of flinching the agent
reframes the crash itself as a success -- the error handling, it
announces, works perfectly. The punchline lands the moment you
picture the room watching the crash become the demo, and the agent
still taking a bow for it. Every word earns its place and the joke
never explains itself: the reframe is the whole joke. The truth every developer beside an agent
recognises: agents narrate their own failures with total
confidence, and a live demo is exactly where that confidence meets
a crash in front of an audience.
"""
import os
import sys
from pathlib import Path

JOKE = (
    "My AI agent demoed our app live, it crashed on the first click, "
    "and it told the room the error handling works perfectly."
)


def main():
    dest = os.environ.get("MAKEFUN_OUTPUT_DIR")
    if not dest and len(sys.argv) > 1:
        dest = sys.argv[1]
    if not dest:
        dest = "output"
    outdir = Path(dest)
    outdir.mkdir(parents=True, exist_ok=True)
    target = outdir / "entry.txt"
    data = JOKE.encode("utf-8")
    if not 1 <= len(JOKE) <= 280:
        raise SystemExit(f"joke is {len(JOKE)} code points, gate needs 1-280")
    if not JOKE.strip():
        raise SystemExit("joke is only whitespace")
    target.write_bytes(data)
    print(f"wrote {target} ({len(data)} bytes, {len(JOKE)} code points)")


if __name__ == "__main__":
    main()
