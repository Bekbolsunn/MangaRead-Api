from django.db import models


class TypeManga(models.Model):
    name = models.CharField("Тип", max_length=50, unique=True)

    def __str__(self):
        return f"Тип: {self.name}"


class GenreManga(models.Model):
    name = models.CharField("Жанр", max_length=50, unique=True, blank=True)

    def __str__(self):
        return f"Жанр: {self.name}"


class CardManga(models.Model):
    name = models.CharField("Название", max_length=100, unique=True, blank=True)
    year = models.IntegerField("Год выпуска", blank=True)
    cover = models.ImageField(
        "Обложка",
        default="https://www.boldstrokesbooks.com/assets/bsb/images/book-default-cover.jpg",
        blank=True,
        # upload_to=cover/
    )
    synopsis = models.TextField("Краткое описание", max_length=255, blank=True)
    publish_date = models.DateField("Дата содания", auto_now_add=True)
    type_manga = models.ForeignKey(
        TypeManga, on_delete=models.CASCADE, verbose_name="Тип манги"
    )
    genre_manga = models.ForeignKey(
        GenreManga, on_delete=models.CASCADE, verbose_name="Жанр манги"
    )

    def __str__(self):
        return f"Название: {self.name}"
