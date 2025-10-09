from rest_framework import serializers
from django.contrib.auth.models import User
from rest_framework.exceptions import ValidationError
from .models import ConfirmationCode
from users.models import CustomUser
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

class UserBaseSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField()

class AuthValidateSerializer(UserBaseSerializer):
    pass

#class AuthValidateSerializer(serializers.Serializer):
    #username = serializers.CharField()
    #password = serializers.CharField()


class RegisterValidateSerializer(UserBaseSerializer):
    def validate_email(self, email):
        try:
            CustomUser.objects.get(email=email)
        except:
            return email
        raise ValidationError('Email уже существует!')
    #username = serializers.CharField()
    #first_name = serializers.CharField()
    #second_name = serializers.CharField()
    #password = serializers.CharField(min_value=6)

    #def validate_username(self, username, first_name, second_name):
        #try:
            #User.objects.get(username=username),
           # User.objects.get(first_name=first_name),
            #User.objects.get(second_name=second_name),
       #except User.DoesNotExist:
            #return username, first_name, second_name
        #raise ValidationError('User already exists!')

class ConfirmationValidateSerializer(serializers.Serializer):
    user_id = serializers.IntegerField()
    code = serializers.CharField(max_length=6)

    def validate(self, attrs):
        user_id = attrs.get('user_id')
        code = attrs.get('code')

        try:
            user = CustomUser.objects.get(id=user_id)
        except CustomUser.DoesNotExist:
            raise ValidationError('User не существует!')

        try:
            confirmation_code = ConfirmationCode.objects.get(user=user)
        except ConfirmationCode.DoesNotExist:
            raise ValidationError('Код подтверждения не найден!')

        if confirmation_code.code != code:
            raise ValidationError('Неверный код подтверждения!')

        return attrs
    #username = serializers.CharField()
    #password = serializers.CharField()




class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        token["email"] = user.emai
        token = super().get_token(user)
        if user.birthdate:
            token['birthdate'] = str(user.birthdate)
        return token
    