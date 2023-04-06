from django.core.exceptions import ObjectDoesNotExist
from requests import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from quiz.serializers import QuestionSerializer
from rest_framework import serializers
from rest_framework.response import Response
from rest_framework import status
from .models import Question, Quiz, QuizResult


class SubmitQuiz(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request, quiz_id):
        res = {}
        questions = Quiz.objects.get(id=quiz_id).question.order_by('id')
        for question, i in zip(questions, range(1, questions.count() + 1)):
            res["ans" + str(i)] = question.ans

        # TODO :: create related quiz result model

        return Response(res)


class GenerateQuiz(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request, book_id):
        try:
            param = request.query_params['q']
            if param == "question_count":
                return Response(min(5, Question.objects.filter(book=book_id).count()))
        except:
            pass

        if (Question.objects.filter(book=book_id).count() == 0):
            return Response(status=status.HTTP_400_BAD_REQUEST)

        if (request.user.past_read.filter(id=book_id).count() == 0 and
                request.user.cur_read.filter(id=book_id).count() == 0 and
                request.user.favourite.filter(id=book_id).count() == 0 and
                request.user.left_read.filter(id=book_id).count() == 0):
            return Response(status=status.HTTP_403_FORBIDDEN)

        queryset = Question.objects.filter(book=book_id).order_by('?')[:5]

        ans = []
        new_quiz = Quiz.objects.create()
        ans.append({"id": new_quiz.id})

        for question in queryset:
            new_quiz.question.add(question)
        new_quiz.save()

        for question in new_quiz.question.order_by('id'):
            question_serializer = QuestionSerializer(instance=question)
            data = question_serializer.data
            del data["ans"]
            del data["book"]
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


class BestScores(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        try:
            results = QuizResult.objects.raw("""
                SELECT
                    accounts_user.id,
                    accounts_user.nickname,
                    profile.fullname,
                    profile.gender,
                    profile.image,
                    SUM((res.score * res.questions_count)/100 ) AS score
                FROM accounts_user , userprofile_profile as profile ,quiz_quizresult as res
                WHERE
                    accounts_user.id = res.user_id
                    AND
                    accounts_user.profile_id = profile.id
                GROUP BY
                    accounts_user.id,
                    accounts_user.nickname,
                    profile.fullname,
                    profile.gender,
                    profile.image
                ORDER BY score DESC
                LIMIT 30
            """)
        except QuizResult.DoesNotExist:
            results = []

        for result in results:
            print(result)

        return Response(results)
