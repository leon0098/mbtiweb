from django.conf.urls import patterns, include, url
from django.contrib import admin

from MBTIWeb.views import index


admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'MBTIWeb.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    ('^index/$', index),
)
