from rest_framework import serializers

from passage.models import Passage, City


class PassageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Passage
        fields = ['id',
                  'origin',
                  'destination',
                  'departure_time',
                  'arrival_time',
                  'price',
                  'available_seats',
                  'vessel']

    def validate_vessel(self, value):
        """Ensure the user owns the vessel when creating a passage"""
        request = self.context.get('request')
        if request and hasattr(request, 'user'):
            if value.owner != request.user:
                raise serializers.ValidationError("You must own the vessel to create a passage.")
        return value

class CitySerializer(serializers.ModelSerializer):
    class Meta:
        model = City
        fields = ['id', 'name']