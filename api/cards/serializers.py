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
    # type_name = serializers.SerializerMethodField()
    # genre_name = serializers.SerializerMethodField()
    

    # def get_type_name(self, instance):
    #     return instance.type_manga.name
    
    # def get_genre_name(self, instance):
    #     return list(map(lambda manga: manga.name, instance.genre_manga.all()))


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
            # "type_name",
            # "genre_name",
            "review",
        )
        read_only_fields = (
            "id",
            "publish_date",
        )