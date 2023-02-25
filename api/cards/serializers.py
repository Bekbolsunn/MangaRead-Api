from rest_framework import serializers
from api.cards.models import TypeManga, GenreManga, Manga, Review


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


class MangaSerializer(serializers.ModelSerializer):
    name = serializers.CharField(max_length=50, min_length=2)
    year = serializers.IntegerField()


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
        )
        read_only_fields = (
            "id",
            "publish_date",
        )

class ReviewSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    text = serializers.CharField(max_length=255, required=True)

    class Meta:
        model = Review
        fields = (
            "id",
            "text",
            "user",
            "manga",
        )

class MangaDetailSerializer(serializers.ModelSerializer):
    genre_manga = GenreMangaSerializer(many=True)
    type_manga = TypeMangaSerializer(many=False)

    class Meta:
        model = Manga
        fields = (
            "__all__"
        )

#helllo onichan