from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from read_book.models import Book
from .serializers import Rateserializer
from .models import Rating
from rest_framework.response import Response
from rest_framework import  status


class Rate(APIView):
    permission_classes = [IsAuthenticated, ]

    def post(self,request):
        if not Book.objects.filter(id=request.data['book'], rating__user=request.user).exists():
            request.data['user'] = request.user.id
            ser_rate = Rateserializer(data=request.data)
            if (ser_rate.is_valid()):
                ser_rate.save()
                return Response(ser_rate.data, status=status.HTTP_200_OK)
            else:
                return Response(ser_rate.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response({"message": "you have rated for this book"},status=status.HTTP_400_BAD_REQUEST)


    def get(self,request):
        book_id = request.data['book']
        book = Book.objects.get(id=book_id)
        return Response({"avg":book.average_rate()}, status=status.HTTP_200_OK)

class Userrate(APIView):
    permission_classes = [IsAuthenticated, ]
    def get(self,request):
        book_id = request.data['book']
        book = Book.objects.get(id=book_id)
        try:
            rate = Rating.objects.get(book=book, user=request.user).rate
            return Response({"rate":rate}, status=status.HTTP_200_OK)
        except:
            return Response({"message":"this user did not rate for this book"}, status=status.HTTP_400_BAD_REQUEST)


