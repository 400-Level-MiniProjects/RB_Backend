from django.shortcuts import render
from django.contrib.auth import login

from rest_framework import permissions
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authtoken.serializers import AuthTokenSerializer

from knox.models import AuthToken
from knox.views import LoginView as KLoginView

from .serializers import *

# Create your views here.

class RegisterUser(GenericAPIView):
    serializer_class = RegisterUserSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)

        if serializer.is_valid():
            user = serializer.save()
            return Response(
                {
                    "user": UserSerializers(user, context=self.get_serializer_context()).data,
                    "token": AuthToken.objects.create(user)[1]
                }
            )
        return Response(serializer.errors, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class LoginUser(KLoginView):
    permission_classes = (permissions.AllowAny,)

    def post(self, request, format=None):
        serializer = AuthTokenSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.validated_data['user']
            login(request, user)
            return super(LoginUser, self).post(request, format=None)
        else:
            return Response(serializer.errors, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

