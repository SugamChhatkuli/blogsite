from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework.generics import ListAPIView, CreateAPIView, UpdateAPIView
from .serializers import UserRegisterSerializer, UserListSerializer, UserProfileUpdateSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.response import Response
from rest_framework.views import APIView

# Create your views here.

class UserRegister(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserRegisterSerializer

    

class UserList(ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserListSerializer

class UpdateProfile(UpdateAPIView):
    queryset =User.objects.all()
    serializer_class = UserProfileUpdateSerializer


class LogoutView(APIView):
    permission_classes=[IsAuthenticated,]

    def post(self, request):
        print(request.data)
        try:
            refresh_token = request.data['refresh_token']
            token = RefreshToken(refresh_token)
            token.blacklist()

            return Response(status= status.HTTP_205_RESET_CONTENT)
        except Exception as e:
            return Response (status = status.HTTP_400_BAD_REQUEST)
