import os
import requests
import logging

logger = logging.getLogger(__name__)

def genera_micro_program_seaman(passage, user):
    url = "https://openrouter.ai/api/v1/chat/completions"
    headers = {
        "Authorization": f"Bearer {os.getenv('OPENROUTER_API_KEY')}",
        "Content-Type": "application/json"
    }
    prompt = f"""
    Você é um guia turístico amigável e experiente da região amazônica.
    O nosso cliente, {user.id}, acaba de comprar uma passagem de barco para a cidade de {passage.destination.name} e precisa de um roteiro.

    Sua tarefa é criar um roteiro de viagem simples e envolvente de 7 dias para a cidade de {passage.destination.name}.

    Por favor, siga estas instruções:
    1. Estruture o roteiro dia a dia (Dia 1, Dia 2, etc.).
    2. Para cada dia, sugira 2 a 3 atividades, incluindo pontos turísticos e comidas típicas.
    3. Ao final, adicione uma seção "Para Viagens Mais Longas:" com sugestões extras.
    4. Use um tom acolhedor e empolgante.
    """
    data = {
        "model": os.getenv("OPENROUTER_MODEL", "google/gemini-1.5-flash"),
        "messages": [{"role": "user", "content": prompt}]
    }
    try:
        response = requests.post(url, headers=headers, json=data, timeout=10)
        response.raise_for_status()
        return response.json()["choices"][0]["message"]["content"]
    except requests.exceptions.RequestException as e:
        logger.error(f"Erro ao chamar a API: {e}")
        return "Não foi possível gerar o roteiro no momento. Tente novamente mais tarde."