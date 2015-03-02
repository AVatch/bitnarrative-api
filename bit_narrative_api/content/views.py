from django.shortcuts import get_object_or_404

from rest_framework import generics
from rest_framework import authentication
from rest_framework import permissions

from content.models import Content
from content.serializers import ContentSerializer
from content.parsers import parse_content
from bits.models import Bit
from bits.serializers import BitSerializer


class ContentList(generics.ListCreateAPIView):
    """
    URL: /api/v1/content/
    Methods: GET, POST
    Returns: List all content or add a new one
    """
    queryset = Content.objects.all()
    serializer_class = ContentSerializer
    authentication_classes = (authentication.SessionAuthentication,
                              authentication.TokenAuthentication)
    permission_classes = (permissions.IsAuthenticated,)

    # Override create method to parse the content
    # -- ISSUE: There is an issue with saving 'date_published'
    def perform_create(self, serializer):
        if not self.request.data[u'domain']:
            # only sending the url, so parse the content
            parsed = parse_content(self.request.data[u'url'])
            serializer.save(domain=parsed['domain'],
                            url=parsed['url'],
                            title=parsed['title'],
                            excerpt=parsed['excerpt'],
                            content=parsed['content'],
                            lead_image_url=parsed['lead_image_url'],
                            word_count=parsed['word_count'],
                            view_count=1,
                            share_count=0, )
        else:
            serializer.save()


class ContentDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    URL: /api/v1/content/<pk>/
    Methods: GET, PUT, DELETE
    Returns: Handle content object
    """
    queryset = Content.objects.all()
    serializer_class = ContentSerializer
    authentication_classes = (authentication.SessionAuthentication,
                              authentication.TokenAuthentication)
    permission_classes = (permissions.IsAuthenticated, )


class ContentBits(generics.ListAPIView):
    """
    URL: /api/v1/content/<pk>/bits/
    Methods: GET
    Returns: List of bits associated with the content ordered by most viewed
    """
    serializer_class = BitSerializer
    authentication_classes = (authentication.SessionAuthentication,
                              authentication.TokenAuthentication)
    permission_classes = (permissions.IsAuthenticated, )

    def get_queryset(self):
        content = get_object_or_404(Content, pk=self.kwargs['pk'])
        return Bit.objects.filter(content=content).order_by('-view_count')


class ContentTopBits(generics.ListAPIView):
    """
    URL: /api/v1/account/<pk>/topbits/
    Methods: GET
    Returns: Top three bits in the content
    """
    serializer_class = BitSerializer
    authentication_classes = (authentication.SessionAuthentication,
                              authentication.TokenAuthentication)
    permission_classes = (permissions.IsAuthenticated, )

    def get_queryset(self):
        content = get_object_or_404(Content, pk=self.kwargs['pk'])
        return Bit.objects.filter(content=content).order_by('-view_count')[:3]
