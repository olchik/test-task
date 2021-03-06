from django.conf.urls.defaults import patterns, url, include
from django.contrib import admin

from django.conf import settings

admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', 'person.views.process_root_request'),
    url(r'^', include('registration.urls')),
    url(r'^accounts/', include('person.urls')),
    url(r'^admin/(.*)', admin.site.root, name="admin"),
    url(r'^static/(.*)$', 'django.views.static.serve',
        {'document_root': settings.STATIC_ROOT}),
)
