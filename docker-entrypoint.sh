#!/bin/bash
set -e
echo "Make migrations"
python manage.py makemigrations --noinput
echo "Apply database migrations"
python manage.py migrate --noinput
echo "Starting server"
python manage.py runserver 0.0.0.0:8000