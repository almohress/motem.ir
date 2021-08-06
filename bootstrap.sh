#!/bin/bash

DEFAULT_ADMIN_USERNAME=$1
DEFAULT_ADMIN_EMAIL=$2
DEFAULT_ADMIN_PASSWORD=$3

echo "from django.contrib.auth.models import User; User.objects.create_superuser('${DEFAULT_ADMIN_USERNAME}', '${DEFAULT_ADMIN_EMAIL}', '${DEFAULT_ADMIN_PASSWORD}')" | python manage.py shell