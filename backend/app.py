from flask import Flask
from flask_cors import CORS
from config import config

def create_app(config_name='default'):
    """
    Application factory pattern for creating the Flask app instance.
    """
    app = Flask(__name__)
    
    # Load configuration
    app.config.from_object(config[config_name])
    
    # Enable Cross-Origin Resource Sharing (CORS) for frontend interaction
    CORS(app)

    # Register Blueprints / Routes
    # We import these here to avoid circular dependencies
    from routes.health_route import health_bp
    from routes.download_route import download_bp

    app.register_blueprint(health_bp)
    app.register_blueprint(download_bp)

    return app

if __name__ == '__main__':
    app = create_app('development')
    app.run(host='0.0.0.0', port=5000)
