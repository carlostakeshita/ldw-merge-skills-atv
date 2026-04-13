from flask import Blueprint, request, jsonify
from apps.backend.main import db
from apps.backend.src.models import Author

authors_bp = Blueprint('authors', __name__)

@authors_bp.route('/authors', methods=['GET'])
def get_authors():
    """Get all authors"""
    authors = Author.query.all()
    return jsonify([a.to_dict() for a in authors])

@authors_bp.route('/authors', methods=['POST'])
def create_author():
    """Create a new author"""
    data = request.get_json()
    if not data or not data.get('name'):
        return jsonify({"error": "Name is required"}), 400
    
    author = Author(name=data['name'], bio=data.get('bio'))
    db.session.add(author)
    db.session.commit()
    return jsonify(author.to_dict()), 201

@authors_bp.route('/authors/<int:id>', methods=['PUT'])
def update_author(id):
    """Update an author"""
    author = Author.query.get(id)
    if not author:
        return jsonify({"error": "Author not found"}), 404
    
    data = request.get_json()
    if data.get('name'):
        author.name = data['name']
    if 'bio' in data:
        author.bio = data['bio']
    
    db.session.commit()
    return jsonify(author.to_dict())

@authors_bp.route('/authors/<int:id>', methods=['DELETE'])
def delete_author(id):
    """Delete an author"""
    author = Author.query.get(id)
    if not author:
        return jsonify({"error": "Author not found"}), 404
    
    db.session.delete(author)
    db.session.commit()
    return jsonify({"message": "Author deleted"})