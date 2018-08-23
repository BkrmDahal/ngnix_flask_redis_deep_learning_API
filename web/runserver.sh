#!/bin/bash
echo "start the deep learning model"
python3 app/run_model_server.py &

echo "start gunicorn server "
gunicorn --log-level info --log-file=/gunicorn.log --workers 4 --name app -b 0.0.0.0:8000--reload app.run_web_server:app
