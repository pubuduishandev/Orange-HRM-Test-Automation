@echo off
cd /d "%~dp0"
call .venv\Scripts\activate
cls

python Utilities\run_tests.py

pause
