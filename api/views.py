from django.shortcuts import render
from .serializers import *
from rest_framework import viewsets, permissions
from rest_framework.decorators import api_view
from .models import *
from rest_framework.response import Response


@api_view(['POST', 'GET'])
def user_list(request):
    users = User.objects.all()
    serializer = UserSerializer(users, many=True)
    return Response(serializer.data)


@api_view(['POST', 'GET'])
def profile_list(request):
    profile = Profile.objects.all()
    serializer = ProfileSerializer(profile, many=True)
    return Response(serializer.data)
