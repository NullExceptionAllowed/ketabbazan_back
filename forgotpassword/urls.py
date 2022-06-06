from django.urls import path, include

urlpatterns = [
    path('', include('django_rest_passwordreset.urls',  namespace='password_reset'))
]