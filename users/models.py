from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.


class User(AbstractUser):
    date_joined = None
    last_login = None
    # date of joining as referral
    referral_date_joined = models.DateField(null=True, blank=True)
    # user-referrer of user
    referrer_user = models.ForeignKey('self', on_delete=models.SET_NULL, null=True, related_name='referrals')

    def __str__(self):
        return self.email
