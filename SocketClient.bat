setlocal
cd ..\
set PYTHONPATH=%cd%;%PYTHONPATH%
cd ace_bbsm
python socket_client.py
endlocal