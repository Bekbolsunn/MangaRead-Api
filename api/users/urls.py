# django imports
from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView

# local imports
from api.users.views import (
    RegisterUserView,
    LoginUserAPIView,
    ListUserView,
)


app_name = "users"

urlpatterns = [
    path("register/", RegisterUserView.as_view(), name="Sign Up"),
    path("login/", LoginUserAPIView.as_view(), name="Sign In"),
    path("list/", ListUserView.as_view(), name="User list"),
    # JWT
    path("login/token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
]
