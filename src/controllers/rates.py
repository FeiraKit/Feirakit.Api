from flask_restx import Resource
from flask import request
from src.program.server import server
from src.models import rate
from src.models.id import id_request
from src.service.rate import rating_service


app, api = server.app, server.api.namespace('Rates',description='Recurso de avaliações')

@api.route('')
class Rate(Resource):
    @api.marshal_list_with(rate.rate_response)
    def get(self):
        rates = rating_service.get()
        return rates, 200

    @api.expect(rate.request)
    @api.marshal_with(rate.rate_default_response)
    def post(self):
        response = rating_service.post(api.payload)
        return response

    @api.expect(rate.rate_update_request)
    @api.marshal_with(rate.rate_update_response)
    def put(self):
        response = rating_service.put(api.payload)
        return response

    @api.expect(id_request)
    @api.marshal_with(rate.rate_default_response)
    def delete(self):
        response = rating_service.delete(api.payload['id'])
        return response
    
@api.route('/<string:id>')
class RateGetaverage(Resource):
    @api.marshal_with(rate.rate_average_response)
    def get(self, id):
        response = rating_service.average(id)
        return response
    