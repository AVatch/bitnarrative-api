from rest_framework import generics
from rest_framework import authentication
from rest_framework import permissions

from content.models import Content
from content.serializers import ContentSerializer
from content.parsers import parse_content


class ContentList(generics.ListCreateAPIView):
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
    queryset = Content.objects.all()
    serializer_class = ContentSerializer
    authentication_classes = (authentication.SessionAuthentication,
                              authentication.TokenAuthentication)
    permission_classes = (permissions.IsAuthenticated, )
