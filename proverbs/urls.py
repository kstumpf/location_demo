from django.conf.urls import patterns, url
from .views import prov_list, prov_detail, prov_create, prov_edit, home, master_create, all_json_countries

urlpatterns = patterns('',
	url(r'^home/$', home, name='home'),
    url(r'^prov_list/$', prov_list, name='prov_list'),
    url(r'^prov_detail/(?P<pk>\d+)/$', prov_detail, name='prov_detail'),
    url(r'^prov_create/$', prov_create, name='prov_create'),
    url(r'^prov_edit/(?P<pk>\d+)/$', prov_edit, name='prov_edit'),
    url(r'^master_create/$', master_create, name='master_create'),

    # This url is used by ajax to create the location's dependent drop down menu.
    url(r'^continent/(?P<continent>[^%20]*[-\w]+)/all_json_countries/$', all_json_countries, name='all_json_countries'),
)
