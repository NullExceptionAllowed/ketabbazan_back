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
from .serializers import Profileserializer, Profileserializerwithimage
from .models import Profile
# Create your views here.


class Profileimage(generics.RetrieveAPIView):
    renderer_classes = [JPEGRenderer]
    permission_classes = [IsAuthenticated, ]


    def get(self,request):
        image=request.user.profile.image
        return Response(image, content_type='image/jpeg')


    def post(self,request):
        image=request.FILES['image']
        user=User.objects.get(email=request.user.email)
        user.profile.image=image
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

    def put(self,request, *args, **kwargs):
        bio=request.data['bio']
        gender=request.data['gender']
        born_date=request.data['born_date']
        request.user.profile.bio=bio
        request.user.profile.born_date=born_date
        if(gender==1):
            request.user.profile.gender=True
        else:
            request.user.profile.gender=False
        request.user.profile.save()
        ser_profile=Profileserializer(request.data)
        return Response(ser_profile.data,status=status.HTTP_200_OK)

    def get(self,request):
        ser_profile=Profileserializer(request.user.profile)
        return Response(ser_profile.data, status=status.HTTP_200_OK)





