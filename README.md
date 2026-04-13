Projeto LDW - Backend Biblioteca
Esta é uma API REST desenvolvida para o gerenciamento de bibliotecas, utilizando o ecossistema Python moderno para integrar autores, livros, membros e empréstimos.

Tecnologias Utilizadas
Linguagem: Python 3.14+

Gerenciador de Pacotes: uv

Framework Web: Flask e Flask-SQLAlchemy

Documentação: Flasgger (Swagger UI)

Banco de Dados: PostgreSQL

Containerização: Docker Compose

Estrutura do Projeto
apps/backend/main.py: Ponto de entrada da aplicação.

apps/backend/src/models.py: Definição das entidades do banco de dados.

apps/backend/src/routes/: Blueprints para organização das rotas.

apps/backend/src/db/seed.sql: Script para carga inicial de dados.

apps/backend/docker-compose.yml: Configuração do banco de dados.

Guia de Instalação e Configuração
Execute os comandos abaixo via Prompt de Comando (CMD).

1. Preparação do Diretório
Acesse a pasta do projeto e o diretório do backend:

DOS
cd ldw-merge-skills-atv\apps\backend
2. Configuração de Ambiente
Crie o arquivo de configuração a partir do modelo disponível:

DOS
copy .env.example .env
3. Gerenciamento do Banco de Dados
Certifique-se de que o Docker está em execução e suba o serviço do PostgreSQL:

DOS
docker compose up -d
As credenciais padrão são host localhost, porta 5432, usuário e senha postgres.

4. Instalação e Execução
Utilize o uv para sincronizar dependências e iniciar o servidor:

DOS
uv sync --project .
uv run --project . python main.py
Endereços de Acesso
API Base: http://localhost:5000/api

Documentação Swagger: http://localhost:5000/docs/

Verificação de Status (Health): http://localhost:5000/health

Carga de Dados (Seed)
Após a primeira execução da API (necessária para a criação automática das tabelas), execute o comando abaixo para inserir os dados iniciais:

DOS
docker exec -i library_postgres psql -U postgres -d library_db < src\db\seed.sql
Resolução de Problemas
Arquivo não encontrado (can't open file): Verifique se o comando está sendo executado dentro do diretório apps\backend.

Porta 5432 ocupada: Encerre instâncias locais do PostgreSQL ou altere a porta mapeada no arquivo docker-compose.yml.

Reset do ambiente: Para remover o banco de dados e todos os dados armazenados, utilize o comando docker compose down -v.
