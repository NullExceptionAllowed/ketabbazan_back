from django.urls import path
from .views import Rate, Userrate

urlpatterns = [
    path('test/', Rate.as_view()),
    path('test2/', Userrate.as_view())
]