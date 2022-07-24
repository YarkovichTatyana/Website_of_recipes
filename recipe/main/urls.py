from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('accommodation', views.accommodation, name='accommodation'),
    path('feedback', views.feedback, name='feedback'),
    ]
