from rest_framework import serializers
from passage.serializers import PassageSerializer, CitySerializer
from user.serializers import UserSerializer
from .models import Ticket
from TravelItinerary.serializer import TravelItinerarySerializer

class TicketSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    passage = PassageSerializer(source='passage_id', read_only=True)
    origin = serializers.CharField(source='passage_id.origin.name', read_only=True)
    destination = CitySerializer(source='passage_id.destination', read_only=True)
    itinerary = TravelItinerarySerializer(read_only=True)

    class Meta:
        model = Ticket
        fields = [
            'id', 'user', 'passage', 'purchase_date', 'purchase_time',
            'payment_method', 'origin', 'destination', 'itinerary'
        ]
        read_only_fields = [
            'id', 'user', 'passage', 'purchase_date', 'purchase_time',
            'origin', 'destination', 'itinerary'
        ]

    def create(self, validated_data):
        user = self.context['request'].user
        passage_id = self.initial_data.get('passage_id')
        if not passage_id:
            raise serializers.ValidationError({'passage_id': 'Este campo é obrigatório.'})
        from passage.models import Passage
        try:
            passage = Passage.objects.get(id=passage_id)
        except Passage.DoesNotExist:
            raise serializers.ValidationError({'passage_id': 'Passagem não encontrada.'})
        ticket = Ticket.objects.create(
            user=user,
            passage_id=passage,
            payment_method=validated_data['payment_method']
        )
        return ticket