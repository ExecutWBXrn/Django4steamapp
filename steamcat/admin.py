from django.contrib import admin, messages
from .models import *

@admin.register(Games)
class GamesAdmin(admin.ModelAdmin):
    list_display = ["id", "game", "year", "price", "time_create", "time_update", "is_published", "cat", "brief_info"]
    list_display_links = ["id", "game"]
    list_editable = ["is_published"]
    list_per_page = 5
    ordering = ["time_create", "game"]
    actions = ["set_published", "set_draft"]
    @admin.display(description="Фурзер інформайшен", ordering="describe")
    def brief_info(self, games: Games):
        return f"{len(games.describe)} символів в описі"
    @admin.action(description="PUBLISHED")
    def set_published(self, request, queryset):
        count = queryset.update(is_published=Games.Status.PUBLISHED)
        self.message_user(request, f"Опубліковано {count} записів")

    @admin.action(description="DRAFT")
    def set_draft(self, request, queryset):
        count = queryset.update(is_published=Games.Status.DRAFT)
        self.message_user(request, f"{count} записів деопубліковано", messages.WARNING)



@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ["id", "name", "slug"]
    list_per_page = 5
    list_display_links = ["id", "name"]
    ordering = ["id"]