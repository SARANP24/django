from django.db import models

# Create your models here.

class signupp(models.Model):

    username = models.CharField(max_length=50,unique=True)
    Email = models.EmailField(unique=True)
    Mobile = models.BigIntegerField(unique=True)
    password = models.CharField(max_length=40)

    