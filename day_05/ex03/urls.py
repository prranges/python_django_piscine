from django.urls import path
from .views import populate, display

urlpatterns = [
    path('populate/', populate, name='ex03_populate'),
    path('display/', display, name='ex03_display'),
]