from rest_framework import serializers
from comments.models import Comment
from read_book.models import Book
from accounts.models import User


class UserCommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username')


class BookCommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ('id', 'name')


class CommentSerializer(serializers.ModelSerializer):
    user = UserCommentSerializer(read_only=True)
    book = BookCommentSerializer(read_only=True)

    class Meta:
        model = Comment
        fields = '__all__'

