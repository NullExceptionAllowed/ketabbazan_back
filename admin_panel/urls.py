from django.urls import path

from admin_panel.views import Comment

urlpatterns = [
    path('comment/', Comment.as_view()),
]