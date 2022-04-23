from write_article.models import Article
from rest_framework import generics, status
from .serializers import ArticleSerializer
from rest_framework.response import Response
from rest_framework import permissions
from write_article.permissions import IsOwnerOrReadOnly
from rest_framework.views import APIView

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

class NewestArticles(APIView):
    authentication_classes = []
    permission_classes = []

    def get(self, request, format=None):
        articles = [article for article in Article.objects.all()]
        articles.sort(key = lambda x : x.created, reverse=True)
        ans = []
        for article in articles[:10]:
            article_serializer = ArticleSerializer(instance=article)
            data = article_serializer.data
            data['id'] = article.id
            ans.append(data)
        return Response(ans)                          

class CreateArticle(APIView):        
    permission_classes = [permissions.IsAuthenticated]
    
    def post(self, request, format=None):
        print(request.data)
        serializer = ArticleSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(owner=self.request.user)
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)