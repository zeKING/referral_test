import datetime

import os

from django.contrib.auth.hashers import make_password
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'referal_project.settings')

django.setup()

from users.models import User


def main():

    user, _ = User.objects.get_or_create(username='admin',
                                         defaults={
                                             'email': 'tigrangri37@gmail.com',
                                             'password': make_password('admin123'),
                                             'is_superuser': True,
                                             'is_staff': True,
                                             'is_active': True,
                                             })


if __name__ == '__main__':
    main()