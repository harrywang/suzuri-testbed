"""Generate a numbered-grid PNG fixture with the stdlib only (no Pillow here).

A flat colour block cannot tell you whether a crop landed; a grid of numbered
cells can. Crop any region and the visible numbers change, so the fixture makes
"did the preview pick up the new file" answerable by eye.
"""

import struct
import sys
import zlib

# Seven-segment digits: which segments each numeral lights.
SEGMENTS = {
    1: "bc",
    2: "abged",
    3: "abgcd",
    4: "fgbc",
    5: "afgcd",
    6: "afgecd",
}


def new_canvas(width, height, colour):
    return [[colour for _ in range(width)] for _ in range(height)]


def fill(canvas, x0, y0, x1, y1, colour):
    height = len(canvas)
    width = len(canvas[0])
    for y in range(max(0, y0), min(height, y1)):
        row = canvas[y]
        for x in range(max(0, x0), min(width, x1)):
            row[x] = colour


def draw_digit(canvas, digit, x, y, w, h, thickness, colour):
    """Draw a seven-segment numeral with its top-left corner at (x, y)."""
    lit = SEGMENTS[digit]
    mid = y + h // 2
    if "a" in lit:
        fill(canvas, x, y, x + w, y + thickness, colour)
    if "g" in lit:
        fill(canvas, x, mid - thickness // 2, x + w, mid + thickness - thickness // 2, colour)
    if "d" in lit:
        fill(canvas, x, y + h - thickness, x + w, y + h, colour)
    if "f" in lit:
        fill(canvas, x, y, x + thickness, mid, colour)
    if "b" in lit:
        fill(canvas, x + w - thickness, y, x + w, mid, colour)
    if "e" in lit:
        fill(canvas, x, mid, x + thickness, y + h, colour)
    if "c" in lit:
        fill(canvas, x + w - thickness, mid, x + w, y + h, colour)


def write_png(path, canvas):
    height = len(canvas)
    width = len(canvas[0])
    raw = b"".join(
        b"\x00" + b"".join(bytes(pixel) for pixel in row) for row in canvas
    )

    def chunk(tag, data):
        body = tag + data
        return (
            struct.pack(">I", len(data))
            + body
            + struct.pack(">I", zlib.crc32(body) & 0xFFFFFFFF)
        )

    png = (
        b"\x89PNG\r\n\x1a\n"
        + chunk(b"IHDR", struct.pack(">IIBBBBB", width, height, 8, 2, 0, 0, 0))
        + chunk(b"IDAT", zlib.compress(raw, 9))
        + chunk(b"IEND", b"")
    )
    with open(path, "wb") as handle:
        handle.write(png)


WARM = [(196, 62, 50), (214, 118, 44), (186, 152, 54), (166, 82, 68), (204, 96, 40), (150, 110, 60)]
COOL = [(46, 92, 158), (52, 128, 146), (74, 96, 176), (40, 110, 132), (64, 84, 150), (48, 120, 160)]

COLUMNS, ROWS = 3, 2
CELL_W, CELL_H = 220, 180
GAP = 6


def build(palette):
    width = COLUMNS * CELL_W
    height = ROWS * CELL_H
    canvas = new_canvas(width, height, (28, 28, 32))
    for index in range(COLUMNS * ROWS):
        column = index % COLUMNS
        row = index // COLUMNS
        x0 = column * CELL_W + GAP
        y0 = row * CELL_H + GAP
        fill(canvas, x0, y0, x0 + CELL_W - 2 * GAP, y0 + CELL_H - 2 * GAP, palette[index])
        draw_digit(
            canvas,
            index + 1,
            x0 + (CELL_W - 2 * GAP) // 2 - 32,
            y0 + (CELL_H - 2 * GAP) // 2 - 52,
            64,
            104,
            16,
            (250, 250, 245),
        )
    return canvas


if __name__ == "__main__":
    # Regenerates both fixtures in place. Run from anywhere; paths are relative
    # to this file, so cropping them for a test is always undoable without git.
    import pathlib

    here = pathlib.Path(__file__).resolve().parent
    targets = [
        (here / "reload-check-sibling.png", COOL),
        (here.parent / "attachments" / "reload-check-parent.png", WARM),
    ]
    for target, palette in targets:
        write_png(target, build(palette))
        print(f"wrote {target} ({COLUMNS * CELL_W}x{ROWS * CELL_H})")
