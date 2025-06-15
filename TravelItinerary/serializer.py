from rest_framework import serializers
from .models import TravelItinerary


class TravelItinerarySerializer(serializers.ModelSerializer):
    passage_id = serializers.CharField(source='passage.id', read_only=True)

    class Meta:
        model = TravelItinerary
        fields = ['id', 'content', 'created_at', 'passage_id']