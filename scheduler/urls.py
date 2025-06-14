from django.urls import path
from .views import CompletionView

urlpatterns = [
    path('completion/', CompletionView.as_view(), name='completion'),
]