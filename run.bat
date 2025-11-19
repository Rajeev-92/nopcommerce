@echo off
call venv\Scripts\activate
pytest -s -v -m "sanity" --html .\reports\test_report_chrome.html --browser chrome
pytest -s -v -m "regression" --html .\reports\test_report_chrome.html --browser chrome
pytest -s -v -m "sanity and regression" --html .\reports\test_report_chrome.html --browser chrome
pause
