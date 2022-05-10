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
        ser_profile = Publicprofileserializer(user)
        return Response(ser_profile.data, status=status.HTTP_200_OK)
