from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .services import get_or_create_itinerary
from TravelItinerary.models import TravelItinerary
from ticket.models import Ticket


class CompletionView(APIView):
    def post(self, request):
        try:
            ticket_id = request.data.get("ticket_id")
            ticket = Ticket.objects.get(id=ticket_id)
            if ticket.user != request.user:
                return Response({"error": "Acesso negado."}, status=status.HTTP_403_FORBIDDEN)
            content, created = get_or_create_itinerary(ticket_id, request.user)
            return Response({"content": content, "created": created}, status=status.HTTP_201_CREATED if created else status.HTTP_200_OK)
        except Ticket.DoesNotExist:
            return Response({"error": "Passagem não encontrada."}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def get(self, request):
        ticket_id = request.query_params.get("ticket_id")
        if not ticket_id:
            return Response({"error": "ticket_id é obrigatório"}, status=status.HTTP_400_BAD_REQUEST)
        try:
            ticket = Ticket.objects.get(id=ticket_id)
            if ticket.user != request.user:
                return Response({"error": "Acesso negado."}, status=status.HTTP_403_FORBIDDEN)
            itinerary = TravelItinerary.objects.get(passage_id=ticket_id)
            return Response({"content": itinerary.content}, status=status.HTTP_200_OK)
        except Ticket.DoesNotExist:
            return Response({"error": "Passagem não encontrada."}, status=status.HTTP_404_NOT_FOUND)
        except TravelItinerary.DoesNotExist:
            return Response({"error": "Roteiro não encontrado para este ticket"}, status=status.HTTP_404_NOT_FOUND)


class TravelItineraryDetailView(APIView):
    def get(self, request, id):
        try:
            itinerary = TravelItinerary.objects.get(id=id)
            if itinerary.user != request.user:
                return Response({"error": "Acesso negado."}, status=status.HTTP_403_FORBIDDEN)
            return Response({"content": itinerary.content}, status=status.HTTP_200_OK)
        except TravelItinerary.DoesNotExist:
            return Response({"error": "Roteiro não encontrado."}, status=status.HTTP_404_NOT_FOUND)