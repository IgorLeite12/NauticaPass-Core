from django.urls import path
from .views import UserListCreateView, UserDetailView

urlpatterns = [
    path('', UserListCreateView.as_view()),       # GET (list), POST (create)
    path('<int:pk>/', UserDetailView.as_view()),  # GET (detail), PUT, PATCH, DELETE
]
