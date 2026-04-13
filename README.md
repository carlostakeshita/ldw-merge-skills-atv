# Projeto LDW - Backend Biblioteca

API REST para gerenciamento de biblioteca usando Flask, Flasgger e PostgreSQL.

## Objetivo

Backend com 4 modulos (authors, books, members e loans), cada um com GET, POST, PUT e DELETE, documentado no Swagger.

## Tecnologias

- Python 3.14+
- uv
- Flask
- Flasgger
- Flask-SQLAlchemy
- PostgreSQL
- Docker Compose

## Estrutura principal

- apps/backend/main.py (ponto de entrada da API)
- apps/backend/src/models.py (modelos do banco)
- apps/backend/src/routes/ (blueprints)
- apps/backend/src/db/seed.sql (dados iniciais)
- apps/backend/docker-compose.yml (PostgreSQL)

## Pre-requisitos

- Python 3.14+
- uv instalado
- Docker Desktop ativo
- CMD (Prompt de Comando)

## Execucao no CMD

Rode os comandos abaixo no CMD.

### 1. Entrar na pasta do projeto

cd ldw-merge-skills-atv

### 2. Entrar no backend

cd apps\backend

### 3. Criar arquivo .env

copy .env.example .env

### 4. Subir o banco

docker compose up -d

Banco padrao:
- host: localhost
- porta: 5432
- database: library_db
- usuario: postgres
- senha: postgres

### 5. Instalar dependencias

uv sync --project .

### 6. Iniciar a API

uv run --project . python main.py

URLs:
- API: http://localhost:5000
- Swagger: http://localhost:5000/docs/
- Health: http://localhost:5000/health

## Seed SQL

Depois da primeira subida da API (para criar tabelas), aplique o seed.

docker exec -i library_postgres psql -U postgres -d library_db < src\db\seed.sql

## Endpoints

Base URL: http://localhost:5000/api

- Authors: GET/POST /authors, PUT/DELETE /authors/{id}
- Books: GET/POST /books, PUT/DELETE /books/{id}
- Members: GET/POST /members, PUT/DELETE /members/{id}
- Loans: GET/POST /loans, PUT/DELETE /loans/{id}

## Exemplo rapido

Criar autor:

POST /api/authors
Content-Type: application/json

{
  "name": "Jorge Amado",
  "bio": "Autor baiano"
}

Criar livro:

POST /api/books
Content-Type: application/json

{
  "title": "Capitaes da Areia",
  "isbn": "9788501000011",
  "available_copies": 5,
  "author_id": 1
}

## Troubleshooting

### Erro: can't open file

Cause: comando executado um nivel acima da pasta do projeto.

Correcao no CMD:

cd C:\Users\seuusuario\pasta\ldw-merge-skills-atv
uv run --project .\apps\backend python .\apps\backend\main.py

### Porta 5432 ocupada

Pare outro PostgreSQL local ou altere a porta no docker-compose.

### API nao inicia

Verifique se o container do banco esta rodando:

docker ps

## Comandos uteis

Parar API: Ctrl + C no terminal da API.

Parar banco:

docker compose down

Recriar banco do zero (remove dados):

docker compose down -v
docker compose up -d
