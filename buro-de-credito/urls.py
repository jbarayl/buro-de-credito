from django.conf.urls import patterns, include, url



import autocomplete_light
autocomplete_light.autodiscover()

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
	 url(r'', include('creditos.urls', namespace='creditos')),
    # Examples:
    # url(r'^$', 'buro-de-credito.views.home', name='home'),
    # url(r'^buro-de-credito/', include('buro-de-credito.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'autocomplete/', include('autocomplete_light.urls')),
    url(r'^admin/', include(admin.site.urls)),
)
