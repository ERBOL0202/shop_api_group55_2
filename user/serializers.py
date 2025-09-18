from rest_framework import serializers
from django.contrib.auth.models import User
from rest_framework.exceptions import ValidationError


class AuthValidateSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()


class RegisterValidateSerializer(serializers.Serializer):
    username = serializers.CharField()
    first_name = serializers.CharField()
    second_name = serializers.CharField()
    password = serializers.CharField(min_value=6)

    def validate_username(self, username, first_name, second_name):
        try:
            User.objects.get(username=username),
            User.objects.get(first_name=first_name),
            User.objects.get(second_name=second_name),
        except User.DoesNotExist:
            return username, first_name, second_name
        raise ValidationError('User already exists!')

class ConfirmationValidateSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()