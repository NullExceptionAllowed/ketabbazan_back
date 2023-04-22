"""core URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include, re_path
from rest_framework import permissions
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('admin-panel/', include('admin_panel.urls')),
    path('accounts/', include('accounts.urls')),
    path('read_book/', include('read_book.urls')),
    path('profile/', include('userprofile.urls')),
    path('search/', include('search.urls')),
    path('write_article/', include('write_article.urls')),
    path('similar_books/', include('similar_books.urls')),
    path('rate/', include('rating.urls')),
    path('comment/', include('comments.urls')),
    path('lists/', include('lists.urls')),
    path('showprofile/', include('show_profile.urls')),
    path('quiz/', include('quiz.urls')),
    path('resetpassword/', include(('forgotpassword.urls', 'forgotpassword') , namespace='forgotpassword')),
    path('gift/', include('gift.urls')),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)