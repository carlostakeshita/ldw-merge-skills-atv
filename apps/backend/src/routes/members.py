from flask import Blueprint, request, jsonify
from apps.backend.main import db
from apps.backend.src.models import Member

members_bp = Blueprint('members', __name__)

@members_bp.route('/members', methods=['GET'])
def get_members():
    """Get all members"""
    members = Member.query.all()
    return jsonify([m.to_dict() for m in members])

@members_bp.route('/members', methods=['POST'])
def create_member():
    """Create a new member"""
    data = request.get_json()
    if not data or not data.get('name') or not data.get('email'):
        return jsonify({"error": "Name and email are required"}), 400
    
    member = Member(
        name=data['name'],
        email=data['email'],
        phone=data.get('phone')
    )
    db.session.add(member)
    db.session.commit()
    return jsonify(member.to_dict()), 201

@members_bp.route('/members/<int:id>', methods=['PUT'])
def update_member(id):
    """Update a member"""
    member = Member.query.get(id)
    if not member:
        return jsonify({"error": "Member not found"}), 404
    
    data = request.get_json()
    if data.get('name'):
        member.name = data['name']
    if data.get('email'):
        member.email = data['email']
    if 'phone' in data:
        member.phone = data['phone']
    
    db.session.commit()
    return jsonify(member.to_dict())

@members_bp.route('/members/<int:id>', methods=['DELETE'])
def delete_member(id):
    """Delete a member"""
    member = Member.query.get(id)
    if not member:
        return jsonify({"error": "Member not found"}), 404
    
    db.session.delete(member)
    db.session.commit()
    return jsonify({"message": "Member deleted"})