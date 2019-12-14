from django.db import models
from django.shortcuts import render,get_object_or_404
# Create your models here.
class Student(models.Model):

    PRN = models.IntegerField(primary_key=True)
    first_name = models.CharField(max_length=50)
    last_name= models.CharField(max_length=50)
    mobile_no = models.CharField(max_length=50)
    email = models.CharField(max_length=50,unique=True)
    gender = models.CharField(max_length=50)
    address = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    course = models.CharField(max_length=50)
    branch = models.CharField(max_length=50)
    division = models.CharField(max_length=50)
    adm_cat = models.CharField(max_length=50)
    dob = models.CharField(max_length=50)
    password = models.CharField(max_length=20)
       




