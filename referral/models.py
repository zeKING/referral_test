from django.db import models

# Create your models here.


class Referrer(models.Model):
    code = models.CharField(max_length=32, unique=True)
    user = models.OneToOneField('users.User', on_delete=models.CASCADE, primary_key=True, related_name='referrer_data')
    created_at = models.DateTimeField(auto_now_add=True)
    deadline = models.DateTimeField()

    def __str__(self):
        return self.code


