from rest_framework import serializers
from write_article.models import Article

class ArticleSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.nickname')

    class Meta:
        model = Article
        fields = ['id', 'title', 'image', 'book', 'created_jalali', 'body', 'summary', 'owner']