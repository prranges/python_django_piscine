from django.urls import path
from .views import init

urlpatterns = [
    path('init/', init, name='ex00_init'),
]