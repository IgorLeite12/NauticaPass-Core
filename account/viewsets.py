from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets
from rest_framework.filters import OrderingFilter
from rest_framework.permissions import IsAuthenticated, AllowAny
from .models import Account
from .serializers import AccountSerializer
from rest_framework.permissions import AllowAny, IsAuthenticated

class AccountViewSet(viewsets.ModelViewSet):
    queryset = Account.objects.all()
    serializer_class = AccountSerializer
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    filterset_fields = ['name', 'Accountname', 'email']
    ordering_fields = ['name', 'Accountname', 'email']

    def get_permissions(self):
        if self.action == "create":
            return [AllowAny()]
        return [IsAuthenticated()]
