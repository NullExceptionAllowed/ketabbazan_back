from django.urls import path
from .views import TimeLine


urlpatterns = [
    path('', TimeLine.as_view())

]
