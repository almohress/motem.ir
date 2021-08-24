#!/bin/sh

echo "apply db migrations"
python3 manage.py makemigrations && python3 manage.py migrate

echo "creating default superuser"
cat bootstrap.py | python3 manage.py shell

echo "run server"
if [ "$DEBUG" = true ] ; then
    python3 manage.py runserver 0.0.0.0:8080
else
    gunicorn --bind :8080 --workers 3 motem_ir.wsgi:application
fi