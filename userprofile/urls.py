from django.urls import path
from .views import Profileimage, Profileinfo
from rest_framework.routers import DefaultRouter



urlpatterns = [
    path('image/', Profileimage.as_view()),
    path('info/', Profileinfo.as_view())

]

