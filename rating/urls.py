from django.urls import path
from .views import Rate, Userrate

urlpatterns = [
    path('', Rate.as_view()),
    path('userrate/', Userrate.as_view()),
]
