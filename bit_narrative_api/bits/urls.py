from django.conf.urls import url

from rest_framework.urlpatterns import format_suffix_patterns

from bits import views


# API endpoints
urlpatterns = format_suffix_patterns([
    url(r'^api/v1/bits/$',
        views.BitList.as_view(),
        name='bit-list'),

    url(r'^api/v1/bit/(?P<pk>[0-9]+)/$',
        views.BitDetail.as_view(),
        name='bit-detail'),

    url(r'^api/v1/bit/(?P<pk>[0-9]+)/accounts/$',
        views.BitAccounts.as_view(),
        name='bit-accounts'),
])
