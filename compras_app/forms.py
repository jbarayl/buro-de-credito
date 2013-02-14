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