from django.db import models

# Create your models here.
class signupForm(models.Model):
    username = models.CharField(max_length=30, null=False, blank=False)
    email = models.EmailField(max_length=50, null=False, blank=False)
    password=models.CharField(max_length=25, null=False, blank=False)
