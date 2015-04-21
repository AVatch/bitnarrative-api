from django.conf.urls import url

from rest_framework.urlpatterns import format_suffix_patterns

from community import views


# API endpoints
urlpatterns = format_suffix_patterns([
    url(r'^api/v1/community/$',
        views.CommunityList.as_view(),
        name='community-list'),

    url(r'^api/v1/community/(?P<pk>[0-9]+)/$',
        views.CommunityDetail.as_view(),
        name='community-detail'),

    url(r'^api/v1/community/(?P<pk>[0-9]+)/content/$',
        views.CommunityContent.as_view(),
        name='community-content'),

    url(r'^api/v1/community/(?P<pk>[0-9]+)/bits/$',
        views.CommunityBits.as_view(),
        name='community-bits'),

    url(r'^api/v1/community/(?P<pk>[0-9]+)/topbits/$',
        views.CommunityTopBits.as_view(),
        name='community-topbits'),

    url(r'^api/v1/community/(?P<pk>[0-9]+)/join/$',
        views.CommunityJoin.as_view(),
        name='community-join'),

    url(r'^api/v1/community/(?P<pk>[0-9]+)/leave/$',
        views.CommunityLeave.as_view(),
        name='community-leave'),

    url(r'^api/v1/community/(?P<pk>[0-9]+)/accounts/$',
        views.CommunityAccounts.as_view(),
        name='community-accounts'),
])
