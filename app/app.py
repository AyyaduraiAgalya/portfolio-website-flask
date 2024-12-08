from flask import Flask

# Import the blueprint from routes.py
from routes import main_routes

def create_app():
    """Application factory function"""
    app = Flask(__name__)

    # Register blueprints
    app.register_blueprint(main_routes)

    return app

if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)
