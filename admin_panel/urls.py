from django.urls import path

from admin_panel.views import Comment, VerifyComment

urlpatterns = [
    path('comment/', Comment.as_view()),
    path('comment/verify/<int:comment_id>', VerifyComment.as_view()),
]