import django_filters
from .models import Account


class AccountFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(field_name='name', lookup_expr='icontains')
    email = django_filters.CharFilter(field_name='email', lookup_expr='icontains')
    cpf = django_filters.CharFilter(field_name='cpf', lookup_expr='icontains')

    class Meta:
        model = Account
        fields = ['name', 'email', 'cpf']