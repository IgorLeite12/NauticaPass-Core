import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()
api_key = os.getenv("OPENROUTER_API_KEY")

client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=api_key,
)

def get_completion():
    return client.chat.completions.create(
        extra_headers={
            "HTTP-Referer": "<YOUR_SITE_URL>",
            "X-Title": "<YOUR_SITE_NAME>",
        },
        model="deepseek/deepseek-r1-0528:free",
        messages=[
            {
                "role": "user",
                "content": """Você é um guia turístico amigável e experiente da região amazônica.
O nosso cliente, Igor, acaba de comprar uma passagem de barco para a cidade de Manaus e precisa de um roteiro.
Sua tarefa é criar um roteiro de viagem simples e envolvente de 7 dias para a cidade de Manaus.
Por favor, siga estas instruções:
1. Estruture o roteiro dia a dia (Dia 1, Dia 2, etc.).
2. Para cada dia, sugira 2 a 3 atividades, incluindo pontos turísticos e comidas típicas.
3. Ao final, adicione uma seção "Para Viagens Mais Longas:" com sugestões extras.
4. Use um tom acolhedor e empolgante."""
            }
        ]
    )