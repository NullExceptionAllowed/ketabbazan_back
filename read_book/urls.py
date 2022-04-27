from django.urls import path, re_path
from .views import NewestBooks, PDFRetrieval, BookInfoRetrieval, AllBooks

app_name = 'read_book'

urlpatterns = [
    path('newest_books/', NewestBooks.as_view()),
    re_path(r'all_books/(?P<page>.*)$', AllBooks.as_view()),
    path('pdf_file/<id>', PDFRetrieval.as_view()),    
    path('info/<id>', BookInfoRetrieval.as_view()),
]