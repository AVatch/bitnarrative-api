from rest_framework import serializers

from topics.models import Topic


class TopicSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Topic
        exclude = ('accounts', 'communities', 'content')
