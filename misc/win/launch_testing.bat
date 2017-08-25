%~d1
cd "%~p1"
cd "../.."
call venv\Scripts\activate.bat
py.test
PAUSE;