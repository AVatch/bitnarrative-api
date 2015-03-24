from rest_framework import serializers

from community.models import Community


class CommunitySerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Community
        fields = ('id', 'group_name', 'lead_image_url',
                  'member_count', 'community_description',
                  'created_at', 'participation_rate',
                  'updated_at')
