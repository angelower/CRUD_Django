from django.db import models

# Create your models here.

class Patient(models.Model):
    id = models.AutoField(primary_key=True)
    documento = models.TextField(max_length=20)
    nombre = models.TextField(max_length=100)
    edad = models.IntegerField()