from django.urls import path
from . import views
# from recipe.db_recipes.templates.db_recipes import views


urlpatterns = [
    path('', views.all_recipes, name='all_recipes'),
    path('calculator', views.calculator, name='calculator'),
    path('recipe_month', views.recipe_month, name='recipe_month'),
    path('ingredient', views.ingredient, name='ingredient'),
    path('<int:pk>', views.RecipesDetailView.as_view(), name='recipe-detail'),
    path('ingredient/<int:pk>', views.IngredientesDetailView.as_view(), name='ingredient_details'),
    # path('ingredient/update/<int:pk>', views.CalculationUpdateView.as_view(), name='update'),
    # path('ingredient/delete/<int:pk>', views.CalculationDeleteView.as_view(), name='delete'),
    # path('update_page/<int:pk>', views.RecipesUpdateView.as_view(), name='update_page'),
    # path('delete_page/<int:pk>', views.RecipesDeleteView.as_view(), name='delete_page'),
    path('', views.all_recipes,name='search'),
    path('edit_page', views.RecipesCreateView.as_view(), name='edit_page'),
    path('register', views.RegisterUser.as_view(), name='register'),
    path('login', views.LoginUser.as_view(), name='login'),
    path('logout', views.logout_user, name='logout'),

    # path('login', views.MyprojectLoginView.as_view(), name='login_page'),
    # path('<int:pk>', views.RecipesDetailView.as_view(), name='create'),
]