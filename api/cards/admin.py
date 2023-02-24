from django.contrib import admin
from ..cards.models import Manga, TypeManga, GenreManga

admin.site.register(Manga)
admin.site.register(TypeManga)
admin.site.register(GenreManga)
