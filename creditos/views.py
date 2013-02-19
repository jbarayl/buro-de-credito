#encoding:utf-8
from django.shortcuts import render_to_response, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext
#MODELOS Y FORMULARIOS DEL PROYECTO
from models import *
from forms import *
#MODELOS DE EL PROYECTO DE CITIES_LIGHT

from cities_light.models import City
from datetime import datetime, date

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

##########################################
## 										##
##               CLIENTE			    ##
##										##
##########################################

@login_required(login_url='/login/')
def cliente_manageView(request, id = None, template_name='clientes/cliente.html'):
	if id:
		cliente = get_object_or_404(Cliente, pk=id)
	else:
		cliente = Cliente()

	msg = '' 

	if request.method == 'POST':
		Cliente_form = ClienteManageForm(request.POST, request.FILES, instance=cliente)

		if Cliente_form.is_valid():
			cliente_O = Cliente_form.save(commit = False)
			clientesIguales = Cliente.objects.filter(city = cliente_O.city).filter(codigo_postal 	= 	cliente_O.codigo_postal).filter(dir_colonia		=	cliente_O.dir_colonia).filter(dir_calle		=	cliente_O.dir_calle).filter(dir_poblacion	=	cliente_O.dir_poblacion)

			if clientesIguales.count() > 1:
				msg = 'Ya existe otro cliente con la misma direccion porfavor revisa bien los datos!'
			else:
				if request.user.has_perm('creditos.change_cliente'):
					cliente_O.save()

				return HttpResponseRedirect('/clientes/')
			
			c = {'cliente_form': Cliente_form, 'msg':msg}
			return render_to_response(template_name, c, context_instance=RequestContext(request))
	else:
		if request.user.has_perm('creditos.add_cliente'):
			Cliente_form = ClienteManageForm(instance=cliente)
		else:
			return HttpResponseRedirect('/clientes/')
		
	c = {'cliente_form': Cliente_form, }

	return render_to_response(template_name, c, context_instance=RequestContext(request))


@login_required(login_url='/login/')
def clientesView(request, id = None, template_name='clientes/clientes.html'):
	
	clientesIguales = None
	msg = '' 
	if request.method == 'POST':
		Cliente_form = ClientesBusquedaForm(request.POST, request.FILES)

		if Cliente_form.is_valid():
			cliente_O = Cliente_form.save(commit = False)
			
			if cliente_O.nombre == '':
				cliente_O.nombre = '*'
			if cliente_O.dir_colonia == '':
				cliente_O.dir_colonia = '*'
			if cliente_O.dir_calle == '':
				cliente_O.dir_calle = '*'
			if cliente_O.codigo_postal == '':
				cliente_O.codigo_postal = '*'
			if cliente_O.dir_poblacion == '':
				cliente_O.dir_poblacion ='*'

			if cliente_O.city == None:
				#clientesIguales = Cliente.objects.filter(Q(nombre__icontains = cliente_O.nombre)|).filter(dir_colonia__icontains = cliente_O.dir_colonia).filter(dir_no_interior__icontains = cliente_O.dir_no_interior).filter(dir_no_exterior__icontains = cliente_O.dir_no_exterior).filter(codigo_postal__icontains = cliente_O.codigo_postal).filter(dir_calle__icontains = cliente_O.dir_calle)
				clientesIguales = Cliente.objects.filter(
					(Q(nombre__icontains = cliente_O.nombre) & Q(telefono__icontains = cliente_O.telefono))|
					Q(dir_colonia__icontains = cliente_O.dir_colonia)|
					Q(dir_colonia__icontains = cliente_O.dir_poblacion)|  
					(Q(dir_calle__icontains = cliente_O.dir_calle)& (Q(dir_no_interior__icontains = cliente_O.dir_no_interior)| Q(dir_no_exterior__icontains = cliente_O.dir_no_exterior)))|
					Q(codigo_postal__icontains = cliente_O.codigo_postal)
					)
			else:
				clientesIguales = Cliente.objects.filter(
					(Q(nombre__icontains = cliente_O.nombre) & Q(telefono__icontains = cliente_O.telefono))|
					Q(dir_colonia__icontains = cliente_O.dir_colonia)|  
					(Q(dir_calle__icontains = cliente_O.dir_calle)& (Q(dir_no_interior__icontains = cliente_O.dir_no_interior)| Q(dir_no_exterior__icontains = cliente_O.dir_no_exterior)))|
					Q(codigo_postal__icontains = cliente_O.codigo_postal)).filter(city = cliente_O.city)
					#Cliente.objects.filter(nombre__icontains = cliente_O.nombre).filter(dir_colonia__icontains = cliente_O.dir_colonia).filter(dir_no_interior__icontains = cliente_O.dir_no_interior).filter(dir_no_exterior__icontains = cliente_O.dir_no_exterior).filter(codigo_postal__icontains = cliente_O.codigo_postal).filter(dir_calle__icontains = cliente_O.dir_calle).filter(city = cliente_O.city)
			
			if clientesIguales.count() > 1:
				msg = 'Existe otro cliente con estos datos'

			
			c = {'cliente_form': Cliente_form, 'msg':msg, 'clientesIguales':clientesIguales,}
			return render_to_response(template_name, c, context_instance=RequestContext(request))
	else:
		clientesIguales = Cliente.objects.all()		
		Cliente_form = ClientesBusquedaForm()
	
	#clientesIguales = Cliente.objects.all()

	paginator = Paginator(clientesIguales, 20) # Muestra 5 inventarios por pagina
	page = request.GET.get('page')

	#####PARA PAGINACION##############
	try:
		clientes = paginator.page(page)
	except PageNotAnInteger:
	    # If page is not an integer, deliver first page.
	    clientes = paginator.page(1)
	except EmptyPage:
	    # If page is out of range (e.g. 9999), deliver last page of results.
	    clientes = paginator.page(paginator.num_pages)

	c = {'cliente_form':Cliente_form, 'clientesIguales':clientes,}
  	return render_to_response(template_name, c, context_instance=RequestContext(request))

