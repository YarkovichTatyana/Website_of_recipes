from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('accommodation', views.accommodation, name='accommodation'),
    # path('calculator', views.calculator, name='calculator'),
    path('feedback', views.feedback, name='feedback'),
    # path('private', views.private, name='private'),
    # path('recipe_month', views.recipe_month, name='recipe_month'),
    ]
