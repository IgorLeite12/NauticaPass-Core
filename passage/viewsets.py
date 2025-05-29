from rest_framework import viewsets
from user.models import Passage
from .serializers import PassageSerializer

class PassageViewSet(viewsets.ModelViewSet):
    queryset = Passage.objects.all()
    serializer_class = PassageSerializer