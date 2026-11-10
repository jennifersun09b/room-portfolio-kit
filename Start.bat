@echo off
rem RoomKit Studio for Windows - double-click this file to start.
title RoomKit Studio
cd /d "%~dp0"

set "PY="
where py >nul 2>nul && py -3 -c "import sys; sys.exit(0 if sys.version_info >= (3, 9) else 1)" >nul 2>nul && set "PY=py -3"
if not defined PY (
  where python >nul 2>nul && python -c "import sys; sys.exit(0 if sys.version_info >= (3, 9) else 1)" >nul 2>nul && set "PY=python"
)
if not defined PY (
  echo.
  echo   RoomKit Studio needs Python 3.9 or newer.
  echo   Your browser will open the Python download page.
  echo   Install it, tick "Add python.exe to PATH", then double-click Start.bat again.
  echo.
  start "" "https://www.python.org/downloads/windows/"
  pause
  exit /b 1
)

echo.
echo   Starting RoomKit Studio...
echo.
%PY% tools\studio.py %*
if errorlevel 1 (
  echo.
  echo   RoomKit Studio stopped with an error.
  pause
)
