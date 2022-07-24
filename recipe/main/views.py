from django.shortcuts import render


def index(request):
    return render (request,'main/index.html')
def accommodation(request):
    return render (request,'main/accommodation.html')
def feedback(request):
    return render (request,'main/feedback.html')
