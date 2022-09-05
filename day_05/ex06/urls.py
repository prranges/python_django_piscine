from django.urls import path
from .views import init, populate, display, remove, update

urlpatterns = [
    path('init/', init, name='ex06_init'),
    path('populate/', populate, name='ex06_populate'),
    path('display/', display, name='ex06_display'),
    path('remove/', remove, name='ex06_remove'),
    path('update/', update, name='ex06_update'),
]