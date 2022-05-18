from requests import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from quiz.serializers import QuestionSerializer
from rest_framework import serializers
from rest_framework.response import Response
from rest_framework import status

class ProposeQuestion(APIView):
    permission_classes = (IsAuthenticated,)

    def post(self, request):
        serializer = QuestionSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def perform_create(self, serializer):
        serializer.save()        