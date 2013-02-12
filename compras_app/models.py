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
	edad = models.CharField(max_length=3)
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

class Compra(models.Model):
	cliente = models.ForeignKey(Cliente, on_delete=models.SET_NULL, blank=True, null=True)
	fecha = models.DateTimeField(default=datetime.now(),blank=True)
	fecha_limite = models.DateTimeField(default=datetime.now(), blank=True, null=True)
	sucursal = models.ForeignKey(Sucursal, on_delete=models.SET_NULL, blank=True, null=True)
	TIPO_PRESTAMO = (
		('T1', 'TIPO 1'),
		('T2', 'TIPO 2'),
		('O', 'OTRO'),
		)
	tipo_prestamo = models.CharField(max_length=10, choices=TIPO_PRESTAMO, default='O')
	descripcion = models.CharField(max_length=100,blank= True, null =True)
	cantidad = models.DecimalField(default=0, blank=True, null=True, max_digits=18, decimal_places=2)
	ESTADO_PRESTAMO = (
		('P', 'PENDIENTE'),
		('M1', 'MALO'),
		('M2', 'URGENTE'),
		)
	adeudo = models.DecimalField(default=0, blank=True, null=True, max_digits=18, decimal_places=2)
	estado = models.CharField(max_length=10, choices=ESTADO_PRESTAMO, default='P')

	def __unicode__(self):
		return u'%s| %s'%(self.id, self.cliente)

class Pago(models.Model):
	Compra = models.ForeignKey(Compra, on_delete=models.SET_NULL, blank=True, null=True)
	fecha = models.DateTimeField(default=datetime.now(),blank=True)
	cantidad = models.DecimalField(default=0, max_digits=18, decimal_places=2)
	descripcion = models.CharField(max_length=100,blank= True, null =True)
	sucursal = models.ForeignKey(Sucursal, on_delete=models.SET_NULL, blank=True, null=True)
	
	def __unicode__(self):
		return u'%s| %s'%(self.id, self.Compra.cliente)