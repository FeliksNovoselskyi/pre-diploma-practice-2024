from django.db import models

# Create your models here.
class Consultations(models.Model):
    name = models.CharField(max_length=255)
    price = models.CharField(max_length=255)