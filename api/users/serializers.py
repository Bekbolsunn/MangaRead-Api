# django imports
from rest_framework import serializers

# local imports
from api.users.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            "id",
            "username",
            "nickname",
            "avatar",
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
    password = serializers.CharField(
        min_length=8,
        max_length=25,
        write_only=True,
        required=True,
        style={"input_type": "password"},
        help_text="min length 8, max length 25",
    )

    class Meta:
        model = User
        fields = [
            "id",
            "username",
            "nickname",
            "password",
            "avatar",
        ]
        read_only_fields = ("id",)

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)


class LoginSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=255, required=True)
    password = serializers.CharField(
        max_length=25,
        min_length=8,
        write_only=True,
        required=True,
        style={"input_type": "password"},
        help_text="min length 8, max length 25",
    )
