from flask import Blueprint, request, jsonify
from app.models import db, Product, Category

products_bp = Blueprint('products', __name__, url_prefix='/api/products')

@products_bp.route('', methods=['GET'])
def get_products():
    """
    Get all products
    ---
    tags:
      - Products
    parameters:
      - name: category_id
        in: query
        type: integer
        required: false
    responses:
      200:
        description: Lista de produtos
        schema:
          type: array
          items:
            $ref: '#/definitions/Product'
    """
    category_id = request.args.get('category_id', type=int)
    if category_id:
        products = Product.query.filter_by(category_id=category_id).all()
    else:
        products = Product.query.all()
    return jsonify([p.to_dict() for p in products])

@products_bp.route('', methods=['POST'])
def create_product():
    """
    Create a new product
    ---
    tags:
      - Products
    parameters:
      - name: body
        in: body
        required: true
        schema:
          type: object
          required:
            - name
            - price
          properties:
            name:
              type: string
            description:
              type: string
            price:
              type: number
            stock:
              type: integer
            category_id:
              type: integer
    responses:
      201:
        description: Produto criado
        schema:
          $ref: '#/definitions/Product'
      400:
        description: Erro de validação
    """
    data = request.get_json()
    if not data or not data.get('name') or not data.get('price'):
        return jsonify({'error': 'Name and price are required'}), 400
    
    product = Product(
        name=data['name'],
        description=data.get('description'),
        price=data['price'],
        stock=data.get('stock', 0),
        category_id=data.get('category_id')
    )
    db.session.add(product)
    db.session.commit()
    return jsonify(product.to_dict()), 201

@products_bp.route('/<int:id>', methods=['PUT'])
def update_product(id):
    """
    Update a product
    ---
    tags:
      - Products
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
            description:
              type: string
            price:
              type: number
            stock:
              type: integer
            category_id:
              type: integer
    responses:
      200:
        description: Produto atualizado
        schema:
          $ref: '#/definitions/Product'
      404:
        description: Produto não encontrado
    """
    product = Product.query.get(id)
    if not product:
        return jsonify({'error': 'Product not found'}), 404
    
    data = request.get_json()
    if data.get('name'):
        product.name = data['name']
    if 'description' in data:
        product.description = data['description']
    if data.get('price'):
        product.price = data['price']
    if 'stock' in data:
        product.stock = data['stock']
    if 'category_id' in data:
        product.category_id = data['category_id']
    
    db.session.commit()
    return jsonify(product.to_dict())

@products_bp.route('/<int:id>', methods=['DELETE'])
def delete_product(id):
    """
    Delete a product
    ---
    tags:
      - Products
    parameters:
      - name: id
        in: path
        type: integer
        required: true
    responses:
      200:
        description: Produto deletado
      404:
        description: Produto não encontrado
    """
    product = Product.query.get(id)
    if not product:
        return jsonify({'error': 'Product not found'}), 404
    
    db.session.delete(product)
    db.session.commit()
    return jsonify({'message': 'Product deleted'})