from datetime import date
from django.db import models

class Studentc02(models.Model):
    email       = models.EmailField(max_length=100,default="")
    password    = models.CharField(max_length=100, default="")
    name        = models.CharField(max_length=100, default="")
    dob     	= models.DateField(default=date.today)
    active 		= models.BooleanField(default=True)
    score		= models.IntegerField(default=0)
    gender      = models.CharField(max_length=10, default="")
    photo       = models.BinaryField()
    date_created= models.DateField(default=date.today)

    def __str__(self):
        return self.email
