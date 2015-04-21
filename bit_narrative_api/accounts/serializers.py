from rest_framework import serializers

from .models import Account


class AccountSerializer(serializers.ModelSerializer):
    community = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    class Meta:
        model = Account
        extra_kwargs = {'password': {'write_only': True, 'allow_blank': True}}
        read_only_fields = ('last_login',)

    def create(self, validated_data):
        account = Account(
            username=validated_data['username'],
            email=validated_data['email'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name'],
        )
        account.set_password(validated_data['password'])
        account.save()
        return account

    def update(self, instance, validated_data):
        instance.email = validated_data.get('email', instance.email)
        instance.first_name = validated_data.get('first_name',
                                                 instance.first_name)
        instance.last_name = validated_data.get('last_name',
                                                instance.last_name)

        if validated_data['password'] == '':
            pass
        else:
            instance.set_password(validated_data['password'])

        instance.save()

        return instance
