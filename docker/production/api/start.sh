#!/bin/bash

set -o errexit
set -o pipefail
set -o nounset

./src/manage.py migrate --noinput
./src/manage.py collectstatic --noinput
cd src

exec gunicorn --bind 0.0.0.0:8000 --max-requests 1000 --workers 4 --log-level debug config.wsgi:application
