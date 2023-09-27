from flask_restx import Resource
from flask import request
from src.program.server import server
from src.models import configs as configs_model
from src.service.configs import configs_service

app, api = server.app, server.api.namespace('configs',description='Recurso de configurações')
@api.route('')
class Configs(Resource):
    @api.marshal_with(configs_model.types_response)
    def get(self):
        product_types = configs_service.get()
        return product_types
