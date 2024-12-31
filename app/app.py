from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_cors import CORS
from config import Config
from dotenv import load_dotenv
import os

load_dotenv()
# Initialize extensions
db = SQLAlchemy()
migrate = Migrate()

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    # Initialize extensions
    db.init_app(app)
    migrate.init_app(app, db)
    CORS(app)

    # Register routes
    from .routes import main_bp
    app.register_blueprint(main_bp)

    return app

# Run the app
if __name__ == "__main__":
    app = create_app()
    app.run(host="127.0.0.1", port=5000)  # Run on 127.0.0.1 and port 5000
    