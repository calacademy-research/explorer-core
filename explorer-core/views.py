from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import status, generics
from rest_framework.permissions import AllowAny
from rest_framework.views import APIView


from django.conf import settings
from django.http import JsonResponse
from django.contrib.auth import authenticate, login

import requests
from concurrent.futures import ThreadPoolExecutor, as_completed


import json
import os

class LoginView(APIView):
    permission_classes = [AllowAny]  # Allow all users (authenticated or not) to access this view

    def post(self, request, *args, **kwargs):
        username = request.data.get("username")
        password = request.data.get("password")

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return Response({"message": "Login successful"}, status=status.HTTP_200_OK)
        else:
            return Response({"error": "Invalid credentials"}, status=status.HTTP_400_BAD_REQUEST)