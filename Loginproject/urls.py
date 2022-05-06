"""Loginproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from app1 import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('Home/',views.Homepage,name ="Home"),
    path('Login/',views.login_user,name ="Login"),
    #path('Register/',views.SignUpView.as_view(),name="register"),
    #path('Register/',views.register_request,name="register"),
    path("Register/", views.register_request, name="register"),

    path('logut/',views.logut_user,name='logout'),
    path('scookies/',views.setcookies,name="cookies"),
    path('showcookies/',views.getcookies,name='showcookies'),
    path('deletecookies/',views.deletecookies,name='deletecookies'),
    path('testcookies/',views.cookies_session,name="testcookies"),
    path('cookie_delete/',views.cookie_delete,name="cookies_delete"),
    path('createsession/',views.create_session,name="createsession"),
    path('accesssession/',views.access_session,name="access_session"),
    path('deletesession',views.delete_session,name="deletesession"),
    path('execption/',views.middlewearException,name='exe'),


]
