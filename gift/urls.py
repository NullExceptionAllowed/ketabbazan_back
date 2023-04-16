from django.urls import path
from .views import SendBook, ShowReceivedGift

urlpatterns = [
    path('sendbook/', SendBook.as_view()),
    path('allreceivedgifts/', ShowReceivedGift.as_view()),
]
