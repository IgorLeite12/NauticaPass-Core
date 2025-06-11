# ⛵ Projeto NauticaPass-Core

Uma API desenvolvida para fins didáticos e apresentada como parte da nossa **FeiraTech**.

---

## ⚙️ Configuração Inicial

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
```
- Para acessar as cidades cadastradas:  
  **Rota de API:**  
  `http://localhost:8000/api/passage/city/`

---

## 📄 Informações adicionais
- **Linguagem e Framework principal:** Python + Django
- **Banco de dados:** PostgreSQL
- Este projeto apresenta as funcionalidades básicas de gerenciamento de usuários, embarcações, passagens e tickets, além de rotas para integração com outros sistemas.

