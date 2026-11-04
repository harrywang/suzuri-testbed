"""Rewrites agent-writes.canvas the way an agent would, one step at a time.

Run from the testbed root while the canvas is open:

    python3 canvas/live-reload/simulate-agent.py 1      # three papers
    python3 canvas/live-reload/simulate-agent.py 2      # adds a synthesis card and edges
    python3 canvas/live-reload/simulate-agent.py 3      # recolors and relabels
    python3 canvas/live-reload/simulate-agent.py broken # a write cut off halfway
    python3 canvas/live-reload/simulate-agent.py reset  # back to the committed state
"""

import json
import sys
from pathlib import Path

CANVAS = Path(__file__).with_name("agent-writes.canvas")


def card(id, x, y, text, color=None):
    node = {"id": id, "type": "text", "x": x, "y": y, "width": 260, "height": 120, "text": text}
    if color:
        node["color"] = color
    return node


def state(step):
    nodes = [
        card("p1", 0, 0, "**Paper 1**\nremote helps"),
        card("p2", 320, 0, "**Paper 2**\nno difference"),
        card("p3", 640, 0, "**Paper 3**\njuniors lose"),
    ]
    edges = []
    if step >= 2:
        nodes.append(card("syn", 320, 260, "**Synthesis** (added in step 2)", color="3"))
        edges = [
            {"id": f"e{index}", "fromNode": f"p{index}", "toNode": "syn"} for index in (1, 2, 3)
        ]
    if step >= 3:
        nodes[2]["color"] = "1"
        nodes[2]["text"] = "**Paper 3**\njuniors lose (red in step 3)"
        edges[2]["label"] = "contradicts?"
        edges[2]["color"] = "1"
    return {"nodes": nodes, "edges": edges}


def main():
    step = sys.argv[1] if len(sys.argv) > 1 else "1"
    if step == "reset":
        step = "0"
    if step == "broken":
        full = json.dumps(state(3), indent="\t")
        CANVAS.write_text(full[: len(full) // 2])
    elif step == "0":
        CANVAS.write_text("")
    else:
        CANVAS.write_text(json.dumps(state(int(step)), indent="\t") + "\n")
    print(f"wrote step {step} to {CANVAS}")


if __name__ == "__main__":
    main()
