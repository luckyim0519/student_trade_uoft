from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.db import models

class User(models.Model):
    username = models.CharField(max_length=30, null=False, blank=False)
    email = models.EmailField(max_length=50, unique=True, null=False, blank=False, primary_key=True)
    password=models.CharField(max_length=25, null=False, blank=False)

    def __str__(self):
        return self.username

    class Meta:
        db_table = 'user'
