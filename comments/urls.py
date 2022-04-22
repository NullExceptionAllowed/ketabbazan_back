from django.urls import path
from .views import Commentapi, Replytocomment

urlpatterns = [
    path('', Commentapi.as_view()),
    path('reply/', Replytocomment.as_view()),
]

