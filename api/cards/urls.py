from django.urls import path, include
from api.cards.views import (TypeMangaViewSet, MangaViewSet, GenreMangaViewSet, ReviewViewSet)

from rest_framework.routers import SimpleRouter, DefaultRouter

ROUTER = DefaultRouter()
ROUTER.register("type", TypeMangaViewSet, "Type")
ROUTER.register("mango", MangaViewSet, "Manga")
ROUTER.register("genre", GenreMangaViewSet, "Genre")
ROUTER.register("review", ReviewViewSet, "Genre")

app_name = "mango"

urlpatterns = [
    path("", include(ROUTER.urls)),
]
