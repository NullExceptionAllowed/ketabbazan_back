from rest_framework import serializers
from comments.models import Comment, Replycomment
from read_book.models import Book
from accounts.models import User


class Usercommentserializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', )


class Replyserializer(serializers.ModelSerializer):
    class Meta:
        model = Replycomment
        fields = ('reply_text', 'user', 'created_on', 'comment')

    def create(self, validated_data):
        obj = super().create(validated_data)
        obj.save()
        return obj


class Commentserializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ('book', 'user', 'comment_text', 'created_on')

    def create(self, validated_data):
        obj = super().create(validated_data)
        obj.save()
        return obj

class Allcommentsserializer(serializers.ModelSerializer):
    all_comments = serializers.SerializerMethodField('getallcomments')

    def getallcomments(self, book):
        return book.allcomments()

    class Meta:
        model = Book
        fields = ('all_comments', )
