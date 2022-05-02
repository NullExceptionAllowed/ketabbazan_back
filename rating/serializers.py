from rest_framework import serializers
from .models import Rating
from accounts.models import User
from read_book.models import Book

class Rateuserserilalizer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id')

class Ratebookserializer(serializers.ModelSerializer):
    class Meta:
        model= Book
        fields = ('id')

class Rateserializer(serializers.ModelSerializer):
    user = Rateuserserilalizer
    book = Ratebookserializer
    class Meta:
        model = Rating
        fields = ('user', 'book', 'rate')

    def create(self, validated_data):
        obj = super().create(validated_data)
        obj.save()
        return obj



class returnrateserializer(serializers.ModelSerializer):
    avg = serializers.SerializerMethodField('getavg')
    count = serializers.SerializerMethodField('getcount')

    def getavg(self, book):
        return book.average_rate()
    def getcount(self, book):
        return book.rating_set.count()
    class Meta:
        model = Book
        fields = ('avg', 'count')






