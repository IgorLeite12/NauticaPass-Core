from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .services import completion

class PlanView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        repost = completion.choices[0].message.content
        return Response({"resposta": repost}, status=status.HTTP_200_OK)