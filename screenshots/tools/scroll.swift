import CoreGraphics
import Foundation

// Usage: scroll <x> <y> <lines>  (negative lines scroll the content up)
let arguments = CommandLine.arguments
let point = CGPoint(x: Double(arguments[1])!, y: Double(arguments[2])!)
let lines = Int32(arguments[3])!
CGEvent(mouseEventSource: nil, mouseType: .mouseMoved, mouseCursorPosition: point, mouseButton: .left)?
    .post(tap: .cghidEventTap)
usleep(200_000)
for _ in 0..<abs(lines) {
    CGEvent(scrollWheelEvent2Source: nil, units: .line, wheelCount: 1, wheel1: lines < 0 ? -1 : 1, wheel2: 0, wheel3: 0)?
        .post(tap: .cghidEventTap)
    usleep(30_000)
}
