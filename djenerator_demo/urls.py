from django.conf.urls import patterns, include, url
from django.contrib import admin

from django.conf import settings

admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', include('base.urls')),
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^accounts/', include('userena.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^organization/', include('organization.urls')),
    url(r'employee/', include('employee.urls')),
)

if settings.DEBUG:
    media_url = settings.MEDIA_URL.lstrip('/').rstrip('/')
    urlpatterns += patterns('',
        (r'^%s/(?P<path>.*)$' % media_url, 'django.views.static.serve',
             {'document_root': settings.MEDIA_ROOT}),
    )
