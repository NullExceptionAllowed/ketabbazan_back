from django.shortcuts import render
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, viewsets

import accounts.serializers
from read_book.models import Book
from read_book.serializers import BookInfoSerializer
from accounts.models import User


# Create your views here.


def all_books(books):
    ans = []
    for book in books:
        book_serializer = BookInfoSerializer(instance=book)
        data = book_serializer.data
        data['id'] = book.id
        data['author'] = "، ".join(str(author) for author in book.author.all())
        ans.append(data)
    return ans


class add_to_list(APIView):
    def post(self, request):
        try:
            list_id = request.data['list_id']
        except:
            return Response({"message": "select a list"}, status=status.HTTP_400_BAD_REQUEST)
        try:
            book_id = request.data['book_id']
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        book = Book.objects.get(id=book_id)
        if list_id == 1:
            request.user.past_read.add(book)
        elif list_id == 2:
            request.user.cur_read.add(book)
        elif list_id == 3:
            request.user.favourite.add(book)
        elif list_id == 4:
            request.user.left_read.add(book)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        return Response(status=status.HTTP_200_OK)

class StandardResultsSetPagination(PageNumberPagination):
    page_size = 1
    page_size_query_param = 'page_size'
    max_page_size = 10

class get_books_of_list(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookInfoSerializer
    pagination_class = StandardResultsSetPagination

    def list(self, request, *args, **kwargs):
        return super().list(request.user.past_read.all())

