from .. import db
from flask_login import UserMixin
import bcrypt
from datetime import datetime

class Role(db.Model):
    __tablename__ = 'roles'
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique=True, nullable=False)
    description = db.Column(db.String(200))
    permissions = db.Column(db.JSON)  # Store permissions as JSON
    
    def __repr__(self):
        return f'<Role {self.name}>'

class User(UserMixin, db.Model):
    __tablename__ = 'users'
    
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password_hash = db.Column(db.String(128))
    role_id = db.Column(db.Integer, db.ForeignKey('roles.id'))
    is_active = db.Column(db.Boolean, default=True)
    last_login = db.Column(db.DateTime)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    
    role = db.relationship('Role', backref=db.backref('users', lazy=True))
    
    def __init__(self, email, username, password, role_id=None):
        self.email = email
        self.username = username
        self.set_password(password)
        self.role_id = role_id
    
    def set_password(self, password):
        """Hash password before storing"""
        salt = bcrypt.gensalt()
        self.password_hash = bcrypt.hashpw(password.encode('utf-8'), salt)
    
    def check_password(self, password):
        """Verify password"""
        return bcrypt.checkpw(password.encode('utf-8'), self.password_hash)
    
    def has_permission(self, permission):
        """Check if user has specific permission"""
        if not self.role or not self.role.permissions:
            return False
        return permission in self.role.permissions
    
    def update_last_login(self):
        """Update last login timestamp"""
        self.last_login = datetime.utcnow()
        db.session.commit()
    
    def __repr__(self):
        return f'<User {self.username}>'

# Define default roles and permissions
DEFAULT_ROLES = {
    'admin': {
        'name': 'Administrator',
        'description': 'Full system access',
        'permissions': [
            'manage_users',
            'manage_roles',
            'manage_events',
            'view_metrics',
            'manage_bugs',
            'export_data'
        ]
    },
    'manager': {
        'name': 'Project Manager',
        'description': 'Manage events and view metrics',
        'permissions': [
            'manage_events',
            'view_metrics',
            'manage_bugs'
        ]
    },
    'developer': {
        'name': 'Developer',
        'description': 'Participate in events and manage bugs',
        'permissions': [
            'view_metrics',
            'manage_bugs'
        ]
    }
}
