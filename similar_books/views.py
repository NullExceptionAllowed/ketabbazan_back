from rest_framework.views import APIView
from django.shortcuts import get_object_or_404
from read_book.models import Book
from accounts.models import User
from read_book.serializers import BookInfoSerializer
from rest_framework.response import Response

class OthersRead(APIView):
    authentication_classes = []
    permission_classes = []

    def get(self, request, id):
        thebook = get_object_or_404(Book, id=id)
        usersreadthebook = []
        res = []
        for user in User.objects.all():
            if thebook in user.favourite.all() or thebook in user.past_read.all() or thebook in user.cur_read.all():
                res.extend([book.id for book in user.favourite.all()])
                res.extend([book.id for book in user.past_read.all()])
                res.extend([book.id for book in user.cur_read.all()])

        res = list(dict.fromkeys(res)) # Remove duplicates

        ans = []

        for book_id in res:
            if int(id) == int(book_id):
                continue
            booki = get_object_or_404(Book, id=book_id)
            book_serializer = BookInfoSerializer(instance=booki)
            data = book_serializer.data
            data['id'] = book_id
            data['author'] = booki.getwriters()
            ans.append(data)

        return Response(ans)
                

def checkSimilarity(authors, book):
    for author1 in authors:
        for author2 in book.author.all():
            if str(author1) == str(author2):
                return True
    return False

class SimilarBooks(APIView):
    authentication_classes = []
    permission_classes = []

    def get(self, request, id):       
        thebook = get_object_or_404(Book, id=id)
        res = []
        ans = []

        thebookgenre = str(thebook.genre)
        for book in Book.objects.filter(genre__name=thebookgenre):
            if book.id == thebook.id:
                continue
            res.append(book.id)

        thebookauthors = thebook.author.all()
        print(thebookauthors)
        for book in Book.objects.all():
            if book.id == thebook.id or book.id in res:
                continue
            if checkSimilarity(thebookauthors, book):
                res.append(book.id)

        for book_id in res:
            booki = get_object_or_404(Book, id=book_id)
            book_serializer = BookInfoSerializer(instance=booki)
            data = book_serializer.data
            data['id'] = book_id
            data['author'] = booki.getwriters()
            ans.append(data)

        return Response(ans)