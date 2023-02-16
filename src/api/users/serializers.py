# django imports
from rest_framework import serializers
from django.core.validators import FileExtensionValidator

# package imports
from phonenumber_field.serializerfields import PhoneNumberField

# local imports
from ..users.models import User
from ..users.services import PasswordFieldService


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            "username",
            "email",
            "is_staff",
            "is_active",
            "is_superuser",
            "date_joined",
        )
        read_only_fields = ("date_joined",)


class RegisterSerializers(serializers.ModelSerializer):
    username = serializers.CharField(
        max_length=100, required=True, help_text="max length 100"
    )
    nickname = serializers.CharField(
        max_length=50, required=True, help_text="max length 50"
    )
    email = serializers.EmailField()
    password = PasswordFieldService(
        min_length=8,
        max_length=25,
        write_only=True,
        required=True,
        help_text="min length 8, max length 25",
    )

    class Meta:
        model = User
        fields = [
            "username",
            "email",
            "nickname",
            "password",
            "avatar",
        ]
        read_only_fields = ("date_joined",)

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)


class LoginSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=255, required=True)
    password = PasswordFieldService(
        max_length=25, min_length=8, write_only=True, required=True
    )
