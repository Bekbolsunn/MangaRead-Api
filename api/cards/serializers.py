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
        fields = "__all__"


class MangaSerializer(serializers.ModelSerializer):
    name = serializers.CharField(max_length=50, min_length=2)
    year = serializers.IntegerField()
    # review = serializers.PrimaryKeyRelatedField(many=True, queryset=Review.objects.all())

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
            # "review",
        )
        read_only_fields = (
            "id",
            "publish_date",
            # "review",
        )


class MangaDetailSerializer(serializers.ModelSerializer):
    genre_manga = GenreMangaSerializer(many=True)
    type_manga = TypeMangaSerializer(many=False)

    class Meta:
        model = Manga
        fields = "__all__"
