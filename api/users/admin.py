from django.contrib import admin
from ..users.models import User

from django.utils.safestring import mark_safe


class UserAdmin(admin.ModelAdmin):
    fields = [
        "username",
        "nickname",
        "avatar",
        "preview",
        "is_staff",
        "is_active",
        "is_superuser",
    ]
    readonly_fields = ["preview"]
    list_display = [
        "id",
        "username",
        "preview",
        "nickname",
        "is_staff",
    ]
    list_display_links = [
        "username",
    ]
    list_filter = [
        "username",
    ]
    search_fields = [
        "username",
    ]

    def preview(self, obj):
        return mark_safe(f'<img src="{obj.avatar.url}" style="max-height: 100px;">')


admin.site.register(User, UserAdmin)
