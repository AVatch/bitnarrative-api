from rest_framework import serializers

from community.models import Community


class CommunitySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Community
