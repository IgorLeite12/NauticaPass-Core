from rest_framework import serializers
from passage.models import Passage, City
from vessel.models import Vessel
from vessel.serializers import VesselSerializer


class CitySerializer(serializers.ModelSerializer):
    class Meta:
        model = City
        fields = ['id', 'name']


class PassageSerializer(serializers.ModelSerializer):
    id_vessel = serializers.PrimaryKeyRelatedField(
        queryset=Vessel.objects.all(), write_only=True, required=True
    )
    vessel = VesselSerializer(source='id_vessel', read_only=True)

    class Meta:
        model = Passage
        fields = [
            'id',
            'origin',
            'destination',
            'travel_date',
            'departure_time',
            'arrival_date',
            'arrival_time',
            'value',
            'id_vessel',
            'vessel',
        ]

