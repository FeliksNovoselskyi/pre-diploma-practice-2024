from django.db import models

# Create your models here.
class Consultations(models.Model):
    name = models.CharField(max_length=255)
    price = models.CharField(max_length=255)

class Service1(models.Model):
    name = models.CharField(max_length=255)
    price = models.CharField(max_length=255)

class Service2(models.Model):
    name = models.CharField(max_length=255)
    price = models.CharField(max_length=255)

class Service3(models.Model):
    name = models.CharField(max_length=255)
    price = models.CharField(max_length=255)