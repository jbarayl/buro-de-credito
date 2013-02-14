#encoding:utf-8
from django.db import models
from datetime import datetime 

# Create your models here.
class Sucursal(models.Model):
	nombre = models.CharField(max_length=40)
	#DIRECCION
	direccion = models.CharField(max_length=60)
	codigo_postal = models.CharField(max_length=5)
	telefono = models.CharField(max_length=10)

	def __unicode__(self):
		return self.nombre

class Cliente(models.Model):
	nombre = models.CharField(max_length=40)
	edad = models.CharField(default='', max_length=3)
	#DIRECCION
	city = models.ForeignKey('cities_light.city', null=True, blank=True)
	codigo_postal = models.CharField(max_length=5)
	#Domicilio
	dir_calle = models.CharField(max_length=100, blank=True, null=True)
	dir_no_exterior = models.CharField(max_length=10, blank=True, null=True)
	dir_no_interior = models.CharField(max_length=10, blank=True, null=True)
	dir_colonia = models.CharField(max_length=100)
	dir_poblacion = models.CharField(max_length=100)
	dir_referencia = models.CharField(max_length=100, blank=True, null=True)

	telefono = models.CharField(max_length=10)

	ocupacion = models.CharField(max_length=30)
	institucion = models.CharField(max_length=30)
	
	def __unicode__(self):
		return self.nombre