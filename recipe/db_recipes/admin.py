from django.contrib import admin
from .models import *


class RecipesAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'compound', 'cooking')
    list_display_links = ('id', 'title')
    search_fields = ('title', 'compound', 'cooking')
    list_editable = ('cooking',)
    list_filter = ('title',)
    list_per_page = 3  # пагинация
    ordering = ('-id',)

#
# class IngredientesAdmin(admin.ModelAdmin):
#     list_display = ('id', 'ingredient', 'calories', 'price', 'amount')
#     list_display_links = ('ingredient',)
#     search_fields = ('ingredient',)
#
#
# class CalculationAdmin(admin.ModelAdmin):
#     list_display = ('id', 'ingredient', 'calories', 'price', 'amount', 'total_price', 'total_calories')


admin.site.register(Recipes, RecipesAdmin)
# admin.site.register(Ingredientes, IngredientesAdmin)
# admin.site.register(Calculation, CalculationAdmin)
from django.contrib import admin