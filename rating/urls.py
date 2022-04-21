from django.urls import path
from .views import Rate, Userrate, Allbookinfo

urlpatterns = [
    path('', Rate.as_view()),
    path('userrate/', Userrate.as_view()),
    path('test/', Allbookinfo.as_view()),
]
