#!/bin/bash

VENV=${PWD}/venvs/celery-test
mkdir -p ${VENV}
rm -rf ${VENV}
virtualenv ${VENV}
source ${VENV}/bin/activate
pip install -r requirements.txt

# run a rabbitmq server
docker rm -vf rabbitmq
docker run -d --name rabbitmq -p 5672:5672 rabbitmq:3.6.6

echo
echo
echo "run the following commands (you'll need 2 terminals)"
echo "$  source ${VENV}/bin/activate"
echo "$  celery -A task worker --loglevel=info -c 1 -P prefork"
echo "$  python test.py"
