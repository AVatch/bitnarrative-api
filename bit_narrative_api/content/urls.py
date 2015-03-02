from django.conf.urls import url

from rest_framework.urlpatterns import format_suffix_patterns

from content import views


# API endpoints
urlpatterns = format_suffix_patterns([
    url(r'^api/v1/content/$',
        views.ContentList.as_view(),
        name='content-list'),

    url(r'^api/v1/content/(?P<pk>[0-9]+)/$',
        views.ContentDetail.as_view(),
        name='content-detail'),

    url(r'^api/v1/content/(?P<pk>[0-9]+)/accounts/$',
        views.ContentDetail.as_view(),
        name='content-accounts'),

    url(r'^api/v1/content/(?P<pk>[0-9]+)/bits/$',
        views.ContentDetail.as_view(),
        name='content-bits'),

    url(r'^api/v1/content/(?P<pk>[0-9]+)/topbits/$',
        views.ContentDetail.as_view(),
        name='content-topbits'),
])
