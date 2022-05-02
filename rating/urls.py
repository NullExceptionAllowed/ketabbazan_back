from django.urls import path
from .views import Rate, Userrate, Getrate

urlpatterns = [
    path('', Rate.as_view()),
    path('userrate/', Userrate.as_view()),
    path('getrate/', Getrate.as_view())
]
