from django.db import models
from read_book.models import Book

class Question(models.Model):
    question = models.CharField(max_length=1000, null=True)
    op1 = models.CharField(max_length=1000, null=True)
    op2 = models.CharField(max_length=1000, null=True)
    op3 = models.CharField(max_length=1000, null=True)
    op4 = models.CharField(max_length=1000, null=True)
    ans = models.IntegerField()
    book = models.ForeignKey(Book, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.question

class Quiz(models.Model):
    question = models.ManyToManyField(Question, blank=True)

    def __str__(self):
        return "Quiz" + str(self.id)