# django imports
from django.urls import path, include
from rest_framework.routers import DefaultRouter

# local imports
from api.cards.views import (
    TypeMangaViewSet,
    MangaViewSet,
    GenreMangaViewSet,
    ReviewViewSet,
)


ROUTER = DefaultRouter()
ROUTER.register("mango", MangaViewSet, "Manga")
ROUTER.register("type", TypeMangaViewSet, "Type")
ROUTER.register("genre", GenreMangaViewSet, "Genre")
ROUTER.register("review", ReviewViewSet, "review")

app_name = "mango"

urlpatterns = [
    path("", include(ROUTER.urls)),
]