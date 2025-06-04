# Imagem base com Python
FROM python:3.13.3

# Variáveis de ambiente para otimização
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

# Diretório de trabalho
WORKDIR /app

# Instala dependências do sistema
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    libpq-dev \
 && rm -rf /var/lib/apt/lists/*

# Copia o requirements e instala dependências Python
COPY requirements.txt ./
RUN pip install --upgrade pip && pip install -r requirements.txt

# Copia o restante da aplicação
COPY . .

# Expõe a porta padrão do Django
EXPOSE 8000

# Comando padrão: aplica as migrations e inicia o servidor de desenvolvimento
CMD ["sh", "-c", "python manage.py migrate --noinput && python manage.py populate_cities && python manage.py runserver 0.0.0.0:8000"]