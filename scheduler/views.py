from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .services import get_completion

class CompletionView(APIView):
    def post(self, request):
        try:
            completion = get_completion()
            return Response({"result": completion.choices[0].message.content}, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)