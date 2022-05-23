from rest_framework import serializers
from write_article.models import Article

class ArticleSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.nickname')
    owner_id = serializers.ReadOnlyField(source='owner.id')

    image = serializers.SerializerMethodField()

    def get_image(self, obj):
        return "http://94.101.185.252" + obj.image.url

    class Meta:
        model = Article
        fields = ['id', 'title', 'image', 'book', 'created_jalali', 'body', 'summary', 'owner', 'owner_id']