from django.contrib.auth.models import User
from os import getenv


def create_default_admin():
    user = User.objects.create_superuser(
        username=getenv('DEFAULT_ADMIN_USERNAME'),
        email=getenv('DEFAULT_ADMIN_EMAIL'),
        password=getenv('DEFAULT_ADMIN_PASSWORD'))


def main():
    create_default_admin()


if __name__ == '__main__':
    main()
