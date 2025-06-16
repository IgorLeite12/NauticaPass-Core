from django.contrib.auth.hashers import make_password
from rest_framework import serializers
from user.models import User
from django.contrib.auth.models import Group



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

    def create(self, validated_data):
        password = validated_data.pop('password', None)
        if password is None:
            raise serializers.ValidationError({'password': 'Este campo é obrigatório.'})
        user = super().create(validated_data)
        user.set_password(password)
        user.save()
        group_user, _ = Group.objects.get_or_create(name='Usuario')
        user.groups.add(group_user)
        return user

    def update(self, instance, validated_data):
        if 'password' in validated_data:
            validated_data['password'] = make_password(validated_data['password'])
        else:
            validated_data.pop('password', None)
        return super().update(instance, validated_data)

    def validate(self, attrs):
        if attrs.get('cpf') == '':
            attrs['cpf'] = None
        if attrs.get('rg') == '':
            attrs['rg'] = None
        if attrs.get('passport') == '':
            attrs['passport'] = None
        return attrs


