#!/bin/sh

echo "apply db migrations"
python3 manage.py makemigrations && python3 manage.py migrate

echo "run server"
gunicorn --bind :8080 --workers 3 motem_ir.wsgi:application