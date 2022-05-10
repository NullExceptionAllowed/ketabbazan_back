from django.db import models

# Create your models here.

class Profile(models.Model):
    fullname = models.CharField(null=True,blank=True,max_length=30)
    image = models.ImageField(default="media/profileimages/default.jpg",upload_to="media/profileimages")
    bio = models.CharField(null=True, blank=True, max_length=1000, default=None)
    gender = models.CharField(null=True, choices=(('M','Male'), ('F','Female')), max_length=1, blank=True)
    born_date = models.DateField(null=True, blank=True, default=None)
    public_profile_info = models.BooleanField(default=False)
    public_show_articles = models.BooleanField(default=False)
    public_show_read_books = models.BooleanField(default=False)

    def __str__(self):
        try:
            return self.user.username+"'s profile"
        except:
            return str(self.id)
