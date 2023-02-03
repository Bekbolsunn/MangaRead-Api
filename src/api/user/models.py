# django imports
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db import models
from django.core.validators import FileExtensionValidator

# package imports
from phonenumber_field.modelfields import PhoneNumberField

# local import
from ..user.managers import UserManager
from ..user.choices import USER_GENDER, REGION
from ..user.base import get_path_upload_avatar, validate_size_image


class User(AbstractBaseUser, PermissionsMixin):
    """Sign Up"""

    username = models.CharField(max_length=150, unique=True)
    email = models.EmailField(db_index=True)

    """Sign In"""
    nikname = models.CharField(max_length=35)
    phone = PhoneNumberField(blank=True, null=True)
    bio = models.TextField(max_length=1000, blank=True, null=True)
    gender = models.CharField(max_length=15, choices=USER_GENDER, null=True, blank=True)
    region = models.CharField(max_length=15, choices=REGION, null=True, blank=True)
    avatar = models.ImageField(
        upload_to=get_path_upload_avatar,
        blank=True,
        null=True,
        validators=[
            FileExtensionValidator(allowed_extensions=["jpg"]),
            validate_size_image,
        ],
    )

    is_active = models.BooleanField("Активен", default=True)
    is_staff = models.BooleanField("Персонал", default=False)
    is_superuser = models.BooleanField("Cуперпользователь", default=False)
    updated_at = models.DateTimeField("Обновлено в", auto_now=True)
    date_joined = models.DateTimeField("Дата регистрации", auto_now_add=True)
    last_active = models.DateTimeField(
        "Дата последой активности", null=True, blank=True
    )

    USERNAME_FIELD = "username"
    REQUIRED_FIELDS = ["email"]

    objects = UserManager()

    def __str__(self):
        return self.username

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"