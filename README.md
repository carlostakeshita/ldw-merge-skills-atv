# Library Backend API - Flask + Flasgger

API REST completa para biblioteca: autores, livros, membros, emprestimos. CRUD + Swagger docs automaticos.

## Requisitos

- Python 3.14+
- uv (instale: pip install uv ou https://uv.rs)
- Docker Desktop ativo
- Terminal: Prompt de Comando (CMD)

## Passo a Passo para Executar

Abra CMD e execute:

1. Navegue ate backend:
```
cd apps\backend
```

2. Crie arquivo .env (copie exemplo se existir):
```
copy .env.example .env
```

3. Inicie banco PostgreSQL:
```
docker compose up -d
```
Aguarde ~30s. Verifique:
```
docker ps
```
Veja container library_postgres rodando.

Credenciais DB:
- Host: localhost
- Porta: 5432
- DB: library_db
- User: postgres
- Pass: postgres

4. Instale pacotes:
```
uv sync
```

5. Rode a API:
```
uv run python main.py
```

API roda em http://localhost:5000
- Docs Swagger: http://localhost:5000/docs/
- Health check: http://localhost:5000/health

Primeira execucao cria tabelas automaticamente.

## Endpoints Base: /api

Autores: GET/POST /authors   PUT/DELETE /authors/{id}
Livros: GET/POST /books   PUT/DELETE /books/{id}
Membros: GET/POST /members   PUT/DELETE /members/{id}
Emprestimos: GET/POST /loans   PUT/DELETE /loans/{id}

Exemplo criar autor (PowerShell ou curl):
```
curl -X POST http://localhost:5000/api/authors -H "Content-Type: application/json" -d "{\"name\": \"Jorge Amado\", \"bio\": \"Escritor brasileiro\"}"
```

## Dados de Exemplo (Seed)

```
docker exec -i library_postgres psql -U postgres -d library_db < src\db\seed.sql
```

## Parar Tudo

```
Ctrl+C  (API)
docker compose down  (DB)
```

## Problemas Comuns

- "can't open file": Confirme cd apps\backend
- Porta 5432 usada: docker compose down -v  ou mude porta no docker-compose.yml
- uv nao encontrado: pip install uv
- Docker nao roda: abra Docker Desktop primeiro

Projeto educacional.
