# django imports
from rest_framework import serializers

# local imports
from api.cards.models import (
    TypeManga,
    GenreManga,
    Manga,
    Review,
)


class TypeMangaSerializer(serializers.ModelSerializer):
    name = serializers.CharField(max_length=50, min_length=2)

    class Meta:
        model = TypeManga
        fields = (
            "id",
            "name",
        )


class GenreMangaSerializer(serializers.ModelSerializer):
    name = serializers.CharField(max_length=50, min_length=2)

    class Meta:
        model = GenreManga
        fields = (
            "id",
            "name",
        )


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = (
            'id',
            'manga',
            'text',
            'user',
            'created_date',
        )
        read_only_fields = (
            'id',
            'created_date',
        )


class MangaSerializer(serializers.ModelSerializer):
    name = serializers.CharField(max_length=50, min_length=2)
    year = serializers.IntegerField(default=0)

    class Meta:
        model = Manga
        fields = (
            "id",
            "name",
            "cover",
            "year",
            "synopsis",
            "type_manga",
            "genre_manga",
        )
        read_only_fields = (
            "id",
        )


class MangaDetailSerializer(MangaSerializer):
    review = ReviewSerializer(many=True)

    class Meta:
        model = Manga
        fields = (
            "id",
            "name",
            "cover",
            "year",
            "synopsis",
            "publish_date",
            "type_manga",
            "genre_manga",
            "review",
        )
        read_only_fields = (
            "id",
            "publish_date",
        )