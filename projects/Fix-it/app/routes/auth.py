from flask import jsonify, request
from flask_jwt_extended import jwt_required, get_jwt_identity, get_jwt
from . import api
from ..services.auth_service import AuthService
from functools import wraps

auth_service = AuthService()

def admin_required():
    """Decorator to require admin role"""
    def wrapper(fn):
        @wraps(fn)
        def decorator(*args, **kwargs):
            jwt_data = get_jwt()
            if 'manage_users' not in jwt_data.get('permissions', []):
                return jsonify({'error': 'Admin access required'}), 403
            return fn(*args, **kwargs)
        return decorator
    return wrapper

@api.route('/auth/register', methods=['POST'])
@jwt_required()
@admin_required()
def register():
    """Register a new user (admin only)"""
    try:
        data = request.get_json()
        user = auth_service.create_user(
            email=data['email'],
            username=data['username'],
            password=data['password'],
            role_name=data.get('role', 'developer')
        )
        return jsonify({
            'message': 'User registered successfully',
            'user': {
                'id': user.id,
                'username': user.username,
                'email': user.email,
                'role': user.role.name
            }
        }), 201
    except ValueError as e:
        return jsonify({'error': str(e)}), 400
    except Exception as e:
        return jsonify({'error': 'Failed to register user'}), 500

@api.route('/auth/login', methods=['POST'])
def login():
    """Authenticate user and return tokens"""
    try:
        data = request.get_json()
        auth_data = auth_service.authenticate_user(
            username=data['username'],
            password=data['password']
        )
        
        if not auth_data:
            return jsonify({'error': 'Invalid credentials'}), 401
        
        return jsonify(auth_data)
    except ValueError as e:
        return jsonify({'error': str(e)}), 401
    except Exception as e:
        return jsonify({'error': 'Authentication failed'}), 500

@api.route('/auth/user', methods=['GET'])
@jwt_required()
def get_current_user():
    """Get current user information"""
    try:
        user_id = get_jwt_identity()
        user = auth_service.get_user_by_id(user_id)
        
        return jsonify({
            'id': user.id,
            'username': user.username,
            'email': user.email,
            'role': user.role.name,
            'permissions': user.role.permissions,
            'last_login': user.last_login.isoformat() if user.last_login else None
        })
    except Exception as e:
        return jsonify({'error': 'Failed to get user information'}), 500

@api.route('/auth/user/<int:user_id>/role', methods=['PUT'])
@jwt_required()
@admin_required()
def update_user_role(user_id):
    """Update user role (admin only)"""
    try:
        data = request.get_json()
        user = auth_service.update_user_role(user_id, data['role'])
        
        return jsonify({
            'message': 'User role updated successfully',
            'user': {
                'id': user.id,
                'username': user.username,
                'role': user.role.name
            }
        })
    except ValueError as e:
        return jsonify({'error': str(e)}), 400
    except Exception as e:
        return jsonify({'error': 'Failed to update user role'}), 500

@api.route('/auth/user/<int:user_id>/deactivate', methods=['POST'])
@jwt_required()
@admin_required()
def deactivate_user(user_id):
    """Deactivate user account (admin only)"""
    try:
        user = auth_service.deactivate_user(user_id)
        return jsonify({
            'message': 'User deactivated successfully',
            'user': {
                'id': user.id,
                'username': user.username,
                'is_active': user.is_active
            }
        })
    except ValueError as e:
        return jsonify({'error': str(e)}), 400
    except Exception as e:
        return jsonify({'error': 'Failed to deactivate user'}), 500
