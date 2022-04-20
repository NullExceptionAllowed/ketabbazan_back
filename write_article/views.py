from write_article.models import Article
from rest_framework import generics, status
from .serializers import ArticleSerializer
from rest_framework.response import Response
from rest_framework import permissions
from write_article.permissions import IsOwnerOrReadOnly

class ArticleList(generics.ListCreateAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        if self.request.user.is_authenticated:
            serializer.save(owner=self.request.user) 
        else:
            return Response(
                data={'message': 'Not Authenticated'},
                status=status.HTTP_401_UNAUTHORIZED
            )            

class ArticleDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly,
                          IsOwnerOrReadOnly]