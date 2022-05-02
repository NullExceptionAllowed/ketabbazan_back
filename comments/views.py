from django.shortcuts import render
# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response
from comments.models import Comment, Replycomment
from rest_framework import status
from comments.serializers import Commentserializer, Allcommentsserializer, Replyserializer
from rest_framework.permissions import AllowAny, IsAuthenticated
from read_book.models import Book


class Commentapi(APIView):
    permission_classes = [IsAuthenticated, ]
    def post(self, request):
        request.data['user'] = request.user.id
        ser_comment = Commentserializer(data=request.data)
        if ser_comment.is_valid():
            ser_comment.save()
            return Response(ser_comment.data, status=status.HTTP_200_OK)
        else:
            return Response(ser_comment.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request):
        book = Book.objects.get(id=request.query_params['id'])
        book_comments = Allcommentsserializer(book)
        return Response(book_comments.data, status=status.HTTP_200_OK)


class Replytocomment(APIView):
    permission_classes = [IsAuthenticated, ]

    def post(self, request):
        request.data['user'] = request.user.id
        ser_reply = Replyserializer(data=request.data)
        if ser_reply.is_valid():
            ser_reply.save()
            return Response(ser_reply.data, status=status.HTTP_200_OK)
        else:
            return Response(ser_reply.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request):
        comment_id = request.query_params['comment_id']
        comment = Comment.objects.get(id=comment_id)
        result=[]
        for reply in comment.replycomment_set.all():
            ser_comment = Replyserializer(reply)
            result.append(ser_comment.data)

        return Response(data=result, status=status.HTTP_200_OK)




