from django.urls import path
from .views import historyPageView

urlpatterns = [
    path("", historyPageView, name="index"),
]