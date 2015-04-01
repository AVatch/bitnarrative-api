from rest_framework import generics
from rest_framework import authentication
from rest_framework import permissions

from topics.models import Topic
from topics.serializers import TopicSerializer
from community.serializers import CommunitySerializer


class TopicList(generics.ListCreateAPIView):
    """
    URL: /api/v1/topics/
    Methods: GET
    Returns: List all topic or add a new one
    """
    queryset = Topic.objects.all()
    serializer_class = TopicSerializer
    authentication_classes = (authentication.SessionAuthentication,
                              authentication.TokenAuthentication)
    permission_classes = (permissions.IsAuthenticated,)


class TopicDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    URL: /api/v1/topic/<pk>/
    Methods: GET, PUT, DELETE
    Returns: Handle topic object
    """
    queryset = Topic.objects.all()
    serializer_class = TopicSerializer
    authentication_classes = (authentication.SessionAuthentication,
                              authentication.TokenAuthentication)
    permission_classes = (permissions.IsAuthenticated, )


class TopicCommunities(generics.ListAPIView):
    """
    URL: /api/v1/topic/<pk>/communities/
    Methods: GET
    Returns: List of communities associated with the topic
    """
    serializer_class = CommunitySerializer
    authentication_classes = (authentication.SessionAuthentication,
                              authentication.TokenAuthentication)
    permission_classes = (permissions.IsAuthenticated, )

    def get_queryset(self):
        return Topic.community.all().order_by('-updated_at')
