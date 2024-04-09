#!/bin/bash

set -o errexit
set -o pipefail
set -o nounset

./src/manage.py migrate --noinput

exec ./src/manage.py runserver 0.0.0.0:8000
