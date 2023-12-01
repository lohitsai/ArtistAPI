from rest_framework import generics, status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated, AllowAny

from django.contrib.auth.models import User
from django.contrib.auth import authenticate

from Artist.models import ArtistModel
from Artist.serializers import ArtistSerializer
import json
from Artist.signals import *


# API endpoint to return all Artist Names
class ArtistList(generics.ListAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    serializer_class = ArtistSerializer
    queryset = ArtistModel.objects.all()


# API endpoint to register a New User
class RegisterUser(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        try:
            data = json.loads(self.request.body)
            username = data["username"]
            password = data["password"]
            artistName = data["displayName"]
            # Creating the User instance using the details and saving it
            user = User.objects.create_user(
                username=username, password=password, first_name=artistName
            )
            # Getting the Token for the user
            token = Token.objects.get(user=user)
            # returning the token key to the user upon successful registration
            return Response({"token": token.key}, status=status.HTTP_201_CREATED)
        except:
            return Response(
                {"Error": "Invalid Format"}, status=status.HTTP_400_BAD_REQUEST
            )


class LoginUser(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        try:
            data = json.loads(self.request.body)
            username = data["username"]
            password = data["password"]
            # Creating the User instance using the details and saving it
            user = authenticate(username=username, password=password)
            if user is not None:
                # Getting the Token for the user
                token = Token.objects.get(user=user)
                # returning the token key to the user upon successful Login
                return Response({"token": token.key}, status=status.HTTP_200_OK)
            return Response(
                {"Error": "Invalid Credentials"}, status=status.HTTP_400_BAD_REQUEST
            )
        except:
            return Response(
                {"Error": "Invalid Format"}, status=status.HTTP_400_BAD_REQUEST
            )
