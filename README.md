# Flask API com Flasgger

API RESTful com Flask e Flasgger para documentação automática.

## Requisitos

- Python 3.11+
- Docker e Docker Compose

## Como Rodar

### Opção 1: Docker Compose (Recomendado)

```bash
# Iniciar os serviços
docker-compose up --build

# Acessar a aplicação
# http://localhost:5000

# Documentação da API (Swagger UI)
# http://localhost:5000/apidocs
```

### Opção 2: Execução Local

```bash
# Criar ambiente virtual
python -m venv venv
source venv/bin/activate  # Linux/Mac
# ou
venv\Scripts\activate  # Windows

# Instalar dependências
pip install -r requirements.txt

# Iniciar PostgreSQL com Docker
docker run -d -e POSTGRES_USER=postgres -e POSTGRES_PASSWORD=postgres -e POSTGRES_DB=flaskdb -p 5432:5432 postgres:15-alpine

# Criar migrations
flask db init
flask db migrate -m "Initial migration"
flask db upgrade

#popular banco com dados iniciais
python seed.py

# Iniciar servidor
python run.py
```

## Endpoints da API

### Categories
| Método | Endpoint | Descrição |
|--------|----------|------------|
| GET | `/api/categories` | Listar todas |
| POST | `/api/categories` | Criar nova |
| PUT | `/api/categories/<id>` | Atualizar |
| DELETE | `/api/categories/<id>` | Deletar |

### Products
| Método | Endpoint | Descrição |
|--------|----------|------------|
| GET | `/api/products` | Listar todos |
| POST | `/api/products` | Criar novo |
| PUT | `/api/products/<id>` | Atualizar |
| DELETE | `/api/products/<id>` | Deletar |

### Clients
| Método | Endpoint | Descrição |
|--------|----------|------------|
| GET | `/api/clients` | Listar todos |
| POST | `/api/clients` | Criar novo |
| PUT | `/api/clients/<id>` | Atualizar |
| DELETE | `/api/clients/<id>` | Deletar |

### Orders
| Método | Endpoint | Descrição |
|--------|----------|------------|
| GET | `/api/orders` | Listar todos |
| POST | `/api/orders` | Criar novo |
| PUT | `/api/orders/<id>` | Atualizar |
| DELETE | `/api/orders/<id>` | Deletar |

## Variáveis de Ambiente

| Variável | Valor Padrão | Descrição |
|----------|--------------|------------|
| `DATABASE_URL` | `postgresql://postgres:postgres@localhost:5432/flaskdb` | String de conexão |
| `SECRET_KEY` | `dev-secret-key` | Chave secreta |

## Documentação

A documentação Swagger está disponível em: `http://localhost:5000/apidocs`

## Estrutura do Projeto

```
.
├── app/
│   ├── __init__.py      # App factory
│   ├── blueprints/      # Blueprints (routes)
│   │   ├── categories.py
│   │   ├── products.py
│   │   ├── clients.py
│   │   └── orders.py
│   └── models/          # Modelos SQLAlchemy
│       └── __init__.py
├── config.py            # Configurações
├── run.py              # Entry point
├── seed.py             # Dados iniciais
├── requirements.txt    # Dependências
├── Dockerfile
├── docker-compose.yml
└── README.md
```