from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated, AllowAny
from read_book.models import Book
from .serializers import Rateserializer, returnrateserializer
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




class Userrate(APIView):
    permission_classes = [IsAuthenticated, ]
    def get(self,request):
        book_id = request.query_params['book']
        book = Book.objects.get(id=book_id)
        try:
            rate = Rating.objects.get(book=book, user=request.user).rate
            return Response({"rate":{"rate":rate}}, status=status.HTTP_200_OK)
        except:
            return Response({"message":"this user did not rate for this book"}, status=status.HTTP_400_BAD_REQUEST)


class Getrate(APIView):
    permission_classes = [AllowAny, ]
    def get(self,request):
        book_id = request.query_params['id']
        book = Book.objects.get(id=book_id)
        ser_book = returnrateserializer(book)
        return Response({"rateinfo":ser_book.data}, status=status.HTTP_200_OK)


