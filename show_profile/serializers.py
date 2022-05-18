from rest_framework import serializers
from accounts.models import User
from userprofile.serializers import AccountProfileserializer
from write_article.models import Article
from read_book.serializers import BookInfoSerializer
#from write_article.serializers import ArticleSerializer


class ArticleSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.nickname')
    image = serializers.SerializerMethodField()
    class Meta:
        model = Article
        fields = ['id', 'title', 'image', 'book', 'created_jalali', 'body', 'summary', 'owner', 'owner_id']
    def get_image(self,article):
        request = self.context.get('request')
        image = article.image.url
        return request.build_absolute_uri(image)

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
            ans=[]
            ans.append(ArticleSerializer(Article.objects.filter(owner=user), many=True, context={"request": self.context.get("request")}).data)
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