@login_required(login_url='/login/')
def clientes_deleteView(request, id = None, template_name='clientes/clientes.html'):
	if request.user.has_perm('creditos.delete_cliente'):
		cliente = get_object_or_404(Cliente, pk=id)
		cliente.delete()

	return HttpResponseRedirect('/clientes/')

##########################################
## 										##
##               CIUDAD  			    ##
##										##
##########################################

@login_required(login_url='/login/')
def ciudad_manageView(request, id = None, template_name='ciudades/ciudad.html'):
	if id:
		ciudad = get_object_or_404(City, pk=id)
	else:
		ciudad = City()

	if request.method == 'POST':
		Ciudad_form = CiudadManageForm(request.POST, request.FILES, instance=ciudad)

		if Ciudad_form.is_valid():
			if request.user.has_perm('creditos.change_city'):
				Ciudad_form.save()
			
			return HttpResponseRedirect('/ciudades/')
	else:
		if request.user.has_perm('creditos.add_city'):
			Ciudad_form = CiudadManageForm(instance=ciudad)
		else:
			return HttpResponseRedirect('/ciudades/')

	c = {'ciudad_form': Ciudad_form, }

	return render_to_response(template_name, c, context_instance=RequestContext(request))

@login_required(login_url='/login/')
def ciudades_View(request, template_name='ciudades/ciudades.html'):
	try: 
		filtro = request.GET['filtro']
	except:
		filtro = ''
	ciudades_list = City.objects.filter(name__icontains=filtro).filter(country__name='Mexico')

	paginator = Paginator(ciudades_list, 20) # Muestra 5 inventarios por pagina
	page = request.GET.get('page')

	#####PARA PAGINACION##############
	try:
		ciudades = paginator.page(page)
	except PageNotAnInteger:
	    # If page is not an integer, deliver first page.
	    ciudades = paginator.page(1)
	except EmptyPage:
	    # If page is out of range (e.g. 9999), deliver last page of results.
	    ciudades = paginator.page(paginator.num_pages)

	c = {'ciudades':ciudades,'filtro':filtro,'msg':ciudades.count}
  	return render_to_response(template_name, c, context_instance=RequestContext(request))

def ajax_View(request, id=None):
	if id:
		compra = get_object_or_404(Compra, pk=id)
	else:
		compra = Compra()

 	if request.method == 'POST':
 		form = Compra_form = CompraManageForm(request.POST, request.FILES, instance=compra)
 		if form.is_valid():
 			cliente_nombre = form.cliente.nombre
 			return HttpResponse('Se lececciono el cliente :[%s]'% cliente_nombre, mimetype="text/plain") 
 		#else:
 		#	HttpResponse('ERROR!! NO SE Guardado correctamente')

##########################################
## 										##
##               CREDITO  			    ##
##										##
##########################################

