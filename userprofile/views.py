import os

from django.shortcuts import render
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import renderer_classes
from rest_framework.views import APIView
from .custom_renders import JPEGRenderer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import AllowAny, IsAuthenticated
from accounts.models import User
from wsgiref.util import FileWrapper
from rest_framework import generics, viewsets
from .serializers import Profileserializer, Profileserializerwithimage, ProfileImageserializer, AccountProfileserializer
from .models import Profile
# Create your views here.


class Profileimage(generics.RetrieveAPIView):
    renderer_classes = [JPEGRenderer]
    permission_classes = [IsAuthenticated, ]

    def get(self,request):
        image=request.user.profile.image
        return Response(image, content_type='image/jpeg')

    def post(self,request):
        if (request.user.profile.image != "media/profileimages/default.jpg"):
            os.remove(f"media/profileimages/{request.user.username}.jpg")

        image = request.FILES['image']
        user = User.objects.get(email=request.user.email)
        user.profile.image = image
        user.profile.save()
        os.rename(f"media/profileimages/{image}", f"media/profileimages/{request.user.username}.jpg")
        user.profile.image = f"media/profileimages/{request.user.username}.jpg"
        user.profile.save()
        return Response(status=status.HTTP_200_OK)


    def delete(self,request):
        if(request.user.profile.image=="media/profileimages/default.jpg"):
            return Response(data={"message": "default image can not deleted"}, status=status.HTTP_400_BAD_REQUEST)
        else:
            os.remove(f"media/profileimages/{request.user.username}.jpg")
            request.user.profile.image="media/profileimages/default.jpg"
            request.user.profile.save()
            return Response(data={"message": "image deleted"}, status=status.HTTP_200_OK)


class Profileinfo(APIView):
    permission_classes = [IsAuthenticated, ]

    def put(self, request):
        try:
            bio = request.data['bio']
        except:
            bio=None
        try:
            gender = request.data['gender']
        except:
            gender=None
        try:
            born_date = request.data['born_date']
        except:
            born_date=None
        request.user.profile.bio = bio
        request.user.profile.born_date = born_date
        if gender is None:
            request.user.profile.gender=None
        else:
            request.user.profile.gender = gender
        request.user.profile.save()
        ser_profile=Profileserializer(request.data)
        return Response(ser_profile.data, status=status.HTTP_200_OK)

    def get(self, request):
        ser_profile = Profileserializer(request.user.profile)
        return Response(ser_profile.data, status=status.HTTP_200_OK)


class Imageprofile(APIView):
    permission_classes = [IsAuthenticated, ]

    def get(self,request):
        profile=request.user.profile
        ser_profile=ProfileImageserializer(instance=profile)
        return Response({'info':ser_profile.data})


class AccountProfile(APIView):
    permission_classes = [IsAuthenticated, ]

    def get(self,request):
        ser_data=AccountProfileserializer(request.user)
        return Response(ser_data.data,status=status.HTTP_200_OK)


class PasswordChange(APIView):
    permission_classes = [IsAuthenticated, ]
    def post(self,request):
        if (request.user.check_password(request.data['old_password'])):
            request.user.set_password(request.data['new_password'])
            request.user.save()
            return Response(data={"message":"new password set succesful"},status=status.HTTP_200_OK)
        else:
            return Response(data={"message":"old password is wrong"},status=status.HTTP_400_BAD_REQUEST)