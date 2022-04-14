from django.db import models

# Create your models here.

class Profile(models.Model):
    fullname = models.CharField(null=True,blank=True,max_length=30)
    image = models.ImageField(default="media/profileimages/default.jpg",upload_to="media/profileimages")
    bio = models.CharField(null=True, blank=True, max_length=1000, default=None)
    gender = models.CharField(null=True, choices=(('M','Male'), ('F','Female')), max_length=1)
    born_date = models.DateField(null=True, blank=True, default=None)

    def __str__(self):
        return self.user.username+"'s profile"
