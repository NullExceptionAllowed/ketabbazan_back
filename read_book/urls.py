from tkinter import Image
from django.urls import path
from .views import NewestBooks, ImageRetrieval, BookInfoRetrieval

app_name = 'read_book'

urlpatterns = [
    path('newest_books', NewestBooks.as_view()),
    path('image/<id>', ImageRetrieval.as_view()),
    path('info/<id>', BookInfoRetrieval.as_view())
]
