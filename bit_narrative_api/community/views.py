# Create your views here.
from django.shortcuts import get_object_or_404

from rest_framework import generics
from rest_framework import authentication
from rest_framework import permissions

from community.models import Community
from community.serializers import CommunitySerializer
from bits.models import Bit
from bits.serializers import BitSerializer
from content.serializers import ContentSerializer
from content.models import Content


class CommunityList(generics.ListCreateAPIView):
    """
    URL: /api/v1/community/
    Methods: GET
    Returns: List all community or add a new one
    """
    queryset = Community.objects.all()
    serializer_class = CommunitySerializer
    authentication_classes = (authentication.SessionAuthentication,
                              authentication.TokenAuthentication)
    permission_classes = (permissions.IsAuthenticated,)


class CommunityDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    URL: /api/v1/community/<pk>/
    Methods: GET, PUT, DELETE
    Returns: Handle community object
    """
    queryset = Community.objects.all()
    serializer_class = CommunitySerializer
    authentication_classes = (authentication.SessionAuthentication,
                              authentication.TokenAuthentication)
    permission_classes = (permissions.IsAuthenticated, )


class CommunityContent(generics.ListAPIView):
    """
    URL: /api/v1/community/<pk>/content/
    Methods: GET
    Returns: List of content associated with the community ordered by most viewed
    """
    serializer_class = ContentSerializer
    authentication_classes = (authentication.SessionAuthentication,
                              authentication.TokenAuthentication)
    permission_classes = (permissions.IsAuthenticated, )

    def get_queryset(self):
        community = get_object_or_404(Community, pk=self.kwargs['pk'])
        return Content.objects.filter(community=community).order_by('-view_count')


class CommunityBits(generics.ListAPIView):
    """
    URL: /api/v1/community/<pk>/bits/
    Methods: GET
    Returns: List of bits associated with the community ordered by most viewed
    """
    serializer_class = BitSerializer
    authentication_classes = (authentication.SessionAuthentication,
                              authentication.TokenAuthentication)
    permission_classes = (permissions.IsAuthenticated, )

    def get_queryset(self):
        community = get_object_or_404(Community, pk=self.kwargs['pk'])
        return Bit.objects.filter(community=community).order_by('-view_count')


class CommunityTopBits(generics.ListAPIView):
    """
    URL: /api/v1/account/<pk>/topbits/
    Methods: GET
    Returns: Top three bits in the community
    """
    serializer_class = BitSerializer
    authentication_classes = (authentication.SessionAuthentication,
                              authentication.TokenAuthentication)
    permission_classes = (permissions.IsAuthenticated, )

    def get_queryset(self):
        community = get_object_or_404(Community, pk=self.kwargs['pk'])
        return Bit.objects.filter(community=community).order_by('-view_count')[:3]
