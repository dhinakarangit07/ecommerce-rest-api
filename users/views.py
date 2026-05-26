from rest_framework import generics
from django.contrib.auth.models import User
from .serializers import RegisterSerializer


class RegisterAPIView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer


from rest_framework.response import Response
from rest_framework.views import APIView
from django.contrib.auth import authenticate


class LoginAPIView(APIView):

    def post(self, request):

        username = request.data.get('username')
        password = request.data.get('password')

        user = authenticate(username=username, password=password)

        if user:
            return Response({
                'message': 'Login Successful'
            })

        return Response({
            'message': 'Invalid Credentials'
        }, status=400)