from django.conf.urls import patterns, include, url
from .views import *
from django.conf import settings

urlpatterns = patterns('',
    #url(r'^story/$', Index.as_view(), name='index'),
    url(r'^$', MapView.as_view(), name='index'),
    url(r'^logout/$', 'logout', name='logout'),
    #url(r'^oauth_callback/$', InstagramAuth.as_view(), name='oauth_callback')
)

