from .models import *
from rest_framework import serializers
# from drf_base64.fields import Base64ImageField, Base64FileField
import re

class UserSerializer(serializers.ModelSerializer):
    old_password = serializers.CharField(write_only=True, required=False)

    def create(self, validated_data):
        password = validated_data.pop('password')

        validated_data['is_active'] = True

        user = User.objects.create(**validated_data)
        user.set_password(password)
        user.save()
        return user

    def update(self, instance, validated_data):
        password = validated_data.pop('password', None)
        old_password = validated_data.pop('old_password', None)

        if password is not None and not instance.check_password(old_password):
            # raise InvalidPassword
            pass
        if password is not None:
            instance.set_password(password)

        new_instance = super().update(instance, validated_data)

        establishment = instance.establishment

        if not UserEstablishment.objects.filter(user=instance, establishment=establishment).exists():
            # raise InvalidEstablishment
            pass
        return new_instance

    class Meta:
        model = User
        fields = '__all__'
        extra_kwargs = {'password': {'write_only': True},
                        'old_password': {'write_only': True}}
        read_only_fields = ('id',)