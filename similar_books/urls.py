from django.urls import path
from .views import SimilarBooks, OthersRead

app_name = 'similar_books'

urlpatterns = [   
    path('<id>', SimilarBooks.as_view()),
    path('others_read/<id>', OthersRead.as_view())
]