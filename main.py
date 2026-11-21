#!/usr/bin/env python3
"""Entry point for the Talvera passport spread.

Copies the stored entry.png to the output directory given by the
MAKEFUN_OUTPUT_DIR environment variable (falling back to this script's
own directory when the variable is unset), then verifies the copy by
comparing sha256 hashes of the source and the destination.

Standard library only: no third-party imports.
"""
import hashlib
import os
import shutil
import sys
from pathlib import Path


def sha256_of(path):
    digest = hashlib.sha256()
    with open(path, "rb") as handle:
        for chunk in iter(lambda: handle.read(65536), b""):
            digest.update(chunk)
    return digest.hexdigest()


def main():
    here = Path(__file__).resolve().parent
    source = here / "entry.png"
    if not source.is_file():
        print("error: entry.png not found next to main.py", file=sys.stderr)
        return 1

    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or str(here)
    out_dir = Path(out_dir)
    out_dir.mkdir(parents=True, exist_ok=True)
    dest = out_dir / "entry.png"

    try:
        shutil.copyfile(source, dest)
    except shutil.SameFileError:
        # The output directory is the repository directory itself:
        # there is nothing to copy, just verify the file in place.
        pass

    src_hash = sha256_of(source)
    dst_hash = sha256_of(dest)
    if src_hash != dst_hash:
        print("error: sha256 mismatch after copy", file=sys.stderr)
        return 1

    print("wrote:", dest)
    print("sha256:", dst_hash)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
