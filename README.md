# Backend API Biblioteca

API REST para gerenciamento de biblioteca usando Flask, Flasgger e PostgreSQL.

## Objetivo

Sistema backend com modulos para authors, books, members e loans. Cada modulo tem endpoints GET, POST, PUT, DELETE totalmente documentados no Swagger.

## Tecnologias usadas

```
Python 3.14+
uv (gerenciador rapido)
Flask (web framework)
Flasgger (Swagger docs)
Flask-SQLAlchemy (ORM)
PostgreSQL (banco)
Docker Compose (containers)
```

## Estrutura dos arquivos

```
apps/backend/main.py : inicia a API
apps/backend/src/models.py : modelos do banco
apps/backend/src/routes/ : endpoints por modulo
apps/backend/src/db/seed.sql : dados de teste
apps/backend/docker-compose.yml : config Postgres
apps/backend/pyproject.toml : dependencias uv
```

## Pre-requisitos antes de começar

```
Instale e tenha pronto:
Python 3.14+
uv (pip install uv)
Docker Desktop aberto
Use CMD como terminal
```

## Como executar - Passo a passo no CMD

### Metodo 1: Entrando na pasta backend (recomendado)

```
1. cd apps\backend

2. copy .env.example .env   (cria config ambiente)

3. docker compose up -d   (inicia Postgres)

4. Aguarde Docker iniciar (veja docker ps)

5. uv sync   (instala pacotes)

6. uv run python main.py   (roda API)
```

### Info do banco criado:

```
host: localhost
porta: 5432
database: library_db
usuario: postgres
senha: postgres
```

### URLs disponiveis:

```
API base: http://localhost:5000
Documentacao Swagger: http://localhost:5000/docs/
Health check: http://localhost:5000/health
```

### Metodo 2: Executando da pasta raiz

```
Da 'Nova pasta (2)':
uv sync --project apps/backend
uv run --project apps/backend python apps/backend/main.py
```

## Como popular com dados de teste (Seed)

```
1. Rode API uma vez (cria tabelas)

2. cd apps\backend

3. docker exec -i library_postgres psql -U postgres -d library_db < src\db\seed.sql
```

## Lista de endpoints

```
Todos em http://localhost:5000/api

Authors - GET/POST /authors , PUT/DELETE /authors/{id}
Books - GET/POST /books , PUT/DELETE /books/{id}
Members - GET/POST /members , PUT/DELETE /members/{id}
Loans - GET/POST /loans , PUT/DELETE /loans/{id}
```

## Exemplos de uso rapido

```
Criar autor (use curl ou Postman):

POST http://localhost:5000/api/authors
Content-Type: application/json
{
  "name": "Jorge Amado",
  "bio": "Autor baiano famoso"
}
```

```
Criar livro:

POST http://localhost:5000/api/books
{
  "title": "Capitães da Areia",
  "isbn": "9788501000011",
  "available_copies": 5,
  "author_id": 1
}
```

## Resolucao de problemas comuns

```
Problema: Arquivo main.py nao encontrado
Solucao: Certifique cd apps\backend antes do uv run python main.py

Problema: Porta 5432 ja usada
Solucao: docker compose down   ou feche outro Postgres local

Problema: API nao sobe
Verifique: docker ps  (container library_postgres deve estar up)
```

## Comandos importantes do dia a dia

```
Parar API: Ctrl + C no terminal

Parar apenas banco:
cd apps\backend
docker compose down

Limpar e recriar banco (perde dados):
docker compose down -v
docker compose up -d

Ver logs banco:
docker compose logs
```

Projeto para estudo e pratica de API Flask.
