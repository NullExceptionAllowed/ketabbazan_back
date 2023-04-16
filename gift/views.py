from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from .serializers import GiftHistorySerializer, ShowGiftSerializer
from rest_framework.generics import ListAPIView
from .models import GiftHistory
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


class ShowReceivedGift(ListAPIView):
    permission_classes = [IsAuthenticated, ]
    serializer_class = ShowGiftSerializer

    def get_queryset(self):
        return GiftHistory.objects.filter(receiver=self.request.user).order_by('-date')
