# ⛵ Projeto NauticaPass-Core

Esta API está sendo desenvolvida para fins didáticos, a fim de ser apresentada na nossa **FeiraTech**.

---

## ⚙️ Configuração Inicial

No arquivo [`settings.py`](nauticapass_core/settings.py), altere a variável `DATABASES` com suas credenciais do **PgAdmin4**:

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'seu_banco',
        'USER': 'seu_usuario',
        'PASSWORD': 'sua_senha',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
```

---

## 🚀 Comandos para rodar o projeto

### 🔧 Criar migrações

```bash
python manage.py makemigrations
```

> Gera os arquivos de migração com base nas mudanças feitas nos modelos.

---

### 🛠 Aplicar migrações

```bash
python manage.py migrate
```

> Aplica as migrações ao banco de dados, criando ou atualizando as tabelas.

---

### ▶️ Iniciar o servidor

```bash
python manage.py runserver
```

> Inicia o servidor local em `http://127.0.0.1:8000/`.
> 
> Arquivo populate_cities.py contem script para popular o banco de dados com cidades para passagens
> rota que pega todas as cidades cadastradas: http://localhost:8000/api/passage/city/
