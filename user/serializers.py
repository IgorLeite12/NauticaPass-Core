from django.contrib.auth.hashers import make_password
from rest_framework import serializers
from user.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id',
                  'username',
                  'name',
                  'email',
                  'phone',
                  'nationality_type',
                  'cpf',
                  'rg',
                  'passport',
                  'gender_type',
                  'birth_date',
                  'password']
        extra_kwargs = {
            'password': {'write_only': True, 'required': False},
            'cpf': {'required': False, 'allow_null': True, 'allow_blank': True},
            'rg': {'required': False, 'allow_null': True, 'allow_blank': True},
            'passport': {'required': False, 'allow_null': True, 'allow_blank': True},
        }

    def validate(self, attrs):
        if attrs.get('cpf') == '':
            attrs['cpf'] = None
        if attrs.get('rg') == '':
            attrs['rg'] = None
        if attrs.get('passport') == '':
            attrs['passport'] = None
        return attrs

    def create(self, validated_data):
        if 'password' not in validated_data:
            raise serializers.ValidationError({'password': 'Este campo é obrigatório.'})
        user = User(
            username=validated_data['username'],
            name=validated_data['name'],
            email=validated_data['email'],
            birth_date=validated_data.get('birth_date'),
            cpf=validated_data['cpf'],
            rg=validated_data['rg'],
        )
        user.set_password(validated_data['password'])
        user.save()
        return user

    def update(self, instance, validated_data):
        if 'password' in validated_data:
            validated_data['password'] = make_password(validated_data['password'])
        else:
            validated_data.pop('password', None)
        return super().update(instance, validated_data)