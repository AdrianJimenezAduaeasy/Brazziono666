from django.db import models

# Create your models here.

class usuario(models.Model):
    nombre = models.CharField(max_length=200)
    apellidos = models.CharField(max_length=200)
    correo = models.CharField(max_length=200)
    password = models.CharField(max_length=200)
    numTel = models.CharField(max_length=200)
    created_at = models.DateField(auto_now_add=True)