from django.urls import path
from .views import SendBook, ShowReceivedGift, ShowSendGift

urlpatterns = [
    path('sendbook/', SendBook.as_view()),
    path('allreceivedgifts/', ShowReceivedGift.as_view()),
    path('allsendgifts/', ShowSendGift.as_view())
]
