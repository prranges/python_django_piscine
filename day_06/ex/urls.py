from django.contrib import admin
from django.urls import path, include
from .views import index, login, registration, logout

urlpatterns = [
    path('', index, name='index'),
    path('login/', login, name='login'),
    path('registration/', registration, name='registration'),
    path('logout/', logout, name='logout'),
]