from django.contrib import admin
from .models import Category, Recipe

@admin.register(Category, Recipe)

class CategoryAdmin (admin.ModelAdmin):
    ''''''

class RecipeAdmin (admin.ModelAdmin):
    ''''''
