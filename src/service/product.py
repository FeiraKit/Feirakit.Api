from bson import ObjectId
from src.program.database import database
from src.service.id_settings import IdSettings
from src.service.configs import configs_service

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
        
        exists_category = database.main['configs'].find_one({'Categories': product['categoria']})
        if not exists_category:
            return {
                'resultado': False,
                'mensagem': "erro ao cadastrar produto, categoria inválida"
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

    def get_by_filter(self, name, user_id, cities):
        filters = [
        {'name': 'nome', 'value': name, 'regex': True}, 
        {'name': 'produtor_id', 'value': user_id, 'regex': False}, 
        {'name': 'cidades', 'value': cities, 'regex': True}
        ]
        products = []
        for filter in filters:
            if filter['value'] != None:
                products.append(list(database.main[self.collection].find(self.search_object(filter))))
        return self.entity_response_list(*products)
            
    def search_object(self, filter):
        if filter['regex']:
            return{filter['name']: {'$regex': filter['value'], '$options' : 'i'}}
        return{filter['name']: filter['value']}

    def get_product_types(self):
        product_types = configs_service.get()
        return product_types
    
    def get_cities(self):
        users = list(database.main['user'].find({}, {"endereco.cidade": 1, "_id": 0}))
        
        cities = []

        for user in users:
                cities.append(user["endereco"]["cidade"])
        
        cities = list(set(cities))

        resultado = []

        for city in cities:
                resultado.append({
                    "nome": city
                })

        return {"resultado": resultado,
                    "mensagem": "Sucesso"}, 200

product_service = Product()
