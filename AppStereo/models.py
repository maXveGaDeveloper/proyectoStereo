from django.db import models

# Create your models here.
class Musicos(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    edad = models.IntegerField()
    instrumento = models.CharField(max_length=50)
    banda = models.CharField(max_length=50)

class Instrumentos(models.Model):
    nombre = models.CharField(max_length=50)
    modelo = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=50)

class albums(models.Model):
    nombre = models.CharField(max_length=50)
    artista = models.CharField(max_length=50)
    fecha_lanzamiento = models.DateField()
    genero = models.CharField(max_length=50)
     