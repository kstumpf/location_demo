from django.conf.urls import patterns, url
from .views import loc_list, loc_detail, loc_create, loc_edit, loc_root, loc_children

urlpatterns = patterns('',
                       url(r'^loc_list/$', loc_list, name='loc_list'),
                       url(r'^loc_root/(?P<pk>\d+)/$', loc_detail, name='loc_root'),
                       url(r'^loc_root/$', loc_root, name='loc_root'),
                       url(r'^loc_detail/(?P<pk>\d+)/$', loc_detail, name='loc_detail'),
                       url(r'^loc_create/$', loc_create, name='loc_create'),
                       url(r'^loc_edit/(?P<pk>\d+)/$', loc_edit, name='loc_edit'),
                       url(r'^loc_children/(?P<pk>\d+)/$', loc_children, name='loc_children'),
)
