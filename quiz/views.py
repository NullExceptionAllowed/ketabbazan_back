from requests import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from quiz.serializers import QuestionSerializer
from rest_framework import serializers
from rest_framework.response import Response
from rest_framework import status
import random
from .models import Question

class GenerateQuiz(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request, book_id):
        
        queryset = Question.objects.filter(book=book_id).order_by('?')[:5]

        ans = []
        for question in queryset:
            question_serializer = QuestionSerializer(instance=question)
            data = question_serializer.data
            ans.append(data)

        return Response(ans)

class ProposeQuestion(APIView):
    permission_classes = (IsAuthenticated,)

    def post(self, request):
        serializer = QuestionSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def perform_create(self, serializer):
        serializer.save()        
