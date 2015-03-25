from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from bit_narrative_api import views

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),

    url(r'^api/v1/$', views.api_root),

    url(r'^', include('accounts.urls')),
    url(r'^', include('content.urls')),
    url(r'^', include('bits.urls')),
    url(r'^', include('community.urls')),
    url(r'^', include('topics.urls')),
)

urlpatterns += staticfiles_urlpatterns()
