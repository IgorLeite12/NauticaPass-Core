from django.contrib.messages import api
from rest_framework import serializers
import vessel.message as messages
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from vessel.models import Vessel

class VesselSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vessel
        fields = ['id',
                  'name_vessel',
                  'owner',
                  'capacity',
                  'navigation_type']
        
        
        
        @api_view(['POST'])
        def validate_capacity(request):
            capacity = request.data.get('capacity')
            
            if capacity is None or not isinstance(capacity, (int, float)):
                return Response(
                    {"error": messages.MUST_BE_NUMBER},
                    status=status.HTTP_400_BAD_REQUEST
                )
                
            if capacity <= 0:
                return Response(
                    {'error': messages.CAPACITY_MUST_BE_POSITIVE},
                    status=status.HTTP_400_BAD_REQUEST
                )

            return Response(
                {'detail': messages.CAPACITY_VALIDATION_SUCCESS},
                status=status.HTTP_200_OK
    )