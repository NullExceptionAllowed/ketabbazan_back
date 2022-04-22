from django.urls import path
from .views import Commentapi, Replytocomment

urlpatterns = [
    path('test/', Commentapi.as_view()),
    path('replytest/', Replytocomment.as_view()),
]

