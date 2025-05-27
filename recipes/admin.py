from django.contrib import admin
from .models import Category, Recipe

@admin.register(Category)

class CategoryAdmin (admin.ModelAdmin):
    ''''''


@admin.register(Recipe)
class RecipeAdmin (admin.ModelAdmin):
    list_display = ['id', 'title', 'is_published', 'created_at']
    list_display_links = ['id', 'title', 'created_at']
    search_fields = ['id', 'tilte', 'slug', 'preparation_steps']
    list_filter = ['category', 'author', 'is_published', 'preparation_steps_is_html']
    list_per_page = 10
    list_editable = ['is_published']
    ordering = ['-id']
    prepopulated_fields = {
        "slug": ('title',)
    }