from django.shortcuts import render
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import UserSerializer
from ..models import User
from rest_framework.exceptions import AuthenticationFailed

import datetime

# Create your views here.

class registerAPIView(APIView):
    def get(self, request):
        # Return an empty serializer or some fields for the registration form
        serializer = UserSerializer()
        return Response(serializer.data)
    def post(self, request):
        # Validate and save the user data
        serializer = UserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)  # Raise an exception if the data is invalid
        user = serializer.save()  # Create the user

        # Automatically generate a JWT token for the newly registered user
        refresh = RefreshToken.for_user(user)

        # Return the user data along with the JWT tokens (access and refresh)
        response = Response({
            'user': serializer.data,
            'refresh': str(refresh),
            'access': str(refresh.access_token)
        }, status=201)
                # Set the tokens in cookies
        response.set_cookie(
            key='accessToken',
            value=str(refresh.access_token),
            httponly=True,  # Prevent access via JavaScript (mitigates XSS attacks)
            secure=True,    # Ensures it's sent over HTTPS (set to True in production)
            samesite='Strict'  # Prevents CSRF (can be 'Lax' or 'None' based on your needs)
        )
        response.set_cookie(
            key='refreshToken',
            value=str(refresh),
            httponly=True,  # Same security settings as accessToken
            secure=True,
            samesite='Strict'
        )
        return response
