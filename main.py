"""One-Line Laugh Sprint.

A one-line joke about everyday life, written to
/output/entry.txt (or $MAKEFUN_OUTPUT_DIR when set, for local runs).
Standard library only, no network, deterministic: the same bytes on
every run.
"""

import os

JOKE = (
    "My fitness tracker congratulated me on 10,000 steps, then quietly "
    "logged my three trips to the fridge as interval training."
)

# The gate allows 1 to 200 characters: refuse to write a line that
# would be invalid, rather than submitting a joke the judge never sees.
if not 1 <= len(JOKE) <= 200:
    raise SystemExit(f"joke is {len(JOKE)} characters, outside the 1-200 gate")


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(JOKE + "\n")
    os.chmod(path, 0o644)
    # Read-back check: the file on disk must hold exactly the approved joke.
    with open(path, encoding="utf-8") as f:
        written = f.read()
    if written != JOKE + "\n":
        raise SystemExit("entry.txt does not match the approved joke")


if __name__ == "__main__":
    main()
