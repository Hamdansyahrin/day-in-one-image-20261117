#!/usr/bin/env python3
"""news-image-20261117 entrypoint.

Writes the entry image to the output directory. The picture itself —
one newspaper front page summing up Tuesday 17 November 2026 — is held
in this repository as entry.png, drawn beforehand by the build tooling
recorded in the transcripts. This program is deliberately small and
uses only the Python 3.13 standard library: it validates the image
(magic bytes, whole-file size, pixel dimensions) and copies it,
byte for byte, to <output>/entry.png. It runs with no network and
writes the same bytes on every run.
"""

import os
import struct
import sys
from pathlib import Path

MAX_BYTES = 1_048_576  # 1 MiB, the competition's whole-file cap
MAX_SIDE = 1024        # no side of the image may exceed 1024 px
PNG_MAGIC = b"\x89PNG\r\n\x1a\n"
JPEG_MAGIC = b"\xff\xd8\xff"


def image_format(data: bytes) -> str:
    """Name the image format from its first bytes, or fail loudly."""
    if data.startswith(PNG_MAGIC):
        return "PNG"
    if data.startswith(JPEG_MAGIC):
        return "JPEG"
    raise ValueError("entry.png is neither PNG nor JPEG (bad magic bytes)")


def png_dimensions(data: bytes) -> tuple[int, int]:
    """Read width and height from the PNG IHDR chunk."""
    if len(data) < 24 or data[12:16] != b"IHDR":
        raise ValueError("entry.png has no IHDR chunk where one belongs")
    width, height = struct.unpack(">II", data[16:24])
    return width, height


def jpeg_dimensions(data: bytes) -> tuple[int, int]:
    """Walk JPEG segments until a start-of-frame marker gives the size."""
    pos = 2
    while pos + 4 <= len(data):
        if data[pos] != 0xFF:
            raise ValueError("entry.png has a malformed JPEG segment")
        marker = data[pos + 1]
        length = struct.unpack(">H", data[pos + 2:pos + 4])[0]
        if marker in (0xC0, 0xC1, 0xC2):
            height, width = struct.unpack(">HH", data[pos + 5:pos + 9])
            return width, height
        pos += 2 + length
    raise ValueError("entry.png has no JPEG start-of-frame segment")


def validate(data: bytes) -> tuple[str, int, int]:
    """Check the competition's file rules; return (format, width, height)."""
    if not data:
        raise ValueError("entry.png is empty")
    if len(data) > MAX_BYTES:
        raise ValueError(f"entry.png is {len(data)} bytes, over the 1 MiB cap")
    fmt = image_format(data)
    width, height = png_dimensions(data) if fmt == "PNG" else jpeg_dimensions(data)
    if width > MAX_SIDE or height > MAX_SIDE:
        raise ValueError(f"entry.png is {width}x{height}, over the 1024 px cap")
    return fmt, width, height


def main() -> int:
    here = Path(__file__).resolve().parent
    source = here / "entry.png"
    data = source.read_bytes()
    fmt, width, height = validate(data)

    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    target = out_dir / "entry.png"
    target.write_bytes(data)

    print(f"wrote {target} ({len(data)} bytes, {fmt} {width}x{height})")
    return 0


if __name__ == "__main__":
    sys.exit(main())
