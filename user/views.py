from rest_framework import generics
from .models import User
from .serializers import UserSerializer

# Listar e criar usuários (GET, POST)
class UserListCreateView(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

# Detalhar, atualizar e deletar usuário específico por ID (GET, PUT, PATCH, DELETE)
class UserDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
