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


