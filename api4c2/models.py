from datetime import date
from django.db import models

class Student4c2(models.Model):
    email       = models.EmailField(max_length=100,default="")
    password    = models.CharField(max_length=100, default="")
    name        = models.CharField(max_length=100, default="")
    dob     	= models.DateField(default=date.today)
    active 		= models.BooleanField(default=True)
    score		= models.IntegerField(default=0)
    gender      = models.CharField(max_length=10, default="")
    status      = models.CharField(max_length=20, default="")
    session     = models.CharField(max_length=20, default="")
    hobbies     = models.CharField(max_length=100, default="")
    photo       = models.BinaryField()
    date_created= models.DateField(default=date.today)

    def __str__(self):
        return self.email
