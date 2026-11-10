#!/usr/bin/env bash
# RoomKit Studio for Linux - run ./start.sh (or double-click and choose "Run in terminal").
cd "$(dirname "$0")" || exit 1

PY=""
for cand in python3 python; do
  if command -v "$cand" >/dev/null 2>&1 && "$cand" -c 'import sys; sys.exit(0 if sys.version_info >= (3, 9) else 1)' >/dev/null 2>&1; then
    PY="$cand"; break
  fi
done
if [ -z "$PY" ]; then
  echo "RoomKit Studio needs Python 3.9 or newer."
  echo "Install it with your package manager, e.g.:  sudo apt install python3   or   sudo dnf install python3"
  exit 1
fi

echo "Starting RoomKit Studio..."
exec "$PY" tools/studio.py "$@"
