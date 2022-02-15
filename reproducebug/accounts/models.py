from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    pass


class Test(models.Model):
    members = models.ManyToManyField(settings.AUTH_USER_MODEL)
