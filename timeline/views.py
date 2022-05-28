from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from .serializers import TimeLineSerializer
from accounts.models import User
# Create your views here.


class TimeLine(generics.ListAPIView):
    permission_classes = [IsAuthenticated, ]
    def get_queryset(self):
        return User.objects.filter(username=self.request.user.username)
    serializer_class = TimeLineSerializer
