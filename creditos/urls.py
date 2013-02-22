from django.conf.urls import patterns, url
from django.views import generic
from creditos import views

urlpatterns = patterns('',
	(r'^$', views.creditosView),
    #LOGIN
    url(r'^login/$',views.ingresar),
    url(r'^logout/$', views.logoutUser),
    #clientes
    (r'^clientes/$', views.clientesView),
    (r'^cliente/$', views.cliente_manageView),
    (r'^cliente/(?P<id>\d+)/', views.cliente_manageView),
    (r'^cliente/delete/(?P<id>\d+)/', views.clientes_deleteView),
    #Ciudades
    (r'^ciudades/$', views.ciudades_View),
    (r'^ciudad/$', views.ciudad_manageView),
    (r'^ciudad/(?P<id>\d+)/', views.ciudad_manageView),
    (r'^ciudad/delete/(?P<id>\d+)/', views.ciudad_deleteView),
    #(r'^ajax/$', views.ajax_View),
    #Creditos
    (r'^creditos/$', views.creditosView),
    (r'^credito/$', views.credito_manageView),
    (r'^credito/(?P<id>\d+)/', views.credito_manageView),
    (r'^credito/delete/(?P<id>\d+)/', views.credito_deleteView),
    (r'^creditos/Reporte/$', views.creditos_reporteView),
    #(r'^error/$', views.problema_View),
)