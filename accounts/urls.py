from django.urls import path
#from rest_framework.authtoken.views import obtain_auth_token

from .views import UserSignUp, UserLogout, ObtainAuthToken, UserProfile

urlpatterns = [
    path('signup/', UserSignUp.as_view()),
    #path('login/', obtain_auth_token),
    path('login/', ObtainAuthToken.as_view()),
    path('profile/', UserProfile.as_view()),
    path('logout/', UserLogout.as_view()),
]