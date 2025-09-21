
## 2. run.bat (Windows Launcher)

```batch
@echo off
echo ========================================
echo    Anime vs Real Image Sorter
echo    Created by amkitpro
echo ========================================
echo.

REM Check if Python is installed
python --version >nul 2>&1
if errorlevel 1 (
    echo Error: Python is not installed or not in PATH
    echo Please install Python 3.7+ from https://python.org
    pause
    exit /b 1
)

REM Check if virtual environment exists
if not exist "dd-env" (
    echo Creating virtual environment...
    python -m venv dd-env
    if errorlevel 1 (
        echo Error: Failed to create virtual environment
        pause
        exit /b 1
    )
)

REM Activate virtual environment
echo Activating virtual environment...
call dd-env\Scripts\activate.bat
if errorlevel 1 (
    echo Error: Failed to activate virtual environment
    pause
    exit /b 1
)

REM Install dependencies
echo Installing dependencies...
pip install --upgrade pip
pip install -r requirements.txt
if errorlevel 1 (
    echo Error: Failed to install dependencies
    pause
    exit /b 1
)

REM Check if dependencies are installed correctly
echo Checking dependencies...
python check_dependencies.py
if errorlevel 1 (
    echo Warning: Some dependencies may not be installed correctly
)

REM Run the application
echo.
echo ========================================
echo    Starting Anime vs Real Image Sorter
echo ========================================
echo.
python anime_real_sorter.py

REM Keep the window open after application closes
echo.
echo Application closed.
echo Press any key to exit...
pause >nul