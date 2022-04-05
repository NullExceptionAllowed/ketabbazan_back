from django.contrib.auth.models import AbstractUser
from django.db import models
from userprofile.models import Profile
from django.contrib.auth import password_validation

class User(AbstractUser):
    nickname = models.CharField(max_length=15, null=True, blank=True)
    email = models.EmailField(unique=True)  
    profile=models.OneToOneField(Profile, on_delete=models.CASCADE, null=True)

    def save(self, *args, **kwargs):
        try:
            profileid=self.profile.id
        except:
            profile=Profile.objects.create()
            self.profile=profile
            profile.save()
        super().save(*args, **kwargs)
        if self._password is not None:
            password_validation.password_changed(self._password, self)
            self._password = None