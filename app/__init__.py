from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_migrate import Migrate
from flask_mail import Mail
from config import Config

# Initialize Flask extensions
db = SQLAlchemy()
login = LoginManager()
migrate = Migrate()
mail = Mail()


def create_app(config_class=Config):
    # Create the Flask application instance
    app = Flask(__name__)
    app.config.from_object(config_class)
    
    # Initialize Flask extensions
    db.init_app(app)
    login.init_app(app)
    login.login_view = 'auth.login'
    migrate.init_app(app, db)
    mail.init_app(app)


    from app.main import bp as main_bp
    app.register_blueprint(main_bp)

    from app.services import bp as services_bp
    app.register_blueprint(services_bp)

    from app.auth import bp as auth_bp
    app.register_blueprint(auth_bp)

    return app
