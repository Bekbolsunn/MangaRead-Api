from django.core.exceptions import ValidationError
from rest_framework_simplejwt.tokens import RefreshToken
import os


def get_path_upload_avatar(instance, file):
    upload_to = "avatar"
    ext = file.split(".")[-1]
    file = f"{instance.username}.{ext}"
    return os.path.join(upload_to, file)


def validate_size_image(file_object):
    size_limit = 2
    if file_object.size > size_limit * 1024 * 1024:
        raise ValidationError(f"Максимальный размер {size_limit}MB")


class GetLoginResponseService:
    @staticmethod
    def get_login_response(user, request):
        refresh = RefreshToken.for_user(user)
        data = {"refresh": str(refresh), "access": str(refresh.access_token)}
        return data
