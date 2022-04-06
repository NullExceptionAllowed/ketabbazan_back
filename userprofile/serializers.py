from rest_framework import serializers
from .models import Profile

class Profileserializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ('bio', 'gender', 'born_date')


class Profileserializerwithimage(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ('bio', 'gender', 'born_date')


class ProfileImageserializer(serializers.Serializer):
    bio=serializers.CharField(max_length=1000)
    gender=serializers.CharField(max_length=1)
    born_date=serializers.DateField()
    image=serializers.ImageField()


