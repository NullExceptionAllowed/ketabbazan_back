from django.shortcuts import render

# Create your views here.
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAdminUser
from rest_framework.views import APIView

from admin_panel.serializers import CommentSerializer
from comments.models import Comment as CommentModel


class Comment(APIView):
    permission_classes = (IsAdminUser,)

    def get(self, request):
        per_page = 20
        try:
            page = max(1, int(request.query_params['page']))
        except:
            page = 1
        comments = CommentModel.objects.order_by('-id').all()[(page - 1) * per_page:page * per_page]
        res = CommentSerializer(comments, many=True)

        return Response(res.data, status=status.HTTP_200_OK)


class VerifyComment(APIView):
    permission_classes = (IsAdminUser,)

    def post(self, request, comment_id):
        comment = CommentModel.objects.get(pk=comment_id)
        comment.is_verified = not comment.is_verified
        comment.save()

        res = CommentSerializer(comment)

        return Response(res.data, status=status.HTTP_200_OK)
