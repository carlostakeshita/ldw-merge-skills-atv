Projeto LDW - Backend Biblioteca
API REST para gerenciamento de biblioteca desenvolvida com Flask, Flasgger e PostgreSQL. O sistema está dividido em quatro módulos principais: autores (authors), livros (books), membros (members) e empréstimos (loans).

Tecnologias Utilizadas
Linguagem: Python 3.14+

Gerenciador de Pacotes: uv

Framework Web: Flask

ORM: Flask-SQLAlchemy

Documentação: Flasgger (Swagger UI)

Banco de Dados: PostgreSQL

Containerização: Docker Compose

Estrutura do Diretório
apps/backend/main.py: Ponto de entrada da API.

apps/backend/src/models.py: Modelos de dados do SQLAlchemy.

apps/backend/src/routes/: Blueprints contendo as rotas da aplicação.

apps/backend/src/db/seed.sql: Script SQL para população inicial do banco.

apps/backend/docker-compose.yml: Configuração do serviço PostgreSQL.

Instruções para Execução (Windows/CMD)
Siga os passos abaixo para configurar e iniciar o ambiente de desenvolvimento.

1. Navegação
Acesse a pasta do backend:

cd ldw-merge-skills-atv\apps\backend

2. Configuração de Variáveis de Ambiente
Crie o arquivo .env a partir do exemplo:

copy .env.example .env

3. Infraestrutura de Banco de Dados
Inicie o container do PostgreSQL (requer Docker Desktop ativo):

docker compose up -d

Configurações padrão: Host localhost, Porta 5432, Base library_db, Usuário/Senha postgres.

4. Instalação e Inicialização
Instale as dependências e rode a API utilizando o gerenciador uv:

uv sync --project .
uv run --project . python main.py

Endpoints e Documentação
Swagger UI: http://localhost:5000/docs/

API Base URL: http://localhost:5000/api

Health Check: http://localhost:5000/health

Carga de Dados Inicial (Seed)
Após a primeira execução da API para criação das tabelas, utilize o comando abaixo para popular o banco:

docker exec -i library_postgres psql -U postgres -d library_db < src\db\seed.sql

Resolução de Problemas
Erro de arquivo não encontrado: Certifique-se de que o terminal está operando dentro da pasta apps\backend.

Conflito na porta 5432: Verifique se não há outra instância do PostgreSQL rodando localmente fora do Docker.

Falha na conexão: Utilize docker ps para validar se o container library_postgres está com status "Up".

Comandos de Manutenção
Parar a API: Ctrl + C no terminal em execução.

Parar o banco de dados: docker compose down

Limpar volumes e resetar banco: docker compose down -v
