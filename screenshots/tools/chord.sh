#!/bin/zsh
# Press ctrl-alt-cmd-<key> in a Suzuri window, bound in config/keymap.json.
# Focus is checked right before the key, since the terminal takes it back
# between commands.
#
# Usage: screenshots/tools/chord.sh <pid> <key>   (page-up, page-down, home)
pid=$1
osascript -e "tell application \"System Events\" to set frontmost of (first process whose unix id is $pid) to true"
sleep 0.5
front=$(osascript -e 'tell application "System Events" to unix id of first process whose frontmost is true')
if [[ "$front" != "$pid" ]]; then
  echo "focus lost to pid $front" >&2
  exit 1
fi
cliclick kd:ctrl,alt,cmd kp:$2 ku:ctrl,alt,cmd
