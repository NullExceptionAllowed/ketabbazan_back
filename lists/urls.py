from django.urls import path
from .views import user_cur_read, user_past_read, user_favourite, favourite_anyway, pastread_anyway, curread_anyway
from rest_framework.routers import DefaultRouter

urlpatterns = [
    path('pastread/', user_past_read.as_view()),
    path('curread/', user_cur_read.as_view()),
    path('favourite/', user_favourite.as_view()),
    path('forcepastread/', pastread_anyway.as_view()),
    path('forcecurread/', curread_anyway.as_view()),
    path('forcefavourite/', favourite_anyway.as_view())
]
