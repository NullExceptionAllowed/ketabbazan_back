from django.shortcuts import render
from read_book.models import Book
from read_book.serializers import BookInfoSerializer
from rest_framework.permissions import AllowAny
from rest_framework.views import APIView
from django.db.models import Q
from rest_framework.response import Response
# Create your views here.


class Booksearch(APIView):
    permission_classes = [AllowAny, ]

    def get(self,request):
        q=request.query_params['q']
        try:
            sort=int(request.query_params['sort'])
        except:
            sort=None
        books = [book for book in Book.objects.filter(Q(name__contains=q) | Q(author__name__contains=q) | Q(genre__name__contains=q)).distinct()]
        if(sort==1): #chippest books
            books.sort(key=lambda x: x.price, reverse=True)
        elif(sort==2): #most expensive books
            books.sort(key=lambda x: x.price, reverse=False)
        if(sort==3): #newset books
            books.sort(key=lambda x: x.created, reverse=True)
        ans = []
        for book in books:
            book_serializer = BookInfoSerializer(instance=book)
            data = book_serializer.data
            ans.append(data)
        return Response(ans)
