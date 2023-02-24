from django.contrib.auth.models import BaseUserManager


class UserManager(BaseUserManager):
    def _create_user(self, username, password, nickname, **extra_fields):
        if not username:
            raise ValueError("Users must have a username.")
        user = self.model(
            username=username,
            nickname=nickname,
            **extra_fields,
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, username, password, nickname, **extra_fields):
        return self._create_user(username, password, nickname, **extra_fields)

    def create_superuser(self, username, nickname, password):
        return self._create_user(
            username,
            password,
            nickname,
            is_staff=True,
            is_superuser=True,
        )
