from django.urls import path
from .views import populate, display, remove, update

urlpatterns = [
    path('populate/', populate, name='ex07_populate'),
    path('display/', display, name='ex07_display'),
    path('remove/', remove, name='ex07_remove'),
    path('update/', update, name='ex07_update'),
]