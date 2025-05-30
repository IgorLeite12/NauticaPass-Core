from rest_framework import viewsets
from user.models import Passage
from .serializers import PassageSerializer
from django_filters.rest_framework import DjangoFilterBackend


class PassageViewSet(viewsets.ModelViewSet):
    queryset = Passage.objects.all()
    serializer_class = PassageSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['origin',
                        'destination']