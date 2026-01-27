from datetime import date
from django.db import models

# Create your models here.
class Students(models.Model):
    email       = models.EmailField(max_length=100,default="")
    password    = models.CharField(max_length=100, default="")
    firstname   = models.CharField(max_length=100, default="")
    lastname    = models.CharField(max_length=100, default="")
    dob     	= models.DateField(default=date.today)
    age 		= models.IntegerField(default=0)
    single		= models.BooleanField(default=True)
    photo		= models.BinaryField()
    date_created= models.DateField(default=date.today)

    def __str__(self):
        return self.email
