from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return render (request,'main/index.html')
def accommodation(request):
    return render (request,'main/accommodation.html')
# def calculator(request):
#     return render (request,'main/calculator.html')
def feedback(request):
    return render (request,'main/feedback.html')
# def private(request):
#     return render (request,'main/register.html')
# def recipe_month(request):
#     return render (request,'main/recipe_month.html')
# def login_page (request):
#     return render(request, 'db_recipes/login.html')