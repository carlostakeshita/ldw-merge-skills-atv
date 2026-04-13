# LDW Library Backend API

Uma API REST completa para gerenciamento de biblioteca, construida com Flask, Flasgger e PostgreSQL.

## Objetivo

Desenvolver um backend robusto com quatro modulos principais:
- Autores (authors)
- Livros (books) 
- Membros (members)
- Emprestimos (loans)

Cada modulo suporta operacoes CRUD completas (GET, POST, PUT, DELETE), com documentacao automatica via Swagger UI.

## Tecnologias Utilizadas

- Python 3.14+
- uv (gerenciador de pacotes/ambientes)
- Flask (framework web)
- Flasgger (documentacao Swagger)
- Flask-SQLAlchemy (ORM para banco de dados)
- PostgreSQL (banco de dados relacional)
- Docker Compose (orquestracao de containers)

## Estrutura do Projeto

apps/
└── backend/
    ├── main.py (ponto de entrada)
    ├── src/
    │   ├── models.py (modelos SQLAlchemy)
    │   ├── routes/ (blueprints dos endpoints)
    │   └── db/
    │       └── seed.sql (dados de exemplo)
    ├── docker-compose.yml (PostgreSQL)
    ├── pyproject.toml (dependencias uv)

## Pre-requisitos

- Python 3.14+
- uv (pip install uv)
- Docker Desktop
- Prompt de Comando (CMD)

## Instruções de Execução

No diretorio apps/backend:

1. copy .env.example .env

2. docker compose up -d

3. uv sync --project .

4. uv run --project . python main.py

URLs:
- API Base: http://localhost:5000
- Swagger Docs: http://localhost:5000/docs/
- Health Check: http://localhost:5000/health

## Endpoints

Base URL: http://localhost:5000/api

- Authors: GET/POST /authors, PUT/DELETE /authors/{id}
- Books: GET/POST /books, PUT/DELETE /books/{id}
- Members: GET/POST /members, PUT/DELETE /members/{id}
- Loans: GET/POST /loans, PUT/DELETE /loans/{id}

## Solução de Problemas

- Erro can't open file: verifique cd apps\backend
- Porta 5432 em uso: pare outros Postgres ou altere docker-compose.yml
- Verifique docker ps para container library_postgres

Licenca: Projeto educacional/demonstracao.
