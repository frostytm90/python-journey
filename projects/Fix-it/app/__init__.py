from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from flask_jwt_extended import JWTManager
from flask_login import LoginManager
from config import config

db = SQLAlchemy()
jwt = JWTManager()
login_manager = LoginManager()

def create_app(config_name='default'):
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    
    # Initialize extensions
    db.init_app(app)
    CORS(app)
    jwt.init_app(app)
    login_manager.init_app(app)
    
    # Initialize login manager
    from .models.user import User
    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))
    
    # Initialize authentication
    from .services.auth_service import AuthService
    with app.app_context():
        db.create_all()
        AuthService.initialize_roles()
    
    # Register blueprints
    from .routes import api
    app.register_blueprint(api, url_prefix='/api')
    
    return app
