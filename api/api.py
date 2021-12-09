from .serializers import *
from .models import *
from rest_framework import viewsets, permissions, generics
from rest_framework import status
from rest_framework.response import Response
from knox.models import AuthToken
from .main2 import TradeAlgo 
# import numpy as np


#register Api

class RegisterAPI(generics.GenericAPIView):
    serializer_class = RegisterSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()

        return Response({
          "user" : UserSerializer(user, context=self.get_serializer_context()).data,
          "token" : AuthToken.objects.create(user)[1]
        })


#Login Api
class LoginAPI(generics.GenericAPIView):
    serializer_class = LoginSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data

        return Response({
        "user": UserSerializer(user, context=self.get_serializer_context()).data,
        "token": AuthToken.objects.create(user)[1]
        })


# Get User API
class UserAPI(generics.RetrieveAPIView):
    permission_classes = [permissions.IsAuthenticated,]
    serializer_class = UserSerializer

    def get_object(self):
        return self.request.user

class ProfileViewSet(viewsets.ModelViewSet):
    serializer_class = ProfileSerializer
    permission_classes = [permissions.IsAuthenticated,]
    queryset = Profile.objects.all()

    # def get_queryset(self):
    #     return self.request.user.profiles.all()

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
        #saving a profile to it's user

    def perform_update(self, serializer):
        serializer.save(user=self.request.user)

class AlgoViewSet(generics.GenericAPIView):
    serializer_class = AlgoSerializer
    
    # algo = TradeAlgo()
    
    def post(self,request):
        symbol = request.data['symbol']
        quantity = request.data['quantity']
        print("symbol", symbol)
        print("quantity", quantity)
        algo = TradeAlgo(symbol, quantity)
        queryset = algo.trade(symbol, quantity)
        return Response(queryset)