from rest_framework import serializers
from rest_framework_simplejwt.tokens import RefreshToken

from django.core.exceptions import ValidationError


def get_path_upload_avatar(instance, file):
    """Путь для хранения аватарок format:(media)/avatar/user_id/photo.jpg"""
    return f"avatar/{instance.id}/{file}"


def validate_size_image(file_object):
    """Проверка размера файла"""
    size_limit = 2
    if file_object.size > size_limit * 1024 * 1024:
        raise ValidationError(f"Максимальный размер {size_limit}MB")


class GetLoginResponseService:
    @staticmethod
    def get_login_response(user, request):
        refresh = RefreshToken.for_user(user)
        data = {"refresh": str(refresh), "access": str(refresh.access_token)}
        return data
