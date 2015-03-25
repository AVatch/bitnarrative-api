from django.conf.urls import url

from rest_framework.urlpatterns import format_suffix_patterns

from topics import views


# API endpoints
urlpatterns = format_suffix_patterns([
    url(r'^api/v1/topics/$',
        views.TopicList.as_view(),
        name='topic-list'),

    url(r'^api/v1/topic/(?P<pk>[0-9]+)/$',
        views.TopicDetail.as_view(),
        name='topic-detail'),

    url(r'^api/v1/topic/(?P<pk>[0-9]+)/communities/$',
        views.TopicCommunities.as_view(),
        name='topic-communities'),
])
