from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from read_book.serializers import BookInfoSerializer
from read_book.models import Book
from django.views.generic import ListView
from django.views.generic.detail import SingleObjectMixin


# Create your views here.


class Advancesearch(APIView):


    def get(self, request):
        books = Book.objects.all()
        try:
            book_name = request.query_params['book_name']
        except:
            book_name = ""
        try:
            contain_book_name = True if request.query_params['ct_book_name'] == "1" else False
        except:
            contain_book_name = True
        if book_name != "":
            if contain_book_name:
                books = books.filter(name__contains=book_name)
            else:
                books = books.filter(name=book_name)

        try:
            author_name = request.query_params['author_name']
        except:
            author_name = ""
        try:
            contain_author_name = True if request.query_params['ct_author_name'] == "1" else False
        except:
            contain_author_name = True
        if author_name != "":
            if contain_author_name:
                books = books.filter(author__name__contains=author_name)
            else:
                books = books.filter(author_name=author_name)

        try:
            genre = request.query_params['genre']
        except:
            genre = ""
        if genre != "" :
            books = books.filter(genre__name=genre)
        try:
            min_price = int(request.query_params['min_price'])
        except:
            min_price = -1
        try:
            max_price = int(request.query_params['max_price'])
        except:
            max_price = 20000000
        books = \
            books.filter(price__gte=min_price , price__lte=max_price)
        ans=[]
        for book in books:
            book_serializer = BookInfoSerializer(instance=book)
            data = book_serializer.data
            data['id'] = book.id
            data['author'] = "، ".join(str(author) for author in book.author.all())
            ans.append(data)
        return Response(ans)
        return Response(books, status=status.HTTP_200_OK)