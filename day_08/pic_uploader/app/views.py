from django.http import HttpResponse
from django.views.generic import ListView, FormView
from .models import UploadImage
from .forms import UserImageForm


class IndexView(ListView, FormView):
    success_url = '/'
    template_name = 'app/index.html'
    form_class = UserImageForm
    model = UploadImage
    queryset = model.objects.all().order_by('-id')

    def form_valid(self, form: UserImageForm) -> HttpResponse:
        form.save()
        return super().form_valid(form)

    def form_invalid(self, form: UserImageForm) -> HttpResponse:
        print(form.errors)
        return super().form_invalid(form)