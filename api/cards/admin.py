# django imports
from django.contrib import admin
from django.utils.safestring import mark_safe

# local imports
from api.cards.models import Manga, TypeManga, GenreManga, Review


@admin.register(Manga)
class MangaAdmin(admin.ModelAdmin):
    readonly_fields = (
        "preview",
        "publish_date",
    )
    list_display_links = ("name",)
    list_filter = ("year",)
    search_fields = (
        "name",
        "nickname",
    )
    list_per_page = 12
    list_display = (
        "id",
        "name",
        "year",
        "publish_date",
        "preview",
    )

    def preview(self, obj):
        return mark_safe(f'<img src="{obj.cover.url}" style="max-height: 100px;">')


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "manga",
        "user",
        "created_date",
    )
    list_display_links = (
        "user",
        "manga",
    )
    search_fields = (
        "username",
        "text",
    )
    list_filter = (
        "manga",
        "user",
    )
    list_per_page = 12


@admin.register(GenreManga)
class GenreAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "name",
    )
    list_display_links = ("name",)
    search_fields = ("name",)
    list_per_page = 12


@admin.register(TypeManga)
class TypeAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "name",
    )
    list_display_links = ("name",)
    search_fields = ("name",)
    list_per_page = 12
