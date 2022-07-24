from django.contrib.auth import logout, login
from django.shortcuts import render, redirect, HttpResponseRedirect
from django.views.generic import DetailView, DeleteView, UpdateView, CreateView
from .forms import *
from django.views.generic.edit import FormMixin
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from .utils import *
from django.contrib.auth.mixins import LoginRequiredMixin



def all_recipes(request):
    search_guery = request.GET.get('q', '')
    if search_guery:
        rec = Recipes.objects.filter(title__icontains=search_guery)
    else:
        rec = Recipes.objects.order_by('-id')
    return render(request, 'db_recipes/all_recipes.html', {'rec': rec})


def calculator(request):
    return render(request, 'db_recipes/calculator.html')

def ingredient(request):
    list = Article.objects.filter(seal='yes')
    search_guery = request.GET.get('q', '')
    if search_guery:
        ing = Ingredientes.objects.filter(ingredient__icontains=search_guery).values()
    else:
        ing = Ingredientes.objects.order_by('ingredient')
    return render(request, 'db_recipes/ingredient.html', {'ing': ing,'list':list})

def articles(request):
    list = Article.objects.filter(seal='no').order_by('-id')
    return render(request, 'db_recipes/articles.html', {'list':list})


class ArticlesDetailView(FormMixin,DetailView):
    model = Article
    template_name = 'db_recipes/articles-detail.html'
    context_object_name = 'all'
    form_class = ArticleForm


def recipe_month(request):
    rec = Recipes.objects.filter(recipe_of_month='yes')
    return render(request, 'db_recipes/recipe_month.html', {'rec': rec})


class IngredientesDetailView(DetailView):
    model = Ingredientes
    template_name = 'db_recipes/details_ingredient.html'
    context_object_name = 'article'


class RecipesDetailView(FormMixin,DetailView):
    model = Recipes
    template_name = 'db_recipes/details_view.html'
    context_object_name = 'article'
    form_class = CommentForm

    def post(self, request, *args, **kwargs):
        form = self.get_form()
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

    def get_success_url(self,**kwargs):
        return reverse_lazy('recipe-detail', kwargs={'pk': self.get_object().id})

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.recipe = self.get_object()
        self.object.author = self.request.user
        self.object.save()
        return (super().form_valid(form))

class RecipesCreateView(LoginRequiredMixin, CreateView):
    model = Recipes
    template_name = 'db_recipes/edit_page.html'
    form_class = RecipesForm
    success_url = reverse_lazy('edit_page')

    def get_context_data(self, **kwargs):
        kwargs['rec'] = Recipes.objects.filter(author=self.request.user).order_by('-id')
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.author = self.request.user
        self.object.save()
        return super().form_valid(form)


class RecipesUpdateView(LoginRequiredMixin, UpdateView):
    model = Recipes
    template_name = 'db_recipes/update.html'
    form_class = RecipesForm
    success_url = reverse_lazy('edit_page')

    def get_context_data(self, **kwargs):
        kwargs['update'] = True
        return super().get_context_data(**kwargs)
    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        if self.request.user != kwargs['instance'].author:
            return self.handle_no_permission()
        return kwargs

class RecipesDeleteView(LoginRequiredMixin, DeleteView):
    model = Recipes
    template_name = 'db_recipes/delete.html'
    success_url = reverse_lazy('edit_page')

    def delete(self, request, *args, **kwargs):
        success_url = self.get_success_url()
        self.object.delete()
        return HttpResponseRedirect(success_url)



class RegisterUser(DataMixin, CreateView):
    form_class = RegisterUserForm
    template_name = 'db_recipes/register.html'
    success_url = reverse_lazy('login')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Регистрация")
        return dict(list(context.items()) + list(c_def.items()))

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('index')


class LoginUser(DataMixin, LoginView):
    form_class = LoginUserForm
    template_name = 'db_recipes/login.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Авторизация")
        return dict(list(context.items()) + list(c_def.items()))

    def get_success_url(self):
        return reverse_lazy('index')


def logout_user(request):
    logout(request)
    return redirect('login')


