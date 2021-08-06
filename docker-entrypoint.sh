#!/bin/sh

echo "apply db migrations"
python3 manage.py makemigrations && python3 manage.py migrate

echo "creating default superuser"
DEFAULT_ADMIN_USERNAME=$1
DEFAULT_ADMIN_EMAIL=$2
DEFAULT_ADMIN_PASSWORD=$3
./bootstrap.sh $DEFAULT_ADMIN_USERNAME $DEFAULT_ADMIN_EMAIL $DEFAULT_ADMIN_PASSWORD

echo "run server"
gunicorn --bind :8080 --workers 3 motem_ir.wsgi:application