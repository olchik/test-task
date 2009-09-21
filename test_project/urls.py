from django.conf.urls.defaults import patterns, url, include
from django.contrib import admin

import settings

admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', 'person.views.process_root_request'),
    url(r'^profile/', include('person.urls')),
    url(r'^admin/(.*)', admin.site.root, name="admin"),
    url(r'^static/(.*)$', 'django.views.static.serve',
        {'document_root': settings.STATIC_ROOT}),
)
