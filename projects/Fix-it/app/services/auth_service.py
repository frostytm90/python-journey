from flask import current_app
from flask_jwt_extended import create_access_token, create_refresh_token
from ..models.user import User, Role, DEFAULT_ROLES
from .. import db
from datetime import timedelta

class AuthService:
    @staticmethod
    def initialize_roles():
        """Initialize default roles if they don't exist"""
        for role_key, role_data in DEFAULT_ROLES.items():
            role = Role.query.filter_by(name=role_data['name']).first()
            if not role:
                role = Role(
                    name=role_data['name'],
                    description=role_data['description'],
                    permissions=role_data['permissions']
                )
                db.session.add(role)
        db.session.commit()
    
    @staticmethod
    def create_user(email, username, password, role_name='developer'):
        """Create a new user with specified role"""
        # Check if user already exists
        if User.query.filter((User.email == email) | (User.username == username)).first():
            raise ValueError('User with this email or username already exists')
        
        # Get role
        role = Role.query.filter_by(name=DEFAULT_ROLES[role_name]['name']).first()
        if not role:
            raise ValueError('Invalid role specified')
        
        # Create user
        user = User(email=email, username=username, password=password, role_id=role.id)
        db.session.add(user)
        db.session.commit()
        return user
    
    @staticmethod
    def authenticate_user(username, password):
        """Authenticate user and return tokens"""
        user = User.query.filter_by(username=username).first()
        
        if not user or not user.check_password(password):
            return None
        
        if not user.is_active:
            raise ValueError('Account is deactivated')
        
        # Update last login
        user.update_last_login()
        
        # Generate tokens
        access_token = create_access_token(
            identity=user.id,
            additional_claims={
                'username': user.username,
                'role': user.role.name,
                'permissions': user.role.permissions
            },
            expires_delta=timedelta(hours=1)
        )
        
        refresh_token = create_refresh_token(
            identity=user.id,
            expires_delta=timedelta(days=30)
        )
        
        return {
            'access_token': access_token,
            'refresh_token': refresh_token,
            'user': {
                'id': user.id,
                'username': user.username,
                'email': user.email,
                'role': user.role.name,
                'permissions': user.role.permissions
            }
        }
    
    @staticmethod
    def get_user_by_id(user_id):
        """Get user by ID"""
        return User.query.get(user_id)
    
    @staticmethod
    def update_user_role(user_id, role_name):
        """Update user's role"""
        user = User.query.get(user_id)
        if not user:
            raise ValueError('User not found')
        
        role = Role.query.filter_by(name=DEFAULT_ROLES[role_name]['name']).first()
        if not role:
            raise ValueError('Invalid role specified')
        
        user.role_id = role.id
        db.session.commit()
        return user
    
    @staticmethod
    def deactivate_user(user_id):
        """Deactivate user account"""
        user = User.query.get(user_id)
        if not user:
            raise ValueError('User not found')
        
        user.is_active = False
        db.session.commit()
        return user
