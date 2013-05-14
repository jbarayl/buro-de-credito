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
##              USUARIOS  			    ##
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
					return HttpResponseRedirect('/creditos/')
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


def usuarios_View(request, template_name='usuarios/usuarios.html'):
	if not request.user.is_staff:
		return HttpResponseRedirect('/creditos/')
		
	usuarios = User.objects.all()
	
	paginator = Paginator(usuarios, 20) # Muestra 5 inventarios por pagina
	page = request.GET.get('page')

	#####PARA PAGINACION##############
	try:
		usuarios = paginator.page(page)
	except PageNotAnInteger:
	    # If page is not an integer, deliver first page.
	    usuarios = paginator.page(1)
	except EmptyPage:
	    # If page is out of range (e.g. 9999), deliver last page of results.
	    usuarios = paginator.page(paginator.num_pages)

	c = {'usuarios':usuarios,}
	return render_to_response(template_name, c, context_instance=RequestContext(request))

def usuario_manageView(request, id=None, template_name='usuarios/usuario.html'):
	nuevousuario = False
	if id:
		usuario = get_object_or_404(User, pk=id)
	else:
		nuevousuario = True
		usuario = User()
	
	if request.method == 'POST':
		if nuevousuario:
			usuario_form =RegisterForm(request.POST, request.FILES, instance=usuario)
		else:			
			usuario_form =UsarioChangeForm(request.POST, request.FILES, instance=usuario)

		if usuario_form.is_valid():
			if request.user.has_perm('creditos.change_user'):
				usuario_form.save()
			return HttpResponseRedirect('/usuarios/')
	else:
		if nuevousuario:
			if request.user.has_perm('creditos.add_user'):
				usuario_form = RegisterForm(instance= usuario)
			else:	
				return HttpResponseRedirect('/usuarios/')
		else:
			if request.user.has_perm('creditos.change_user'):
				usuario_form =UsarioChangeForm(instance=usuario)
			else:	
				return HttpResponseRedirect('/usuarios/')	

	c = {'usuario_form':usuario_form,}
	return render_to_response(template_name, c, context_instance=RequestContext(request))

@login_required(login_url='/login/')
def usuario_deleteView(request, id = None):
	#para crear un superusuario
	# user = get_object_or_404(User, username='bccomercial')
	# user.is_staff = True
	# user.save()

	if request.user.has_perm('creditos.delete_user'):
		usuario = get_object_or_404(User, pk=id)
		if not usuario.username == 'bccomercial':
			usuario.delete()

	return HttpResponseRedirect('/usuarios/')

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
	if not request.user.is_staff:
		return HttpResponseRedirect('/creditos/')

	clientesIguales = None
	msg = '' 
	if request.method == 'POST':
		Cliente_form = ClientesBusquedaForm(request.POST, request.FILES)

		if Cliente_form.is_valid():
			cliente_O = Cliente_form.save(commit = False)
			
			if cliente_O.dir_calle == '':
				cliente_O.dir_calle = '*'
			if cliente_O.nombre == '':
				cliente_O.nombre = '*'
			if cliente_O.dir_no_exterior == '':
				cliente_O.dir_no_exterior = '*'
				
			clientesIguales = Cliente.objects.filter(
					Q(nombre__icontains 		= cliente_O.nombre) |
					(Q(dir_calle__icontains 	= cliente_O.dir_calle) &  Q(dir_no_exterior__icontains = cliente_O.dir_no_exterior))
					)
	else:
		clientesIguales = Cliente.objects.all()		
		Cliente_form = ClientesBusquedaForm()

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
	if not request.user.is_staff:
		return HttpResponseRedirect('/creditos/')

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

