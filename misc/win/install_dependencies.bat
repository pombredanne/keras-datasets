%~d1
cd "%~p1"
cd "../.."
cd "%~p1"
call venv\Scripts\activate.bat
call pip install --upgrade pip
call pip install "misc\libraries\scipy-0.19.1-cp36-cp36m-win_amd64.whl"
call pip install -e .[dev]
PAUSE;
