from django.conf.urls.defaults import *

from california.views import *

urlpatterns = patterns('',
    url(r'^counties/$', counties, name='counties'),
    url(r'^places/$', places, name='places'),
)