from django.urls import path
from .views import Profileimage, Profileinfo, Imageprofile, AccountProfile, PasswordChange
from rest_framework.routers import DefaultRouter



urlpatterns = [
    path('image/', Profileimage.as_view()),
    path('info/', Profileinfo.as_view()),
    path('pimg/', Imageprofile.as_view()),
    path('fullprofile/', AccountProfile.as_view()),
    path('changepassword/', PasswordChange.as_view()),
]

