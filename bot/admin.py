from django.contrib import admin
from django.contrib.auth.models import Group
from .models import Ingredient, Food


@admin.register(Ingredient)
class IngredientAdmin(admin.ModelAdmin):

    list_display = ['name']


@admin.register(Food)
class FoodAdmin(admin.ModelAdmin):

    list_display = ['name', 'cooking_time']


admin.site.site_header = "Food Bot"
admin.site.unregister(Group)
