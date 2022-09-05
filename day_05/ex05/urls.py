from django.urls import path
from .views import populate, display, remove

urlpatterns = [
    path('populate/', populate, name='ex05_populate'),
    path('display/', display, name='ex05_display'),
    path('remove/', remove, name='ex05_remove'),
]