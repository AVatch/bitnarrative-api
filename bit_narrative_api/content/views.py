from django.shortcuts import get_object_or_404

from rest_framework import generics
from rest_framework import authentication
from rest_framework import permissions
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response

from content.models import Content
from content.serializers import ContentSerializer, ContentParserSerializer
from content.parsers import parse_content, strip_tags, parse_bits
from bits.models import Bit
from bits.serializers import BitSerializer


class ContentList(generics.ListAPIView):
    """
    URL: /api/v1/content/
    Methods: GET
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


class ContentParse(APIView):
    """
    URL: /api/v1/parse/content/
    Methods: POST
    Returns: parsed content meta data and array of bits
    """
    authentication_classes = (authentication.SessionAuthentication,
                              authentication.TokenAuthentication)
    permission_classes = (permissions.IsAuthenticated,)

    def post(self, request, format=None):
        serializer = ContentParserSerializer(data=request.data)
        if serializer.is_valid():
            # check to see if content exists, otherwise create it
            try:
                content = Content.objects.get(url=serializer.data['url'])
            except Exception:
                # object does not exist so create it
                # parse the content
                parsed = parse_content(self.request.data[u'url'])
                content = Content.objects.create(domain=parsed['domain'],
                                                 url=parsed['url'],
                                                 title=parsed['title'],
                                                 excerpt=parsed['excerpt'],
                                                 content=parsed['content'],
                                                 lead_image_url=parsed['lead_image_url'],
                                                 word_count=parsed['word_count'],
                                                 view_count=1,
                                                 share_count=0, )
                # break it down to bits
                content.content = strip_tags(content.content)
                bits_parsed = parse_bits(content.content)
                bits_response = []
                for i, bit in enumerate(bits_parsed):
                    b = Bit.objects.create(bit=bit,
                                           content_index=i,
                                           content=content)
                    b_r = {
                        "id": b.pk,
                        "bit": b.bit,
                        "content_index": b.content_index,
                        "view_count": b.view_count,
                        "share_count": b.share_count,
                        "up_count": b.up_count,
                        "down_count": b.down_count,
                        "created_at": b.created_at,
                        "updated_at": b.updated_at,
                    }
                    bits_response.append(b_r)

            response = {
                "content": {"id": content.pk,
                            "domain": content.domain,
                            "url": content.url,
                            "title": content.title,
                            "excerpt": content.excerpt,
                            "lead_image_url": content.lead_image_url,
                            "word_count": content.word_count,
                            "view_count": content.view_count,
                            "share_count": content.share_count
                            },
                "bits": bits_response
            }
            return Response(response, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors,
                            status=status.HTTP_400_BAD_REQUEST)
