import os
from dotenv import load_dotenv
from openai import OpenAI
from TravelItinerary.models import TravelItinerary
from ticket.serializers import TicketSerializer
from ticket.models import Ticket

load_dotenv()
api_key = os.getenv("OPENROUTER_API_KEY")

client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=api_key,
)

def get_or_create_itinerary(ticket_id, user):
    try:
        itinerary = TravelItinerary.objects.get(passage_id=ticket_id)
        return itinerary.content, False
    except TravelItinerary.DoesNotExist:
        ticket = Ticket.objects.get(id=ticket_id)
        ticket_dict = TicketSerializer(ticket).data
        completion = get_completion(ticket_dict)
        content = completion.choices[0].message.content
        itinerary = TravelItinerary.objects.create(
            user=user,
            passage=ticket,
            content=content
        )
        return itinerary.content, True

def get_completion(ticket):
    name_user = ticket["user"]["username"]
    city_name = ticket["destination"]["name"]

    prompt = f"""
    Você é um guia turístico amigável e experiente da região amazônica.

    O cliente {name_user} acabou de comprar uma passagem de barco com destino à cidade de {city_name} e precisa da sua ajuda.

    Sua missão é criar um roteiro de viagem confiável, empolgante e acolhedor, com duração de 7 dias, focado nas principais atrações, eventos culturais e comidas típicas que a cidade de {city_name} oferece.

    Siga estas instruções:

    📅 Estruture o roteiro por dia (Dia 1, Dia 2, etc.).
    🎯 Em cada dia, recomende de 2 a 3 atividades: podem incluir visitas a pontos turísticos, experiências culturais, eventos locais e pratos típicos.
    ✨ Ao final do roteiro, adicione uma seção chamada "Para Viagens Mais Longas" com sugestões extras para quem pretende ficar mais tempo na cidade.
    📝 Não use formatações como ###, ** ou qualquer outro caractere de estilização Markdown, pois o conteúdo será exibido diretamente na tela do usuário.
    🙂 Use emojis e uma linguagem acessível para tornar a leitura mais agradável, sem exageros.

    É essencial que as informações sejam verídicas e coerentes com a realidade da cidade de {city_name}, com foco em proporcionar uma experiência inesquecível para o viajante.
    """

    return client.chat.completions.create(
        extra_headers={
            "HTTP-Referer": "<YOUR_SITE_URL>",
            "X-Title": "<YOUR_SITE_NAME>",
        },
        model="deepseek/deepseek-r1-0528:free",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ]
    )