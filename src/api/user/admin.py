from django.contrib import admin
from ..user.models import User

admin.site.regsiter(User)