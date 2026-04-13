from flask import Blueprint, request, jsonify
from app.models import db, Category

categories_bp = Blueprint('categories', __name__, url_prefix='/api/categories')

@categories_bp.route('', methods=['GET'])
def get_categories():
    """
    Get all categories
    ---
    tags:
      - Categories
    responses:
      200:
        description: Lista de categorias
        schema:
          type: array
          items:
            $ref: '#/definitions/Category'
    """
    categories = Category.query.all()
    return jsonify([c.to_dict() for c in categories])

@categories_bp.route('', methods=['POST'])
def create_category():
    """
    Create a new category
    ---
    tags:
      - Categories
    parameters:
      - name: body
        in: body
        required: true
        schema:
          type: object
          required:
            - name
          properties:
            name:
              type: string
            description:
              type: string
    responses:
      201:
        description: Categoria criada
        schema:
          $ref: '#/definitions/Category'
      400:
        description: Erro de validação
    """
    data = request.get_json()
    if not data or not data.get('name'):
        return jsonify({'error': 'Name is required'}), 400
    
    category = Category(
        name=data['name'],
        description=data.get('description')
    )
    db.session.add(category)
    db.session.commit()
    return jsonify(category.to_dict()), 201

@categories_bp.route('/<int:id>', methods=['PUT'])
def update_category(id):
    """
    Update a category
    ---
    tags:
      - Categories
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
    responses:
      200:
        description: Categoria atualizada
        schema:
          $ref: '#/definitions/Category'
      404:
        description: Categoria não encontrada
    """
    category = Category.query.get(id)
    if not category:
        return jsonify({'error': 'Category not found'}), 404
    
    data = request.get_json()
    if data.get('name'):
        category.name = data['name']
    if 'description' in data:
        category.description = data['description']
    
    db.session.commit()
    return jsonify(category.to_dict())

@categories_bp.route('/<int:id>', methods=['DELETE'])
def delete_category(id):
    """
    Delete a category
    ---
    tags:
      - Categories
    parameters:
      - name: id
        in: path
        type: integer
        required: true
    responses:
      200:
        description: Categoria deletada
      404:
        description: Categoria não encontrada
    """
    category = Category.query.get(id)
    if not category:
        return jsonify({'error': 'Category not found'}), 404
    
    db.session.delete(category)
    db.session.commit()
    return jsonify({'message': 'Category deleted'})