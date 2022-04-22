from django.urls import path
from .views import SimilarBooks

app_name = 'similar_books'

urlpatterns = [   
    path('<id>', SimilarBooks.as_view()),
]