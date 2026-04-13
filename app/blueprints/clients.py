from flask import Blueprint, request, jsonify
from app.models import db, Client

clients_bp = Blueprint('clients', __name__, url_prefix='/api/clients')

@clients_bp.route('', methods=['GET'])
def get_clients():
    """
    Get all clients
    ---
    tags:
      - Clients
    responses:
      200:
        description: Lista de clientes
        schema:
          type: array
          items:
            $ref: '#/definitions/Client'
    """
    clients = Client.query.all()
    return jsonify([c.to_dict() for c in clients])

@clients_bp.route('', methods=['POST'])
def create_client():
    """
    Create a new client
    ---
    tags:
      - Clients
    parameters:
      - name: body
        in: body
        required: true
        schema:
          type: object
          required:
            - name
            - email
          properties:
            name:
              type: string
            email:
              type: string
            phone:
              type: string
            address:
              type: string
    responses:
      201:
        description: Cliente criado
        schema:
          $ref: '#/definitions/Client'
      400:
        description: Erro de validação
    """
    data = request.get_json()
    if not data or not data.get('name') or not data.get('email'):
        return jsonify({'error': 'Name and email are required'}), 400
    
    existing = Client.query.filter_by(email=data['email']).first()
    if existing:
        return jsonify({'error': 'Email already exists'}), 400
    
    client = Client(
        name=data['name'],
        email=data['email'],
        phone=data.get('phone'),
        address=data.get('address')
    )
    db.session.add(client)
    db.session.commit()
    return jsonify(client.to_dict()), 201

@clients_bp.route('/<int:id>', methods=['PUT'])
def update_client(id):
    """
    Update a client
    ---
    tags:
      - Clients
    parameters:
      - name: id
        in: path
        type: integer
        required: true
      - name: body
        in: body
        schema:
          type: object
          properties:
            name:
              type: string
            email:
              type: string
            phone:
              type: string
            address:
              type: string
    responses:
      200:
        description: Cliente atualizado
        schema:
          $ref: '#/definitions/Client'
      404:
        description: Cliente não encontrado
    """
    client = Client.query.get(id)
    if not client:
        return jsonify({'error': 'Client not found'}), 404
    
    data = request.get_json()
    if data.get('name'):
        client.name = data['name']
    if data.get('email'):
        existing = Client.query.filter(Client.email == data['email'], Client.id != id).first()
        if existing:
            return jsonify({'error': 'Email already exists'}), 400
        client.email = data['email']
    if 'phone' in data:
        client.phone = data['phone']
    if 'address' in data:
        client.address = data['address']
    
    db.session.commit()
    return jsonify(client.to_dict())

@clients_bp.route('/<int:id>', methods=['DELETE'])
def delete_client(id):
    """
    Delete a client
    ---
    tags:
      - Clients
    parameters:
      - name: id
        in: path
        type: integer
        required: true
    responses:
      200:
        description: Cliente deletado
      404:
        description: Cliente não encontrado
    """
    client = Client.query.get(id)
    if not client:
        return jsonify({'error': 'Client not found'}), 404
    
    db.session.delete(client)
    db.session.commit()
    return jsonify({'message': 'Client deleted'})