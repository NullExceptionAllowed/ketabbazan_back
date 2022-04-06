from django.db import models
from django.utils import timezone

class Book(models.Model):
    name = models.CharField(max_length=50)
    summary = models.TextField(max_length=1000)
    author = models.CharField(max_length=50)
    price = models.IntegerField()
    publisher = models.CharField(max_length=50)
    image_url = models.URLField()
    created = models.DateTimeField(default=timezone.now)
    pdf_url = models.URLField(null=True)

    def __str__(self):
        formatter = 'Name: {:28} | Written by: {:8} | Price: {:6}'
        return formatter.format(self.name, self.author, self.price)