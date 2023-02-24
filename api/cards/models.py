from django.db import models


class TypeManga(models.Model):
    name = models.CharField(verbose_name="Тип", name='tip', max_length=50, blank=True, unique=True)

    def __str__(self):
        return f"Тип: {self.name}"


class GenreManga(models.Model):
    name = models.CharField(verbose_name="Жанр", name='genre', max_length=50, blank=True, unique=True)

    def __str__(self):
        return f"Жанр: {self.name}"


class Manga(models.Model):
    name = models.CharField("Название", max_length=100, unique=True, blank=True)
    year = models.IntegerField("Год выпуска", blank=True)
    synopsis = models.TextField("Краткое описание", max_length=255, blank=True)
    publish_date = models.DateField("Дата содания", auto_now_add=True)
    type_manga = models.ForeignKey(
        TypeManga, on_delete=models.CASCADE, related_name="bsdfgdsfg", blank=True, null=True
    )
    genre_manga = models.ForeignKey(
        GenreManga, on_delete=models.CASCADE, related_name="dsfgsdfg", blank=True, null=True
    )

    def __str__(self):
        return f"Название: {self.name}"
