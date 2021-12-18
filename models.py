from django.db import models

# Create your models here.
class administrator(models.Model):
    username = models.CharField(max_length=150,unique=True)
    email = models.EmailField(max_length=200,unique=True)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    password = models.CharField(max_length=20)

class scholar(models.Model):
    username = models.CharField(max_length=150,unique=True)
    email = models.EmailField(max_length=200, unique=True)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    password = models.CharField(max_length=20)

class hackathon(models.Model):
    h_name = models.CharField(max_length=150,unique=True)
    h_date = models.DateField()
    last_date = models.DateField()
    venue = models.CharField(max_length=150)
    link = models.CharField(max_length=150)