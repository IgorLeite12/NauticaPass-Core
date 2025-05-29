from rest_framework import serializers
from user.models import Passage

class PassageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Passage
        fields = ['id', 'origin', 'destination', 'travel_date', 'departure_time',  'arrival_date',  'arrival_time','value']