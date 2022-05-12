from django.urls import path
from .views import NewestBooks, PDFRetrieval, BookInfoRetrieval, AllBooks, BuyAPI

app_name = 'read_book'

urlpatterns = [
    path('newest_books/', NewestBooks.as_view()),
    path('all_books/', AllBooks.as_view()),
    path('all_books/<page>', AllBooks.as_view()),
    path('pdf_file/<id>', PDFRetrieval.as_view()),    
    path('info/<id>', BookInfoRetrieval.as_view()),
    path('buy/<int:id>', BuyAPI.as_view()),
]