from django.db import models
from django.utils import timezone

class Author(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

# class Genre(models.Model):
#     name = models.CharField(max_length=100)

#     def __str__(self):
#         return self.name

class Book(models.Model):
    name = models.CharField(max_length=200)
    summary = models.TextField(max_length=1000)
    author = models.ManyToManyField(Author, blank=True)
    price = models.IntegerField()
    publisher = models.CharField(max_length=50)
    image_url = models.URLField()
    created = models.DateTimeField(default=timezone.now)
    pdf_url = models.URLField(null=True)

    def __str__(self):
        formatter = 'Name: {:28} | Written by: {:8} | Price: {:6}'
        writers = "، ".join(str(author) for author in self.author.all())
        return formatter.format(self.name, writers, self.price)        