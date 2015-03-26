from rest_framework import serializers

from bits.models import Bit


class BitSerializer(serializers.HyperlinkedModelSerializer):
    accounts = serializers.HyperlinkedRelatedField(many=True,
                                                   view_name='account-detail',
                                                   read_only=True)
    community = serializers.HyperlinkedRelatedField(many=True,
                                                   view_name='community-detail',
                                                   read_only=True)

    class Meta:
        model = Bit
        fields = ('id', 'bit', 'content_index',
                  'accounts', 'content', 'view_count',
                  'share_count', 'up_count', 'down_count',
                  'created_at', 'community')

    def create(self, validated_data):
        return Bit.objects.create(**validated_data)
