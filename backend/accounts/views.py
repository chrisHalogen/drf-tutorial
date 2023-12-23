from django.shortcuts import render
from rest_framework.generics import CreateAPIView
from django.contrib.auth.models import User
from .serializers import UserSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import BasicAuthentication, TokenAuthentication, SessionAuthentication
# from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.views import APIView
from django.contrib.auth import authenticate, logout, login
from rest_framework.authtoken.models import Token

# Create your views here.

class UserCreateView(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

@api_view(['GET'])
def unprotected_view(request):
    data = {
        'message' : 'This is an unprotected view'
    }
    return Response(data, status=status.HTTP_200_OK )

@api_view(['GET'])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
def protected_view(request):
    data = {
        'message' : f'Hello {request.user.username}, This is a protected view'
    }
    return Response(data, status=status.HTTP_200_OK )

class ProtectedView(APIView):
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]

    def get(self, request):
        data = {
                'message' : f'Hello {request.user.username}, This is a protected Class Based view'
            }
        return Response(data, status=status.HTTP_200_OK )
    

class ObtainToken(APIView):
    def post(self, request, *args, **kwargs):
        username = request.data.get('username')
        password = request.data['password']
        print(request)

        if username and password:
            user = authenticate(
                    username=username, 
                    password=password
                )
            
            if user:
                token, created = Token.objects.get_or_create(user=user)
                data = {
                        'message' : 'Token Generated Successfully',
                        'token' : token.key
                    }
                return Response(data, status=status.HTTP_200_OK)
            else:
                data = {
                        'message' : 'Username - Password Mismatch'
                    }
                return Response(data, status=status.HTTP_401_UNAUTHORIZED)

        else:
            data = {
                'message' : 'Invalid Cridentials'
            }
            return Response(data, status=status.HTTP_401_UNAUTHORIZED)


@api_view(['GET'])
@authentication_classes([SessionAuthentication])
@permission_classes([IsAuthenticated])
def logout_view(request):
    logout(request)
    data = {
        'message' : 'User Logged out Successfully'
    }
    return Response(data)

@api_view(['POST'])
def create_session_view(request):
    username = request.data.get('username')
    password = request.data.get('password')

    user = User.objects.get(username=username)

    if user:
        if user.check_password(password):
            login(request, user)
            data = {
                    'message' : 'User Logged in Successfully'
                }
            return Response(data)
        else:
            data = {
                    'message' : "Username - Password Mismatch"
                }
            return Response(data, status=status.HTTP_401_UNAUTHORIZED)
    else:
        data = {
                'message' : "Invalid Username"
                }
        return Response(data, status=status.HTTP_401_UNAUTHORIZED)