@login_required(login_url='/login/')
def ciudad_deleteView(request, id = None, template_name='ciudades/ciudades.html'):
	if request.user.has_perm('creditos.delete_ciudad'):
		ciudad = get_object_or_404(City, pk=id)
		ciudad.delete()

	return HttpResponseRedirect('/ciudades/')

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
		Cliente_form = ClientesBusquedaForm(request.POST)

		if Cliente_form.is_valid():
			cliente_O = Cliente_form.save(commit = False)

			if cliente_O.dir_calle == '':
				cliente_O.dir_calle = '*'
			if cliente_O.nombre == '':
				cliente_O.nombre = '*'
			if cliente_O.dir_no_exterior == '':
				cliente_O.dir_no_exterior = '*'
				
			creditosIguales = Credito.objects.filter(
					Q(cliente__nombre__icontains 		= cliente_O.nombre) |
					(Q(cliente__dir_calle__icontains 	= cliente_O.dir_calle) &  Q(cliente__dir_no_exterior__icontains = cliente_O.dir_no_exterior))
					).order_by('fecha_limite')
	else:
		creditosIguales = Credito.objects.filter(cliente__nombre__icontains = '*'). filter(cliente__dir_calle__icontains = '*').filter(cliente__dir_no_exterior__icontains = '*').order_by('fecha_limite')

		Cliente_form = ClientesBusquedaForm()

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
		dias_atraso = datetime.now().toordinal() - fecha_limite.toordinal()
		
		if dias_atraso < 0:
			dias_atraso = 0

		creditosData.append ({
			'id':credito.id,
        	'cliente_nombre'	: credito.cliente.nombre,
         	'cliente_city'		: u'%s (%s)'% (credito.cliente.city, credito.cliente.dir_colonia),
         	'cliente_calle'		: '%s, # %s %s'% (credito.cliente.dir_calle, credito.cliente.dir_no_interior, credito.cliente.dir_no_exterior),
         	'cliente_empresa_otorga'	: credito.empresa_otorga,
         	'fecha_limite'				: credito.fecha_limite,
         	'dias_atraso'		: dias_atraso,                  
         	'cantidad'			: credito.monto_total,
         	'liquidado'			: credito.liquidado,
                 })
	
	c = {'cliente_form':Cliente_form, 'creditos':creditosData,  'msg':msg, }
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

		if Credito_form.is_valid() and request.user.has_perm('creditos.edit_credito'):
			Credito_form.save()

			return HttpResponseRedirect('/creditos/')
	else:
		if request.user.has_perm('creditos.add_credito'):
				Credito_form = CreditoManageForm(instance=credito)
		else:
			return HttpResponseRedirect('/creditos/')
		
	c = {'credito_form': Credito_form,}

	return render_to_response(template_name, c, context_instance=RequestContext(request))

@login_required(login_url='/login/')
def credito_deleteView(request, id = None, template_name='creditos/creditos.html'):
	if request.user.has_perm('creditos.delete_credito'):
		credito = get_object_or_404(Credito, pk=id)
		credito.delete()

	return HttpResponseRedirect('/creditos/')

@login_required(login_url='/login/')
def creditos_reporteView(request, template_name='creditos/reporte_creditos.html'):
	creditos = Credito.objects.all()
	creditosData = []
	for credito in creditos:
		fecha_limite = date(credito.fecha_limite.year, credito.fecha_limite.month, credito.fecha_limite.day)
		dias_atraso = datetime.now().toordinal() - fecha_limite.toordinal()
		
		if dias_atraso < 0:
			dias_atraso = 0

		creditosData.append ({
			'id':credito.id,
        	'cliente_nombre'	: credito.cliente.nombre,
         	'cliente_city'		: u'%s (%s)'% (credito.cliente.city, credito.cliente.dir_colonia),
         	'cliente_calle'		: '%s, # %s %s'% (credito.cliente.dir_calle, credito.cliente.dir_no_interior, credito.cliente.dir_no_exterior),
         	'cliente_empresa_otorga'	: credito.empresa_otorga,
         	'fecha_limite'				: credito.fecha_limite,
         	'dias_atraso'		: dias_atraso,                  
         	'cantidad'			: credito.monto_total,
                 })

	c = {'creditos':creditosData,}
	return render_to_response(template_name, c, context_instance=RequestContext(request))

@login_required(login_url='/login/')
def creditoscliente_reporteView(request, id=None, template_name='creditos/reporte_creditos_cliente.html'):
	creditos = Credito.objects.filter(cliente__id = id)
	creditosData = []
	for credito in creditos:
		fecha_limite = date(credito.fecha_limite.year, credito.fecha_limite.month, credito.fecha_limite.day)
		dias_atraso = datetime.now().toordinal() - fecha_limite.toordinal()
		
		if dias_atraso < 0:
			dias_atraso = 0

		creditosData.append ({
			'id':credito.id,
        	'cliente_nombre'	: credito.cliente.nombre,
         	'cliente_city'		: u'%s (%s)'% (credito.cliente.city, credito.cliente.dir_colonia),
         	'cliente_calle'		: '%s, # %s %s'% (credito.cliente.dir_calle, credito.cliente.dir_no_interior, credito.cliente.dir_no_exterior),
         	'cliente_empresa_otorga'	: credito.empresa_otorga,
         	'fecha_limite'				: credito.fecha_limite,
         	'dias_atraso'		: dias_atraso,                  
         	'cantidad'			: credito.monto_total,
                 })

	cliente = None
	if creditosData !=  []:
		cliente = creditos[0].cliente

	c = {'creditos':creditosData,'cliente':cliente}
	return render_to_response(template_name, c , context_instance=RequestContext(request))

def index_View(request, template_name='index.html'):

	return render_to_response(template_name, {}, context_instance=RequestContext(request))
