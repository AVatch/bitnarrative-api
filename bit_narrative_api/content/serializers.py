from rest_framework import serializers

from content.models import Content

from accounts.models import Account


class ContentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Content


class ContentParserSerializer(serializers.Serializer):
    url = serializers.URLField()
    community = serializers.IntegerField()
