from django.conf.urls.defaults import patterns, url
from person import views

urlpatterns = patterns('',
    url(r'^profile/$', views.edit_profile, name='edit_profile'),
)
