#!/bin/zsh
# Capture a Suzuri window the way the suzuri.ai screenshots are framed:
# the window alone (no shadow, no desktop), scaled to 2000px wide.
#
# Usage: screenshots/capture.sh <pid> <out.png>
set -e
here=${0:A:h}
pid=$1
out=$2
window=$(swift $here/tools/winfo.swift $pid | awk '$2 == 0 { print $1 }' | head -1)
if [[ -z "$window" ]]; then
  echo "no on-screen window for pid $pid" >&2
  exit 1
fi
screencapture -x -o -l $window $out
sips -Z 2000 $out > /dev/null
sips -g pixelWidth -g pixelHeight $out | tail -2
