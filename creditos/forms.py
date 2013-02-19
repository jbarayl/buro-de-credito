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

class CompraManageForm(forms.ModelForm):
	class Meta:
		widgets = autocomplete_light.get_widgets_dict(Compra)
		model = Compra

class PagoManageForm(forms.ModelForm):
	class Meta:
		model = Pago
		readonly_fields = ['fecha',]

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


def PagosCompra_formset(form, formset = BaseInlineFormSet, **kwargs):
	return inlineformset_factory(Compra, Pago, form, formset, **kwargs)