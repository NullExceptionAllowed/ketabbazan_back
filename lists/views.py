from django.shortcuts import render
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from read_book.models import Book
from read_book.serializers import BookInfoSerializer
from accounts.models import User
# Create your views here.


class Addtopast_read(APIView):
    permission_classes = [IsAuthenticated, ]

    def post(self, request):
        book_id = request.data['book']
        book = Book.objects.get(id=book_id)
        request.user.past_read.add(book)
        request.user.save()
        return Response(status=status.HTTP_200_OK )

    def get(self, request):
        books = [book for book in request.user.past_read.all()]
        ans = []
        for book in books:
            book_serializer = BookInfoSerializer(instance=book)
            data = book_serializer.data
            data['id'] = book.id
            data['author'] = "، ".join(str(author) for author in book.author.all())
            ans.append(data)
        return Response(ans)

    def delete(self, request):
        book_id = request.data['book']
        book = Book.objects.get(id=book_id)
        request.user.past_read.remove(book)
        return Response(status=status.HTTP_200_OK)
