@echo off
cd /d "%~dp0"
call .venv\Scripts\activate
pytest testCases/ -v
pause