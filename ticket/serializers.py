from rest_framework import serializers
from passage.serializers import PassageSerializer
from .models import Ticket


class TicketSerializer(serializers.ModelSerializer):
    passage = PassageSerializer(source='passage_id', read_only=True)
    origin = serializers.CharField(source='passage_id.origin.name', read_only=True)
    destination = serializers.CharField(source='passage_id.destination.name', read_only=True)

    class Meta:
        model = Ticket
        fields = ['id', 'passage', 'purchase_date', 'purchase_time', 'payment_method', 'origin', 'destination']
        read_only_fields = ['id', 'passage', 'purchase_date', 'purchase_time', 'origin', 'destination']


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
            user_id=user,
            passage_id=passage,
            payment_method=validated_data['payment_method']
        )
        return ticket