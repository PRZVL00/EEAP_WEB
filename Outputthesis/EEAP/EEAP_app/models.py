from pyexpat import model
from django.db import models

from django.contrib.auth.models import AbstractUser

# Create your models here.

# class accounts(AbstractUser):
#     id = models.AutoField(primary_key = True, unique = True)
#     fname = models.CharField(max_length = 20)
#     lname = models.CharField(max_length = 20)
#     birthday = models.DateField(max_length = 30)
#     idnumber = models.CharField(max_length = 12, unique = True)
#     gsfe = models.EmailField(max_length = 30)


class student(models.Model):
    id = models.AutoField(primary_key=True, unique=True)
    fname = models.CharField(max_length=20)
    lname = models.CharField(max_length=20)
    birthday = models.DateField()
    idnumber = models.CharField(max_length=12)
    gsfe = models.EmailField(max_length=20)
    Timein = models.TimeField()
    Timeout = models.TimeField()
    withvehicle = models.CharField(max_length=5)

    # try


class registered_vehicles(models.Model):
    id = models.AutoField(primary_key=True, unique=True)
    fname = models.CharField(max_length=20)
    lname = models.CharField(max_length=20)
    idnumber = models.CharField(max_length=12)
    platenumber = models.CharField(max_length=10)
    vehiclemodel = models.CharField(max_length=12)
    imageF = models.ImageField(upload_to="imageF/")
    imageL = models.ImageField(upload_to="imageL/")
    imageR = models.ImageField(upload_to="imageR/")
    imageB = models.ImageField(upload_to="imageB/")
    ORCR = models.ImageField(upload_to="ORCR/")
    status = models.CharField(max_length=20)
