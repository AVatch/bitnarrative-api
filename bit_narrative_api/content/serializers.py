from rest_framework import serializers

from content.models import Content
from bits.serializers import BitSerializer


class ContentSerializer(serializers.HyperlinkedModelSerializer):
    # bits = serializers.HyperlinkedRelatedField(many=True,
    #                                            view_name='bit-detail',
    #                                            read_only=True)
    bits = BitSerializer(many=True, read_only=True)

    class Meta:
        model = Content
        fields = ('id', 'domain', 'url',
                  'title', 'excerpt', 'content', 'bits',
                  'lead_image_url', 'date_published',
                  'word_count', 'view_count', 'share_count',
                  'created_at', )
