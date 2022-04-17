from django.urls import path
from .views import Profileimage, Profileinfo, Imageprofile, AccountProfile, PasswordChange,\
    UsernameChange, Profileimagelink
from rest_framework.routers import DefaultRouter



urlpatterns = [
    path('image/', Profileimage.as_view()), #main
    path('info/', Profileinfo.as_view()), #main
    path('pimg/', Imageprofile.as_view()),
    path('fullprofile/', AccountProfile.as_view()),
    path('changepassword/', PasswordChange.as_view()), #main
    path('changeusername/', UsernameChange.as_view()), #main
]

