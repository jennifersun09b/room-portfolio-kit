#!/bin/bash
# RoomKit Studio for macOS - double-click this file to start.
# (First time: if macOS says it can't be opened, right-click it and choose Open.)
cd "$(dirname "$0")" || exit 1

PY=""
for cand in python3 /usr/bin/python3 /opt/homebrew/bin/python3 /usr/local/bin/python3; do
  if command -v "$cand" >/dev/null 2>&1 && "$cand" -c 'import sys; sys.exit(0 if sys.version_info >= (3, 9) else 1)' >/dev/null 2>&1; then
    PY="$cand"; break
  fi
done

if [ -z "$PY" ]; then
  echo ""
  echo "  RoomKit Studio needs Python 3.9 or newer."
  echo "  macOS will now offer to install the free Apple developer tools, which include Python."
  echo "  (Or download Python from https://www.python.org/downloads/)"
  echo "  When it's done, double-click Start.command again."
  echo ""
  xcode-select --install >/dev/null 2>&1
  open "https://www.python.org/downloads/macos/" >/dev/null 2>&1
  read -r -p "  Press Return to close this window. "
  exit 1
fi

clear
echo ""
echo "  Starting RoomKit Studio..."
echo ""
"$PY" tools/studio.py "$@"
status=$?
if [ $status -ne 0 ]; then
  echo ""
  read -r -p "  RoomKit Studio stopped (code $status). Press Return to close this window. "
fi
