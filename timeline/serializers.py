from rest_framework import serializers
from accounts.models import User
from read_book.serializers import BookInfoSerializer
from write_article.serializers import ArticleSerializer
from write_article.models import Article


class ArticleSerializerTimeLine(ArticleSerializer):
    class Meta:
        model = Article
        fields = ['id', 'title', 'image', 'book', 'created_jalali', 'body', 'summary']


class TimeLineSerializer(serializers.ModelSerializer):
    past_read_books = serializers.SerializerMethodField('get_past_read_books')
    user_articles = serializers.SerializerMethodField('get_user_articles')

    class Meta:
        model = User
        fields = ('past_read_books', 'user_articles')

    def get_past_read_books(self, user):
        return BookInfoSerializer(user.past_read.all(), many=True).data


    def get_user_articles(self, user):
        return ArticleSerializerTimeLine(Article.objects.filter(owner=user), many=True).data
