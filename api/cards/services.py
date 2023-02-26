from django.core.exceptions import ValidationError
import os


def get_path_upload_cover(instance, file):
    upload_to = "covers"
    ext = file.split(".")[-1]
    file = f"{instance.cover}.{ext}"
    return os.path.join(upload_to, file)


def validate_size_image(file_object):
    size_limit = 4
    if file_object.size > size_limit * 1024 * 1024:
        raise ValidationError(f"Максимальный размер {size_limit}MB")
