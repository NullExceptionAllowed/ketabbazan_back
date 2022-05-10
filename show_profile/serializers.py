from rest_framework import serializers
from accounts.models import User
from userprofile.serializers import AccountProfileserializer
from write_article.models import Article
from read_book.serializers import BookInfoSerializer
from write_article.serializers import ArticleSerializer

class Publicprofileserializer(serializers.ModelSerializer):
    profile = serializers.SerializerMethodField('get_profile')
    read_books = serializers.SerializerMethodField('get_read_books')
    user_articles = serializers.SerializerMethodField('get_user_articles')

    def get_read_books(self, user):
        if user.profile.public_show_read_books:
            ans = [BookInfoSerializer(book).data for book in user.past_read.all()]
            return ans
        else:
            return "no public"

    def get_user_articles(self, user):
        if user.profile.public_show_articles:
            ans = [ArticleSerializer(article).data for article in Article.objects.filter(owner=user)]
            return ans
        else:
            return "no public"

    def get_profile(self, user):
        if user.profile.public_profile_info:
            return AccountProfileserializer(user).data
        else:
            return user.username

    class Meta:
        model = User
        fields = ('profile', 'read_books', 'user_articles')
