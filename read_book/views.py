from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Book
from rest_framework import generics
from read_book.custom_renderers import JPEGRenderer
from .serializers import BookInfoSerializer

class AllBooks(APIView):
    authentication_classes = []
    permission_classes = []

    def get(self, request, page):
        books = [book for book in Book.objects.all()]
        books.sort(key = lambda x : x.created, reverse=True)
        ans = []
        iteratingset = books
        if len(page) > 0:
            page = int(page)
            iteratingset = books[(page - 1) * 16 : page * 16]
        for book in iteratingset:
            book_serializer = BookInfoSerializer(instance=book)
            data = book_serializer.data
            data['id'] = book.id
            data['author'] = "، ".join(str(author) for author in book.author.all())
            ans.append(data)
        return Response(ans)    

class NewestBooks(APIView):
    authentication_classes = []
    permission_classes = []

    def get(self, request, format=None):
        books = [book for book in Book.objects.all()]
        books.sort(key = lambda x : x.created, reverse=True)
        ans = []
        for book in books[:10]:
            book_serializer = BookInfoSerializer(instance=book)
            data = book_serializer.data
            data['id'] = book.id
            data['author'] = book.getwriters()
            ans.append(data)
        return Response(ans)

class PDFRetrieval(APIView):
    def get(self, request, id):
        book = get_object_or_404(Book, id=id)    
        return Response(book.pdf_url)    

class BookInfoRetrieval(APIView):
    def get(self, request, id):
        book = get_object_or_404(Book, id=id)
        book_serializer = BookInfoSerializer(instance=book)
        data = book_serializer.data
        data['id'] = book.id
        data['author'] = book.getwriters()
        return Response({'book_info': data})        