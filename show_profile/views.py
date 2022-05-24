from django.shortcuts import render
from accounts.models import User
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import Publicprofileserializer
from write_article.models import Article
# Create your views here.


class Showprofile(APIView):
    def get(self, request):
        try:
            user_id = request.query_params['id']
        except:
            return Response({"message": "no id found!"}, status=status.HTTP_400_BAD_REQUEST)
        try:
            user = User.objects.get(id=user_id)
        except:
            return Response({"message": "no user with this id"}, status=status.HTTP_400_BAD_REQUEST)
        ser_profile = Publicprofileserializer(user, context={"request":self.request})
        return Response(ser_profile.data, status=status.HTTP_200_OK)


class ChangeProfileInfoPublicOrPrivate(APIView):
    def put(self, request):
        if request.data['is_public']==1:
            request.user.profile.public_profile_info = True
        else:
            request.user.profile.public_profile_info = False
        request.user.profile.save()
        return Response(status=status.HTTP_200_OK)


class ChangeProfileReadbookPublicOrPrivate(APIView):
    def put(self, request):
        if request.data['is_public'] == 1:
            request.user.profile.public_show_read_books = True
        else:
            request.user.profile.public_show_read_books = False
        request.user.profile.save()
        return Response(status=status.HTTP_200_OK)


class ChangeProfileArticlePublicOrPrivate(APIView):
    def put(self, request):
        if request.data['is_public'] == 1:
            request.user.profile.public_show_articles = True
        else:
            request.user.profile.public_show_articles = False
        request.user.profile.save()
        return Response(status=status.HTTP_200_OK)


