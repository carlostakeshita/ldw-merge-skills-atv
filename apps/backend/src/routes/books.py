from flask import Blueprint, request, jsonify
from apps.backend.main import db
from apps.backend.src.models import Book

books_bp = Blueprint('books', __name__)

@books_bp.route('/books', methods=['GET'])
def get_books():
    """Get all books"""
    books = Book.query.all()
    return jsonify([b.to_dict() for b in books])

@books_bp.route('/books', methods=['POST'])
def create_book():
    """Create a new book"""
    data = request.get_json()
    if not data or not data.get('title'):
        return jsonify({"error": "Title is required"}), 400
    
    book = Book(
        title=data['title'],
        isbn=data.get('isbn'),
        available_copies=data.get('available_copies', 1),
        author_id=data.get('author_id')
    )
    db.session.add(book)
    db.session.commit()
    return jsonify(book.to_dict()), 201

@books_bp.route('/books/<int:id>', methods=['PUT'])
def update_book(id):
    """Update a book"""
    book = Book.query.get(id)
    if not book:
        return jsonify({"error": "Book not found"}), 404
    
    data = request.get_json()
    if data.get('title'):
        book.title = data['title']
    if 'isbn' in data:
        book.isbn = data['isbn']
    if 'available_copies' in data:
        book.available_copies = data['available_copies']
    if 'author_id' in data:
        book.author_id = data['author_id']
    
    db.session.commit()
    return jsonify(book.to_dict())

@books_bp.route('/books/<int:id>', methods=['DELETE'])
def delete_book(id):
    """Delete a book"""
    book = Book.query.get(id)
    if not book:
        return jsonify({"error": "Book not found"}), 404
    
    db.session.delete(book)
    db.session.commit()
    return jsonify({"message": "Book deleted"})