from django.urls import path
from .views import Addtopast_read
from rest_framework.routers import DefaultRouter

urlpatterns = [
    path('pastread/', Addtopast_read.as_view()),

]