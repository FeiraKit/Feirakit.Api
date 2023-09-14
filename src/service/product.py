from bson import ObjectId
from src.program.database import database
from src.service.id_settings import IdSettings
from src.constants.products import categorias, unidades

class Product(IdSettings):
    def __init__(self):
        self.collection = 'product'

    def get(self, page, limit, sort):
        skip = limit * (page - 1)
        products = list(database.main[self.collection].find().skip(
            skip).limit(limit).sort('_id', sort))
        return self.entity_response_list(products)

    def post(self, product, current_user):
        if product['produtor_id'] != current_user['id']:
            return {
                'resultado': False,
                'mensagem': "erro ao cadastrar produto, os dados de usuário são inconsitentes"
            }, 401

        database.main[self.collection].insert_one(product)
        return {
            'resultado': True,
            'mensagem': "Produto criado com sucesso"
        }, 201

    def put(self, product, current_user):
        if product['produtor_id'] != current_user['id']:
            return {
                'resultado': {},
                'mensagem': "erro ao atualizar produto,esse produto pertence a outro usuário"
            }, 403

        my_query = {'_id':  ObjectId(product['id'])}
        del product['id']
        new_values = {'$set': product}
        database.main[self.collection].update_one(my_query, new_values)
        updated_product = database.main[self.collection].find_one(my_query)
        return {
            'resultado': self.entity_response(updated_product),
            'mensagem': "O produto foi alterado com sucesso"
        }, 201

    def delete(self, id, current_user):
        product = database.main[self.collection].find_one({'_id':  ObjectId(id)})
        if product['produtor_id'] != current_user['id']:
            return {
                'resultado': False,
                'mensagem': "erro ao apagar produto,esse produto pertence a outro usuário"
            }, 403

        database.main[self.collection].delete_one({'_id':  ObjectId(id)})
        return {
            'resultado': True,
            'mensagem': "Produto apagado com sucesso"
        }, 200

    def get_one(self, id):
        product = database.main[self.collection].find_one({'_id':  ObjectId(id)})
        return self.entity_response(product)

    def get_products_by_name(self, name):
        products = list(database.main[self.collection].find(
            {'nome': {'$regex': name, '$options' : 'i'}}))
        return self.entity_response_list(products)

    def get_products_by_id_usuario(self, id_usuario):
        products = list(database.main[self.collection].find(
            {'produtor_id': id_usuario}))
        return self.entity_response_list(products)

    def get_product_types(self):
        return {
            'unidades': unidades,
            'categorias': categorias
        }

product_service = Product()
