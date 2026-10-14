#!/bin/sh
# Reproduces the reload that used to leave the PDF viewer hit-testing against a
# document it was no longer showing.
#
# Open doc.pdf in Suzuri, then run `./swap.sh race`. The first copy starts a six
# page text extraction; the second replaces the file before that extraction has
# finished, which is the window a typeset preview opens every time it recompiles
# while you type.
#
# Then press cmd-c in the PDF pane and look at the clipboard. It should hold
# SHORTDOCUMENTMARKER. LONGDOCUMENTMARKER means the viewer is still describing
# the replaced document, and text selection will be hit-testing against glyph
# positions that no longer match the page.
set -eu

cd "$(dirname "$0")"
DELAY=${2:-0.15}

case "${1:-race}" in
reset)
    cp long.pdf doc.pdf
    echo "doc.pdf = long.pdf (6 pages, LONGDOCUMENTMARKER)"
    ;;
race)
    cp long.pdf doc.pdf
    sleep "$DELAY"
    cp short.pdf doc.pdf
    echo "swapped long.pdf -> short.pdf after ${DELAY}s; expect SHORTDOCUMENTMARKER"
    ;;
*)
    echo "usage: $0 [reset|race] [delay-seconds]" >&2
    exit 2
    ;;
esac
