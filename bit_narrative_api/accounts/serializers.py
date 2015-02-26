from rest_framework import serializers

from accounts.models import Account
from bits.serializers import BitSerializer


class AccountSerializer(serializers.HyperlinkedModelSerializer):
    password = serializers.CharField(write_only=True,
                                     allow_blank=True,
                                     required=False)
    confirm_password = serializers.CharField(write_only=True,
                                             allow_blank=True,
                                             required=False)

    # only hyperlink
    # bits = serializers.HyperlinkedRelatedField(many=True,
    #                                            view_name='bit-detail',
    #                                            read_only=True)
    # Example of using a serializer
    # bits = BitSerializer(many=True, read_only=True)

    class Meta:
        model = Account
        fields = ('id', 'username', 'email',
                  'first_name', 'last_name', 'profile_picture_url',
                  'password', 'confirm_password',
                  'is_manager', 'created_at', 'updated_at')
        read_only_fields = ('id', 'created_at', 'updated_at')

    def create(self, validated_data):
        return Account.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.username = validated_data.get(
                              'username', instance.username)
        instance.first_name = validated_data.get(
                              'first_name', instance.first_name)
        instance.last_name = validated_data.get(
                              'last_name', instance.last_name)
        instance.profile_picture_url = validated_data.get(
                          'profile_picture_url', instance.profile_picture_url)

        instance.save()

        password = validated_data.get('password', None)
        confirm_password = validated_data.get('confirm_password', None)

        if password and confirm_password and password == confirm_password:
            instance.set_password(password)
            instance.save()

        return instance
