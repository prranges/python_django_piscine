from django.urls import path
from .views import display

urlpatterns = [
    path('display/', display, name='ex09_display'),
]