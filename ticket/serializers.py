from rest_framework import serializers
from user.models import Ticket
from datetime import date, datetime

class TicketSerializer(serializers.ModelSerializer):
    id = serializers.CharField(read_only=True)
    purchase_date = serializers.DateField(read_only=True)
    purchase_time = serializers.TimeField(read_only=True)

    class Meta:
        model = Ticket
        fields = '__all__'

    def validate(self, data):
        if data['origin'] == data['destination']:
            raise serializers.ValidationError("A origem e o destino não podem ser iguais.")
        return data

    def create(self, validated_data):
        validated_data['purchase_date'] = date.today()
        validated_data['purchase_time'] = datetime.now().time().replace(microsecond=0)
        return super().create(validated_data)