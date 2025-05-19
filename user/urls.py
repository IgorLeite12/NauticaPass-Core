# seu_app/urls.py
from rest_framework import routers
from .viewsets import UserViewSet
from django.urls import path, include

router = routers.DefaultRouter()
router.register(r'', UserViewSet)

urlpatterns = [
    path('', include(router.urls)),
]