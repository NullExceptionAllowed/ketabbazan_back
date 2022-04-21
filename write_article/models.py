from django.conf import settings
from django.db import models
from django.utils.translation import gettext_lazy as _

def upload_to(instance, filename):
    return 'articles/{filename}'.format(filename=filename)

class Article(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=100, blank=True, default='')
    body = models.TextField(blank=True, default='')
    summary = models.TextField(blank=True, default='')
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, blank=True, null=True, on_delete=models.CASCADE)
    image = models.ImageField(_("Image"), upload_to=upload_to, default='articles/default.jpg')

    class Meta:
        ordering = ['created']

    def __str__(self):
        return self.title