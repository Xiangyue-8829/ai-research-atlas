@echo off
setlocal
cd /d "%~dp0"
echo ===========================================================
echo   AI Research Atlas V3 -- prepare & validate local checkout
 echo ===========================================================
where py >nul 2>&1
if %ERRORLEVEL%==0 (
    py -3 tools\finish_v3.py
    if errorlevel 1 goto failed
    py -3 tools\check_v3.py
    if errorlevel 1 goto failed
    goto success
)
where python >nul 2>&1
if %ERRORLEVEL% NEQ 0 (
    echo ERROR: Please install Python 3.10 or later first.
    goto failed
)
python tools\finish_v3.py
if errorlevel 1 goto failed
python tools\check_v3.py
if errorlevel 1 goto failed
:success
echo.
echo SUCCESS: V3 source is prepared; commit to feature/atlas-v3 using GitHub Desktop.
echo NOTE: This did not publish or push anything automatically.
pause
exit /b 0
:failed
echo.
echo FAILED: Please read README_V3_DEPLOY.md and check folder placement.
pause
exit /b 1
