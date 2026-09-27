import CoreGraphics
import Foundation

let targetPid = Int32(CommandLine.arguments[1])!
let windows = CGWindowListCopyWindowInfo([.optionOnScreenOnly], kCGNullWindowID) as! [[String: Any]]
for window in windows where (window[kCGWindowOwnerPID as String] as? Int32) == targetPid {
    let layer = window[kCGWindowLayer as String] as? Int ?? -1
    let bounds = window[kCGWindowBounds as String] as? [String: Any] ?? [:]
    print(window[kCGWindowNumber as String]!, layer, bounds["Width"]!, bounds["Height"]!)
}
