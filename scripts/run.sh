#!/bin/sh
set -e

python manage.py collectstatic --noinput
python manage.py migrate
gunicorn -b :80 --chdir /UCClimbingWebApp UCClimbingWebApp.wsgi:application