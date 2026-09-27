#!/bin/zsh
# Open a screenshot vault in an isolated Suzuri window sized for suzuri.ai.
#
# Usage: screenshots/open.sh <vault> [file ...]
#   screenshots/open.sh inkstone-notes notes/grinding-the-ink.md paper/ink-density.typ
#
# The vault is copied to $SUZURI_SHOTS_DIR (default /tmp/suzuri-shots) and made
# its own git repo, so the title bar reads the vault's name rather than a path
# inside this testbed, and autosave or kernel metadata never dirty the fixtures.
# Prints the app's pid; pass it to capture.sh.
set -e
here=${0:A:h}
vault=$1
shift
if [[ -z "$vault" || ! -d "$here/$vault" ]]; then
  echo "usage: $0 <vault> [file ...]; vaults: $(ls -d $here/*/ | xargs -n1 basename | grep -v -e tools -e config | tr '\n' ' ')" >&2
  exit 1
fi

app=${SUZURI_APP:-/Applications/Suzuri.app/Contents/MacOS/zed}
root=${SUZURI_SHOTS_DIR:-/tmp/suzuri-shots}
copy=$root/$vault
data=$root/data-$vault

# The data dir is kept between runs: it remembers dismissed toasts, such as
# the offer to install the typst extension, which no setting can turn off.
rm -rf $copy
mkdir -p $root $data/config
cp -R $here/$vault $copy
cp $here/config/keymap.json $data/config/
# Machine-specific settings, such as an agent login's proxy, go in
# settings.local.json beside it: a full settings file used in place of ours.
if [[ -f $data/config/settings.local.json ]]; then
  cp $data/config/settings.local.json $data/config/settings.json
else
  cp $here/config/settings.json $data/config/
fi

# Reuse compilers the installed app already downloaded, so a Typst or LaTeX
# preview does not start with a provisioning toast.
installed_data="$HOME/Library/Application Support/Zed"
if [[ -d "$installed_data/typeset_compilers" && ! -d $data/typeset_compilers ]]; then
  cp -R "$installed_data/typeset_compilers" $data/
fi

(
  cd $copy
  git init -q -b main
  git add -A
  git -c user.name=Suzuri -c user.email=suzuri@example.com commit -qm "Screenshot vault"
  # A vault with a notebook gets a project .venv, which Suzuri picks as the kernel.
  if [[ -n "$(find . -name '*.ipynb' -not -path './.venv/*' | head -1)" ]]; then
    uv venv -q .venv
    uv pip install -q --python .venv/bin/python ipykernel numpy matplotlib
  fi
)

files=()
for file in "$@"; do
  files+=("$copy/$file")
done

# The nightly channel gives this instance its own single-instance socket, so
# it never hands off to a running Suzuri.
ZED_RELEASE_CHANNEL=nightly nohup $app --user-data-dir $data $copy "${files[@]}" > $root/$vault.log 2>&1 &
pid=$!
osascript $here/tools/size.applescript $pid 1430 825 > /dev/null
echo $pid
