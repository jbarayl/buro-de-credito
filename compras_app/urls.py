from django.conf.urls import patterns, url
from django.views import generic
from compras_app import views

urlpatterns = patterns('',
	(r'^$', views.index),
    #LOGIN
    url(r'^login/$',views.ingresar),
    url(r'^logout/$', views.logoutUser),
    #COMPRAS
    (r'^compra/$', views.compra_manageView),
    (r'^compra/(?P<id>\d+)/', views.compra_manageView),
    #clientes
    (r'^clientes/$', views.clientes_View),
    (r'^cliente/$', views.cliente_manageView),
    (r'^cliente/(?P<id>\d+)/', views.cliente_manageView),
    (r'^cliente/delete/(?P<id>\d+)/', views.clientes_deleteView),
    #Ciudades
    (r'^ciudades/$', views.ciudades_View),
    (r'^ciudad/$', views.ciudad_manageView),
    (r'^ciudad/(?P<id>\d+)/', views.ciudad_manageView),

)