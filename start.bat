@echo off

REM Install required packages
echo Installing required packages...
pip install -r requirements.txt

IF NOT "%errorlevel%"=="0" (
    echo Failed to install required packages.
    echo Press any key to exit...
    pause >nul
    exit /b
)

REM Run the script
echo Running the script...
python main.py

echo Script execution completed.
echo Press any key to exit...
pause >nul
