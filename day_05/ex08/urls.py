from django.urls import path
from .views import init, populate, display

urlpatterns = [
    path('init/', init, name='ex08_init'),
    path('populate/', populate, name='ex08_populate'),
    path('display/', display, name='ex08_display'),
]