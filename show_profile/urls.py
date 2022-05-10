from django.urls import path
from .views import Showprofile

urlpatterns = [
    path('', Showprofile.as_view()),
]
