from django.urls import path
from .views import Commentapi

urlpatterns = [
    path('test/', Commentapi.as_view()),
]

