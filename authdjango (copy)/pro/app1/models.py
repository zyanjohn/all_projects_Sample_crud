from django.db import models
# from django.contrib.auth.models import AbstractUser
# Create your models here.
class user(models.Model):
     username = models.CharField(max_length=25)
     password = models.CharField(max_length=15)
     email = models.EmailField()
