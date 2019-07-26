from django.shortcuts import get_object_or_404, get_list_or_404, render
from django.urls import reverse
from django.views.generic import(
    CreateView,
    DeleteView,
    DetailView,
    ListView,
    UpdateView,
)
from .models import Article

# Create your views here.
class ArticleListView(ListView):
    template_name = 'article/home.html'
    queryset = Article.objects.all()