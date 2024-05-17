@echo off

REM Check if the requirements.txt file exists
IF NOT EXIST requirements.txt (
    echo requirements.txt not found!
    exit /b 1
)

REM Check if the required libraries are already installed by trying to import them
REM If not installed, then install them using pip
echo Checking required libraries...

REM Use a temporary file to check if pip installs are needed
pip freeze > installed_packages.txt

FOR /F "delims=" %%i IN (requirements.txt) DO (
    FIND /I "%%i" installed_packages.txt >nul
    IF ERRORLEVEL 1 (
        echo Installing %%i...
        pip install %%i
    ) ELSE (
        echo %%i already installed.
    )
)

DEL installed_packages.txt

REM Navigate to the data directory
cd ./data

REM Run the Python script
python pages.py

echo Script execution completed.
pause