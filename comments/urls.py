from django.urls import path
from .views import Commentapi, Replytocomment, UserComments

urlpatterns = [
    path('', Commentapi.as_view()),
    path('reply/', Replytocomment.as_view()),
    path('usercomments/', UserComments.as_view()),
]

