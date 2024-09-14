from flask import Flask

def create_app():
    app = Flask(__name__)

    # Register routes
    from app.routes import main,voicesearch,waterstress
    app.register_blueprint(main)
    app.register_blueprint(voicesearch)


    # Enable debug mode
    app.config['DEBUG'] = True  # Alternatively, you can set this in run.py

    return app
