from django.contrib import admin
from .models import *


class RecipesAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'compound', 'cooking','recipe_of_month')
    list_display_links = ('id', 'title')
    search_fields = ('title', 'compound', 'cooking')
    list_editable = ('cooking','recipe_of_month')
    list_filter = ('title',)
    list_per_page = 10  # пагинация
    ordering = ('-id',)

#
class IngredientesAdmin(admin.ModelAdmin):
    list_display = ('id', 'ingredient', 'calories','description', 'price', 'amount')
    list_display_links = ('ingredient',)
    search_fields = ('ingredient',)
#

class CommentsAdmin(admin.ModelAdmin):
    list_display = ('id', 'recipe', 'author', 'create_date', 'text', 'status')
    list_display_links = ('text',)
    search_fields = ('recipe','author','status')
    list_editable = ('status',)
#
# class CalculationAdmin(admin.ModelAdmin):
#     list_display = ('id', 'ingredient', 'calories', 'price', 'amount', 'total_price', 'total_calories')

class ArticleAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'article', 'seal')
    search_fields = ('title',)
    list_editable = ('title', 'article', 'seal')
    list_filter = ('title',)
    list_per_page = 10  # пагинация
    ordering = ('-id',)

admin.site.register(Recipes, RecipesAdmin)
admin.site.register(Ingredientes, IngredientesAdmin)
admin.site.register(Comments, CommentsAdmin)
admin.site.register(Article, ArticleAdmin)
from django.contrib import admin