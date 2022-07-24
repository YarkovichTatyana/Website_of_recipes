from django.contrib.auth.models import *
from django.db import models

class Recipes(models.Model):
    author = models.ForeignKey(User, on_delete = models.CASCADE, verbose_name='Автор', blank = True, null = True, related_name='author')
    title = models.CharField (max_length=100, verbose_name='Название рецепта')
    compound = models.TextField(max_length=500, verbose_name='Ингрeдиенты')
    cooking = models.TextField(max_length=2000, verbose_name='Процесс приготовления')
    recipe_of_month = models.CharField (max_length=100, verbose_name='Отметка "рецепт" месяца', default='no')

    def __str__(self):
        return self.title

    class Meta:
        db_table='recipe'
        verbose_name='Рецепт'
        verbose_name_plural = 'Рецепты'

class Comments(models.Model):
    recipe = models.ForeignKey(Recipes, on_delete=models.CASCADE, verbose_name='Рецепт', blank=True, null=True, related_name='comments_recipes')
    author = models.ForeignKey(User, on_delete = models.CASCADE, verbose_name='Автор', blank = True, null = True )
    create_date = models.DateTimeField(auto_now=True)
    text = models.TextField(verbose_name='Текст комментария')
    status = models.BooleanField(verbose_name='Видимость статьи', default=False)


class Ingredientes(models.Model):
    ingredient = models.CharField (max_length=100, verbose_name='Ингрeдиент')
    calories = models.FloatField (verbose_name='Ккал на 100гр')
    description =models.TextField(verbose_name='Описание',default='Описание')
    price = models.FloatField(verbose_name='Цена за 100 гр', default=0)
    amount = models.FloatField(verbose_name='Кол-во, гр', default=0)

    def __str__(self):
        return self.ingredient
    class Meta:
        verbose_name='Ингредиент'
        verbose_name_plural = 'Ингредиенты'

class Article(models.Model):
    title = models.CharField (max_length=100, verbose_name='Название статьи')
    article = models.TextField(max_length=5000, verbose_name='Статья')
    seal = models.CharField (max_length=100, verbose_name='Текущая статья', default='no')

    def __str__(self):
        return self.title

    class Meta:
        db_table='article'
        verbose_name='Статья'
        verbose_name_plural = 'Статьи'