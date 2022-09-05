from django.urls import path
from .views import init, populate, display

urlpatterns = [
    path('init/', init, name='ex02_init'),
    path('populate/', populate, name='ex02_populate'),
    path('display/', display, name='ex02_display'),
]