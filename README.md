# ⛵ Projeto NauticaPass-Core

Uma API desenvolvida com fins didáticos e apresentada como parte da nossa **FeiraTech**.

O NauticaPass é uma solução criada para facilitar a compra de passagens fluviais na região Norte do Brasil, com foco nos estados do Amazonas e Pará. A ideia surgiu a partir da experiência frustrante de um dos desenvolvedores da equipe, que precisou ir pessoalmente ao porto para buscar informações sobre horários e preços — algo comum para muitos moradores da região.

🎯 **Objetivo**
Atender pessoas que utilizam embarcações fluviais como meio de transporte e enfrentam dificuldades para adquirir passagens de forma acessível e prática. O sistema foi pensado especialmente para quem possui:

Pouco ou nenhum acesso à internet;

Baixo domínio de tecnologia e compras online;

Dificuldade em encontrar informações sobre rotas e preços de passagens.

Nosso foco está em proporcionar:

✅ Facilidade na busca e compra de passagens fluviais;

✅ Experiência acessível para diferentes tipos de usuários;

✅ Redução da necessidade de deslocamentos físicos até os portos.

💡 **Funcionalidade Extra**: Roteiros de Viagem Inteligentes
Além da venda de passagens, o NauticaPass oferece roteiros personalizados de viagem. Utilizamos a API da OpenRouter, integrada com um modelo de linguagem (LLM), para gerar sugestões de passeios e atividades para viagens de até 7 dias no destino escolhido.

Caso a viagem seja mais longa, o sistema também sugere atividades extras para aproveitar ao máximo o tempo na cidade.

---
## ⚙️ Criar e acessar ambiente virtual `.venv`
Para você poder trabalhar de forma isolada, você vai precisar seguir estes passos para criar um ambiente virtual:
```bash
python -m venv .venv
python .venv\Scripts\activate
```

## ⚙️ Configuração do arquivo `.env`

Para configurar o projeto corretamente, siga as etapas abaixo:

1. Crie um arquivo `.env` na raiz do projeto.
2. Atualize as variáveis relacionadas ao banco de dados com as credenciais do **PgAdmin4**:

### Exemplo de configuração no `.env`:
```ini
DB_ENGINE=django.db.backends.postgresql
DB_HOST=localhost
DB_PORT=5432
DB_NAME=seu_banco
DB_USER=seu_usuario
DB_PASS=sua_senha

DJANGO_SECRET_KEY='sua-chave-secreta'
HASHID_FIELD_SALT='seu-salt-para-hashid'
```

### Configuração do banco no projeto:
```python
DATABASES = {
    'default': {
        'ENGINE': os.getenv('DB_ENGINE'),
        'NAME': os.getenv('DB_NAME'),
        'USER': os.getenv('DB_USER'),
        'PASSWORD': os.getenv('DB_PASS'),
        'HOST': os.getenv('DB_HOST'),
        'PORT': os.getenv('DB_PORT'),
    }
}
```

---

## 🚀 Comandos úteis para rodar o projeto

### 🔧 Criar migrações
```bash
python manage.py makemigrations
```
> Este comando cria arquivos de migração com base nas alterações feitas nos modelos no diretório `migrations/`.

---

### 🛠 Aplicar migrações
```bash
python manage.py migrate
```
> Aplica as migrações ao banco de dados, criando ou atualizando as tabelas conforme os modelos definidos.

---

### ▶️ Iniciar o servidor
```bash
python manage.py runserver
```
> Inicia o servidor local na URL padrão:  
> **`http://127.0.0.1:8000/`**

### 🗂 População inicial do banco de dados
- Arquivo `populate_cities.py`: contém um script para preencher o banco com dados de cidades para passagens.
- Para executar o script de população, utilize o seguinte comando:
```bash
python manage.py populate_cities 
python manage.py setup_groups

```
- Para acessar as cidades cadastradas:  
  **Rota de API:**  
  `http://localhost:8000/api/passage/city/`

---

## 📄 Informações adicionais
- **Linguagem e Framework principal:** Python + Django
- **Banco de dados:** PostgreSQL
- Este projeto apresenta as funcionalidades básicas de gerenciamento de usuários, embarcações, passagens e tickets, além de rotas para integração com outros sistemas.

