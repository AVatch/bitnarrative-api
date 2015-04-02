from rest_framework import serializers

from bits.models import Bit


class BitSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bit
