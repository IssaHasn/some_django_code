from django.shortcuts import render
from .models import Book, Type, Users_data

def about(request):
    return render(request, 'pages/about.html',{'book':Book.objects.all(),'type':Type.objects.all()})

def login(request):
    user = request.POST.get('user')
    password = request.POST.get('password')
    login = Users_data(user = user, password = password)
    login.save()
    return render(request, 'pages/login.html')



def serverise(request):
    return render(request, 'pages/serverise.html')
# Create your views here.