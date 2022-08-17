from flask import Flask, jsonify, request, abort
from models import setup_db, Plant
from flask_cors import CORS, cross_origin


def create_app(test_config=None):
    app = Flask(__name__)
    setup_db(app)
    CORS(app)

    @app.after_request
    def after_request(response):
        response.headers.add('Access-Control-Allow-Headers', 'Content-Type, Authorization')
        response.headers.add('Access-Control-Allow-Methods', 'GET, POST, PATCH, DELETE, OPTIONS')
        return response

    @app.route('/')
    @cross_origin()
    def hello():
        return jsonify({'message': 'HELLO WORLD'})

    return app
