from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class patientdetails(models.Model):
    Date = models.DateField()
    Name = models.CharField(max_length=50)
    Age  = models.IntegerField()
    CHOICES =[
        ('male','male'),
        ('female','female')
    ]
    Gender = models.CharField(max_length=10,choices=CHOICES,null= False,blank=False)
    Address =models.TextField()
    Contactno = models.IntegerField()
    History = models.CharField(max_length=100)
    Pain = models.CharField(max_length=100)
    Duration =models.TimeField()