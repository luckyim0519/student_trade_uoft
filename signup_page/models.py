from django.db import models

# Create your models here.
class signupModel(models.Model):
    username = models.CharField(max_length=30, null=False, blank=False)
    email = models.EmailField(max_length=50, null=False, blank=False, primary_key=True)
    password=models.CharField(max_length=25, null=False, blank=False)

