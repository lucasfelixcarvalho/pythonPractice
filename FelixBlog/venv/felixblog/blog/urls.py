from django.conf.urls import url, include
from .views import(
    ArticleListView
)

app_name = 'blog'
urlpatterns = [
    url('', ArticleListView.as_view(), name='article-list')
]