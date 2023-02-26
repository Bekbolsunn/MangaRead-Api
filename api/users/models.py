# django imports
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db import models
from django.core.validators import FileExtensionValidator

# local imports
from api.users.services import get_path_upload_avatar, validate_size_image
from api.users.managers import UserManager


class User(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(
        "Имя",
        max_length=100,
        unique=True,
    )
    nickname = models.CharField("Прозвище", max_length=50, unique=True)
    avatar = models.ImageField(
        "Фото профиля",
        upload_to=get_path_upload_avatar,
        default="default/default.jpg",
        validators=[
            FileExtensionValidator(allowed_extensions=["jpg", "png"]),
            validate_size_image,
        ],
    )
    is_active = models.BooleanField("Активен", default=True)
    is_staff = models.BooleanField("Персонал", default=False)
    is_superuser = models.BooleanField("Cуперпользователь", default=False)
    date_joined = models.DateTimeField("Дата регистрации", auto_now_add=True)

    USERNAME_FIELD = "username"
    REQUIRED_FIELDS = ["nickname"]

    objects = UserManager()

    def __str__(self):
        return self.username

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"
