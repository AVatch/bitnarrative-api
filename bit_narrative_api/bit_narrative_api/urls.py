from django.conf.urls import patterns, include, url
from django.contrib import admin

from bit_narrative_api import views

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),

    url(r'^api/v1/$', views.api_root),

    url(r'^', include('accounts.urls')),
    url(r'^', include('content.urls')),
    url(r'^', include('bits.urls')),
)
