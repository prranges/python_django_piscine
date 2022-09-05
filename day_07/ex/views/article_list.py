# views.py
from django.views.generic import ListView
from ..models.models import Article 

class ArticleListView(ListView):
    model = Article
    context_object_name = 'articles.html'
    template_name = 'articles.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["object_list"] = Article.objects.all().order_by('-created')
        return context