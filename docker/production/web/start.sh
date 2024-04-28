#!/bin/bash

set -o errexit
set -o pipefail
set -o nounset

cp -rfu /cache/node_modules/. /app/node_modules/

exec npm run preview
