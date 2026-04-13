from flask import Blueprint, request, jsonify
from app.models import db, Order, Client
from decimal import Decimal

orders_bp = Blueprint('orders', __name__, url_prefix='/api/orders')

@orders_bp.route('', methods=['GET'])
def get_orders():
    """
    Get all orders
    ---
    tags:
      - Orders
    parameters:
      - name: client_id
        in: query
        type: integer
        required: false
      - name: status
        in: query
        type: string
        required: false
    responses:
      200:
        description: Lista de pedidos
        schema:
          type: array
          items:
            $ref: '#/definitions/Order'
    """
    client_id = request.args.get('client_id', type=int)
    status = request.args.get('status')
    
    query = Order.query
    if client_id:
        query = query.filter_by(client_id=client_id)
    if status:
        query = query.filter_by(status=status)
    
    orders = query.all()
    return jsonify([o.to_dict() for o in orders])

@orders_bp.route('', methods=['POST'])
def create_order():
    """
    Create a new order
    ---
    tags:
      - Orders
    parameters:
      - name: body
        in: body
        required: true
        schema:
          type: object
          required:
            - client_id
          properties:
            client_id:
              type: integer
            status:
              type: string
    responses:
      201:
        description: Pedido criado
        schema:
          $ref: '#/definitions/Order'
      400:
        description: Erro de validação
    """
    data = request.get_json()
    if not data or not data.get('client_id'):
        return jsonify({'error': 'Client_id is required'}), 400
    
    client = Client.query.get(data['client_id'])
    if not client:
        return jsonify({'error': 'Client not found'}), 404
    
    order = Order(
        client_id=data['client_id'],
        total=data.get('total', 0),
        status=data.get('status', 'pending')
    )
    db.session.add(order)
    db.session.commit()
    return jsonify(order.to_dict()), 201

@orders_bp.route('/<int:id>', methods=['PUT'])
def update_order(id):
    """
    Update an order
    ---
    tags:
      - Orders
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
            total:
              type: number
            status:
              type: string
    responses:
      200:
        description: Pedido atualizado
        schema:
          $ref: '#/definitions/Order'
      404:
        description: Pedido não encontrado
    """
    order = Order.query.get(id)
    if not order:
        return jsonify({'error': 'Order not found'}), 404
    
    data = request.get_json()
    if data.get('total') is not None:
        order.total = data['total']
    if data.get('status'):
        order.status = data['status']
    
    db.session.commit()
    return jsonify(order.to_dict())

@orders_bp.route('/<int:id>', methods=['DELETE'])
def delete_order(id):
    """
    Delete an order
    ---
    tags:
      - Orders
    parameters:
      - name: id
        in: path
        type: integer
        required: true
    responses:
      200:
        description: Pedido deletado
      404:
        description: Pedido não encontrado
    """
    order = Order.query.get(id)
    if not order:
        return jsonify({'error': 'Order not found'}), 404
    
    db.session.delete(order)
    db.session.commit()
    return jsonify({'message': 'Order deleted'})