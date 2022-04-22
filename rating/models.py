from django.db import models
from accounts.models import User
from django.core.validators import MaxValueValidator, MinValueValidator
from read_book.models import Book
# Create your models here.

class Rating(models.Model):
    user = models.ForeignKey(to=User, on_delete=models.CASCADE)
    book = models.ForeignKey(to=Book, on_delete=models.CASCADE, null=True)
    rate = models.PositiveIntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)], null=True, unique=False)

    def __str__(self):
        return "username:" + self.user.username + " | rate:" + str(self.book.name)

