from django.urls import path
from .views import SendBook

urlpatterns = [
    path('sendbook/', SendBook.as_view()),
]
