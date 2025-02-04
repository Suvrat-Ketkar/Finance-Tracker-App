from flask import Flask
from flask_cors import CORS
from dotenv import load_dotenv
from app.extensions import init_extensions
from flask_session import Session
load_dotenv()

def create_app():
    app = Flask(__name__)
    app.config.from_prefixed_env()  # Load environment variables
    
    # Initialize extensions
    init_extensions(app)
    Session(app)
    CORS(app)
    # Register blueprints
    from app.authentication.auth import auth_bp
    app.register_blueprint(auth_bp, url_prefix='/')

    from app.transaction.transaction import transaction_bp
    app.register_blueprint(transaction_bp, url_prefix='/')

    from app.DashBoard.routes import dashboard_bp
    app.register_blueprint(dashboard_bp, url_prefix='/')


    return app
