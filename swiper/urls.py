"""swiper URL Configuration

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
from django.urls import path
from user.views import get_verify_code, login, get_profile, modify_profile, upload_avatar

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('user/verify_code/', get_verify_code),
    path('user/login/', login),
    path('user/profile/', get_profile),
    path('user/modify_profile/', modify_profile),
    path('user/upload_avatar/', upload_avatar),
]
