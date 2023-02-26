# django imports
from django.db import models
from django.core.validators import FileExtensionValidator

# local imports
from api.users.models import User
from api.cards.services import get_path_upload_cover, validate_size_image


class TypeManga(models.Model):
    name = models.CharField("Название", max_length=50, blank=True, unique=True)

    def __str__(self):
        return f"Тип: {self.name}"

    class Meta:
        verbose_name = "Тип"
        verbose_name_plural = "Типы"


class GenreManga(models.Model):
    name = models.CharField("Название", max_length=50, blank=True, unique=True)

    def __str__(self):
        return f"Жанр: {self.name}"

    class Meta:
        verbose_name = "Жанр"
        verbose_name_plural = "Жанры"


class Manga(models.Model):
    name = models.CharField("Название", max_length=100, unique=True, blank=True)
    cover = models.ImageField(
        "Обложка",
        upload_to=get_path_upload_cover,
        default="default/cover.jpg",
        validators=[
            FileExtensionValidator(allowed_extensions=["jpg", "png"]),
            validate_size_image,
        ],
    )
    year = models.IntegerField("Год выпуска", blank=True)
    synopsis = models.TextField("Краткое описание", max_length=255, blank=True)
    publish_date = models.DateField("Дата Публикации", auto_now_add=True)
    type_manga = models.ForeignKey(
        TypeManga,
        on_delete=models.CASCADE,
        related_name="Тип_манги",
        blank=True,
        null=True,
    )
    genre_manga = models.ManyToManyField(
        GenreManga, related_name="Жанр_манги", blank=True
    )

    def __str__(self):
        return f"Название: {self.name}"

    class Meta:
        verbose_name = "Манга"
        verbose_name_plural = "Манги"


class Review(models.Model):
    manga = models.ForeignKey(Manga, on_delete=models.CASCADE, related_name="review")
    text = models.TextField("Текст", max_length=255, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_date = models.DateField("Дата создания", auto_now_add=True)

    def __str__(self):
        return f"{self.user}-Чан оставил рецензию на {self.manga}"

    class Meta:
        verbose_name = "Рецензия"
        verbose_name_plural = "Рецензии"
