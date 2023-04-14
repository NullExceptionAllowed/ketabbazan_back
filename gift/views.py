from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from .serializers import GiftHistorySerializer
# Create your views here.


class SendBook(APIView):
    permission_classes = [IsAuthenticated, ]

    def post(self, request):
        self.request.data['sender'] = self.request.user.id
        gift_detail = GiftHistorySerializer(data=self.request.data)
        if gift_detail.is_valid():
            gift_detail.save()
            return Response(gift_detail.data, status=status.HTTP_200_OK)
        return Response(data=gift_detail.errors, status=status.HTTP_400_BAD_REQUEST)