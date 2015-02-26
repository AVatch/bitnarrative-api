from django.conf.urls import url

from rest_framework.urlpatterns import format_suffix_patterns

from bits import views


# API endpoints
urlpatterns = format_suffix_patterns([
    url(r'^api/v1/bits/$',
        views.BitList.as_view(),
        name='bit-list'),

    url(r'^api/v1/account/(?P<pk>[0-9]+)/bits/$',
        views.AccountBitList.as_view(),
        name='account-bit-list'),

    url(r'^api/v1/content/(?P<pk>[0-9]+)/bits/$',
        views.ContentBitList.as_view(),
        name='content-bit-list'),

    url(r'^api/v1/content/(?P<pk>[0-9]+)/topbits/$',
        views.ContentTopBitList.as_view(),
        name='content-topbit-list'),

    url(r'^api/v1/bits/(?P<pk>[0-9]+)/$',
        views.BitDetail.as_view(),
        name='bit-detail'),
])
