from django.conf.urls import url, include
from django.urls import path
from .views import *
from rest_framework.authtoken import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'user', UserViewSet)


urlpatterns = [
    path('auth/', CustomAuthToken.as_view()),
    path('', include(router.urls)),
]
