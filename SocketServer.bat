setlocal
cd ..\
set PYTHONPATH=%cd%;%PYTHONPATH%
cd ace_bbsm
python socket_server.py
endlocal