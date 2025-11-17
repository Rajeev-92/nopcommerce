@echo off
cd %WORKSPACE%

REM --- Activate the virtual environment correctly ---
call venv\Scripts\activate

REM --- Run pytest ---
pytest -s -v -m "sanity" --html reports\test_report.html --browser chrome

pause
