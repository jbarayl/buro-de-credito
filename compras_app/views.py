#encoding:utf-8
from django.shortcuts import render_to_response, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext
from models import *
from forms import *
import datetime, time
from django.db.models import Q

from django.forms.formsets import formset_factory, BaseFormSet
from django.forms.models import inlineformset_factory

#Paginacion
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

# user autentication
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, AdminPasswordChangeForm
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required, permission_required

from django.db import connection

##########################################
## 										##
##               LOGIN     			    ##
##										##
##########################################

def ingresar(request):
	# if not request.user.is_anonymous():
	# 	return HttpResponseRedirect('/')
	if request.method == 'POST':
		formulario = AuthenticationForm(request.POST)
		if formulario.is_valid:
			usuario = request.POST['username']
			clave = request.POST['password']
			acceso = authenticate(username=usuario, password=clave)
			if acceso is not None:
				if acceso.is_active:
					login(request, acceso)
					return HttpResponseRedirect('/')
				else:
					return render_to_response('noactivo.html', context_instance=RequestContext(request))
			else:
				return render_to_response('login.html',{'form':formulario, 'message':'Nombre de usaurio o password no validos',}, context_instance=RequestContext(request))
	else:
		formulario = AuthenticationForm()
	return render_to_response('login.html',{'form':formulario, 'message':'',}, context_instance=RequestContext(request))

@login_required(login_url='/login/')
def logoutUser(request):
    logout(request)
    return HttpResponseRedirect('/')

@login_required(login_url='/login/')
def index(request):
	try: 
		filtro = request.GET['filtro']
	except:
		filtro = ''

	compras = Compra.objects.filter(
		Q(cliente__nombre__icontains=filtro)| Q(sucursal__nombre__icontains=filtro) | Q(estado=filtro)
		)
	c = {'compras':compras,'filtro':filtro,}
  	return render_to_response('index.html', c, context_instance=RequestContext(request))


##########################################
## 										##
##               COMPRAS  			    ##
##										##
##########################################

@login_required(login_url='/login/')
def compra_manageView(request, id = None, template_name='compras/compra.html'):
	if id:
		compra = get_object_or_404(Compra, pk=id)
	else:
		compra = Compra()

	if request.method == 'POST':
		Compra_form = CompraManageForm(request.POST, request.FILES, instance=compra)

		pagos_formset = PagosCompra_formset(PagoManageForm, extra=1, can_delete=True)
		pagosCompra_formset = pagos_formset(request.POST, request.FILES, instance=compra)
		
		if Compra_form.is_valid() and pagosCompra_formset.is_valid():
			compra_O = Compra_form.save(commit = False)

			total = compra_O.cantidad
			adeudo = compra_O.cantidad

			#GUARDA ARTICULOS DE INVENTARIO FISICO
			for pago_form in pagosCompra_formset:
				pago = pago_form.save(commit = False)
				
				if not pagosCompra_formset._should_delete_form(pago_form):
					adeudo -= pago.cantidad 

				#PARA CREAR UNO NUEVO
				if not pago.id:
					pago.Compra = compra_O
					pago.fecha = datetime.datetime.now()
			
			compra_O.adeudo = adeudo
			compra_O.save()
			pagosCompra_formset.save()
			return HttpResponseRedirect('/')
	else:
		Compra_form = CompraManageForm(instance=compra)
		pagos_formset = PagosCompra_formset(PagoManageForm, extra=1, can_delete=True)
		pagosCompra_formset = pagos_formset(instance=compra)
	c = {'compra_form': Compra_form, 'formset': pagosCompra_formset,}

	return render_to_response(template_name, c, context_instance=RequestContext(request))

@login_required(login_url='/login/')
def cliente_manageView(request, id = None, template_name='clientes/cliente.html'):
	if id:
		cliente = get_object_or_404(Cliente, pk=id)
	else:
		cliente = Cliente()

	if request.method == 'POST':
		Cliente_form = ClienteManageForm(request.POST, request.FILES, instance=cliente)

		if Cliente_form.is_valid():
			cliente_O = Cliente_form.save(commit = False)

			cliente_O.save()
			
			return HttpResponseRedirect('/')
	else:
		Cliente_form = ClienteManageForm(instance=cliente)
		
	c = {'cliente_form': Cliente_form, }

	return render_to_response(template_name, c, context_instance=RequestContext(request))

@login_required(login_url='/login/')
def clientes_View(request, template_name='clientes/clientes.html'):
	try: 
		filtro = request.GET['filtro']
	except:
		filtro = ''

	clientes = Cliente.objects.filter(nombre__icontains=filtro)
	c = {'clientes':clientes,'filtro':filtro,}
  	return render_to_response(template_name, c, context_instance=RequestContext(request))