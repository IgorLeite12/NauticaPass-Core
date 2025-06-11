from rest_framework import serializers
from .models import Ticket
from passage.models import Passage

class PassageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Passage
        fields = '__all__'

class TicketSerializer(serializers.ModelSerializer):
    passage = PassageSerializer(source='passage_id', read_only=True)

    class Meta:
        model = Ticket
        fields = ['id', 'passage', 'purchase_date', 'purchase_time', 'payment_method']

    def create(self, validated_data):
        user = self.context['request'].user
        passage = self.initial_data.get('passage_id')
        ticket = Ticket.objects.create(
            user_id=user,
            passage_id=passage,
            purchase_date=validated_data['purchase_date'],
            purchase_time=validated_data['purchase_time'],
            payment_method=validated_data['payment_method']
        )
        return ticket