#!/bin/bash
DJANGODIR=$(dirname "$(realpath "$0")")/..
cd "$DJANGODIR"
source env/bin/activate
export DJANGO_SETTINGS_MODULE=ShinyLove.settings
exec python manage.py runserver 0:9000