@login_required(login_url='/login/')
def creditosView(request, id = None, template_name='creditos/creditos.html'):
	
	creditosIguales = None
	msg = '' 
	if request.method == 'POST':
		credito_form = CreditoForm(request.POST)
		Cliente_form = ClientesBusquedaForm(request.POST)

		if Cliente_form.is_valid() and credito_form.is_valid():
			cliente_O = Cliente_form.save(commit = False)
			credito_O = credito_form.save(commit = False)
			
			if cliente_O.rfc == '':
				cliente_O.rfc = '*'
			if cliente_O.nombre == '':
				cliente_O.nombre = '*'
			if cliente_O.dir_colonia == '':
				cliente_O.dir_colonia = '*'
			if cliente_O.dir_calle == '':
				cliente_O.dir_calle = '*'
			if cliente_O.codigo_postal == '':
				cliente_O.codigo_postal = '*'
			if cliente_O.dir_poblacion == '':
				cliente_O.dir_poblacion ='*'

			#if (credito_O.fecha_limite) == '':
			#	fecha_limite = '07/02/2013'
			if credito_O.empresa_otorga == None:
				empresa_otorga1 = 0
				empresa_otorga2 = 99999
			else:
				empresa_otorga1 = credito_O.empresa_otorga
				empresa_otorga2 = credito_O.empresa_otorga

			if cliente_O.city == None:
				creditosIguales = Credito.objects.filter(
					(Q(cliente__nombre__icontains 		= cliente_O.nombre) & Q(cliente__telefono__icontains = cliente_O.telefono))|
					Q(cliente__dir_colonia__icontains 	= cliente_O.dir_colonia)|
					Q(cliente__dir_colonia__icontains 	= cliente_O.dir_poblacion)|  
					(Q(cliente__dir_calle__icontains 	= cliente_O.dir_calle)& (Q(cliente__dir_no_interior__icontains = cliente_O.dir_no_interior)| Q(cliente__dir_no_exterior__icontains = cliente_O.dir_no_exterior)))|
					Q(cliente__codigo_postal__icontains = cliente_O.codigo_postal)|
					Q(empresa_otorga__gte 	= empresa_otorga1) & Q(empresa_otorga__lte = empresa_otorga2)|
					Q(cliente__rfc 						= cliente_O.rfc)
					).filter(liquidado = credito_O.liquidado)
					#.filter(fecha_limite__lte =  credito_O.fecha_limite)
			else:
				creditosIguales = Credito.objects.filter(
					(Q(cliente__nombre__icontains 		= cliente_O.nombre) & Q(cliente__telefono__icontains = cliente_O.telefono))|
					Q(cliente__dir_colonia__icontains 	= cliente_O.dir_colonia)|
					Q(cliente__dir_colonia__icontains 	= cliente_O.dir_poblacion)|  
					(Q(cliente__dir_calle__icontains 	= cliente_O.dir_calle)& (Q(cliente__dir_no_interior__icontains = cliente_O.dir_no_interior)| Q(cliente__dir_no_exterior__icontains = cliente_O.dir_no_exterior)))|
					Q(cliente__codigo_postal__icontains = cliente_O.codigo_postal)|
					(Q(empresa_otorga__gte 	= empresa_otorga1) & Q(empresa_otorga__lte = empresa_otorga2))|
					Q(cliente__rfc 						= cliente_O.rfc)
					).filter(cliente__city = cliente_O.city).filter(liquidado = credito_O.liquidado)
				#.filter(fecha_limite__lte =  credito_O.fecha_limite)
			
			if creditosIguales.count() > 1:
				msg = 'Existe otro cliente con estos datos'

	else:
		creditosIguales = Credito.objects.all()
		Cliente_form = ClientesBusquedaForm()
		credito_form = CreditoForm()
	
	creditosIguales = creditosIguales.order_by('fecha_limite')
	paginator = Paginator(creditosIguales, 20) # Muestra 20 
	page = request.GET.get('page')

	#####PARA PAGINACION##############
	try:
		creditos = paginator.page(page)
	except PageNotAnInteger:
	    # If page is not an integer, deliver first page.
	    creditos = paginator.page(1)
	except EmptyPage:
	    # If page is out of range (e.g. 9999), deliver last page of results.
	    creditos = paginator.page(paginator.num_pages)

	creditosData = []
	for credito in creditos:
		fecha_limite = date(credito.fecha_limite.year, credito.fecha_limite.month, credito.fecha_limite.day)
		creditosData.append ({
			'id':credito.id,
        	'cliente_nombre'	: credito.cliente.nombre,
         	'cliente_telefono'	: credito.cliente.telefono,
         	'cliente_city'		: credito.cliente.city,
         	'cliente_localidad'	: '%s, %s'% (credito.cliente.dir_colonia, credito.cliente.dir_poblacion),
         	'cliente_calle'		: '%s, %s %s'% (credito.cliente.dir_calle, credito.cliente.dir_no_interior, credito.cliente.dir_no_exterior),
         	'fecha_limite'				: credito.fecha_limite,
         	'dias_atraso'		: str(datetime.now().toordinal() - fecha_limite.toordinal()),                  
         	'cantidad'			: credito.monto_total,
                 })

	c = {'cliente_form':Cliente_form, 'creditos':creditosData, 'creditos_form':credito_form, 'msg':'', }
  	return render_to_response(template_name, c, context_instance=RequestContext(request))

@login_required(login_url='/login/')
def credito_manageView(request, id = None, template_name='creditos/credito.html'):
	if id:
		credito = get_object_or_404(Credito, pk=id)
	else:
		credito = Credito()

	msg = '' 

	if request.method == 'POST':
		Credito_form = CreditoManageForm(request.POST, instance=credito)

		if Credito_form.is_valid():
			Credito_form.save()
			return HttpResponseRedirect('/creditos/')
	else:
		if request.user.has_perm('creditos.add_credito'):
			Credito_form = CreditoManageForm(instance=credito)
		else:
			return HttpResponseRedirect('/creditos/')
		
	c = {'credito_form': Credito_form, }

	return render_to_response(template_name, c, context_instance=RequestContext(request))