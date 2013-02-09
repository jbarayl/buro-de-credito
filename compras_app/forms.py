#encoding:utf-8
from django import forms

import autocomplete_light

from models import *
from django.contrib.auth.models import User
from django.forms.models import BaseInlineFormSet, inlineformset_factory
     
class ClienteManageForm(forms.ModelForm):
	class Meta:
		model = Cliente

class CompraManageForm(forms.ModelForm):
	class Meta:
		model = Compra

class PagoManageForm(forms.ModelForm):
	class Meta:
		model = Pago
		readonly_fields = ['fecha',]

		
def PagosCompra_formset(form, formset = BaseInlineFormSet, **kwargs):
	return inlineformset_factory(Compra, Pago, form, formset, **kwargs)