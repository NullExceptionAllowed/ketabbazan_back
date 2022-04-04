from rest_framework import serializers
from .models import Book
from django.utils import timezone
import os
import uuid

def get_file_path(instance, filename):
    ext = filename.split('.')[-1]
    filename = "%s.%s" % (uuid.uuid4(), ext)
    return os.path.join('images', filename)

class BookInfoSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=50)
    summary = serializers.CharField(max_length=1000)
    author = serializers.CharField(max_length=50)
    price = serializers.IntegerField()
    publisher = serializers.CharField(max_length=50)
    book_image = serializers.ImageField()
    created = serializers.DateTimeField(default=timezone.now)    