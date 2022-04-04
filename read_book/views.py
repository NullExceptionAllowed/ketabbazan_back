from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import authentication, permissions
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
        ids = [book.id for book in books]
        return Response(ids[:5])

class ImageRetrieval(generics.RetrieveAPIView):
    renderer_classes = [JPEGRenderer] 
    def get(self, request, *args, **kwargs):
        queryset = Book.objects.get(id=self.kwargs['id']).book_image
        data = queryset   
        return Response(data, content_type='image/jpg')      

class BookInfoRetrieval(APIView):
    def get(self, request, id):
        book = get_object_or_404(Book, id=id)
        book_serializer = BookInfoSerializer(instance=book)
        data = book_serializer.data
        return Response({'book_info': data})