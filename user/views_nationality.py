import requests
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny

class CountryListIBGE(APIView):
    permission_classes = [AllowAny]

    def get(self, request):
        url = "https://restcountries.com/v3.1/all?fields=translations,cca3"
        try:
            response = requests.get(url, timeout=10)
            response.raise_for_status()
            data = response.json()
            # Monta lista de dicionários com nome e sigla
            paises = [
                {
                    "name": country['translations']['por']['common'],
                    "acronym": country['cca3']
                }
                for country in data
                if 'translations' in country and 'por' in country['translations'] and 'cca3' in country
            ]
            # Ordena alfabeticamente pelo nome
            paises_ordenados = sorted(paises, key=lambda x: x['name'])
            return Response(paises_ordenados)
        except Exception as e:
            return Response({"error": str(e)}, status=500)