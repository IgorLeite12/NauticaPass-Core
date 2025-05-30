from rest_framework import serializers
from user.models import Vessel

class VesselSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vessel
        fields = ['id',
                  'name_vessel',
                  'name_owner',
                  'capacity',
                  'navigation_type']