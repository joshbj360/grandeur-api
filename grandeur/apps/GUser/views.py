from django.shortcuts import render

from rest_framework import generics

from .serializer import UserSerializer
from .models import GUser

class UserView(generics.ListCreateAPIView):
    queryset = GUser.objects.all()
    serializer_class = UserSerializer