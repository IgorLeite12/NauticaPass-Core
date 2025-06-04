from rest_framework import serializers
from user.models import Passage, City


class PassageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Passage
        fields = ['id',
                  'origin',
                  'destination',
                  'travel_date',
                  'departure_time',
                  'arrival_date',
                  'arrival_time',
                  'value',
                  'id_vessel']

class CitySerializer(serializers.ModelSerializer):
    class Meta:
        model = City
        fields = ['id', 'name']
