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

class competition(models.Model):
    c_name = models.CharField(max_length=150,unique=True)
    c_date = models.DateField()
    last_date = models.DateField()
    c_type = models.CharField(max_length=150)
    num_round = models.IntegerField()
    venue = models.CharField(max_length=150)
    c_link = models.CharField(max_length=150)

class event(models.Model):
    e_name = models.CharField(max_length=150,unique=True)
    e_date = models.DateField()
    last_date = models.DateField()
    venue = models.CharField(max_length=150)
    e_link = models.CharField(max_length=150)
    e_speaker = models.CharField(max_length=150,unique=True)
    timing = models.IntegerField()