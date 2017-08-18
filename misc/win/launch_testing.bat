%~d1
cd "%~p1"
cd "../.."
call venv\Scripts\activate.bat
coverage run setup.py test
coverage report
PAUSE;