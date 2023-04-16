from django.urls import path
from .views import SendBook, ShowReceivedGift, ShowSendGift, HasUnreadMessage

urlpatterns = [
    path('sendbook/', SendBook.as_view()),
    path('allreceivedgifts/', ShowReceivedGift.as_view()),
    path('allsendgifts/', ShowSendGift.as_view()),
    path('hasunread/', HasUnreadMessage.as_view())
]
