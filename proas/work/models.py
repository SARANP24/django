from django.db import models


# Create your models here.

class emailu(models.Model):
    subject = models.CharField(max_length=200)
    message = models.TextField()
    fromaddress = models.EmailField()
    toaddress = models.TextField()
    


