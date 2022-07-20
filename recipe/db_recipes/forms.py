from .models import *
from django.forms import ModelForm, TextInput, NumberInput, Textarea
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from  django import forms
from  django.contrib.auth.models import User


class RecipesForm(forms.ModelForm):
    class Meta:
        model=Recipes
        fields=['title','compound', 'cooking']
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'form-control'

class AuthUserForm(AuthenticationForm, forms.ModelForm):
    class Meta:
        model = User
        fields = ('username','password')
    # def __init__(self,*args,**kwargs):
    #     super().__init__(*args,**kwargs)
    #     for field in self.fields:
    #         self.fields[field].widget.attrs['class'] = 'form-control'

class RegisterUserForm(UserCreationForm):
    username = forms.CharField(label='Логин', widget=forms.TextInput(attrs={'class': 'form-input'}))
    email = forms.EmailField(label='Email', widget=forms.EmailInput(attrs={'class': 'form-input'}))
    password1 = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class': 'form-input'}))
    password2 = forms.CharField(label='Повтор пароля', widget=forms.PasswordInput(attrs={'class': 'form-input'}))

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

class LoginUserForm(AuthenticationForm):
    username = forms.CharField(label='Логин', widget=forms.TextInput(attrs={'class': 'form-input'}))
    password = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class': 'form-input'}))

class IngredientesForm(forms.ModelForm):
    class Meta:
        model = Ingredientes
        fields = ['ingredient', 'calories', 'price', 'amount']

        widgets = {
            'ingredient': TextInput(attrs={
                'class': 'form-control',
                'placeholder': "название"
            }),
            'calories': NumberInput(attrs={
                'class': 'form-control',
                'placeholder': "Калорийность продукта"
            }),
            'price': NumberInput(attrs={
                'class': 'form-control',
                'placeholder': "Цена в рублях за 100 гр "
            }),
            'amount': NumberInput(attrs={
                'class': 'form-control',
                'placeholder': "Количество в граммах"
            })
        }
