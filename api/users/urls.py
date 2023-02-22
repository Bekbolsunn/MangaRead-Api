from django.urls import path, include
from ..users.views import (
    RegisterUserView,
    LoginAPIView,
    ListUserView,
)

from rest_framework.routers import SimpleRouter
from rest_framework_simplejwt.views import (
    TokenRefreshView,
)

# ROUTER = SimpleRouter()
# ROUTER.register(r"profile", ProfileViewSet, "profile")

app_name = "users"

urlpatterns = [
    path("register/", RegisterUserView.as_view(), name="Sign Up"),
    path("login/", LoginAPIView.as_view(), name="Sign In"),
    path("list/", ListUserView.as_view(), name="User list"),
    # JWT
    path("login/token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    # path("", include(ROUTER.urls)),
]
