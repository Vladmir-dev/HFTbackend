from django.urls import path, include
from .api import *
from .views import *
from rest_framework.routers import DefaultRouter
from knox import views as knox_views
from rest_framework_swagger.views import get_swagger_view
from django.conf.urls import url

router = DefaultRouter()
# router.register(r'profiles', ProfileViewSet, basename='profile')

schema_view = get_swagger_view(title='Maxima api')


urlpatterns = [
    url(r'^$', schema_view),
    path('user_list/', user_list, name="user_list"),
    path('profile_list/', profile_list, name="profile_list"),
    path('auth', include('knox.urls')),
    path('auth/register', RegisterAPI.as_view()),
    path('auth/login', LoginAPI.as_view()),
    path('auth/logout', knox_views.LogoutView.as_view()),
    path('auth/user', UserAPI.as_view()),
    path('auth/order/', AlgoViewSet.as_view()),
    path('auth/profile/', ProfileViewSet.as_view()),
    # path('', include(router.urls)),
]
