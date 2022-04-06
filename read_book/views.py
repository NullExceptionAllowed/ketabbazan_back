from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Book
from rest_framework import generics
from read_book.custom_renderers import JPEGRenderer
from .serializers import BookInfoSerializer

class NewestBooks(APIView):
    authentication_classes = []
    permission_classes = []

    def get(self, request, format=None):
        books = [book for book in Book.objects.all()]
        books.sort(key = lambda x : x.created, reverse=True)
        ans = []
        for book in books:
            book_serializer = BookInfoSerializer(instance=book)
            data = book_serializer.data
            ans.append(data)
        return Response(ans[:5])

class PDFRetrieval(APIView):
    def get(self, request, id):
        book = get_object_or_404(Book, id=id)    
        return Response(book.pdf_url)    