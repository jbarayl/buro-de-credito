#encoding:utf-8
from django import forms

import autocomplete_light

from models import *
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, AuthenticationForm, AdminPasswordChangeForm
from django.forms.models import BaseInlineFormSet, inlineformset_factory


from cities_light.models import City, Country, Region
from django.utils.formats import get_format
my_formats = get_format('DATETIME_INPUT_FORMATS')


class ClienteManageForm(forms.ModelForm):
	
	class Meta:
		widgets = autocomplete_light.get_widgets_dict(Cliente)
		model = Cliente

class RegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ("username", "is_staff", )

class UsarioChangeForm(forms.ModelForm):
    username = forms.RegexField(label="Nombre de Usuario", max_length=30, regex=r'^[\w.@+-]+$',
        help_text = "Maximo. 30 caracteres. letras, digitos y @/./+/-/_ solamente.",
        error_messages = {'invalid': "Este campo solo puede contener letras, numeros y caracteres '@/./+/-/_' "})
    new_password1 = forms.CharField(label="Nueva contraseña", widget=forms.PasswordInput, required=False)
    new_password2 = forms.CharField(label="Confirma Nueva Contraseña", widget=forms.PasswordInput, required=False)

    class Meta(UserChangeForm):
        model = User
        exclude = ('password', 'last_login', 'date_joined','last_name','first_name','email','is_superuser','groups','user_permissions','is_active',)

    def clean_new_password2(self):
        password1 = self.cleaned_data.get('new_password1')
        password2 = self.cleaned_data.get('new_password2')

        if password1 != password2:
            raise forms.ValidationError("Las contraseñas no coinciden")
        #else:
         #   if len(password2) > 0 and len(password2) < 8:
          #      raise forms.ValidationError("Your password must be a minimum of 8 characters.")
        return password2

    def save(self, commit=True):
        user = super(UsarioChangeForm, self).save(commit=False)
        if len(self.cleaned_data['new_password2']) > 0:
            user.set_password(self.cleaned_data['new_password2'])
        if commit:
        	if user.is_staff:
        		user.is_superuser = True
        		
        	if user.username == 'bccomercial':
        		user.is_staff = True
        		user.is_superuser = True

        	user.save()
        return user

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
			'empresa',
		}
	
class CreditoManageForm(forms.ModelForm):
	#widgets = autocomplete_light.get_widgets_dict(Credito)
	fecha = forms.DateField(widget=forms.DateInput(attrs={'maxlength':'10','class':'span2'}))
	fecha_limite = forms.DateField(widget=forms.DateInput(attrs={'maxlength':'10','class':'span2'}))
	fecha_liquidacion = forms.DateField(widget=forms.DateInput(attrs={'maxlength':'10','class':'span2'}),required=False)
	monto_total = forms.CharField(widget=forms.TextInput(attrs={'class':'span1'}))
	monto_liquidado = forms.CharField(widget=forms.TextInput(attrs={'class':'span1'}))
	class Meta:
		model = Credito
		
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

class PaisManageForm(forms.ModelForm):
	class Meta:
		model = Country
		exclude = (
			'latitude',
			'code2',
			'code3',
			'tld',
			'longitude',
			'alternate_names',
			'geoname_id',
			'name_ascii',
			)
class EstadoManageForm(forms.ModelForm):
	class Meta:
		model = Region
		exclude = (
			'latitude',
			'longitude',
			'alternate_names',
			'geoname_id',
			'name_ascii',
			)