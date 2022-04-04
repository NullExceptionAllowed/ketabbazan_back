from django.db import models
from django.utils import timezone
import os
import uuid

def get_file_path(instance, filename):
    ext = filename.split('.')[-1]
    filename = "%s.%s" % (uuid.uuid4(), ext)
    return os.path.join('images', filename)

class Book(models.Model):
    name = models.CharField(max_length=50)
    summary = models.TextField(max_length=1000)
    author = models.CharField(max_length=50)
    price = models.IntegerField()
    publisher = models.CharField(max_length=50)
    book_image = models.ImageField(upload_to=get_file_path)
    created = models.DateTimeField(default=timezone.now)

    def __str__(self):
        formatter = 'Name: {:28} | Written by: {:8} | Price: {:6}'
        return formatter.format(self.name, self.author, self.price)