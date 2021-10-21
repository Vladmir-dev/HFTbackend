from django.urls import path, include
from .api import *
from .views import *
from rest_framework.routers import DefaultRouter
from knox import views as knox_views


urlpatterns = [
    path('user_list/', user_list, name="user_list"),
    path('profile_list/', profile_list, name="profile_list"),
    path('auth', include('knox.urls')),
    path('auth/register', RegisterAPI.as_view()),
    path('auth/login', LoginAPI.as_view()),
    path('auth/user', UserAPI.as_view()),
]
