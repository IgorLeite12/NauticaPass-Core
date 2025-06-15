from django.urls import path
from .views import CompletionView, TravelItineraryDetailView

urlpatterns = [
    path('completion/', CompletionView.as_view(), name='completion'),
    path('script/<int:id>/', TravelItineraryDetailView.as_view(), name='travelitinerary-detail'),
]