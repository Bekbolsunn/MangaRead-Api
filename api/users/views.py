# django imports
from django.contrib.auth import login, authenticate
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.exceptions import AuthenticationFailed
from rest_framework.permissions import AllowAny, IsAdminUser
from rest_framework.filters import SearchFilter


# local imports
from api.users.models import User
from api.users.services import GetLoginResponseService
from api.users.paginations import UserPagination
from api.users.serializers import (
    RegisterSerializers,
    LoginSerializer,
    UserSerializer,
)


class ListUserView(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (IsAdminUser,)
    pagination_class = UserPagination
    filter_backends = [SearchFilter]
    search_fields = ["name", "nickname"]


class RegisterUserView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterSerializers
    permission_classes = (AllowAny,)


class LoginUserAPIView(generics.CreateAPIView):
    serializer_class = LoginSerializer
    permission_classes = (AllowAny,)

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = authenticate(
            username=serializer.validated_data["username"],
            password=serializer.validated_data["password"],
        )
        if not user:
            raise AuthenticationFailed()
        login(request, user)
        return Response(data=GetLoginResponseService.get_login_response(user, request))
