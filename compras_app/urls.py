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
)