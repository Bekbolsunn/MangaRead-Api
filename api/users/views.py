# django imports
from django.contrib.auth import login, authenticate
from rest_framework import views, generics
from rest_framework.response import Response
from rest_framework.exceptions import AuthenticationFailed
from rest_framework.permissions import AllowAny, IsAdminUser

# local imports
from api.users.models import User
from api.users.services import GetLoginResponseService
from api.users.serializers import RegisterSerializers, LoginSerializer, UserSerializer
from api.users.paginations import UserPagination


class ListUserView(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (IsAdminUser,)
    pagination_class = UserPagination


class RegisterUserView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterSerializers
    permission_classes = (AllowAny,)


class LoginUserAPIView(views.APIView):
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
