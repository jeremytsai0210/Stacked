from flask import Blueprint, jsonify, request
from flask_login import login_required, current_user
from app.models import db, Avatar
from app.forms import AvatarForm

avatar_routes = Blueprint('avatars', __name__)

# Get all default avatars
@avatar_routes.route('/')
def avatars():
    """
    Query for all avatars and returns them in a list of avatar dictionaries
    """
    avatars = Avatar.query.filter_by(is_default=True).all()
    if not avatars:
        return jsonify({'message': 'No avatars found'}), 404

    return jsonify({'avatars': [avatar.to_dict() for avatar in avatars]}), 200

# Get all avatars of the current user
@avatar_routes.route('/user/<int:user_id>')
@login_required
def user_avatars(user_id):
    """
    Query for all avatars of the current user and returns them in a list of avatar dictionaries
    """
    if user_id != current_user.id:
        return jsonify({'message': 'You are not authorized to view these avatars'}), 403
    
    avatars = Avatar.query.filter_by(user_id=user_id).all()
    if not avatars:
        return jsonify({'message': 'User did not create any avatars'}), 404
    
    return jsonify({'avatars': [avatar.to_dict() for avatar in avatars]}), 200

# Create a new avatar
@avatar_routes.route('/new', methods=['POST'])
@login_required
def new_avatar():
    """
    Create a new avatar and returns it as an avatar dictionary
    """
    form = AvatarForm()
    form['csrf_token'].data = request.cookies['csrf_token']

    if form.validate_on_submit():
        avatar = Avatar(
            user_id = current_user.id,
            avatar_image = form.data['avatar_image'],
            description = form.data['description'],
            is_default = False,
            selected = False
        )
        db.session.add(avatar)
        db.session.commit()
        return jsonify({'avatar': avatar.to_dict()}), 201
    
    return jsonify({
        'message': 'Failed to create a new avatar',
        'errors': form.errors
    }), 400

# Update an avatar
@avatar_routes.route('/<int:avatar_id>', methods=['PUT'])
@login_required
def update_avatar(avatar_id):
    """
    Update an avatar and returns it as an avatar dictionary
    """
    avatar = Avatar.query.get(avatar_id)
    if not avatar:
        return jsonify({'message': 'Avatar not found'}), 404
    
    if avatar.user_id != current_user.id:
        return jsonify({'message': 'You are not authorized to update this avatar'}), 403
    
    data = request.get_json()
    existing_data = avatar.to_dict()
    form = AvatarForm(data={**existing_data, **data})
    form['csrf_token'].data = request.cookies['csrf_token']

    if form.validate_on_submit():
        avatar.avatar_image = form.data['avatar_image']
        avatar.description = form.data['description']
        db.session.commit()
        return jsonify({'avatar': avatar.to_dict()}), 200
    
    return jsonify({
        'message': 'Failed to update the avatar',
        'errors': form.errors
    }), 400

# Select an avatar
@avatar_routes.route('/select/<int:avatar_id>', methods=['PUT'])
@login_required
def select_avatar(avatar_id):
    """
    Select an avatar for the current user
    """
    avatar = Avatar.query.get(avatar_id)
    if not avatar:
        return jsonify({'message': 'Avatar not found'}), 404
    
    if avatar.user_id != current_user.id and not avatar.is_default:
        return jsonify({'message': 'You are not authorized to select this avatar'}), 403
    
    Avatar.query.filter_by(user_id=current_user.id, selected=True).update({'selected': False})
    avatar.selected = True

    db.session.commit()

    return jsonify({
        'message': 'Avatar selected successfully',
        'avatar': avatar.to_dict()
    }), 200


# Delete an avatar
@avatar_routes.route('/<int:avatar_id>', methods=['DELETE'])
@login_required
def delete_avatar(avatar_id):
    """
    Delete an avatar
    """
    avatar = Avatar.query.get(avatar_id)
    if not avatar:
        return jsonify({'message': 'Avatar not found'}), 404
    
    if avatar.user_id != current_user.id:
        return jsonify({'message': 'You are not authorized to delete this avatar'}), 403
    
    db.session.delete(avatar)
    db.session.commit()
    return jsonify({'message': 'Avatar deleted successfully'}), 200