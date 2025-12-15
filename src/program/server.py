from flask import Flask, make_response, request
from flask_restx import Api
from flask_cors import CORS
from src.core.var_env import var_env
class Server():
    def __init__(self):
        self.app = Flask(__name__)
        self.app.config.setdefault("RESTX_MASK_SWAGGER", False)
        self.app.config['SECRET_KEY'] = [var_env.secret_key]
        CORS(self.app, resources={r"/*": {"origins": "*"}} )
        @self.app.before_request
        def handle_options():
            if request.method == 'OPTIONS':
                response = make_response()
                response.headers.add('Access-Control-Allow-Origin', '*')
                response.headers.add('Access-Control-Allow-Headers', 'Content-Type, Authorization')
                response.headers.add('Access-Control-Allow-Methods', 'GET, POST, PUT, DELETE, OPTIONS')
                response.status_code = 200
                return response
        self.api = Api(self.app,
                       version='1.0',
                       title='Feirakit API',
                       description='',
                       doc='/swagger',
                       authorizations={
                             'Bearer': {
                                 'type': 'apiKey',
                                 'in': 'header',
                                 'name': 'Authorization'
                             }
                       }
                       )

    def app_flask(self):
        return self.app


server = Server()
