from rest_framework import serializers
from write_article.models import Article

class ArticleSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Article
        fields = ['id', 'title', 'body', 'summary', 'owner']