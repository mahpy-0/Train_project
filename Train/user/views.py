from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.authentication import BasicAuthentication, BaseAuthentication
from rest_framework.permissions import BasePermission
from .models import User
from .serializres import UserSerializer


# Create your views here.
class RegisterUser(APIView):
    authentication_classes = [
        BasicAuthentication,
    ]
    permission_classes = [
        BasePermission,
    ]

    def post(self, request):
        user_name = request.data.get("username")
        email = request.data.get("email")
        password = request.data.get("password")
        is_staff = request.data.get("is_staff") if request.data.get("is_staff") is not None else False
        
        if User.objects.filter(username=user_name, email=email).exists():
            return Response({"message": "Email or Username already exists"}, status=status.HTTP_403_FORBIDDEN)
        else:
            new_user = User(username=user_name, email=email, is_staff=is_staff, is_active=True)
            new_user.set_password(password)
            new_user.save()
            return Response({"message": "User created successfully"},
                            status=status.HTTP_201_CREATED)


class UserList(APIView):
    def get(self, request):
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
