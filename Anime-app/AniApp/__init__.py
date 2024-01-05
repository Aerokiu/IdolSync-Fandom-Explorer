
from flask import Flask

def create_app():
    app = Flask(__name__)

    # Set the base URL
    app.config['BASE_URL'] = 'http://IdolSync/'

    # Import and register blueprints, configure app, etc.
    from AniApp.routes import main_bp

    app.register_blueprint(main_bp)

    return app

