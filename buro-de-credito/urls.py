from django.conf.urls import patterns, include, url



import autocomplete_light
autocomplete_light.autodiscover()

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
	 url(r'', include('creditos.urls', namespace='creditos')),
    url(r'autocomplete/', include('autocomplete_light.urls')),
    #url(r'^admin/', include(admin.site.urls)),
)
