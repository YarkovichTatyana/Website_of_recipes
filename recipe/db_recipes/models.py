from django.contrib.auth.models import *
from django.db import models

class Recipes(models.Model):
    title = models.CharField (max_length=100, verbose_name='Название рецепта')
    compound = models.TextField(max_length=500, verbose_name='Ингридиенты')
    cooking = models.TextField(max_length=2000, verbose_name='Процесс приготовления')

    def __str__(self):
        return self.title

    class Meta:
        db_table='recipe'
        verbose_name='Рецепт'
        verbose_name_plural = 'Рецепты'



class Ingredientes(models.Model):
    ingredient = models.CharField (max_length=100, verbose_name='Ингридиент')
    calories = models.FloatField (verbose_name='Ккал на 100гр')
    price = models.FloatField(verbose_name='Цена за 100 гр', default=0)
    amount = models.FloatField(verbose_name='Кол-во, гр', default=0)

    def __str__(self):
        return self.ingredient
    class Meta:
        verbose_name='Ингредиент'
        verbose_name_plural = 'Ингредиенты'
#
# class Calculation(models.Model):
#     ingredient = models.CharField (max_length=100, verbose_name='Ингридиент')
#     calories = models.IntegerField (verbose_name='Ккал на 100гр')
#     price = models.IntegerField(verbose_name='Цена за 100 гр')
#     amount = models.IntegerField(verbose_name='Кол-во, гр')
#     total_price=models.FloatField(verbose_name='Стоимость позиции, руб', default=0)
#     total_calories = models.FloatField(verbose_name='Калорийность позиции', default=0)
#
#     def get_absolute_url(self):
#         return "/db_recipes/ingredient"
#
#     def __str__(self):
#         return self.ingredient
#
#     class Meta:
#         verbose_name='Калькулятор'
#         verbose_name_plural = 'Калькулятор'
#
#
# class Comments(models.Model):
#     recipe = models.ForeignKey(Recipes, on_delete=models.CASCADE, verbose_name='Рецепт', blank=True, null=True, related_name='comments_recipes')
#     author = models.ForeignKey(User, on_delete = models.CASCADE, verbose_name='Автор комментария', blank = True, null = True )
#     create_date = models.DateTimeField(auto_now=True)
#     text = models.TextField(verbose_name='Текст комментария')
#     status = models.BooleanField(verbose_name='Видимость статьи', default=False)
