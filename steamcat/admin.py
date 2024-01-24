from django.contrib import admin
from .models import *

@admin.register(Games)
class GamesAdmin(admin.ModelAdmin):
    list_display = ["id", "game", "year", "price", "time_create", "time_update", "is_published", "cat"]
    list_display_links = ["id", "game"]
    list_editable = "is_published",
    list_per_page = 5
    ordering = "time_create", "game"

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ["id", "name", "slug"]
    list_per_page = 5
    list_display_links = ["id", "name"]
    ordering = ["id"]