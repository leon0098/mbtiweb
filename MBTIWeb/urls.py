from django.conf.urls import patterns, include, url
from django.conf.urls.static import static
from django.contrib import admin
from django.views.generic.base import TemplateView

from MBTIWeb import settings
from MBTIWeb.views import index, question, startExam, saveAnswer, report


admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'MBTIWeb.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^redactor/', include('redactor.urls')),
    url(r'^admin/', include(admin.site.urls)),
    ('^index/$', index),
    (r'^exam/$', TemplateView.as_view(template_name="exam.html")),
    ('^question/$', question),
    ('^startExam/$', startExam),
    ('^saveAnswer/$', saveAnswer),
    ('^report/$', report),
) + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
#+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
