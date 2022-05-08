from rest_framework import generics
from read_book.serializers import BookInfoSerializer
from read_book.models import Book
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
# Create your views here.


class Advancesearch(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookInfoSerializer
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter]
    filterset_fields = {'name': ['contains'], 'author__name': ['contains'], 'genre__name': ['contains'],
                        'price': ['gte', 'lte'], 'publisher': ['contains']}
    ordering_fields = ['price', 'created']

    def list(self, request, *args, **kwargs):
        objs = super().list(request, *args, **kwargs)

        return objs
