from django.views.generic import TemplateView


class DjangoPageView(TemplateView):
    template_name = "ex01/django.html"


class TemplatesPageView(TemplateView):
    template_name = "ex01/templates.html"


class DisplayPageView(TemplateView):
    template_name = "ex01/display.html"
