import jinja2.meta
from django.db import models
from accounts.models import User
# Create your models here.


class UserActivity(models.Model):
    user = models.ManyToOneRel(User, on_delete=models.CASCADE())
    data = models.DateTimeField(auto_now=True)
    type = models.CharField(max_length=10)
    action_id = models.IntegerField()
