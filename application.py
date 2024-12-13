from flask import Flask

# Import the blueprint from routes.py
from routes import main_routes

def create_app():
    """Application factory function"""
    application = Flask(__name__)

    # Register blueprints
    application.register_blueprint(main_routes)

    return application

application = create_app()

if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)
