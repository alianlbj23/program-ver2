"""mblog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from robot.views import index, login,  logout, signup, userinfo, userlist, userdelete
urlpatterns = [
    path('', index),
    path('Login/', login),
    path('logout/', logout),
    path('Signup/', signup),
    path('userinfo/', userinfo),
    path('userlist/', userlist),
    path('userdelete/<str:name>/<int:password>/', userdelete),
    path('admin/', admin.site.urls),
]
