from flask_restx import Resource
from flask import request
from src.program.server import server
from src.models import product as product_model
from src.models.id import id_request
from src.service.product import product_service
from src.core.authenticate import authenticate

app, api = server.app, server.api.namespace('products',description='Recurso de produtos')
@api.route('')
class Product(Resource):
    @api.marshal_list_with(product_model.response)
    @api.doc(params={'page': 'Index of page','limit':'Quantity of products by request','sort':'order of results (1=asc / -1= dec)'})
    def get(self):
        page= request.args.get('page',type=int,default=1)
        limit= request.args.get('limit',type=int ,default=10)
        sort= request.args.get('sort',type=int ,default=1)
        products = product_service.get(page,limit,sort)
        return products, 200

    @api.expect(product_model.request, validate=True)
    @authenticate.jwt_required
    @api.marshal_with(product_model.response_default)
    @api.doc(security='Bearer')
    def post(self,current_user):
        response = product_service.post(api.payload,current_user)
        return response

    @api.expect(product_model.update_request)
    @authenticate.jwt_required
    @api.marshal_with(product_model.update_response)
    @api.doc(security='Bearer')
    def put(self,current_user):
        response = product_service.put(api.payload,current_user)
        return response

    @api.expect(id_request, validate=True)
    @authenticate.jwt_required
    @api.marshal_with(product_model.response_default)
    @api.doc(security='Bearer')
    def delete(self,current_user):
        response = product_service.delete(api.payload['id'],current_user)
        return response

@api.route('/<string:id>')
class ProductSeachById(Resource):
    @api.marshal_list_with(product_model.responseProductById)
    def get(self, id):
        products = product_service.get_one(id)
        return products, 200

@api.route('/units')
class GetUnity(Resource):
    def get(self):
        product_types = product_service.get_product_types()
        return product_types, 200
        
@api.route('/filters')
class GetProductsByfilters(Resource):
    @api.marshal_with(product_model.response)
    @api.doc(params={'nome':'nome do produto','id':"id do usuário", 'cidade':"cidade que o produto possa ser entregue"})
    def get(self):
        nome= request.args.get('nome', type=str)
        id= request.args.get('id', type=str)
        cidade= request.args.get('cidade', type=str)
        products = product_service.get_by_filter(nome, id, cidade)
        return products, 200

@api.route('/get_cities')
class GetCities(Resource):
    @authenticate.jwt_required
    @api.doc(security='Bearer')
    @api.marshal_with(product_model.cities_response)
    def get(self, current_user):
        cities = product_service.get_cities()
        return cities
