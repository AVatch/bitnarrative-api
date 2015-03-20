from rest_framework import serializers

from content.models import Content


class ContentSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Content
        fields = ('id', 'domain', 'url',
                  'title', 'excerpt', 'content',
                  'lead_image_url', 'date_published',
                  'word_count', 'view_count', 'share_count',
                  'created_at', )


class ContentParserSerializer(serializers.Serializer):
    url = serializers.URLField()
