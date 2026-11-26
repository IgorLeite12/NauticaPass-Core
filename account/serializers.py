from django.contrib.auth.hashers import make_password
from rest_framework import serializers
from account.models import Account


class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = ['id',
                  'username',
                  'name',
                  'email',
                  'phone',
                  'cpf',
                  'birth_date',
                  'password']
        extra_kwargs = {
            'password': {'write_only': True},
            'cpf': {'required': False, 'allow_null': True, 'allow_blank': True},
        }

    def validate(self, attrs):
        if attrs.get('cpf') == '':
            attrs['cpf'] = None
        return attrs

    def create(self, validated_data):
        account = Account(
            username=validated_data['username'],
            name=validated_data.get('name', ''),
            email=validated_data['email'],
            birth_date=validated_data.get('birth_date'),
            cpf=validated_data.get('cpf', None),
        )
        account.set_password(validated_data['password'])
        account.save()
        return account

    def update(self, instance, validated_data):
        if 'password' in validated_data:
            validated_data['password'] = make_password(validated_data['password'])
        return super().update(instance, validated_data)