from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
	url(r'', include('locations.urls', namespace="locations")),
  	url(r'', include('proverbs.urls', namespace="proverbs")),
        url(r'^$', 'proverbs.views.home', name='home'),
        url(r'^admin/', include(admin.site.urls)),
)
