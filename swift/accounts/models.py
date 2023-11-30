from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    course = models.CharField(max_length=100, null=True, blank=True)
    sex = models.CharField(max_length=100, null=True, blank=True)
    contact_details = models.IntegerField(null=True, blank=True)
    user_type = models.CharField(max_length=100, null=True, blank=True)
    is_verified = models.BooleanField(default=False)

    def __str__(self):
        return self.username
