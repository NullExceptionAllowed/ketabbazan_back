from django.urls import path
from .views import NewestBooks

app_name = 'read_book'

urlpatterns = [
    path('newest_books', NewestBooks.as_view())
]
