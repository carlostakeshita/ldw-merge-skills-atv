from flask import Blueprint, request, jsonify
from apps.backend.main import db
from apps.backend.src.models import Loan

loans_bp = Blueprint('loans', __name__)

@loans_bp.route('/loans', methods=['GET'])
def get_loans():
    """Get all loans"""
    loans = Loan.query.all()
    return jsonify([l.to_dict() for l in loans])

@loans_bp.route('/loans', methods=['POST'])
def create_loan():
    """Create a new loan"""
    data = request.get_json()
    if not data or not data.get('book_id') or not data.get('member_id'):
        return jsonify({"error": "Book_id and member_id are required"}), 400
    
    loan = Loan(
        book_id=data['book_id'],
        member_id=data['member_id']
    )
    db.session.add(loan)
    db.session.commit()
    return jsonify(loan.to_dict()), 201

@loans_bp.route('/loans/<int:id>', methods=['PUT'])
def update_loan(id):
    """Update a loan"""
    loan = Loan.query.get(id)
    if not loan:
        return jsonify({"error": "Loan not found"}), 404
    
    data = request.get_json()
    if data.get('book_id'):
        loan.book_id = data['book_id']
    if data.get('member_id'):
        loan.member_id = data['member_id']
    if data.get('return_date'):
        loan.return_date = data['return_date']
    
    db.session.commit()
    return jsonify(loan.to_dict())

@loans_bp.route('/loans/<int:id>', methods=['DELETE'])
def delete_loan(id):
    """Delete a loan"""
    loan = Loan.query.get(id)
    if not loan:
        return jsonify({"error": "Loan not found"}), 404
    
    db.session.delete(loan)
    db.session.commit()
    return jsonify({"message": "Loan deleted"})