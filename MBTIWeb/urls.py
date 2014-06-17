from django.conf.urls import patterns, include, url
from django.conf.urls.static import static
from django.contrib import admin
from django.views.generic.base import TemplateView

from MBTIWeb import settings
from MBTIWeb.views import index, question, jsonTest, startExam


admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'MBTIWeb.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    ('^index/$', index),
    (r'^exam/$', TemplateView.as_view(template_name="exam.html")),
    ('^question/$', question),
    ('^jsonTest/$', jsonTest),
    ('^startExam/$', startExam),
) + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
