on run argv
	set targetPid to (item 1 of argv) as integer
	tell application "System Events"
		repeat 60 times
			if exists (first process whose unix id is targetPid) then
				set appProcess to first process whose unix id is targetPid
				if (count of windows of appProcess) > 0 then exit repeat
			end if
			delay 1
		end repeat
		set appProcess to first process whose unix id is targetPid
		set frontmost of appProcess to true
		set position of window 1 of appProcess to {60, 60}
		set size of window 1 of appProcess to {(item 2 of argv) as integer, (item 3 of argv) as integer}
		return (size of window 1 of appProcess) as text
	end tell
end run
