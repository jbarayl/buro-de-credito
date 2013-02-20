#encoding:utf-8
from django import forms

import autocomplete_light

from models import *
from django.contrib.auth.models import User
from django.forms.models import BaseInlineFormSet, inlineformset_factory

from cities_light.models import City

class ClienteManageForm(forms.ModelForm):
	
	class Meta:
		widgets = autocomplete_light.get_widgets_dict(Cliente)
		model = Cliente

class ClientesBusquedaForm(forms.ModelForm):
	"""""
		Permite hacer busquedas de clientes basado en un conjunto de criterios
	"""""
	nombre 			= forms.CharField(required=False)
	dir_calle = forms.CharField(required=False)
	dir_no_exterior = forms.CharField(widget=forms.TextInput(attrs={'maxlength':'5','class':'span1'}),required=False)

	class Meta:
		widgets = autocomplete_light.get_widgets_dict(Cliente)
		model = Cliente
		exclude ={
			'dir_colonia',
			'dir_poblacion',
			'city',
			'edad',
			'ocupacion',
			'institucion',
			'rfc',
			'codigo_postal',
			'dir_no_interior',
			'dir_referencia',
		}
	
class CreditoForm(forms.ModelForm):
	"""""
		Permite hacer busquedas de de creditos basado en un conjunto de criterios
	"""""
	#fecha_limite = forms.CharField(widget=forms.TextInput(attrs={'maxlength':'10','class':'span2'}),required=False)
	class Meta:
		model = Credito
		exclude = {
			'monto_total',
			'cliente',
			'fecha',
			'empresa_otorga',
			'fecha_limite',
			'liquidado',
		}
	
class CreditoManageForm(forms.ModelForm):
	widgets = autocomplete_light.get_widgets_dict(Credito)
	fecha = forms.CharField(widget=forms.TextInput(attrs={'maxlength':'10','class':'span2'}))
	fecha_limite = forms.CharField(widget=forms.TextInput(attrs={'maxlength':'10','class':'span2'}))
	monto_total = forms.CharField(widget=forms.TextInput(attrs={'class':'span1'}))
	class Meta:
		model = Credito
		exclude = {
			'liquidado',
		}

class CiudadManageForm(forms.ModelForm):
	class Meta:
		model = City
		exclude = (
			'latitude',
			'longitude',
			'alternate_names',
			'geoname_id',
			'name_ascii',
			)