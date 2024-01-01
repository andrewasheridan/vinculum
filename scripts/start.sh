#!/bin/bash

# - starts Litestar application

set -o errexit
set -o pipefail
set -o nounset

echo Running migrations
alembic upgrade head


echo Starting Litestar App...
gunicorn app.vinculum_api.main:app --config app/vinculum_api/settings/_gunicorn_config.py
