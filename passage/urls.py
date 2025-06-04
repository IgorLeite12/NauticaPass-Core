from rest_framework.routers import DefaultRouter
from django.urls import path, include
from .viewsets import PassageViewSet, CityListView

router = DefaultRouter()
router.register(r'', PassageViewSet, basename='passage')

urlpatterns = [
    path('city/', CityListView.as_view(), name='city-list'),
    path('', include(router.urls)),
]
