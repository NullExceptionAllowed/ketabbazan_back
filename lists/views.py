from django.shortcuts import render
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
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


class user_past_read(APIView):
    permission_classes = [IsAuthenticated, ]

    def post(self, request):
        book_id = request.data['book']
        book = Book.objects.get(id=book_id)
        if request.user.cur_read.filter(id=book_id).exists():
            return Response({"message": "this book is in cur read list"}, status=status.HTTP_400_BAD_REQUEST)
        elif request.user.favourite.filter(id=book_id).exists():
            return Response({"message": "this book in favourite list"}, status=status.HTTP_405_METHOD_NOT_ALLOWED)
        request.user.past_read.add(book)
        request.user.save()
        return Response({"message": "book add successfully"}, status=status.HTTP_200_OK)

    def get(self, request):
        books = [book for book in request.user.past_read.all()]
        ans = all_books(books)
        return Response(ans, status=status.HTTP_200_OK)

    def delete(self, request):
        book_id = request.data['book']
        book = Book.objects.get(id=book_id)
        request.user.past_read.remove(book)
        return Response(status=status.HTTP_200_OK)


class user_cur_read(APIView):
    permission_classes = [IsAuthenticated, ]

    def post(self, request):
        book_id = request.data['book']
        book = Book.objects.get(id=book_id)
        if request.user.past_read.filter(id=book_id).exists():
            return Response({"message": "this book is in past read list"}, status=status.HTTP_406_NOT_ACCEPTABLE)
        elif request.user.favourite.filter(id=book_id).exists():
            return Response({"message": "this book is in cur read list"}, status=status.HTTP_400_BAD_REQUEST)
        request.user.cur_read.add(book)
        request.user.save()
        return Response({"message": "book add successfully"}, status=status.HTTP_200_OK)

    def get(self, request):
        books = [book for book in request.user.cur_read.all()]
        ans = all_books(books)
        return Response(ans, status=status.HTTP_200_OK)

    def delete(self, request):
        book_id = request.data['book']
        book = Book.objects.get(id=book_id)
        request.user.cur_read.remove(book)
        return Response(status=status.HTTP_200_OK)


class user_favourite(APIView):
    permission_classes = [IsAuthenticated, ]

    def post(self, request):
        book_id = request.data['book']
        book = Book.objects.get(id=book_id)
        if request.user.past_read.filter(id=book_id).exists():
            return Response({"message": "this book is in past read list"}, status=status.HTTP_406_NOT_ACCEPTABLE)
        elif request.user.cur_read.filter(id=book_id).exists():
            return Response({"message": "this book is in cur read list"}, status=status.HTTP_400_BAD_REQUEST)
        request.user.favourite.add(book)
        request.user.save()
        return Response({"message": "book add successfully"}, status=status.HTTP_200_OK)

    def get(self, request):
        books = [book for book in request.user.favourite.all()]
        ans = all_books(books)
        return Response(ans, status=status.HTTP_200_OK)

    def delete(self, request):
        book_id = request.data['book']
        book = Book.objects.get(id=book_id)
        request.user.favourite.remove(book)
        return Response(status=status.HTTP_200_OK)

class user_left_read(APIView):
    permission_classes = [IsAuthenticated, ]

    def post(self, request):
        book_id = request.data['book']
        book = Book.objects.get(id=book_id)
        if request.user.cur_read.filter(id=book_id).exists():
            return Response({"message": "this book is in cur read list"}, status=status.HTTP_400_BAD_REQUEST)
        elif request.user.favourite.filter(id=book_id).exists():
            return Response({"message": "this book in favourite list"}, status=status.HTTP_405_METHOD_NOT_ALLOWED)
        request.user.past_read.add(book)
        request.user.save()
        return Response({"message": "book add successfully"}, status=status.HTTP_200_OK)

    def get(self, request):
        books = [book for book in request.user.past_read.all()]
        ans = all_books(books)
        return Response(ans, status=status.HTTP_200_OK)

    def delete(self, request):
        book_id = request.data['book']
        book = Book.objects.get(id=book_id)
        request.user.past_read.remove(book)
        return Response(status=status.HTTP_200_OK)


class pastread_anyway(APIView):
    permission_classes = [IsAuthenticated, ]

    def post(self, request):
        book_id = request.data['book']
        book = Book.objects.get(id=book_id)
        if request.user.favourite.filter(id=book_id).exists():
            request.user.favourite.remove(book)
        elif request.user.cur_read.filter(id=book_id).exists():
            request.user.cur_read.remove(book)
        request.user.past_read.add(book)
        return Response(status=status.HTTP_200_OK)


class curread_anyway(APIView):
    permission_classes = [IsAuthenticated, ]

    def post(self, request):
        book_id = request.data['book']
        book = Book.objects.get(id=book_id)
        if request.user.past_read.filter(id=book_id).exists():
            request.user.past_read.remove(book)
        elif request.user.favourite.filter(id=book_id).exists():
            request.user.favourite.remove(book)
        request.user.cur_read.add(book)
        return Response(status=status.HTTP_200_OK)


class favourite_anyway(APIView):
    permission_classes = [IsAuthenticated, ]

    def post(self, request):
        book_id = request.data['book']
        book = Book.objects.get(id=book_id)
        if request.user.past_read.filter(id=book_id).exists():
            request.user.past_read.remove(book)
        elif request.user.cur_read.filter(id=book_id).exists():
            request.user.cur_read.remove(book)
        request.user.favourite.add(book)
        return Response(status=status.HTTP_200_OK)
