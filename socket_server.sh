submodulesdir=$(cd ../ && pwd)
if [[ $PYTHONPATH != *"$submodulesdir"* ]]; then
  export PYTHONPATH=$submodulesdir:$PYTHONPATH
fi
python3 socket_server.py
