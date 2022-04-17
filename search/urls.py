from django.urls import path
from .views import Booksearch
urlpatterns = [
    path('', Booksearch.as_view())
]