# django imports
from rest_framework.filters import OrderingFilter, SearchFilter
from rest_framework import viewsets
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticatedOrReadOnly, AllowAny

# local imports
from api.cards.models import (
    TypeManga,
    Manga,
    GenreManga,
    Review,
)
from api.cards.serializers import (
    TypeMangaSerializer,
    MangaSerializer,
    GenreMangaSerializer,
    ReviewSerializer,
    MangaDetailSerializer,
)
from api.cards.paginations import (
    CardPagination,
    TypePagination,
    GenrePagination,
    ReviewPagination,
)


class TypeMangaViewSet(viewsets.ModelViewSet):
    queryset = TypeManga.objects.all()
    serializer_class = TypeMangaSerializer
    authentication_classes = (JWTAuthentication,)
    permission_classes = (AllowAny,)
    pagination_class = TypePagination
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ["name"]
    ordering_fields = ["name", "id"]


class MangaViewSet(viewsets.ModelViewSet):
    def get_serializer_class(self):
        if self.action == "retrive":
            return MangaDetailSerializer
        return MangaSerializer

    queryset = Manga.objects.all()
    authentication_classes = (JWTAuthentication,)
    permission_classes = (AllowAny,)
    pagination_class = CardPagination
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ["name", "id", "year"]
    ordering_fields = ["name", "year", "genre_manga", "type_manga"]


class GenreMangaViewSet(viewsets.ModelViewSet):
    queryset = GenreManga.objects.all()
    serializer_class = GenreMangaSerializer
    authentication_classes = (JWTAuthentication,)
    permission_classes = (AllowAny,)
    pagination_class = GenrePagination
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ["name", "id", "year"]
    ordering_fields = ["name", "year", "genre_manga", "type_manga"]


class ReviewViewSet(viewsets.ModelViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    authentication_classes = (JWTAuthentication,)
    permission_classes = (AllowAny,)
    pagination_class = ReviewPagination
