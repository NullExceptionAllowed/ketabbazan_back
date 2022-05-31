from rest_framework import serializers
from accounts.models import User
from read_book.serializers import BookInfoSerializer
from write_article.serializers import ArticleSerializer
from write_article.models import Article
from quiz.serializers import QuestionSerializer
from quiz.models import Question


class TimeLineSerializer(serializers.ModelSerializer):
    past_read_books = serializers.SerializerMethodField('get_past_read_books')
    user_articles = serializers.SerializerMethodField('get_user_articles')
    questions = serializers.SerializerMethodField('get_questions')

    class Meta:
        model = User
        fields = ('past_read_books', 'user_articles', 'questions')

    def get_past_read_books(self, user):
        return BookInfoSerializer(user.past_read.all(), many=True).data

    def get_user_articles(self, user):
        return ArticleSerializer(Article.objects.filter(owner=user), many=True).data

    def get_questions(self, user):
        return QuestionSerializer(Question.objects.filter(book__in=user.past_read.all()), many=True).data