from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets
from rest_framework.filters import OrderingFilter
from rest_framework.permissions import IsAuthenticated, AllowAny
from .models import Account
from .serializers import AccountSerializer
from .filter import AccountFilter
from rest_framework.permissions import AllowAny, IsAuthenticated
from core.permissions import IsOwnerOrReadOnly

class AccountViewSet(viewsets.ModelViewSet):
    queryset = Account.objects.all()
    serializer_class = AccountSerializer
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    filterset_class = AccountFilter
    ordering_fields = ['name', 'email', 'cpf']

    def get_permissions(self):
        if self.action == "create":
            return [AllowAny()]
        if self.action in ["update", "partial_update", "destroy"]:
            return [IsAuthenticated(), IsOwnerOrReadOnly()]
        return [IsAuthenticated()]
