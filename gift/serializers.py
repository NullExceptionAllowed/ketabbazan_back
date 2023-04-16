from rest_framework import serializers
from rest_framework.exceptions import ValidationError
from .models import GiftHistory
from accounts.models import User
from read_book.models import Book
from django.utils.translation import gettext_lazy as _
from read_book.serializers import BookInfoSerializer


class GiftHistorySerializer(serializers.ModelSerializer):

    class Meta:
        model = GiftHistory
        fields = ('sender', 'receiver', 'book', 'is_read', 'message')

    def validate(self, attrs):
        sender = attrs.get('sender')
        receiver = attrs.get('receiver')
        book = attrs.get('book')
        if sender == receiver:
            msg = _('sender and receiver can not be same')
            raise ValidationError(msg)
        if not sender.purchased_books.filter(id=book.id).exists():
            msg = _('you dont have this book')
            raise ValidationError(msg)
        if receiver.purchased_books.filter(id=book.id).exists():
            msg = _('receiver already has this book')
            raise ValidationError(msg)
        return attrs

    def save(self, **kwargs):
        sender = self.validated_data.get('sender')
        receiver = self.validated_data.get('receiver')
        book = self.validated_data.get('book')
        sender.purchased_books.remove(book)
        receiver.purchased_books.add(book)
        return super().save(**kwargs)
