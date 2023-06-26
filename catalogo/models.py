from django.db import models
from django.urls import reverse

class Peliculas(models.Model):
    nombre=models.CharField(max_length=25)
    resumen=models.TextField(max_length=400)

    def __str__(self):
        return self.nombre

class Director(models.Model):
    nombre=models.CharField(max_length=40)
    apellidos=models.CharField(max_length=40)
    peliculas=models.ManyToManyField('Peliculas')
    def __str__(self):
        return self.nombre + " " + self.apellidos



















# Create your models here.
# class Directores(models.Model):
#     name = models.CharField(max_length=64, help_text="pon el nombre del director")
#
#
#     def __str__(self):
#         return self.name
#
# class Pelicula(models.Model):
#     titulo = models.CharField(max_length=32)
#     descripcion = models.TextField(max_length=500, help_text="pon la descripcion de la pelicula")
#     directores = models.ManyToManyField(Directores)
#     def __str__(self):
#         return self.titulo






