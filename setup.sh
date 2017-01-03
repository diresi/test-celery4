#!/bin/bash

VENV=${PWD}/venvs/celery-test
mkdir -p ${VENV}
rm -rf ${VENV}
virtualenv ${VENV}
source ${VENV}/bin/activate
pip install -r requirements.txt

# run a rabbitmq server
docker run -d rabbitmq:3.6.6

echo
echo
echo "run the following commands (you'll need 2 terminals)"
echo "$  source ${VENV}/bin/activate"
echo "$  celery -A task worker --loglevel=info -c 4 -P prefork"
echo "$  python test.py"
