from django.urls import path
from .views import init, populate, display, remove

urlpatterns = [
    path('init/', init, name='ex04_init'),
    path('populate/', populate, name='ex04_populate'),
    path('display/', display, name='ex04_display'),
    path('remove/', remove, name='ex04_remove'),
]