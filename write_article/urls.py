from django.urls import path
from .views import ArticleList, ArticleDetail, NewestArticles

app_name = 'write_article'

urlpatterns = [
    path('', ArticleList.as_view()),
    path('<int:pk>/', ArticleDetail.as_view()),
    path('newest_articles/', NewestArticles.as_view()),
]