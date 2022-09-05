from django.urls import path
from .views import DjangoPageView
from .views import TemplatesPageView
from .views import DisplayPageView

urlpatterns = [
    path("django", DjangoPageView.as_view(), name="django"),
    path("templates", TemplatesPageView.as_view(), name="templates"),
    path("display", DisplayPageView.as_view(), name="display"),

]