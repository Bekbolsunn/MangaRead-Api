from django.shortcuts import render
from rest_framework import viewsets
from api.cards.models import TypeManga, Manga, GenreManga, Review
from api.cards.serializers import (
    TypeMangaSerializer,
    MangaSerializer,
    GenreMangaSerializer,
    ReviewSerializer,
    MangaDetailSerializer
)
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticatedOrReadOnly, AllowAny, IsAdminUser


class TypeMangaViewSet(viewsets.ModelViewSet):
    queryset = TypeManga.objects.all()
    serializer_class = TypeMangaSerializer
    authentication_classes = (JWTAuthentication,)
    permission_classes = (AllowAny,)


class MangaViewSet(viewsets.ModelViewSet):
    
    def get_serializer_class(self):
        if self.action == "retrive":
            return MangaDetailSerializer
        return MangaSerializer
    
    queryset = Manga.objects.all()
    authentication_classes = (JWTAuthentication,)
    permission_classes = (AllowAny,)




class GenreMangaViewSet(viewsets.ModelViewSet):
    queryset = GenreManga.objects.all()
    serializer_class = GenreMangaSerializer
    authentication_classes = (JWTAuthentication,)
    permission_classes = (AllowAny,)
        


class ReviewViewSet(viewsets.ModelViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    authentication_classes = (JWTAuthentication,)
    permission_classes = (AllowAny,)