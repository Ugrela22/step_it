@echo off
setlocal enabledelayedexpansion

REM Helper to add origin remote and push to GitHub (Windows cmd)
REM Usage: double-click or run from cmd in this folder.

cd /d "%~dp0"

necho This script will add a remote named "origin" pointing to https://github.com/<USERNAME>/<REPO>.git and push the current branch as "main".
echo If your repository doesn't exist on GitHub yet, create it first at https://github.com/new?name=step_it
echo.
set /p USERNAME=Enter your GitHub username (leave empty to cancel): 
if "%USERNAME%"=="" (
  echo No username provided — aborting.
  goto :eof
)
set /p REPO=Enter repository name [default: step_it]: 
if "%REPO%"=="" set REPO=step_it

necho Will use: https://github.com/%USERNAME%/%REPO%.git
echo.
pause

nREM Ensure we're on main branch (create/rename if needed)
ngit branch -M main 2>nul || (
  echo Failed renaming to main — continuing with current branch.
)

nREM Add remote (remove existing origin first if present)
ngit remote remove origin 2>nul || echo No existing origin to remove.
ngit remote add origin https://github.com/%USERNAME%/%REPO%.git
n
necho Pushing to origin main (you may be prompted for credentials)...
ngit push -u origin main
necho Done.
pause
