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
	dir_colonia 	= forms.CharField(required=False)
	dir_no_exterior = forms.CharField(widget=forms.TextInput(attrs={'maxlength':'5','class':'span1'}),required=False)
	dir_no_interior = forms.CharField(widget=forms.TextInput(attrs={'maxlength':'5','class':'span1'}),required=False)
	codigo_postal 	= forms.CharField(widget=forms.TextInput(attrs={'maxlength':'5','class':'span1'}),required=False)
	telefono 		= forms.CharField(widget=forms.TextInput(attrs={'maxlength':'10'}), required=False)
	dir_poblacion 	= forms.CharField(required=False)

	class Meta:
		widgets = autocomplete_light.get_widgets_dict(Cliente)
		model = Cliente
		exclude ={
			'edad',
			'ocupacion',
			'institucion',

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