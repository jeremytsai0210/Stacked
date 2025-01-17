from flask import Blueprint, jsonify, request
from flask_login import login_required, current_user
from app.models import db, User

user_routes = Blueprint('users', __name__)

# Get all users
@user_routes.route('/')
@login_required
def users():
    """
    Query for all users and returns them in a list of user dictionaries
    """
    users = User.query.all()
    return {'users': [user.to_dict() for user in users]}

# Get a specific user
@user_routes.route('/<int:id>')
@login_required
def user(id):
    """
    Query for a user by id and returns that user in a dictionary
    """
    user = User.query.get(id)
    return user.to_dict()

# Update a user
@user_routes.route('/<int:user_id>', methods=['PUT'])
@login_required
def update_user(user_id):
    """
    Update a user by ID
    """
    user = User.query.get(user_id)
    if not user:
        return jsonify({'message': 'User not found'}), 404
    
    if user.id != current_user.id:
        return jsonify({'message': 'You are not authorized to update this user'}), 403
    
    data = request.get_json()
    first_name = data.get('first_name')
    last_name = data.get('last_name')
    username = data.get('username')
    email = data.get('email')

    if not first_name and not last_name and not username and not email:
        return jsonify({'message': 'Invalid data'}), 400
    
    user.first_name = first_name
    user.last_name = last_name
    user.username = username
    user.email = email
    db.session.commit()

    return jsonify({ 
        'message': 'User updated successfully', 
        'user': user.to_dict() 
    }), 200

# Delete a user
@user_routes.route('/<int:user_id>', methods=['DELETE'])
@login_required
def delete_user(user_id):
    """
    Delete a user by ID
    """
    user = User.query.get(user_id)
    if not user:
        return jsonify({'message': 'User not found'}), 404
    
    if not current_user.is_admin:
        return jsonify({'message': 'You are not authorized to delete this user'}), 403
    
    if current_user.is_admin:
        db.session.delete(user)
        db.session.commit()
        return jsonify({ 'message': 'User deleted successfully' }), 200
    
    return jsonify({'error': 'Something went wrong'}), 500