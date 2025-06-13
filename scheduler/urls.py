from django.urls import path
from .views import PlanView

urlpatterns = [
    path('gerar-roteiro/', PlanView.as_view(), name='gerar-roteiro'),
]