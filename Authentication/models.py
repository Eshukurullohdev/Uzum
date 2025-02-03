from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    phone_number = models.CharField(max_length=15, unique=True)

    class Meta:
        swappable = 'AUTH_USER_MODEL'
