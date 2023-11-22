from flask_restx import Resource
from flask import request
from src.program.server import server
from src.models import kit as kit_model
from src.models.id import id_request
from src.service.kit import kit_service
from src.core.authenticate import authenticate

app, api = server.app, server.api.namespace('kits',description='Recurso de kits')
@api.route('')
class Kit(Resource):
    @api.marshal_list_with(kit_model.response)
    @api.doc(params={'page': 'Index of page','limit':'Quantity of kits by request','sort':'order of results (1=asc / -1= dec)'})
    def get(self):
        page= request.args.get('page',type=int,default=1)
        limit= request.args.get('limit',type=int ,default=10)
        sort= request.args.get('sort',type=int ,default=1)
        kits = kit_service.get(page,limit,sort)
        return kits, 200
    
    @api.expect(kit_model.request, validate=True)
    @authenticate.jwt_required
    @api.marshal_with(kit_model.response_default)
    @api.doc(security='Bearer')
    def post(self,current_user):
        response = kit_model.post(api.payload,current_user)
        return response
    
    @api.expect(kit_model.update_request)
    @authenticate.jwt_required
    @api.marshal_with(kit_model.update_response)
    @api.doc(security='Bearer')
    def put(self,current_user):
        response = kit_service.put(api.payload,current_user)
        return response
    
    @api.expect(id_request, validate=True)
    @authenticate.jwt_required
    @api.marshal_with(kit_model.response_default)
    @api.doc(security='Bearer')
    def delete(self,current_user):
        response = kit_service.delete(api.payload['id'],current_user)
        return response