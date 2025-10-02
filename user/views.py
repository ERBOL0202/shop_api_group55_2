from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .serializers import RegisterValidateSerializer, AuthValidateSerializer, ConfirmationSerializer
#from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token
from rest_framework.generics import CreateAPIView
from .models import ConfirmationCode
import random
import string
from users.models import CustomUser


class AuthorizationAPIView(CreateAPIView):
    serializer_class = AuthValidateSerializer

    def post(self, request):
        serializer = AuthValidateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        user = authenticate(**serializer.validated_data)

        if user:
            if not user.is_active:
                return Response(
                    status=status.HTTP_401_UNAUTHORIZED,
                    data={'error': 'User account is not activated yet!'}
                )

            token, _ = Token.objects.get_or_create(user=user)
            return Response(data={'key': token.key})

        return Response(
            status=status.HTTP_401_UNAUTHORIZED,
            data={'error': 'User credentials are wrong!'}
        )


class RegistrationAPIView(CreateAPIView):
    serializer_class = RegisterValidateSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        email = serializer.validated_data['email']
        password = serializer.validated_data['password']

        # Use transaction to ensure data consistency
        with transaction.atomic():
            user = CustomUser.objects.create_user(
                email=email,
                password=password,
                is_active=False
            )

            # Create a random 6-digit code
            code = ''.join(random.choices(string.digits, k=6))

            confirmation_code = ConfirmationCode.objects.create(
                user=user,
                code=code
            )

        return Response(
            status=status.HTTP_201_CREATED,
            data={
                'user_id': user.id,
                'confirmation_code': code
            }
        )


class ConfirmUserAPIView(CreateAPIView):
    serializer_class = ConfirmationSerializer

    def post(self, request):
        serializer = ConfirmationSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        user_id = serializer.validated_data['user_id']

        with transaction.atomic():
            user = CustomUser.objects.get(id=user_id)
            user.is_active = True
            user.save()

            token, _ = Token.objects.get_or_create(user=user)

            ConfirmationCode.objects.filter(user=user).delete()

        return Response(
            status=status.HTTP_200_OK,
            data={
                'message': 'User аккаунт успешно активирован',
                'key': token.key
            }
        )
#@api_view(['POST'])
#def registration_api_view(request):
    #serializer = RegisterValidateSerializer(data=request.data)
    #if not serializer.is_valid():
        #eturn Response(status=status.HTTP_400_BAD_REQUEST,
                        #data={'errors': serializer.errors})

    #user = User.objects.create_user(
        #username=serializer.validated_data['username'],
        #first_name=serializer.validated_data['first_name'],
        #second_name=serializer.validated_data['second_name'],
        #password=serializer.validated_data['password'],
        #is_active=False
    )

    #return Response(status=status.HTTP_201_CREATED, data={'user_id': user.id})


#@api_view(['POST'])
#def authorization_api_view(request):
    #serializer = AuthValidateSerializer(data=request.data)
    #serializer.is_valid(raise_exception=True)

    #user = authenticate(
        #username=serializer.validated_data['username'],
        #password=serializer.validated_data['password'])
    
    #if user is not None:
        #try:
           # token_ = Token.objects.get(user=user)
        #except:
            #token_ = Token.objects.create(user=user)
        #return Response(data={'key': token_.key})
    #return Response(status=status.HTTP_401_UNAUTHORIZED)

#@api_view(['POST'])
#def confirmation_api_view(request):
    #serializer = ConfirmationValidateSerializer(data=request.data)
   # serializer.is_valid(raise_exception=True)
    
    #user = confirmation(
        #username=serializer.validated_data['username'],
        #password=serializer.validated_data['password'])