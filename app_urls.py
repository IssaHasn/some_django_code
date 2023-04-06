from django.urls import path
from . import views

urlpatterns = [
    path('',views.login, name = 'pages/login.html'),
    path('about/',views.about, name = 'pages/about.html'),
    path('serverise',views.serverise, name = 'page/serverise.html')
]
