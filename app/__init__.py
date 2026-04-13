from flask import Flask
from flask_cors import CORS
from flask_migrate import Migrate
from flasgger import Swagger
from config import config
from app.models import db

migrate = Migrate()

def create_app(config_name='default'):
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    
    db.init_app(app)
    migrate.init_app(app, db)
    CORS(app)
    Swagger(app)
    
    from app.blueprints.categories import categories_bp
    from app.blueprints.products import products_bp
    from app.blueprints.clients import clients_bp
    from app.blueprints.orders import orders_bp
    
    app.register_blueprint(categories_bp)
    app.register_blueprint(products_bp)
    app.register_blueprint(clients_bp)
    app.register_blueprint(orders_bp)
    
    @app.route('/')
    def index():
        return {'message': 'Flask API with Flasgger', 'docs': '/apidocs'}
    
    @app.route('/health')
    def health():
        return {'status': 'healthy'}
    
    return app

if __name__ == '__main__':
    app = create_app('development')
    app.run(host='0.0.0.0', port=5000, debug=True)