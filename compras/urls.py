from django.conf.urls import patterns, include, url



import autocomplete_light
autocomplete_light.autodiscover()

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
	 url(r'', include('compras_app.urls', namespace='compras_app')),
    # Examples:
    # url(r'^$', 'compras.views.home', name='home'),
    # url(r'^compras/', include('compras.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'autocomplete/', include('autocomplete_light.urls')),
    url(r'^admin/', include(admin.site.urls)),
)
