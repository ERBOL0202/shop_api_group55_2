from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .serializers import RegisterValidateSerializer, AuthValidateSerializer
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token


@api_view(['POST'])
def registration_api_view(request):
    serializer = RegisterValidateSerializer(data=request.data)
    if not serializer.is_valid():
        return Response(status=status.HTTP_400_BAD_REQUEST,
                        data={'errors': serializer.errors})

    user = User.objects.create_user(
        username=serializer.validated_data['username'],
        first_name=serializer.validated_data['first_name'],
        second_name=serializer.validated_data['second_name'],
        password=serializer.validated_data['password'],
        is_active=False
    )

    return Response(status=status.HTTP_201_CREATED, data={'user_id': user.id})


@api_view(['POST'])
def authorization_api_view(request):
    serializer = AuthValidateSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)

    user = authenticate(
        username=serializer.validated_data['username'],
        password=serializer.validated_data['password'])
    
    if user is not None:
        try:
            token_ = Token.objects.get(user=user)
        except:
            token_ = Token.objects.create(user=user)
        return Response(data={'key': token_.key})
    return Response(status=status.HTTP_401_UNAUTHORIZED)

@api_view(['POST'])
def confirmation_api_view(request):
    serializer = ConfirmationValidateSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    
    user = confirmation(
        username=serializer.validated_data['username'],
        password=serializer.validated_data['password'])