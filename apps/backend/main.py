from flask import Flask, jsonify
from flasgger import Swagger
from flask_sqlalchemy import SQLAlchemy
from dotenv import load_dotenv
import os

load_dotenv()

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    
    app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')
    
    db.init_app(app)
    
    Swagger(app, template={
        "info": {
            "title": "Library API",
            "description": "API for library management",
            "version": "1.0.0"
        },
        "basePath": "/"
    })
    
    from apps.backend.src.routes.authors import authors_bp
    from apps.backend.src.routes.books import books_bp
    from apps.backend.src.routes.members import members_bp
    from apps.backend.src.routes.loans import loans_bp
    
    app.register_blueprint(authors_bp, url_prefix='/api')
    app.register_blueprint(books_bp, url_prefix='/api')
    app.register_blueprint(members_bp, url_prefix='/api')
    app.register_blueprint(loans_bp, url_prefix='/api')
    
    @app.route('/')
    def index():
        return jsonify({"message": "Library API", "docs": "/docs/"})
    
    @app.route('/health')
    def health():
        return jsonify({"status": "healthy"})
    
    with app.app_context():
        db.create_all()
    
    return app

app = create_app()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)